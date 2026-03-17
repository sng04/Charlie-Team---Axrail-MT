r'''
# Amazon EKS V2 Construct Library

The aws-eks-v2 module is a rewrite of the existing aws-eks module (https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_eks-readme.html). This new iteration leverages native L1 CFN resources, replacing the previous custom resource approach for creating EKS clusters and Fargate Profiles.

Compared to the original EKS module, it has the following major changes:

* Use native L1 AWS::EKS::Cluster resource to replace custom resource Custom::AWSCDK-EKS-Cluster
* Use native L1 AWS::EKS::FargateProfile resource to replace custom resource Custom::AWSCDK-EKS-FargateProfile
* Kubectl Handler will not be created by default. It will only be created if users specify it.
* Remove AwsAuth construct. Permissions to the cluster will be managed by Access Entry.
* Remove the limit of 1 cluster per stack
* Remove nested stacks
* API changes to make them more ergonomic.

## Quick start

Here is the minimal example of defining an AWS EKS cluster

```python
cluster = eks.Cluster(self, "hello-eks",
    version=eks.KubernetesVersion.V1_34
)
```

## Architecture

```text                                             +-----------------+
                                         kubectl    |                 |
                                      +------------>| Kubectl Handler |
                                      |             |   (Optional)    |
                                      |             +-----------------+
+-------------------------------------+-------------------------------------+
|                        EKS Cluster (Auto Mode)                            |
|                          AWS::EKS::Cluster                                |
|                                                                           |
|  +---------------------------------------------------------------------+  |
|  |           Auto Mode Compute (Managed by EKS) (Default)              |  |
|  |                                                                     |  |
|  |  - Automatically provisions EC2 instances                           |  |
|  |  - Auto scaling based on pod requirements                           |  |
|  |  - No manual node group configuration needed                        |  |
|  |                                                                     |  |
|  +---------------------------------------------------------------------+  |
|                                                                           |
+---------------------------------------------------------------------------+
```

In a nutshell:

* **[Auto Mode](#eks-auto-mode)** (Default) – The fully managed capacity mode in EKS.
  EKS automatically provisions and scales  EC2 capacity based on pod requirements.
  It manages internal *system* and *general-purpose* NodePools, handles networking and storage setup, and removes the need for user-managed node groups or Auto Scaling Groups.

  ```python
  cluster = eks.Cluster(self, "AutoModeCluster",
      version=eks.KubernetesVersion.V1_34
  )
  ```
* **[Managed Node Groups](#managed-node-groups)** – The semi-managed capacity mode.
  EKS provisions and manages EC2 nodes on your behalf but you configure the instance types, scaling ranges, and update strategy.
  AWS handles node health, draining, and rolling updates while you retain control over scaling and cost optimization.

  You can also define *Fargate Profiles* that determine which pods or namespaces run on Fargate infrastructure.

  ```python
  cluster = eks.Cluster(self, "ManagedNodeCluster",
      version=eks.KubernetesVersion.V1_34,
      default_capacity_type=eks.DefaultCapacityType.NODEGROUP
  )

  # Add a Fargate Profile for specific workloads (e.g., default namespace)
  cluster.add_fargate_profile("FargateProfile",
      selectors=[eks.Selector(namespace="default")
      ]
  )
  ```
* **[Fargate Mode](#fargate-profiles)** – The Fargate capacity mode.
  EKS runs your pods directly on AWS Fargate without provisioning EC2 nodes.

  ```python
  cluster = eks.FargateCluster(self, "FargateCluster",
      version=eks.KubernetesVersion.V1_34
  )
  ```
* **[Self-Managed Nodes](#self-managed-capacity)** – The fully manual capacity mode.
  You create and manage EC2 instances (via an Auto Scaling Group) and connect them to the cluster manually.
  This provides maximum flexibility for custom AMIs or configurations but also the highest operational overhead.

  ```python
  cluster = eks.Cluster(self, "SelfManagedCluster",
      version=eks.KubernetesVersion.V1_34
  )

  # Add self-managed Auto Scaling Group
  cluster.add_auto_scaling_group_capacity("self-managed-asg",
      instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
      min_capacity=1,
      max_capacity=5
  )
  ```
* **[Kubectl Handler](#kubectl-support) (Optional)** – A Lambda-backed custom resource created by the AWS CDK to execute `kubectl` commands (like `apply` or `patch`) during deployment.
  Regardless of the capacity mode, this handler may still be created to apply Kubernetes manifests as part of CDK provisioning.

## Provisioning cluster

Creating a new cluster is done using the `Cluster` constructs. The only required property is the kubernetes version.

```python
eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34
)
```

You can also use `FargateCluster` to provision a cluster that uses only fargate workers.

```python
eks.FargateCluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34
)
```

**Note: Unlike the previous EKS cluster, `Kubectl Handler` will not
be created by default. It will only be deployed when `kubectlProviderOptions`
property is used.**

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


eks.Cluster(self, "hello-eks",
    version=eks.KubernetesVersion.V1_34,
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl")
    )
)
```

### EKS Auto Mode

[Amazon EKS Auto Mode](https://aws.amazon.com/eks/auto-mode/) extends AWS management of Kubernetes clusters beyond the cluster itself, allowing AWS to set up and manage the infrastructure that enables the smooth operation of your workloads.

#### Using Auto Mode

While `aws-eks` uses `DefaultCapacityType.NODEGROUP` by default, `aws-eks-v2` uses `DefaultCapacityType.AUTOMODE` as the default capacity type.

Auto Mode is enabled by default when creating a new cluster without specifying any capacity-related properties:

```python
# Create EKS cluster with Auto Mode implicitly enabled
cluster = eks.Cluster(self, "EksAutoCluster",
    version=eks.KubernetesVersion.V1_34
)
```

You can also explicitly enable Auto Mode using `defaultCapacityType`:

```python
# Create EKS cluster with Auto Mode explicitly enabled
cluster = eks.Cluster(self, "EksAutoCluster",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.AUTOMODE
)
```

#### Node Pools

When Auto Mode is enabled, the cluster comes with two default node pools:

* `system`: For running system components and add-ons
* `general-purpose`: For running your application workloads

These node pools are managed automatically by EKS. You can configure which node pools to enable through the `compute` property:

```python
cluster = eks.Cluster(self, "EksAutoCluster",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.AUTOMODE,
    compute=eks.ComputeConfig(
        node_pools=["system", "general-purpose"]
    )
)
```

For more information, see [Create a Node Pool for EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/create-node-pool.html).

#### Disabling Default Node Pools

You can disable the default node pools entirely by setting an empty array for `nodePools`. This is useful when you want to use Auto Mode features but manage your compute resources separately:

```python
cluster = eks.Cluster(self, "EksAutoCluster",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.AUTOMODE,
    compute=eks.ComputeConfig(
        node_pools=[]
    )
)
```

When node pools are disabled this way, no IAM role will be created for the node pools, preventing deployment failures that would otherwise occur when a role is created without any node pools.

### Node Groups as the default capacity type

If you prefer to manage your own node groups instead of using Auto Mode, you can use the traditional node group approach by specifying `defaultCapacityType` as `NODEGROUP`:

```python
# Create EKS cluster with traditional managed node group
cluster = eks.Cluster(self, "EksCluster",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
    default_capacity=3,  # Number of instances
    default_capacity_instance=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.LARGE)
)
```

You can also create a cluster with no initial capacity and add node groups later:

```python
cluster = eks.Cluster(self, "EksCluster",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
    default_capacity=0
)

# Add node groups as needed
cluster.add_nodegroup_capacity("custom-node-group",
    min_size=1,
    max_size=3,
    instance_types=[ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.LARGE)]
)
```

Read [Managed node groups](#managed-node-groups) for more information on how to add node groups to the cluster.

### Mixed with Auto Mode and Node Groups

You can combine Auto Mode with traditional node groups for specific workload requirements:

```python
cluster = eks.Cluster(self, "Cluster",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.AUTOMODE,
    compute=eks.ComputeConfig(
        node_pools=["system", "general-purpose"]
    )
)

# Add specialized node group for specific workloads
cluster.add_nodegroup_capacity("specialized-workload",
    min_size=1,
    max_size=3,
    instance_types=[ec2.InstanceType.of(ec2.InstanceClass.C5, ec2.InstanceSize.XLARGE)],
    labels={
        "workload": "specialized"
    }
)
```

### Important Notes

1. Auto Mode and traditional capacity management are mutually exclusive at the default capacity level. You cannot opt in to Auto Mode and specify `defaultCapacity` or `defaultCapacityInstance`.
2. When Auto Mode is enabled:

   * The cluster will automatically manage compute resources
   * Node pools cannot be modified, only enabled or disabled
   * EKS will handle scaling and management of the node pools
3. Auto Mode requires specific IAM permissions. The construct will automatically attach the required managed policies.

### Managed node groups

Amazon EKS managed node groups automate the provisioning and lifecycle management of nodes (Amazon EC2 instances) for Amazon EKS Kubernetes clusters.
With Amazon EKS managed node groups, you don't need to separately provision or register the Amazon EC2 instances that provide compute capacity to run your Kubernetes applications. You can create, update, or terminate nodes for your cluster with a single operation. Nodes run using the latest Amazon EKS optimized AMIs in your AWS account while node updates and terminations gracefully drain nodes to ensure that your applications stay available.

> For more details visit [Amazon EKS Managed Node Groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

By default, when using `DefaultCapacityType.NODEGROUP`, this library will allocate a managed node group with 2 *m5.large* instances (this instance type suits most common use-cases, and is good value for money).

```python
eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.NODEGROUP
)
```

At cluster instantiation time, you can customize the number of instances and their type:

```python
eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
    default_capacity=5,
    default_capacity_instance=ec2.InstanceType.of(ec2.InstanceClass.M5, ec2.InstanceSize.SMALL)
)
```

To access the node group that was created on your behalf, you can use `cluster.defaultNodegroup`.

Additional customizations are available post instantiation. To apply them, set the default capacity to 0, and use the `cluster.addNodegroupCapacity` method:

```python
cluster = eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
    default_capacity=0
)

cluster.add_nodegroup_capacity("custom-node-group",
    instance_types=[ec2.InstanceType("m5.large")],
    min_size=4,
    disk_size=100
)
```

### Fargate profiles

AWS Fargate is a technology that provides on-demand, right-sized compute
capacity for containers. With AWS Fargate, you no longer have to provision,
configure, or scale groups of virtual machines to run containers. This removes
the need to choose server types, decide when to scale your node groups, or
optimize cluster packing.

You can control which pods start on Fargate and how they run with Fargate
Profiles, which are defined as part of your Amazon EKS cluster.

See [Fargate Considerations](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html#fargate-considerations) in the AWS EKS User Guide.

You can add Fargate Profiles to any EKS cluster defined in your CDK app
through the `addFargateProfile()` method. The following example adds a profile
that will match all pods from the "default" namespace:

```python
# cluster: eks.Cluster

cluster.add_fargate_profile("MyProfile",
    selectors=[eks.Selector(namespace="default")]
)
```

You can also directly use the `FargateProfile` construct to create profiles under different scopes:

```python
# cluster: eks.Cluster

eks.FargateProfile(self, "MyProfile",
    cluster=cluster,
    selectors=[eks.Selector(namespace="default")]
)
```

To create an EKS cluster that **only** uses Fargate capacity, you can use `FargateCluster`.
The following code defines an Amazon EKS cluster with a default Fargate Profile that matches all pods from the "kube-system" and "default" namespaces. It is also configured to [run CoreDNS on Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html#fargate-gs-coredns).

```python
cluster = eks.FargateCluster(self, "MyCluster",
    version=eks.KubernetesVersion.V1_34
)
```

`FargateCluster` will create a default `FargateProfile` which can be accessed via the cluster's `defaultProfile` property. The created profile can also be customized by passing options as with `addFargateProfile`.

**NOTE**: Classic Load Balancers and Network Load Balancers are not supported on
pods running on Fargate. For ingress, we recommend that you use the [ALB Ingress
Controller](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html)
on Amazon EKS (minimum version v1.1.4).

### Self-managed capacity

Self-managed capacity gives you the most control over your worker nodes by allowing you to create and manage your own EC2 Auto Scaling Groups. This approach provides maximum flexibility for custom AMIs, instance configurations, and scaling policies, but requires more operational overhead.

You can add self-managed capacity to any cluster using the `addAutoScalingGroupCapacity` method:

```python
cluster = eks.Cluster(self, "Cluster",
    version=eks.KubernetesVersion.V1_34
)

cluster.add_auto_scaling_group_capacity("self-managed-nodes",
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
    min_capacity=1,
    max_capacity=10,
    desired_capacity=3
)
```

You can specify custom subnets for the Auto Scaling Group:

```python
# vpc: ec2.Vpc
# cluster: eks.Cluster


cluster.add_auto_scaling_group_capacity("custom-subnet-nodes",
    vpc_subnets=ec2.SubnetSelection(subnets=vpc.private_subnets),
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
    min_capacity=2
)
```

### Endpoint Access

When you create a new cluster, Amazon EKS creates an endpoint for the managed Kubernetes API server that you use to communicate with your cluster (using Kubernetes management tools such as `kubectl`)

You can configure the [cluster endpoint access](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) by using the `endpointAccess` property:

```python
cluster = eks.Cluster(self, "hello-eks",
    version=eks.KubernetesVersion.V1_34,
    endpoint_access=eks.EndpointAccess.PRIVATE
)
```

The default value is `eks.EndpointAccess.PUBLIC_AND_PRIVATE`. Which means the cluster endpoint is accessible from outside of your VPC, but worker node traffic and `kubectl` commands issued by this library stay within your VPC.

### Alb Controller

Some Kubernetes resources are commonly implemented on AWS with the help of the [ALB Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/).

From the docs:

> AWS Load Balancer Controller is a controller to help manage Elastic Load Balancers for a Kubernetes cluster.
>
> * It satisfies Kubernetes Ingress resources by provisioning Application Load Balancers.
> * It satisfies Kubernetes Service resources by provisioning Network Load Balancers.

To deploy the controller on your EKS cluster, configure the `albController` property:

```python
eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    alb_controller=eks.AlbControllerOptions(
        version=eks.AlbControllerVersion.V2_8_2
    )
)
```

To provide additional Helm chart values supported by `albController` in CDK, use the `additionalHelmChartValues` property. For example, the following code snippet shows how to set the `enableWafV2` flag:

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    alb_controller=eks.AlbControllerOptions(
        version=eks.AlbControllerVersion.V2_8_2,
        additional_helm_chart_values={
            "enable_wafv2": False
        }
    )
)
```

To overwrite an existing ALB controller service account, use the `overwriteServiceAccount` property:

```python
eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    alb_controller=eks.AlbControllerOptions(
        version=eks.AlbControllerVersion.V2_8_2,
        overwrite_service_account=True
    )
)
```

The `albController` requires `defaultCapacity` or at least one nodegroup. If there's no `defaultCapacity` or available
nodegroup for the cluster, the `albController` deployment would fail.

Querying the controller pods should look something like this:

```console
❯ kubectl get pods -n kube-system
NAME                                            READY   STATUS    RESTARTS   AGE
aws-load-balancer-controller-76bd6c7586-d929p   1/1     Running   0          109m
aws-load-balancer-controller-76bd6c7586-fqxph   1/1     Running   0          109m
...
...
```

Every Kubernetes manifest that utilizes the ALB Controller is effectively dependant on the controller.
If the controller is deleted before the manifest, it might result in dangling ELB/ALB resources.
Currently, the EKS construct library does not detect such dependencies, and they should be done explicitly.

For example:

```python
# cluster: eks.Cluster

manifest = cluster.add_manifest("manifest", {})
if cluster.alb_controller:
    manifest.node.add_dependency(cluster.alb_controller)
```

You can specify the VPC of the cluster using the `vpc` and `vpcSubnets` properties:

```python
# vpc: ec2.Vpc


eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    vpc=vpc,
    vpc_subnets=[ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)]
)
```

If you do not specify a VPC, one will be created on your behalf, which you can then access via `cluster.vpc`. The cluster VPC will be associated to any EKS managed capacity (i.e Managed Node Groups and Fargate Profiles).

Please note that the `vpcSubnets` property defines the subnets where EKS will place the *control plane* ENIs. To choose
the subnets where EKS will place the worker nodes, please refer to the **Provisioning clusters** section above.

If you allocate self managed capacity, you can specify which subnets should the auto-scaling group use:

```python
# vpc: ec2.Vpc
# cluster: eks.Cluster

cluster.add_auto_scaling_group_capacity("nodes",
    vpc_subnets=ec2.SubnetSelection(subnets=vpc.private_subnets),
    instance_type=ec2.InstanceType("t2.medium")
)
```

There is an additional components you might want to provision within the VPC.

The `KubectlHandler` is a Lambda function responsible to issuing `kubectl` and `helm` commands against the cluster when you add resource manifests to the cluster.

The handler association to the VPC is derived from the `endpointAccess` configuration. The rule of thumb is: *If the cluster VPC can be associated, it will be*.

Breaking this down, it means that if the endpoint exposes private access (via `EndpointAccess.PRIVATE` or `EndpointAccess.PUBLIC_AND_PRIVATE`), and the VPC contains **private** subnets, the Lambda function will be provisioned inside the VPC and use the private subnets to interact with the cluster. This is the common use-case.

If the endpoint does not expose private access (via `EndpointAccess.PUBLIC`) **or** the VPC does not contain private subnets, the function will not be provisioned within the VPC.

If your use-case requires control over the IAM role that the KubeCtl Handler assumes, a custom role can be passed through the ClusterProps (as `kubectlLambdaRole`) of the EKS Cluster construct.

### Kubectl Support

You can choose to have CDK create a `Kubectl Handler` - a Python Lambda Function to
apply k8s manifests using `kubectl apply`. This handler will not be created by default.

To create a `Kubectl Handler`, use `kubectlProviderOptions` when creating the cluster.
`kubectlLayer` is the only required property in `kubectlProviderOptions`.

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


eks.Cluster(self, "hello-eks",
    version=eks.KubernetesVersion.V1_34,
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl")
    )
)
```

`Kubectl Handler` created along with the cluster will be granted admin permissions to the cluster.

If you want to use an existing kubectl provider function, for example with tight trusted entities on your IAM Roles - you can import the existing provider and then use the imported provider when importing the cluster:

```python
handler_role = iam.Role.from_role_arn(self, "HandlerRole", "arn:aws:iam::123456789012:role/lambda-role")
# get the serivceToken from the custom resource provider
function_arn = lambda_.Function.from_function_name(self, "ProviderOnEventFunc", "ProviderframeworkonEvent-XXX").function_arn
kubectl_provider = eks.KubectlProvider.from_kubectl_provider_attributes(self, "KubectlProvider",
    service_token=function_arn,
    role=handler_role
)

cluster = eks.Cluster.from_cluster_attributes(self, "Cluster",
    cluster_name="cluster",
    kubectl_provider=kubectl_provider
)
```

#### Environment

You can configure the environment of this function by specifying it at cluster instantiation. For example, this can be useful in order to configure an http proxy:

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


cluster = eks.Cluster(self, "hello-eks",
    version=eks.KubernetesVersion.V1_34,
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl"),
        environment={
            "http_proxy": "http://proxy.myproxy.com"
        }
    )
)
```

#### Runtime

The kubectl handler uses `kubectl`, `helm` and the `aws` CLI in order to
interact with the cluster. These are bundled into AWS Lambda layers included in
the `@aws-cdk/lambda-layer-awscli` and `@aws-cdk/lambda-layer-kubectl` modules.

The version of kubectl used must be compatible with the Kubernetes version of the
cluster. kubectl is supported within one minor version (older or newer) of Kubernetes
(see [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/#kubectl)).
Depending on which version of kubernetes you're targeting, you will need to use one of
the `@aws-cdk/lambda-layer-kubectl-vXY` packages.

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


cluster = eks.Cluster(self, "hello-eks",
    version=eks.KubernetesVersion.V1_34,
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl")
    )
)
```

#### Memory

By default, the kubectl provider is configured with 1024MiB of memory. You can use the `memory` option to specify the memory size for the AWS Lambda function:

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


eks.Cluster(self, "MyCluster",
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl"),
        memory=Size.gibibytes(4)
    ),
    version=eks.KubernetesVersion.V1_34
)
```

### ARM64 Support

Instance types with `ARM64` architecture are supported in both managed nodegroup and self-managed capacity. Simply specify an ARM64 `instanceType` (such as `m6g.medium`), and the latest
Amazon Linux 2 AMI for ARM64 will be automatically selected.

```python
# cluster: eks.Cluster

# add a managed ARM64 nodegroup
cluster.add_nodegroup_capacity("extra-ng-arm",
    instance_types=[ec2.InstanceType("m6g.medium")],
    min_size=2
)

# add a self-managed ARM64 nodegroup
cluster.add_auto_scaling_group_capacity("self-ng-arm",
    instance_type=ec2.InstanceType("m6g.medium"),
    min_capacity=2
)
```

### Masters Role

When you create a cluster, you can specify a `mastersRole`. The `Cluster` construct will associate this role with `AmazonEKSClusterAdminPolicy` through [Access Entry](https://docs.aws.amazon.com/eks/latest/userguide/access-policy-permissions.html).

```python
# role: iam.Role

eks.Cluster(self, "HelloEKS",
    version=eks.KubernetesVersion.V1_34,
    masters_role=role
)
```

If you do not specify it, you won't have access to the cluster from outside of the CDK application.

### Encryption

When you create an Amazon EKS cluster, envelope encryption of Kubernetes secrets using the AWS Key Management Service (AWS KMS) can be enabled.
The documentation on [creating a cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)
can provide more details about the customer master key (CMK) that can be used for the encryption.

You can use the `secretsEncryptionKey` to configure which key the cluster will use to encrypt Kubernetes secrets. By default, an AWS Managed key will be used.

> This setting can only be specified when the cluster is created and cannot be updated.

```python
secrets_key = kms.Key(self, "SecretsKey")
cluster = eks.Cluster(self, "MyCluster",
    secrets_encryption_key=secrets_key,
    version=eks.KubernetesVersion.V1_34
)
```

You can also use a similar configuration for running a cluster built using the FargateCluster construct.

```python
secrets_key = kms.Key(self, "SecretsKey")
cluster = eks.FargateCluster(self, "MyFargateCluster",
    secrets_encryption_key=secrets_key,
    version=eks.KubernetesVersion.V1_34
)
```

The Amazon Resource Name (ARN) for that CMK can be retrieved.

```python
# cluster: eks.Cluster

cluster_encryption_config_key_arn = cluster.cluster_encryption_config_key_arn
```

### Hybrid Nodes

When you create an Amazon EKS cluster, you can configure it to leverage the [EKS Hybrid Nodes](https://aws.amazon.com/eks/hybrid-nodes/) feature, allowing you to use your on-premises and edge infrastructure as nodes in your EKS cluster. Refer to the Hyrid Nodes [networking documentation](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-networking.html) to configure your on-premises network, node and pod CIDRs, access control, etc before creating your EKS Cluster.

Once you have identified the on-premises node and pod (optional) CIDRs you will use for your hybrid nodes and the workloads running on them, you can specify them during cluster creation using the `remoteNodeNetworks` and `remotePodNetworks` (optional) properties:

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer


eks.Cluster(self, "Cluster",
    version=eks.KubernetesVersion.V1_34,
    remote_node_networks=[eks.RemoteNodeNetwork(
        cidrs=["10.0.0.0/16"]
    )
    ],
    remote_pod_networks=[eks.RemotePodNetwork(
        cidrs=["192.168.0.0/16"]
    )
    ]
)
```

### Self-Managed Add-ons

Amazon EKS automatically installs self-managed add-ons such as the Amazon VPC CNI plugin for Kubernetes, kube-proxy, and CoreDNS for every cluster. You can change the default configuration of the add-ons and update them when desired. If you wish to create a cluster without the default add-ons, set `bootstrapSelfManagedAddons` as `false`. When this is set to false, make sure to install the necessary alternatives which provide functionality that enables pod and service operations for your EKS cluster.

> Changing the value of `bootstrapSelfManagedAddons` after the EKS cluster creation will result in a replacement of the cluster.

## Permissions and Security

In the new EKS module, `ConfigMap` is deprecated. Clusters created by the new module will use `API` as authentication mode. Access Entry will be the only way for granting permissions to specific IAM users and roles.

### Access Entry

An access entry is a cluster identity—directly linked to an AWS IAM principal user or role that is used to authenticate to
an Amazon EKS cluster. An Amazon EKS access policy authorizes an access entry to perform specific cluster actions.

Access policies are Amazon EKS-specific policies that assign Kubernetes permissions to access entries. Amazon EKS supports
only predefined and AWS managed policies. Access policies are not AWS IAM entities and are defined and managed by Amazon EKS.
Amazon EKS access policies include permission sets that support common use cases of administration, editing, or read-only access
to Kubernetes resources. See [Access Policy Permissions](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html#access-policy-permissions) for more details.

Use `AccessPolicy` to include predefined AWS managed policies:

```python
# AmazonEKSClusterAdminPolicy with `cluster` scope
eks.AccessPolicy.from_access_policy_name("AmazonEKSClusterAdminPolicy",
    access_scope_type=eks.AccessScopeType.CLUSTER
)
# AmazonEKSAdminPolicy with `namespace` scope
eks.AccessPolicy.from_access_policy_name("AmazonEKSAdminPolicy",
    access_scope_type=eks.AccessScopeType.NAMESPACE,
    namespaces=["foo", "bar"]
)
```

Use `grantAccess()` to grant the AccessPolicy to an IAM principal:

```python
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer
# vpc: ec2.Vpc


cluster_admin_role = iam.Role(self, "ClusterAdminRole",
    assumed_by=iam.ArnPrincipal("arn_for_trusted_principal")
)

eks_admin_role = iam.Role(self, "EKSAdminRole",
    assumed_by=iam.ArnPrincipal("arn_for_trusted_principal")
)

cluster = eks.Cluster(self, "Cluster",
    vpc=vpc,
    masters_role=cluster_admin_role,
    version=eks.KubernetesVersion.V1_34,
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl"),
        memory=Size.gibibytes(4)
    )
)

# Cluster Admin role for this cluster
cluster.grant_access("clusterAdminAccess", cluster_admin_role.role_arn, [
    eks.AccessPolicy.from_access_policy_name("AmazonEKSClusterAdminPolicy",
        access_scope_type=eks.AccessScopeType.CLUSTER
    )
])

# EKS Admin role for specified namespaces of this cluster
cluster.grant_access("eksAdminRoleAccess", eks_admin_role.role_arn, [
    eks.AccessPolicy.from_access_policy_name("AmazonEKSAdminPolicy",
        access_scope_type=eks.AccessScopeType.NAMESPACE,
        namespaces=["foo", "bar"]
    )
])
```

#### Access Entry Types

You can optionally specify an access entry type when granting access. This is particularly useful for EKS Auto Mode clusters with custom node roles, which require the `EC2` type:

```python
# cluster: eks.Cluster
# node_role: iam.Role


# Grant access with EC2 type for Auto Mode node role
cluster.grant_access("nodeAccess", node_role.role_arn, [
    eks.AccessPolicy.from_access_policy_name("AmazonEKSAutoNodePolicy",
        access_scope_type=eks.AccessScopeType.CLUSTER
    )
], access_entry_type=eks.AccessEntryType.EC2)
```

The following access entry types are supported:

* `STANDARD` - Default type for standard IAM principals (default when not specified)
* `FARGATE_LINUX` - For Fargate profiles
* `EC2_LINUX` - For EC2 Linux worker nodes
* `EC2_WINDOWS` - For EC2 Windows worker nodes
* `EC2` - For EKS Auto Mode node roles
* `HYBRID_LINUX` - For EKS Hybrid Nodes
* `HYPERPOD_LINUX` - For Amazon SageMaker HyperPod

**Note**: Access entries with type `EC2`, `HYBRID_LINUX`, or `HYPERPOD_LINUX` cannot have access policies attached per AWS EKS API constraints. For these types, use the `AccessEntry` construct directly with an empty access policies array.

By default, the cluster creator role will be granted the cluster admin permissions. You can disable it by setting
`bootstrapClusterCreatorAdminPermissions` to false.

> **Note** - Switching `bootstrapClusterCreatorAdminPermissions` on an existing cluster would cause cluster replacement and should be avoided in production.

### Service Accounts

With services account you can provide Kubernetes Pods access to AWS resources.

```python
import aws_cdk.aws_s3 as s3
# cluster: eks.Cluster

# add service account
service_account = cluster.add_service_account("MyServiceAccount")

bucket = s3.Bucket(self, "Bucket")
bucket.grant_read_write(service_account)

mypod = cluster.add_manifest("mypod", {
    "api_version": "v1",
    "kind": "Pod",
    "metadata": {"name": "mypod"},
    "spec": {
        "service_account_name": service_account.service_account_name,
        "containers": [{
            "name": "hello",
            "image": "paulbouwer/hello-kubernetes:1.5",
            "ports": [{"container_port": 8080}]
        }
        ]
    }
})

# create the resource after the service account.
mypod.node.add_dependency(service_account)

# print the IAM role arn for this service account
CfnOutput(self, "ServiceAccountIamRole", value=service_account.role.role_arn)
```

Note that using `serviceAccount.serviceAccountName` above **does not** translate into a resource dependency.
This is why an explicit dependency is needed. See [https://github.com/aws/aws-cdk/issues/9910](https://github.com/aws/aws-cdk/issues/9910) for more details.

It is possible to pass annotations and labels to the service account.

```python
# cluster: eks.Cluster

# add service account with annotations and labels
service_account = cluster.add_service_account("MyServiceAccount",
    annotations={
        "eks.amazonaws.com/sts-regional-endpoints": "false"
    },
    labels={
        "some-label": "with-some-value"
    }
)
```

You can also add service accounts to existing clusters.
To do so, pass the `openIdConnectProvider` property when you import the cluster into the application.

```python
import aws_cdk.aws_s3 as s3

# or create a new one using an existing issuer url
# issuer_url: str

from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer

# you can import an existing provider
provider = eks.OidcProviderNative.from_oidc_provider_arn(self, "Provider", "arn:aws:iam::123456:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/AB123456ABC")
provider2 = eks.OidcProviderNative(self, "Provider",
    url=issuer_url
)

cluster = eks.Cluster.from_cluster_attributes(self, "MyCluster",
    cluster_name="Cluster",
    open_id_connect_provider=provider,
    kubectl_provider_options=eks.KubectlProviderOptions(
        kubectl_layer=KubectlV35Layer(self, "kubectl")
    )
)

service_account = cluster.add_service_account("MyServiceAccount")

bucket = s3.Bucket(self, "Bucket")
bucket.grant_read_write(service_account)
```

Note that adding service accounts requires running `kubectl` commands against the cluster which requires you to provide `kubectlProviderOptions` in the cluster props to create the `kubectl` provider. See [Kubectl Support](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-eks-v2-readme.html#kubectl-support)

#### Migrating from the deprecated eks.OpenIdConnectProvider to eks.OidcProviderNative

`eks.OpenIdConnectProvider` creates an IAM OIDC (OpenId Connect) provider using a custom resource while `eks.OidcProviderNative` uses the CFN L1 (AWS::IAM::OidcProvider) to create the provider. It is recommended for new and existing projects to use `eks.OidcProviderNative`.

To migrate without temporarily removing the OIDCProvider, follow these steps:

1. Set the `removalPolicy` of `cluster.openIdConnectProvider` to `RETAIN`.

   ```python
   import aws_cdk as cdk
   # cluster: eks.Cluster


   cdk.RemovalPolicies.of(cluster.open_id_connect_provider).apply(cdk.RemovalPolicy.RETAIN)
   ```
2. Run `cdk diff` to verify the changes are expected then `cdk deploy`.
3. Add the following to the `context` field of your `cdk.json` to enable the feature flag that creates the native oidc provider.

   ```json
   "@aws-cdk/aws-eks:useNativeOidcProvider": true,
   ```
4. Run `cdk diff` and ensure the changes are expected. Example of an expected diff:

   ```bash
   Resources
   [-] Custom::AWSCDKOpenIdConnectProvider TestCluster/OpenIdConnectProvider/Resource TestClusterOpenIdConnectProviderE18F0FD0 orphan
   [-] AWS::IAM::Role Custom::AWSCDKOpenIdConnectProviderCustomResourceProvider/Role CustomAWSCDKOpenIdConnectProviderCustomResourceProviderRole517FED65 destroy
   [-] AWS::Lambda::Function Custom::AWSCDKOpenIdConnectProviderCustomResourceProvider/Handler CustomAWSCDKOpenIdConnectProviderCustomResourceProviderHandlerF2C543E0 destroy
   [+] AWS::IAM::OIDCProvider TestCluster/OidcProviderNative TestClusterOidcProviderNative0BE3F155
   ```
5. Run `cdk import --force` and provide the ARN of the existing OpenIdConnectProvider when prompted. You will get a warning about pending changes to existing resources which is expected.
6. Run `cdk deploy` to apply any pending changes. This will apply the destroy/orphan changes in the above example.

If you are creating the OpenIdConnectProvider manually via `new eks.OpenIdConnectProvider`, follow these steps:

1. Set the `removalPolicy` of the existing `OpenIdConnectProvider` to `RemovalPolicy.RETAIN`.

   ```python
   import aws_cdk as cdk

   # Step 1: Add retain policy to existing provider
   existing_provider = eks.OpenIdConnectProvider(self, "Provider",
       url="https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLE",
       removal_policy=cdk.RemovalPolicy.RETAIN
   )
   ```
2. Deploy with the retain policy to avoid deletion of the underlying resource.

   ```bash
   cdk deploy
   ```
3. Replace `OpenIdConnectProvider` with `OidcProviderNative` in your code.

   ```python
   # Step 3: Replace with native provider
   native_provider = eks.OidcProviderNative(self, "Provider",
       url="https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLE"
   )
   ```
4. Run `cdk diff` and verify the changes are expected. Example of an expected diff:

   ```bash
   Resources
   [-] Custom::AWSCDKOpenIdConnectProvider TestCluster/OpenIdConnectProvider/Resource TestClusterOpenIdConnectProviderE18F0FD0 orphan
   [-] AWS::IAM::Role Custom::AWSCDKOpenIdConnectProviderCustomResourceProvider/Role CustomAWSCDKOpenIdConnectProviderCustomResourceProviderRole517FED65 destroy
   [-] AWS::Lambda::Function Custom::AWSCDKOpenIdConnectProviderCustomResourceProvider/Handler CustomAWSCDKOpenIdConnectProviderCustomResourceProviderHandlerF2C543E0 destroy
   [+] AWS::IAM::OIDCProvider TestCluster/OidcProviderNative TestClusterOidcProviderNative0BE3F155
   ```
5. Run `cdk import --force` to import the existing OIDC provider resource by providing the existing ARN.
6. Run `cdk deploy` to apply any pending changes. This will apply the destroy/orphan operations in the example diff above.

### Cluster Security Group

When you create an Amazon EKS cluster, a [cluster security group](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
is automatically created as well. This security group is designed to allow all traffic from the control plane and managed node groups to flow freely
between each other.

The ID for that security group can be retrieved after creating the cluster.

```python
# cluster: eks.Cluster

cluster_security_group_id = cluster.cluster_security_group_id
```

## Applying Kubernetes Resources

To apply kubernetes resource, kubectl provider needs to be created for the cluster. You can use `kubectlProviderOptions` to create the kubectl Provider.

The library supports several popular resource deployment mechanisms, among which are:

### Kubernetes Manifests

The `KubernetesManifest` construct or `cluster.addManifest` method can be used
to apply Kubernetes resource manifests to this cluster.

> When using `cluster.addManifest`, the manifest construct is defined within the cluster's stack scope. If the manifest contains
> attributes from a different stack which depend on the cluster stack, a circular dependency will be created and you will get a synth time error.
> To avoid this, directly use `new KubernetesManifest` to create the manifest in the scope of the other stack.

The following examples will deploy the [paulbouwer/hello-kubernetes](https://github.com/paulbouwer/hello-kubernetes)
service on the cluster:

```python
# cluster: eks.Cluster

app_label = {"app": "hello-kubernetes"}

deployment = {
    "api_version": "apps/v1",
    "kind": "Deployment",
    "metadata": {"name": "hello-kubernetes"},
    "spec": {
        "replicas": 3,
        "selector": {"match_labels": app_label},
        "template": {
            "metadata": {"labels": app_label},
            "spec": {
                "containers": [{
                    "name": "hello-kubernetes",
                    "image": "paulbouwer/hello-kubernetes:1.5",
                    "ports": [{"container_port": 8080}]
                }
                ]
            }
        }
    }
}

service = {
    "api_version": "v1",
    "kind": "Service",
    "metadata": {"name": "hello-kubernetes"},
    "spec": {
        "type": "LoadBalancer",
        "ports": [{"port": 80, "target_port": 8080}],
        "selector": app_label
    }
}

# option 1: use a construct
eks.KubernetesManifest(self, "hello-kub",
    cluster=cluster,
    manifest=[deployment, service]
)

# or, option2: use `addManifest`
cluster.add_manifest("hello-kub", service, deployment)
```

#### ALB Controller Integration

The `KubernetesManifest` construct can detect ingress resources inside your manifest and automatically add the necessary annotations
so they are picked up by the ALB Controller.

> See [Alb Controller](#alb-controller)

To that end, it offers the following properties:

* `ingressAlb` - Signal that the ingress detection should be done.
* `ingressAlbScheme` - Which ALB scheme should be applied. Defaults to `internal`.

#### Adding resources from a URL

The following example will deploy the resource manifest hosting on remote server:

```text
// This example is only available in TypeScript

import * as yaml from 'js-yaml';
import * as request from 'sync-request';

declare const cluster: eks.Cluster;
const manifestUrl = 'https://url/of/manifest.yaml';
const manifest = yaml.safeLoadAll(request('GET', manifestUrl).getBody());
cluster.addManifest('my-resource', manifest);
```

#### Dependencies

There are cases where Kubernetes resources must be deployed in a specific order.
For example, you cannot define a resource in a Kubernetes namespace before the
namespace was created.

You can represent dependencies between `KubernetesManifest`s using
`resource.node.addDependency()`:

```python
# cluster: eks.Cluster

namespace = cluster.add_manifest("my-namespace", {
    "api_version": "v1",
    "kind": "Namespace",
    "metadata": {"name": "my-app"}
})

service = cluster.add_manifest("my-service", {
    "metadata": {
        "name": "myservice",
        "namespace": "my-app"
    },
    "spec": {}
})

service.node.add_dependency(namespace)
```

**NOTE:** when a `KubernetesManifest` includes multiple resources (either directly
or through `cluster.addManifest()`) (e.g. `cluster.addManifest('foo', r1, r2, r3,...)`), these resources will be applied as a single manifest via `kubectl`
and will be applied sequentially (the standard behavior in `kubectl`).

---


Since Kubernetes manifests are implemented as CloudFormation resources in the
CDK. This means that if the manifest is deleted from your code (or the stack is
deleted), the next `cdk deploy` will issue a `kubectl delete` command and the
Kubernetes resources in that manifest will be deleted.

#### Resource Pruning

When a resource is deleted from a Kubernetes manifest, the EKS module will
automatically delete these resources by injecting a *prune label* to all
manifest resources. This label is then passed to [`kubectl apply --prune`](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune-l-your-label).

Pruning is enabled by default but can be disabled through the `prune` option
when a cluster is defined:

```python
eks.Cluster(self, "MyCluster",
    version=eks.KubernetesVersion.V1_34,
    prune=False
)
```

#### Manifests Validation

The `kubectl` CLI supports applying a manifest by skipping the validation.
This can be accomplished by setting the `skipValidation` flag to `true` in the `KubernetesManifest` props.

```python
# cluster: eks.Cluster

eks.KubernetesManifest(self, "HelloAppWithoutValidation",
    cluster=cluster,
    manifest=[{"foo": "bar"}],
    skip_validation=True
)
```

### Helm Charts

The `HelmChart` construct or `cluster.addHelmChart` method can be used
to add Kubernetes resources to this cluster using Helm.

> When using `cluster.addHelmChart`, the manifest construct is defined within the cluster's stack scope. If the manifest contains
> attributes from a different stack which depend on the cluster stack, a circular dependency will be created and you will get a synth time error.
> To avoid this, directly use `new HelmChart` to create the chart in the scope of the other stack.

The following example will install the [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/) to your cluster using Helm.

```python
# cluster: eks.Cluster

# option 1: use a construct
eks.HelmChart(self, "NginxIngress",
    cluster=cluster,
    chart="nginx-ingress",
    repository="https://helm.nginx.com/stable",
    namespace="kube-system"
)

# or, option2: use `addHelmChart`
cluster.add_helm_chart("NginxIngress",
    chart="nginx-ingress",
    repository="https://helm.nginx.com/stable",
    namespace="kube-system"
)
```

Helm charts will be installed and updated using `helm upgrade --install`, where a few parameters
are being passed down (such as `repo`, `values`, `version`, `namespace`, `wait`, `timeout`, etc).
This means that if the chart is added to CDK with the same release name, it will try to update
the chart in the cluster.

Additionally, the `chartAsset` property can be an `aws-s3-assets.Asset`. This allows the use of local, private helm charts.

```python
import aws_cdk.aws_s3_assets as s3_assets

# cluster: eks.Cluster

chart_asset = s3_assets.Asset(self, "ChartAsset",
    path="/path/to/asset"
)

cluster.add_helm_chart("test-chart",
    chart_asset=chart_asset
)
```

Nested values passed to the `values` parameter should be provided as a nested dictionary:

```python
# cluster: eks.Cluster


cluster.add_helm_chart("ExternalSecretsOperator",
    chart="external-secrets",
    release="external-secrets",
    repository="https://charts.external-secrets.io",
    namespace="external-secrets",
    values={
        "install_cRDs": True,
        "webhook": {
            "port": 9443
        }
    }
)
```

Helm chart can come with Custom Resource Definitions (CRDs) defined that by default will be installed by helm as well. However in special cases it might be needed to skip the installation of CRDs, for that the property `skipCrds` can be used.

```python
# cluster: eks.Cluster

# option 1: use a construct
eks.HelmChart(self, "NginxIngress",
    cluster=cluster,
    chart="nginx-ingress",
    repository="https://helm.nginx.com/stable",
    namespace="kube-system",
    skip_crds=True
)
```

### OCI Charts

OCI charts are also supported.
Also replace the `${VARS}` with appropriate values.

```python
# cluster: eks.Cluster

# option 1: use a construct
eks.HelmChart(self, "MyOCIChart",
    cluster=cluster,
    chart="some-chart",
    repository="oci://${ACCOUNT_ID}.dkr.ecr.${ACCOUNT_REGION}.amazonaws.com/${REPO_NAME}",
    namespace="oci",
    version="0.0.1"
)
```

Helm charts are implemented as CloudFormation resources in CDK.
This means that if the chart is deleted from your code (or the stack is
deleted), the next `cdk deploy` will issue a `helm uninstall` command and the
Helm chart will be deleted.

When there is no `release` defined, a unique ID will be allocated for the release based
on the construct path.

By default, all Helm charts will be installed concurrently. In some cases, this
could cause race conditions where two Helm charts attempt to deploy the same
resource or if Helm charts depend on each other. You can use
`chart.node.addDependency()` in order to declare a dependency order between
charts:

```python
# cluster: eks.Cluster

chart1 = cluster.add_helm_chart("MyChart",
    chart="foo"
)
chart2 = cluster.add_helm_chart("MyChart",
    chart="bar"
)

chart2.node.add_dependency(chart1)
```

#### Custom CDK8s Constructs

You can also compose a few stock `cdk8s+` constructs into your own custom construct. However, since mixing scopes between `aws-cdk` and `cdk8s` is currently not supported, the `Construct` class
you'll need to use is the one from the [`constructs`](https://github.com/aws/constructs) module, and not from `aws-cdk-lib` like you normally would.
This is why we used `new cdk8s.App()` as the scope of the chart above.

```python
import constructs as constructs
import cdk8s as cdk8s
import cdk8s_plus_25 as kplus


app = cdk8s.App()
chart = cdk8s.Chart(app, "my-chart")

class LoadBalancedWebService(constructs.Construct):
    def __init__(self, scope, id, props):
        super().__init__(scope, id)

        deployment = kplus.Deployment(chart, "Deployment",
            replicas=props.replicas,
            containers=[kplus.Container(image=props.image)]
        )

        deployment.expose_via_service(
            ports=[kplus.ServicePort(port=props.port)
            ],
            service_type=kplus.ServiceType.LOAD_BALANCER
        )
```

#### Manually importing k8s specs and CRD's

If you find yourself unable to use `cdk8s+`, or just like to directly use the `k8s` native objects or CRD's, you can do so by manually importing them using the `cdk8s-cli`.

See [Importing kubernetes objects](https://cdk8s.io/docs/latest/cli/import/) for detailed instructions.

## Patching Kubernetes Resources

The `KubernetesPatch` construct can be used to update existing kubernetes
resources. The following example can be used to patch the `hello-kubernetes`
deployment from the example above with 5 replicas.

```python
# cluster: eks.Cluster

eks.KubernetesPatch(self, "hello-kub-deployment-label",
    cluster=cluster,
    resource_name="deployment/hello-kubernetes",
    apply_patch={"spec": {"replicas": 5}},
    restore_patch={"spec": {"replicas": 3}}
)
```

## Querying Kubernetes Resources

The `KubernetesObjectValue` construct can be used to query for information about kubernetes objects,
and use that as part of your CDK application.

For example, you can fetch the address of a [`LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) type service:

```python
# cluster: eks.Cluster

# query the load balancer address
my_service_address = eks.KubernetesObjectValue(self, "LoadBalancerAttribute",
    cluster=cluster,
    object_type="service",
    object_name="my-service",
    json_path=".status.loadBalancer.ingress[0].hostname"
)

# pass the address to a lambda function
proxy_function = lambda_.Function(self, "ProxyFunction",
    handler="index.handler",
    code=lambda_.Code.from_inline("my-code"),
    runtime=lambda_.Runtime.NODEJS_LATEST,
    environment={
        "my_service_address": my_service_address.value
    }
)
```

Specifically, since the above use-case is quite common, there is an easier way to access that information:

```python
# cluster: eks.Cluster

load_balancer_address = cluster.get_service_load_balancer_address("my-service")
```

## Add-ons

[Add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) is a software that provides supporting operational capabilities to Kubernetes applications. The EKS module supports adding add-ons to your cluster using the `eks.Addon` class.

```python
# cluster: eks.Cluster


eks.Addon(self, "Addon",
    cluster=cluster,
    addon_name="coredns",
    addon_version="v1.11.4-eksbuild.2",
    # whether to preserve the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on.
    preserve_on_delete=False,
    configuration_values={
        "replica_count": 2
    }
)
```

## Using existing clusters

The EKS library allows defining Kubernetes resources such as [Kubernetes
manifests](#kubernetes-resources) and [Helm charts](#helm-charts) on clusters
that are not defined as part of your CDK app.

First you will need to import the kubectl provider and cluster created in another stack

```python
handler_role = iam.Role.from_role_arn(self, "HandlerRole", "arn:aws:iam::123456789012:role/lambda-role")

kubectl_provider = eks.KubectlProvider.from_kubectl_provider_attributes(self, "KubectlProvider",
    service_token="arn:aws:lambda:us-east-2:123456789012:function:my-function:1",
    role=handler_role
)

cluster = eks.Cluster.from_cluster_attributes(self, "Cluster",
    cluster_name="cluster",
    kubectl_provider=kubectl_provider
)
```

Then, you can use `addManifest` or `addHelmChart` to define resources inside
your Kubernetes cluster.

```python
# cluster: eks.Cluster

cluster.add_manifest("Test", {
    "api_version": "v1",
    "kind": "ConfigMap",
    "metadata": {
        "name": "myconfigmap"
    },
    "data": {
        "Key": "value",
        "Another": "123454"
    }
})
```

## Logging

EKS supports cluster logging for 5 different types of events:

* API requests to the cluster.
* Cluster access via the Kubernetes API.
* Authentication requests into the cluster.
* State of cluster controllers.
* Scheduling decisions.

You can enable logging for each one separately using the `clusterLogging`
property. For example:

```python
cluster = eks.Cluster(self, "Cluster",
    # ...
    version=eks.KubernetesVersion.V1_34,
    cluster_logging=[eks.ClusterLoggingTypes.API, eks.ClusterLoggingTypes.AUTHENTICATOR, eks.ClusterLoggingTypes.SCHEDULER
    ]
)
```

## NodeGroup Repair Config

You can enable Managed Node Group [auto-repair config](https://docs.aws.amazon.com/eks/latest/userguide/node-health.html#node-auto-repair) using `enableNodeAutoRepair`
property. For example:

```python
# cluster: eks.Cluster


cluster.add_nodegroup_capacity("NodeGroup",
    enable_node_auto_repair=True
)
```
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    Duration as _Duration_4839e8c3,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    Size as _Size_7b441c34,
    TagManager as _TagManager_0a598cb3,
)
from ..aws_autoscaling import (
    AutoScalingGroup as _AutoScalingGroup_c547a7b9,
    BlockDevice as _BlockDevice_0cfc0568,
    CapacityDistributionStrategy as _CapacityDistributionStrategy_2393ccfe,
    CommonAutoScalingGroupProps as _CommonAutoScalingGroupProps_808bbf2d,
    DeletionProtection as _DeletionProtection_3beb1830,
    GroupMetrics as _GroupMetrics_7cdf729b,
    HealthCheck as _HealthCheck_03a4bd5a,
    HealthChecks as _HealthChecks_b8757873,
    Monitoring as _Monitoring_50020f91,
    NotificationConfiguration as _NotificationConfiguration_d5911670,
    Signals as _Signals_69fbeb6e,
    TerminationPolicy as _TerminationPolicy_89633c56,
    UpdatePolicy as _UpdatePolicy_6dffc7ca,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8,
    IConnectable as _IConnectable_10015a05,
    IKeyPair as _IKeyPair_bc344eda,
    IMachineImage as _IMachineImage_0e8bd50b,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    ISubnet as _ISubnet_d57d1229,
    IVpc as _IVpc_f30d5663,
    InstanceType as _InstanceType_f64915b9,
    MachineImageConfig as _MachineImageConfig_187edaee,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import (
    AddToPrincipalPolicyResult as _AddToPrincipalPolicyResult_946c9561,
    IOpenIdConnectProvider as _IOpenIdConnectProvider_203f0793,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    OidcProviderNative as _OidcProviderNative_18002ae4,
    OpenIdConnectProvider as _OpenIdConnectProvider_5cb7bc9f,
    PolicyStatement as _PolicyStatement_0fe33853,
    PrincipalPolicyFragment as _PrincipalPolicyFragment_6a855d11,
)
from ..aws_lambda import ILayerVersion as _ILayerVersion_5ac127c8
from ..aws_s3_assets import Asset as _Asset_ac2a7e61
from ..interfaces.aws_eks import (
    AccessEntryReference as _AccessEntryReference_447195cd,
    AddonReference as _AddonReference_afb1bd13,
    ClusterReference as _ClusterReference_d6e6b9ff,
    IAccessEntryRef as _IAccessEntryRef_14bb9c0a,
    IAddonRef as _IAddonRef_fb5de88c,
    IClusterRef as _IClusterRef_5527f448,
    INodegroupRef as _INodegroupRef_cac0d8aa,
    NodegroupReference as _NodegroupReference_eab944f6,
)
from ..interfaces.aws_kms import IKeyRef as _IKeyRef_d4fc6ef3


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessEntryAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "access_entry_arn": "accessEntryArn",
        "access_entry_name": "accessEntryName",
    },
)
class AccessEntryAttributes:
    def __init__(
        self,
        *,
        access_entry_arn: builtins.str,
        access_entry_name: builtins.str,
    ) -> None:
        '''Represents the attributes of an access entry.

        :param access_entry_arn: The Amazon Resource Name (ARN) of the access entry.
        :param access_entry_name: The name of the access entry.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            access_entry_attributes = eks_v2.AccessEntryAttributes(
                access_entry_arn="accessEntryArn",
                access_entry_name="accessEntryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ff0d4e31fc232f50ec6deba77cb81f4fb5845640f58041046e6014a98f5349)
            check_type(argname="argument access_entry_arn", value=access_entry_arn, expected_type=type_hints["access_entry_arn"])
            check_type(argname="argument access_entry_name", value=access_entry_name, expected_type=type_hints["access_entry_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_entry_arn": access_entry_arn,
            "access_entry_name": access_entry_name,
        }

    @builtins.property
    def access_entry_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access entry.'''
        result = self._values.get("access_entry_arn")
        assert result is not None, "Required property 'access_entry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_entry_name(self) -> builtins.str:
        '''The name of the access entry.'''
        result = self._values.get("access_entry_name")
        assert result is not None, "Required property 'access_entry_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessEntryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessEntryProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policies": "accessPolicies",
        "cluster": "cluster",
        "principal": "principal",
        "access_entry_name": "accessEntryName",
        "access_entry_type": "accessEntryType",
        "removal_policy": "removalPolicy",
    },
)
class AccessEntryProps:
    def __init__(
        self,
        *,
        access_policies: typing.Sequence["IAccessPolicy"],
        cluster: "ICluster",
        principal: builtins.str,
        access_entry_name: typing.Optional[builtins.str] = None,
        access_entry_type: typing.Optional["AccessEntryType"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Represents the properties required to create an Amazon EKS access entry.

        :param access_policies: The access policies that define the permissions and scope for the access entry.
        :param cluster: The Amazon EKS cluster to which the access entry applies.
        :param principal: The Amazon Resource Name (ARN) of the principal (user or role) to associate the access entry with.
        :param access_entry_name: The name of the AccessEntry. Default: - No access entry name is provided
        :param access_entry_type: The type of the AccessEntry. Default: STANDARD
        :param removal_policy: The removal policy applied to the access entry. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_eks_v2 as eks_v2
            
            # access_policy: eks_v2.AccessPolicy
            # cluster: eks_v2.Cluster
            
            access_entry_props = eks_v2.AccessEntryProps(
                access_policies=[access_policy],
                cluster=cluster,
                principal="principal",
            
                # the properties below are optional
                access_entry_name="accessEntryName",
                access_entry_type=eks_v2.AccessEntryType.STANDARD,
                removal_policy=cdk.RemovalPolicy.DESTROY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41ffcd9c9b81f2eb3b57e856565badd460fd76ba6e94407016e97fbe71e2e93)
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument access_entry_name", value=access_entry_name, expected_type=type_hints["access_entry_name"])
            check_type(argname="argument access_entry_type", value=access_entry_type, expected_type=type_hints["access_entry_type"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_policies": access_policies,
            "cluster": cluster,
            "principal": principal,
        }
        if access_entry_name is not None:
            self._values["access_entry_name"] = access_entry_name
        if access_entry_type is not None:
            self._values["access_entry_type"] = access_entry_type
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def access_policies(self) -> typing.List["IAccessPolicy"]:
        '''The access policies that define the permissions and scope for the access entry.'''
        result = self._values.get("access_policies")
        assert result is not None, "Required property 'access_policies' is missing"
        return typing.cast(typing.List["IAccessPolicy"], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The Amazon EKS cluster to which the access entry applies.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the principal (user or role) to associate the access entry with.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_entry_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AccessEntry.

        :default: - No access entry name is provided
        '''
        result = self._values.get("access_entry_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_entry_type(self) -> typing.Optional["AccessEntryType"]:
        '''The type of the AccessEntry.

        :default: STANDARD
        '''
        result = self._values.get("access_entry_type")
        return typing.cast(typing.Optional["AccessEntryType"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the access entry.

        The removal policy controls what happens to the resources if they stop being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessEntryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.AccessEntryType")
class AccessEntryType(enum.Enum):
    '''Represents the different types of access entries that can be used in an Amazon EKS cluster.

    :enum: true
    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        # node_role: iam.Role
        
        
        # Grant access with EC2 type for Auto Mode node role
        cluster.grant_access("nodeAccess", node_role.role_arn, [
            eks.AccessPolicy.from_access_policy_name("AmazonEKSAutoNodePolicy",
                access_scope_type=eks.AccessScopeType.CLUSTER
            )
        ], access_entry_type=eks.AccessEntryType.EC2)
    '''

    STANDARD = "STANDARD"
    '''Represents a standard access entry.

    Use this type for standard IAM principals that need cluster access with policies.
    '''
    FARGATE_LINUX = "FARGATE_LINUX"
    '''Represents a Fargate Linux access entry.

    Use this type for AWS Fargate profiles running Linux containers.
    '''
    EC2_LINUX = "EC2_LINUX"
    '''Represents an EC2 Linux access entry.

    Use this type for self-managed EC2 instances running Linux that join the cluster as worker nodes.
    '''
    EC2_WINDOWS = "EC2_WINDOWS"
    '''Represents an EC2 Windows access entry.

    Use this type for self-managed EC2 instances running Windows that join the cluster as worker nodes.
    '''
    EC2 = "EC2"
    '''Represents an EC2 access entry for EKS Auto Mode.

    Use this type for node roles in EKS Auto Mode clusters where AWS automatically manages
    the compute infrastructure. This type cannot have access policies attached.

    :see: https://docs.aws.amazon.com/eks/latest/userguide/eks-auto-mode.html
    '''
    HYBRID_LINUX = "HYBRID_LINUX"
    '''Represents a Hybrid Linux access entry for EKS Hybrid Nodes.

    Use this type for on-premises or edge infrastructure running Linux that connects
    to your EKS cluster. This type cannot have access policies attached.

    :see: https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes.html
    '''
    HYPERPOD_LINUX = "HYPERPOD_LINUX"
    '''Represents a HyperPod Linux access entry for Amazon SageMaker HyperPod.

    Use this type for SageMaker HyperPod clusters that need access to your EKS cluster
    for distributed machine learning workloads. This type cannot have access policies attached.

    :see: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html
    '''


class AccessPolicyArn(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessPolicyArn",
):
    '''Represents an Amazon EKS Access Policy ARN.

    Amazon EKS Access Policies are used to control access to Amazon EKS clusters.

    :see: https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eks_v2 as eks_v2
        
        access_policy_arn = eks_v2.AccessPolicyArn.AMAZON_EKS_ADMIN_POLICY
    '''

    def __init__(self, policy_name: builtins.str) -> None:
        '''Constructs a new instance of the ``AccessEntry`` class.

        :param policy_name: - The name of the Amazon EKS access policy. This is used to construct the policy ARN.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a237b0f2cfab19d79117494ac74e6238ff1b3f480722f7397495ec42935073)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        jsii.create(self.__class__, self, [policy_name])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, policy_name: builtins.str) -> "AccessPolicyArn":
        '''Creates a new instance of the AccessPolicy class with the specified policy name.

        :param policy_name: The name of the access policy.

        :return: A new instance of the AccessPolicy class.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d82653df0194bb22dd76fc4eece2e78a6f4587af11e18bfb3e9af007005ec909)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        return typing.cast("AccessPolicyArn", jsii.sinvoke(cls, "of", [policy_name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_ADMIN_POLICY")
    def AMAZON_EKS_ADMIN_POLICY(cls) -> "AccessPolicyArn":
        '''The Amazon EKS Admin Policy.

        This access policy includes permissions that grant an IAM principal
        most permissions to resources. When associated to an access entry, its access scope is typically
        one or more Kubernetes namespaces.
        '''
        return typing.cast("AccessPolicyArn", jsii.sget(cls, "AMAZON_EKS_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_ADMIN_VIEW_POLICY")
    def AMAZON_EKS_ADMIN_VIEW_POLICY(cls) -> "AccessPolicyArn":
        '''The Amazon EKS Admin View Policy.

        This access policy includes permissions that grant an IAM principal
        access to list/view all resources in a cluster.
        '''
        return typing.cast("AccessPolicyArn", jsii.sget(cls, "AMAZON_EKS_ADMIN_VIEW_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_CLUSTER_ADMIN_POLICY")
    def AMAZON_EKS_CLUSTER_ADMIN_POLICY(cls) -> "AccessPolicyArn":
        '''The Amazon EKS Cluster Admin Policy.

        This access policy includes permissions that grant an IAM
        principal administrator access to a cluster. When associated to an access entry, its access scope
        is typically the cluster, rather than a Kubernetes namespace.
        '''
        return typing.cast("AccessPolicyArn", jsii.sget(cls, "AMAZON_EKS_CLUSTER_ADMIN_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_EDIT_POLICY")
    def AMAZON_EKS_EDIT_POLICY(cls) -> "AccessPolicyArn":
        '''The Amazon EKS Edit Policy.

        This access policy includes permissions that allow an IAM principal
        to edit most Kubernetes resources.
        '''
        return typing.cast("AccessPolicyArn", jsii.sget(cls, "AMAZON_EKS_EDIT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_VIEW_POLICY")
    def AMAZON_EKS_VIEW_POLICY(cls) -> "AccessPolicyArn":
        '''The Amazon EKS View Policy.

        This access policy includes permissions that grant an IAM principal
        access to list/view all resources in a cluster.
        '''
        return typing.cast("AccessPolicyArn", jsii.sget(cls, "AMAZON_EKS_VIEW_POLICY"))

    @builtins.property
    @jsii.member(jsii_name="policyArn")
    def policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyArn"))

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''- The name of the Amazon EKS access policy.

        This is used to construct the policy ARN.
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessPolicyNameOptions",
    jsii_struct_bases=[],
    name_mapping={"access_scope_type": "accessScopeType", "namespaces": "namespaces"},
)
class AccessPolicyNameOptions:
    def __init__(
        self,
        *,
        access_scope_type: "AccessScopeType",
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Represents the options required to create an Amazon EKS Access Policy using the ``fromAccessPolicyName()`` method.

        :param access_scope_type: The scope of the access policy. This determines the level of access granted by the policy.
        :param namespaces: An optional array of Kubernetes namespaces to which the access policy applies. Default: - no specific namespaces for this scope

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            # node_role: iam.Role
            
            
            # Grant access with EC2 type for Auto Mode node role
            cluster.grant_access("nodeAccess", node_role.role_arn, [
                eks.AccessPolicy.from_access_policy_name("AmazonEKSAutoNodePolicy",
                    access_scope_type=eks.AccessScopeType.CLUSTER
                )
            ], access_entry_type=eks.AccessEntryType.EC2)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dff1b0b387fb8027e6aac0f02cc65e0f2374f9905525c8e2820653e0a2e86ab0)
            check_type(argname="argument access_scope_type", value=access_scope_type, expected_type=type_hints["access_scope_type"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_scope_type": access_scope_type,
        }
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def access_scope_type(self) -> "AccessScopeType":
        '''The scope of the access policy.

        This determines the level of access granted by the policy.
        '''
        result = self._values.get("access_scope_type")
        assert result is not None, "Required property 'access_scope_type' is missing"
        return typing.cast("AccessScopeType", result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional array of Kubernetes namespaces to which the access policy applies.

        :default: - no specific namespaces for this scope
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyNameOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"access_scope": "accessScope", "policy": "policy"},
)
class AccessPolicyProps:
    def __init__(
        self,
        *,
        access_scope: typing.Union["AccessScope", typing.Dict[builtins.str, typing.Any]],
        policy: "AccessPolicyArn",
    ) -> None:
        '''Properties for configuring an Amazon EKS Access Policy.

        :param access_scope: The scope of the access policy, which determines the level of access granted.
        :param policy: The access policy itself, which defines the specific permissions.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            # access_policy_arn: eks_v2.AccessPolicyArn
            
            access_policy_props = eks_v2.AccessPolicyProps(
                access_scope=eks_v2.AccessScope(
                    type=eks_v2.AccessScopeType.NAMESPACE,
            
                    # the properties below are optional
                    namespaces=["namespaces"]
                ),
                policy=access_policy_arn
            )
        '''
        if isinstance(access_scope, dict):
            access_scope = AccessScope(**access_scope)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8865fa4a16d35049e4c14ad235632b968637b3b2ef3009b51b8dbb010dcbaaf)
            check_type(argname="argument access_scope", value=access_scope, expected_type=type_hints["access_scope"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_scope": access_scope,
            "policy": policy,
        }

    @builtins.property
    def access_scope(self) -> "AccessScope":
        '''The scope of the access policy, which determines the level of access granted.'''
        result = self._values.get("access_scope")
        assert result is not None, "Required property 'access_scope' is missing"
        return typing.cast("AccessScope", result)

    @builtins.property
    def policy(self) -> "AccessPolicyArn":
        '''The access policy itself, which defines the specific permissions.'''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast("AccessPolicyArn", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessScope",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "namespaces": "namespaces"},
)
class AccessScope:
    def __init__(
        self,
        *,
        type: "AccessScopeType",
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Represents the scope of an access policy.

        The scope defines the namespaces or cluster-level access granted by the policy.

        :param type: The scope type of the policy, either 'namespace' or 'cluster'.
        :param namespaces: A Kubernetes namespace that an access policy is scoped to. A value is required if you specified namespace for Type. Default: - no specific namespaces for this scope.

        :interface: AccessScope
        :property: {AccessScopeType} type - The scope type of the policy, either 'namespace' or 'cluster'.
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            access_scope = eks_v2.AccessScope(
                type=eks_v2.AccessScopeType.NAMESPACE,
            
                # the properties below are optional
                namespaces=["namespaces"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f22be5c9e99863839d12fee0ecae363a8a609eb9205801f3ace86534f407e3)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def type(self) -> "AccessScopeType":
        '''The scope type of the policy, either 'namespace' or 'cluster'.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("AccessScopeType", result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A Kubernetes namespace that an access policy is scoped to.

        A value is required if you specified
        namespace for Type.

        :default: - no specific namespaces for this scope.
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.AccessScopeType")
class AccessScopeType(enum.Enum):
    '''Represents the scope type of an access policy.

    The scope type determines the level of access granted by the policy.

    :enum: true
    :export: true
    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        # node_role: iam.Role
        
        
        # Grant access with EC2 type for Auto Mode node role
        cluster.grant_access("nodeAccess", node_role.role_arn, [
            eks.AccessPolicy.from_access_policy_name("AmazonEKSAutoNodePolicy",
                access_scope_type=eks.AccessScopeType.CLUSTER
            )
        ], access_entry_type=eks.AccessEntryType.EC2)
    '''

    NAMESPACE = "NAMESPACE"
    '''The policy applies to a specific namespace within the cluster.'''
    CLUSTER = "CLUSTER"
    '''The policy applies to the entire cluster.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AddonAttributes",
    jsii_struct_bases=[],
    name_mapping={"addon_name": "addonName", "cluster_name": "clusterName"},
)
class AddonAttributes:
    def __init__(self, *, addon_name: builtins.str, cluster_name: builtins.str) -> None:
        '''Represents the attributes of an addon for an Amazon EKS cluster.

        :param addon_name: The name of the addon.
        :param cluster_name: The name of the Amazon EKS cluster the addon is associated with.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            addon_attributes = eks_v2.AddonAttributes(
                addon_name="addonName",
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ada43f0a3b31dd320bd9eff13550c1f471682e5b0bda0a274f68a371bb6d87)
            check_type(argname="argument addon_name", value=addon_name, expected_type=type_hints["addon_name"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addon_name": addon_name,
            "cluster_name": cluster_name,
        }

    @builtins.property
    def addon_name(self) -> builtins.str:
        '''The name of the addon.'''
        result = self._values.get("addon_name")
        assert result is not None, "Required property 'addon_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the Amazon EKS cluster the addon is associated with.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddonAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AddonProps",
    jsii_struct_bases=[],
    name_mapping={
        "addon_name": "addonName",
        "cluster": "cluster",
        "addon_version": "addonVersion",
        "configuration_values": "configurationValues",
        "preserve_on_delete": "preserveOnDelete",
        "removal_policy": "removalPolicy",
    },
)
class AddonProps:
    def __init__(
        self,
        *,
        addon_name: builtins.str,
        cluster: "ICluster",
        addon_version: typing.Optional[builtins.str] = None,
        configuration_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        preserve_on_delete: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Properties for creating an Amazon EKS Add-On.

        :param addon_name: Name of the Add-On.
        :param cluster: The EKS cluster the Add-On is associated with.
        :param addon_version: Version of the Add-On. You can check all available versions with describe-addon-versions. For example, this lists all available versions for the ``eks-pod-identity-agent`` addon: $ aws eks describe-addon-versions --addon-name eks-pod-identity-agent --query 'addons[*].addonVersions[*].addonVersion' Default: the latest version.
        :param configuration_values: The configuration values for the Add-on. Default: - Use default configuration.
        :param preserve_on_delete: Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn't removed. Default: true
        :param removal_policy: The removal policy applied to the EKS add-on. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            
            eks.Addon(self, "Addon",
                cluster=cluster,
                addon_name="coredns",
                addon_version="v1.11.4-eksbuild.2",
                # whether to preserve the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on.
                preserve_on_delete=False,
                configuration_values={
                    "replica_count": 2
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d11ec069708c7b4208a323d8379cab46576729e75eb29e4c9e64df4e798fd88)
            check_type(argname="argument addon_name", value=addon_name, expected_type=type_hints["addon_name"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument addon_version", value=addon_version, expected_type=type_hints["addon_version"])
            check_type(argname="argument configuration_values", value=configuration_values, expected_type=type_hints["configuration_values"])
            check_type(argname="argument preserve_on_delete", value=preserve_on_delete, expected_type=type_hints["preserve_on_delete"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addon_name": addon_name,
            "cluster": cluster,
        }
        if addon_version is not None:
            self._values["addon_version"] = addon_version
        if configuration_values is not None:
            self._values["configuration_values"] = configuration_values
        if preserve_on_delete is not None:
            self._values["preserve_on_delete"] = preserve_on_delete
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def addon_name(self) -> builtins.str:
        '''Name of the Add-On.'''
        result = self._values.get("addon_name")
        assert result is not None, "Required property 'addon_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The EKS cluster the Add-On is associated with.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    @builtins.property
    def addon_version(self) -> typing.Optional[builtins.str]:
        '''Version of the Add-On.

        You can check all available versions with describe-addon-versions.
        For example, this lists all available versions for the ``eks-pod-identity-agent`` addon:
        $ aws eks describe-addon-versions --addon-name eks-pod-identity-agent
        --query 'addons[*].addonVersions[*].addonVersion'

        :default: the latest version.
        '''
        result = self._values.get("addon_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The configuration values for the Add-on.

        :default: - Use default configuration.
        '''
        result = self._values.get("configuration_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def preserve_on_delete(self) -> typing.Optional[builtins.bool]:
        '''Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on.

        If an IAM account is associated with the add-on, it isn't removed.

        :default: true
        '''
        result = self._values.get("preserve_on_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the EKS add-on.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddonProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbController(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.AlbController",
):
    '''Construct for installing the AWS ALB Contoller on EKS clusters.

    Use the factory functions ``get`` and ``getOrCreate`` to obtain/create instances of this controller.

    :see: https://kubernetes-sigs.github.io/aws-load-balancer-controller
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_eks_v2 as eks_v2
        
        # additional_helm_chart_values: Any
        # alb_controller_version: eks_v2.AlbControllerVersion
        # cluster: eks_v2.Cluster
        # policy: Any
        
        alb_controller = eks_v2.AlbController(self, "MyAlbController",
            cluster=cluster,
            version=alb_controller_version,
        
            # the properties below are optional
            additional_helm_chart_values={
                "additional_helm_chart_values_key": additional_helm_chart_values
            },
            overwrite_service_account=False,
            policy=policy,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            repository="repository"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "Cluster",
        version: "AlbControllerVersion",
        additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        policy: typing.Any = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: [disable-awslint:ref-via-interface] Cluster to install the controller onto.
        :param version: Version of the controller.
        :param additional_helm_chart_values: Additional helm chart values for ALB controller. For available options, see: https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/helm/aws-load-balancer-controller/values.yaml Default: - no additional helm chart values
        :param overwrite_service_account: Overwrite any existing ALB controller service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the ALB controller service account is created. Otherwise, if there is already a service account named 'aws-load-balancer-controller' in the kube-system namespace, the operation will fail. Default: false
        :param policy: The IAM policy to apply to the service account. If you're using one of the built-in versions, this is not required since CDK ships with the appropriate policies for those versions. However, if you are using a custom version, this is required (and validated). Default: - Corresponds to the predefined version.
        :param removal_policy: The removal policy applied to the ALB controller resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository to pull the controller image from. Note that the default repository works for most regions, but not all. If the repository is not applicable to your region, use a custom repository according to the information here: https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases. Default: '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon/aws-load-balancer-controller'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de1a5fab31e27ea56ec8314431ac439667aa7b3a5634280a9817f052982292c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AlbControllerProps(
            cluster=cluster,
            version=version,
            additional_helm_chart_values=additional_helm_chart_values,
            overwrite_service_account=overwrite_service_account,
            policy=policy,
            removal_policy=removal_policy,
            repository=repository,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="create")
    @builtins.classmethod
    def create(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        *,
        cluster: "Cluster",
        version: "AlbControllerVersion",
        additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        policy: typing.Any = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
    ) -> "AlbController":
        '''Create the controller construct associated with this cluster and scope.

        Singleton per stack/cluster.

        :param scope: -
        :param cluster: [disable-awslint:ref-via-interface] Cluster to install the controller onto.
        :param version: Version of the controller.
        :param additional_helm_chart_values: Additional helm chart values for ALB controller. For available options, see: https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/helm/aws-load-balancer-controller/values.yaml Default: - no additional helm chart values
        :param overwrite_service_account: Overwrite any existing ALB controller service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the ALB controller service account is created. Otherwise, if there is already a service account named 'aws-load-balancer-controller' in the kube-system namespace, the operation will fail. Default: false
        :param policy: The IAM policy to apply to the service account. If you're using one of the built-in versions, this is not required since CDK ships with the appropriate policies for those versions. However, if you are using a custom version, this is required (and validated). Default: - Corresponds to the predefined version.
        :param removal_policy: The removal policy applied to the ALB controller resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository to pull the controller image from. Note that the default repository works for most regions, but not all. If the repository is not applicable to your region, use a custom repository according to the information here: https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases. Default: '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon/aws-load-balancer-controller'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d1cff94c29713e5c5b7bb7ba2b00b4278e38ed60ba8a6db024eea79b759762)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        props = AlbControllerProps(
            cluster=cluster,
            version=version,
            additional_helm_chart_values=additional_helm_chart_values,
            overwrite_service_account=overwrite_service_account,
            policy=policy,
            removal_policy=removal_policy,
            repository=repository,
        )

        return typing.cast("AlbController", jsii.sinvoke(cls, "create", [scope, props]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AlbControllerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "additional_helm_chart_values": "additionalHelmChartValues",
        "overwrite_service_account": "overwriteServiceAccount",
        "policy": "policy",
        "removal_policy": "removalPolicy",
        "repository": "repository",
    },
)
class AlbControllerOptions:
    def __init__(
        self,
        *,
        version: "AlbControllerVersion",
        additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        policy: typing.Any = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for ``AlbController``.

        :param version: Version of the controller.
        :param additional_helm_chart_values: Additional helm chart values for ALB controller. For available options, see: https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/helm/aws-load-balancer-controller/values.yaml Default: - no additional helm chart values
        :param overwrite_service_account: Overwrite any existing ALB controller service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the ALB controller service account is created. Otherwise, if there is already a service account named 'aws-load-balancer-controller' in the kube-system namespace, the operation will fail. Default: false
        :param policy: The IAM policy to apply to the service account. If you're using one of the built-in versions, this is not required since CDK ships with the appropriate policies for those versions. However, if you are using a custom version, this is required (and validated). Default: - Corresponds to the predefined version.
        :param removal_policy: The removal policy applied to the ALB controller resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository to pull the controller image from. Note that the default repository works for most regions, but not all. If the repository is not applicable to your region, use a custom repository according to the information here: https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases. Default: '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon/aws-load-balancer-controller'

        :exampleMetadata: infused

        Example::

            eks.Cluster(self, "HelloEKS",
                version=eks.KubernetesVersion.V1_34,
                alb_controller=eks.AlbControllerOptions(
                    version=eks.AlbControllerVersion.V2_8_2,
                    overwrite_service_account=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc3b82a59d8b4ad560f5757657e3397afe031e63d197ae8f3fc25327bece995d)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument additional_helm_chart_values", value=additional_helm_chart_values, expected_type=type_hints["additional_helm_chart_values"])
            check_type(argname="argument overwrite_service_account", value=overwrite_service_account, expected_type=type_hints["overwrite_service_account"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if additional_helm_chart_values is not None:
            self._values["additional_helm_chart_values"] = additional_helm_chart_values
        if overwrite_service_account is not None:
            self._values["overwrite_service_account"] = overwrite_service_account
        if policy is not None:
            self._values["policy"] = policy
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if repository is not None:
            self._values["repository"] = repository

    @builtins.property
    def version(self) -> "AlbControllerVersion":
        '''Version of the controller.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("AlbControllerVersion", result)

    @builtins.property
    def additional_helm_chart_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional helm chart values for ALB controller.

        For available options, see:
        https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/helm/aws-load-balancer-controller/values.yaml

        :default: - no additional helm chart values
        '''
        result = self._values.get("additional_helm_chart_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def overwrite_service_account(self) -> typing.Optional[builtins.bool]:
        '''Overwrite any existing ALB controller service account.

        If this is set, we will use ``kubectl apply`` instead of ``kubectl create``
        when the ALB controller service account is created. Otherwise, if there is already a service account
        named 'aws-load-balancer-controller' in the kube-system namespace, the operation will fail.

        :default: false
        '''
        result = self._values.get("overwrite_service_account")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''The IAM policy to apply to the service account.

        If you're using one of the built-in versions, this is not required since
        CDK ships with the appropriate policies for those versions.

        However, if you are using a custom version, this is required (and validated).

        :default: - Corresponds to the predefined version.
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the ALB controller resources.

        The removal policy controls what happens to the resources if they stop being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository to pull the controller image from.

        Note that the default repository works for most regions, but not all.
        If the repository is not applicable to your region, use a custom repository
        according to the information here: https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases.

        :default: '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon/aws-load-balancer-controller'
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbControllerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AlbControllerProps",
    jsii_struct_bases=[AlbControllerOptions],
    name_mapping={
        "version": "version",
        "additional_helm_chart_values": "additionalHelmChartValues",
        "overwrite_service_account": "overwriteServiceAccount",
        "policy": "policy",
        "removal_policy": "removalPolicy",
        "repository": "repository",
        "cluster": "cluster",
    },
)
class AlbControllerProps(AlbControllerOptions):
    def __init__(
        self,
        *,
        version: "AlbControllerVersion",
        additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        policy: typing.Any = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        cluster: "Cluster",
    ) -> None:
        '''Properties for ``AlbController``.

        :param version: Version of the controller.
        :param additional_helm_chart_values: Additional helm chart values for ALB controller. For available options, see: https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/helm/aws-load-balancer-controller/values.yaml Default: - no additional helm chart values
        :param overwrite_service_account: Overwrite any existing ALB controller service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the ALB controller service account is created. Otherwise, if there is already a service account named 'aws-load-balancer-controller' in the kube-system namespace, the operation will fail. Default: false
        :param policy: The IAM policy to apply to the service account. If you're using one of the built-in versions, this is not required since CDK ships with the appropriate policies for those versions. However, if you are using a custom version, this is required (and validated). Default: - Corresponds to the predefined version.
        :param removal_policy: The removal policy applied to the ALB controller resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository to pull the controller image from. Note that the default repository works for most regions, but not all. If the repository is not applicable to your region, use a custom repository according to the information here: https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases. Default: '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon/aws-load-balancer-controller'
        :param cluster: [disable-awslint:ref-via-interface] Cluster to install the controller onto.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_eks_v2 as eks_v2
            
            # additional_helm_chart_values: Any
            # alb_controller_version: eks_v2.AlbControllerVersion
            # cluster: eks_v2.Cluster
            # policy: Any
            
            alb_controller_props = eks_v2.AlbControllerProps(
                cluster=cluster,
                version=alb_controller_version,
            
                # the properties below are optional
                additional_helm_chart_values={
                    "additional_helm_chart_values_key": additional_helm_chart_values
                },
                overwrite_service_account=False,
                policy=policy,
                removal_policy=cdk.RemovalPolicy.DESTROY,
                repository="repository"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cde38e59a61de7f0bc23764fca6ef8ffc2d9c2007d5c7c13a0350fb7761eeb0)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument additional_helm_chart_values", value=additional_helm_chart_values, expected_type=type_hints["additional_helm_chart_values"])
            check_type(argname="argument overwrite_service_account", value=overwrite_service_account, expected_type=type_hints["overwrite_service_account"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
            "cluster": cluster,
        }
        if additional_helm_chart_values is not None:
            self._values["additional_helm_chart_values"] = additional_helm_chart_values
        if overwrite_service_account is not None:
            self._values["overwrite_service_account"] = overwrite_service_account
        if policy is not None:
            self._values["policy"] = policy
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if repository is not None:
            self._values["repository"] = repository

    @builtins.property
    def version(self) -> "AlbControllerVersion":
        '''Version of the controller.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("AlbControllerVersion", result)

    @builtins.property
    def additional_helm_chart_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional helm chart values for ALB controller.

        For available options, see:
        https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/helm/aws-load-balancer-controller/values.yaml

        :default: - no additional helm chart values
        '''
        result = self._values.get("additional_helm_chart_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def overwrite_service_account(self) -> typing.Optional[builtins.bool]:
        '''Overwrite any existing ALB controller service account.

        If this is set, we will use ``kubectl apply`` instead of ``kubectl create``
        when the ALB controller service account is created. Otherwise, if there is already a service account
        named 'aws-load-balancer-controller' in the kube-system namespace, the operation will fail.

        :default: false
        '''
        result = self._values.get("overwrite_service_account")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''The IAM policy to apply to the service account.

        If you're using one of the built-in versions, this is not required since
        CDK ships with the appropriate policies for those versions.

        However, if you are using a custom version, this is required (and validated).

        :default: - Corresponds to the predefined version.
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the ALB controller resources.

        The removal policy controls what happens to the resources if they stop being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository to pull the controller image from.

        Note that the default repository works for most regions, but not all.
        If the repository is not applicable to your region, use a custom repository
        according to the information here: https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases.

        :default: '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon/aws-load-balancer-controller'
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster(self) -> "Cluster":
        '''[disable-awslint:ref-via-interface] Cluster to install the controller onto.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("Cluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbControllerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbControllerVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.AlbControllerVersion",
):
    '''Controller version.

    Corresponds to the image tag of 'amazon/aws-load-balancer-controller' image.

    :exampleMetadata: infused

    Example::

        eks.Cluster(self, "HelloEKS",
            version=eks.KubernetesVersion.V1_34,
            alb_controller=eks.AlbControllerOptions(
                version=eks.AlbControllerVersion.V2_8_2,
                overwrite_service_account=True
            )
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(
        cls,
        version: builtins.str,
        helm_chart_version: typing.Optional[builtins.str] = None,
    ) -> "AlbControllerVersion":
        '''Specify a custom version and an associated helm chart version.

        Use this if the version you need is not available in one of the predefined versions.
        Note that in this case, you will also need to provide an IAM policy in the controller options.

        ALB controller version and helm chart version compatibility information can be found
        here: https://github.com/aws/eks-charts/blob/v0.0.133/stable/aws-load-balancer-controller/Chart.yaml

        :param version: The version number.
        :param helm_chart_version: The version of the helm chart. Version 1.4.1 is the default version to support legacy users.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e5bc4c0842880bd155fb4ca89e2ad6bd5ba51c35fef2f63867918ecb8a1264c)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument helm_chart_version", value=helm_chart_version, expected_type=type_hints["helm_chart_version"])
        return typing.cast("AlbControllerVersion", jsii.sinvoke(cls, "of", [version, helm_chart_version]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_0_0")
    def V2_0_0(cls) -> "AlbControllerVersion":
        '''v2.0.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_0_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_0_1")
    def V2_0_1(cls) -> "AlbControllerVersion":
        '''v2.0.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_0_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_1_0")
    def V2_1_0(cls) -> "AlbControllerVersion":
        '''v2.1.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_1_1")
    def V2_1_1(cls) -> "AlbControllerVersion":
        '''v2.1.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_1_2")
    def V2_1_2(cls) -> "AlbControllerVersion":
        '''v2.1.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_1_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_1_3")
    def V2_1_3(cls) -> "AlbControllerVersion":
        '''v2.1.3.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_1_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_2_0")
    def V2_2_0(cls) -> "AlbControllerVersion":
        '''v2.0.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_2_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_2_1")
    def V2_2_1(cls) -> "AlbControllerVersion":
        '''v2.2.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_2_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_2_2")
    def V2_2_2(cls) -> "AlbControllerVersion":
        '''v2.2.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_2_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_2_3")
    def V2_2_3(cls) -> "AlbControllerVersion":
        '''v2.2.3.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_2_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_2_4")
    def V2_2_4(cls) -> "AlbControllerVersion":
        '''v2.2.4.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_2_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_3_0")
    def V2_3_0(cls) -> "AlbControllerVersion":
        '''v2.3.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_3_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_3_1")
    def V2_3_1(cls) -> "AlbControllerVersion":
        '''v2.3.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_3_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_1")
    def V2_4_1(cls) -> "AlbControllerVersion":
        '''v2.4.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_2")
    def V2_4_2(cls) -> "AlbControllerVersion":
        '''v2.4.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_3")
    def V2_4_3(cls) -> "AlbControllerVersion":
        '''v2.4.3.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_4")
    def V2_4_4(cls) -> "AlbControllerVersion":
        '''v2.4.4.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_5")
    def V2_4_5(cls) -> "AlbControllerVersion":
        '''v2.4.5.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_6")
    def V2_4_6(cls) -> "AlbControllerVersion":
        '''v2.4.6.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_6"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_7")
    def V2_4_7(cls) -> "AlbControllerVersion":
        '''v2.4.7.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_4_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_5_0")
    def V2_5_0(cls) -> "AlbControllerVersion":
        '''v2.5.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_5_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_5_1")
    def V2_5_1(cls) -> "AlbControllerVersion":
        '''v2.5.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_5_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_5_2")
    def V2_5_2(cls) -> "AlbControllerVersion":
        '''v2.5.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_5_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_5_3")
    def V2_5_3(cls) -> "AlbControllerVersion":
        '''v2.5.3.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_5_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_5_4")
    def V2_5_4(cls) -> "AlbControllerVersion":
        '''v2.5.4.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_5_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_0")
    def V2_6_0(cls) -> "AlbControllerVersion":
        '''v2.6.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_6_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_1")
    def V2_6_1(cls) -> "AlbControllerVersion":
        '''v2.6.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_6_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_2")
    def V2_6_2(cls) -> "AlbControllerVersion":
        '''v2.6.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_6_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_7_0")
    def V2_7_0(cls) -> "AlbControllerVersion":
        '''v2.7.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_7_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_7_1")
    def V2_7_1(cls) -> "AlbControllerVersion":
        '''v2.7.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_7_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_7_2")
    def V2_7_2(cls) -> "AlbControllerVersion":
        '''v2.7.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_7_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_8_0")
    def V2_8_0(cls) -> "AlbControllerVersion":
        '''v2.8.0.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_8_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_8_1")
    def V2_8_1(cls) -> "AlbControllerVersion":
        '''v2.8.1.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_8_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_8_2")
    def V2_8_2(cls) -> "AlbControllerVersion":
        '''v2.8.2.'''
        return typing.cast("AlbControllerVersion", jsii.sget(cls, "V2_8_2"))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(self) -> builtins.bool:
        '''Whether or not its a custom version.'''
        return typing.cast(builtins.bool, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="helmChartVersion")
    def helm_chart_version(self) -> builtins.str:
        '''The version of the helm chart to use.'''
        return typing.cast(builtins.str, jsii.get(self, "helmChartVersion"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The version string.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.AlbScheme")
class AlbScheme(enum.Enum):
    '''ALB Scheme.

    :see: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.3/guide/ingress/annotations/#scheme
    '''

    INTERNAL = "INTERNAL"
    '''The nodes of an internal load balancer have only private IP addresses.

    The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes.
    Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.
    '''
    INTERNET_FACING = "INTERNET_FACING"
    '''An internet-facing load balancer has a publicly resolvable DNS name, so it can route requests from clients over the internet to the EC2 instances that are registered with the load balancer.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AutoScalingGroupCapacityOptions",
    jsii_struct_bases=[_CommonAutoScalingGroupProps_808bbf2d],
    name_mapping={
        "allow_all_outbound": "allowAllOutbound",
        "associate_public_ip_address": "associatePublicIpAddress",
        "auto_scaling_group_name": "autoScalingGroupName",
        "az_capacity_distribution_strategy": "azCapacityDistributionStrategy",
        "block_devices": "blockDevices",
        "capacity_rebalance": "capacityRebalance",
        "cooldown": "cooldown",
        "default_instance_warmup": "defaultInstanceWarmup",
        "deletion_protection": "deletionProtection",
        "desired_capacity": "desiredCapacity",
        "group_metrics": "groupMetrics",
        "health_check": "healthCheck",
        "health_checks": "healthChecks",
        "ignore_unmodified_size_properties": "ignoreUnmodifiedSizeProperties",
        "instance_monitoring": "instanceMonitoring",
        "key_name": "keyName",
        "key_pair": "keyPair",
        "max_capacity": "maxCapacity",
        "max_instance_lifetime": "maxInstanceLifetime",
        "min_capacity": "minCapacity",
        "new_instances_protected_from_scale_in": "newInstancesProtectedFromScaleIn",
        "notifications": "notifications",
        "signals": "signals",
        "spot_price": "spotPrice",
        "ssm_session_permissions": "ssmSessionPermissions",
        "termination_policies": "terminationPolicies",
        "termination_policy_custom_lambda_function_arn": "terminationPolicyCustomLambdaFunctionArn",
        "update_policy": "updatePolicy",
        "vpc_subnets": "vpcSubnets",
        "instance_type": "instanceType",
        "bootstrap_enabled": "bootstrapEnabled",
        "bootstrap_options": "bootstrapOptions",
        "machine_image_type": "machineImageType",
    },
)
class AutoScalingGroupCapacityOptions(_CommonAutoScalingGroupProps_808bbf2d):
    def __init__(
        self,
        *,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        associate_public_ip_address: typing.Optional[builtins.bool] = None,
        auto_scaling_group_name: typing.Optional[builtins.str] = None,
        az_capacity_distribution_strategy: typing.Optional["_CapacityDistributionStrategy_2393ccfe"] = None,
        block_devices: typing.Optional[typing.Sequence[typing.Union["_BlockDevice_0cfc0568", typing.Dict[builtins.str, typing.Any]]]] = None,
        capacity_rebalance: typing.Optional[builtins.bool] = None,
        cooldown: typing.Optional["_Duration_4839e8c3"] = None,
        default_instance_warmup: typing.Optional["_Duration_4839e8c3"] = None,
        deletion_protection: typing.Optional["_DeletionProtection_3beb1830"] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        group_metrics: typing.Optional[typing.Sequence["_GroupMetrics_7cdf729b"]] = None,
        health_check: typing.Optional["_HealthCheck_03a4bd5a"] = None,
        health_checks: typing.Optional["_HealthChecks_b8757873"] = None,
        ignore_unmodified_size_properties: typing.Optional[builtins.bool] = None,
        instance_monitoring: typing.Optional["_Monitoring_50020f91"] = None,
        key_name: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional["_IKeyPair_bc344eda"] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_instance_lifetime: typing.Optional["_Duration_4839e8c3"] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        new_instances_protected_from_scale_in: typing.Optional[builtins.bool] = None,
        notifications: typing.Optional[typing.Sequence[typing.Union["_NotificationConfiguration_d5911670", typing.Dict[builtins.str, typing.Any]]]] = None,
        signals: typing.Optional["_Signals_69fbeb6e"] = None,
        spot_price: typing.Optional[builtins.str] = None,
        ssm_session_permissions: typing.Optional[builtins.bool] = None,
        termination_policies: typing.Optional[typing.Sequence["_TerminationPolicy_89633c56"]] = None,
        termination_policy_custom_lambda_function_arn: typing.Optional[builtins.str] = None,
        update_policy: typing.Optional["_UpdatePolicy_6dffc7ca"] = None,
        vpc_subnets: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_type: "_InstanceType_f64915b9",
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[typing.Union["BootstrapOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        machine_image_type: typing.Optional["MachineImageType"] = None,
    ) -> None:
        '''Options for adding worker nodes.

        :param allow_all_outbound: Whether the instances can initiate connections to anywhere by default. Default: true
        :param associate_public_ip_address: Whether instances in the Auto Scaling Group should have public IP addresses associated with them. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: - Use subnet setting.
        :param auto_scaling_group_name: The name of the Auto Scaling group. This name must be unique per Region per account. Default: - Auto generated by CloudFormation
        :param az_capacity_distribution_strategy: The strategy for distributing instances across Availability Zones. Default: None
        :param block_devices: Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes. Each instance that is launched has an associated root device volume, either an Amazon EBS volume or an instance store volume. You can use block device mappings to specify additional EBS volumes or instance store volumes to attach to an instance when it is launched. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: - Uses the block device mapping of the AMI
        :param capacity_rebalance: Indicates whether Capacity Rebalancing is enabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. Default: false
        :param cooldown: Default scaling cooldown for this AutoScalingGroup. Default: Duration.minutes(5)
        :param default_instance_warmup: The amount of time, in seconds, until a newly launched instance can contribute to the Amazon CloudWatch metrics. This delay lets an instance finish initializing before Amazon EC2 Auto Scaling aggregates instance metrics, resulting in more reliable usage data. Set this value equal to the amount of time that it takes for resource consumption to become stable after an instance reaches the InService state. To optimize the performance of scaling policies that scale continuously, such as target tracking and step scaling policies, we strongly recommend that you enable the default instance warmup, even if its value is set to 0 seconds Default instance warmup will not be added if no value is specified Default: None
        :param deletion_protection: Deletion protection for the Auto Scaling group. Default: DeletionProtection.NONE
        :param desired_capacity: Initial amount of instances in the fleet. If this is set to a number, every deployment will reset the amount of instances to this number. It is recommended to leave this value blank. Default: minCapacity, and leave unchanged during deployment
        :param group_metrics: Enable monitoring for group metrics, these metrics describe the group rather than any of its instances. To report all group metrics use ``GroupMetrics.all()`` Group metrics are reported in a granularity of 1 minute at no additional charge. Default: - no group metrics will be reported
        :param health_check: (deprecated) Configuration for health checks. Default: - HealthCheck.ec2 with no grace period
        :param health_checks: Configuration for EC2 or additional health checks. Even when using ``HealthChecks.withAdditionalChecks()``, the EC2 type is implicitly included. Default: - EC2 type with no grace period
        :param ignore_unmodified_size_properties: If the ASG has scheduled actions, don't reset unchanged group sizes. Only used if the ASG has scheduled actions (which may scale your ASG up or down regardless of cdk deployments). If true, the size of the group will only be reset if it has been changed in the CDK app. If false, the sizes will always be changed back to what they were in the CDK app on deployment. Default: true
        :param instance_monitoring: Controls whether instances in this group are launched with detailed or basic monitoring. When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: - Monitoring.DETAILED
        :param key_name: (deprecated) Name of SSH keypair to grant access to instances. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified You can either specify ``keyPair`` or ``keyName``, not both. Default: - No SSH access will be possible.
        :param key_pair: The SSH keypair to grant access to the instance. Feature flag ``AUTOSCALING_GENERATE_LAUNCH_TEMPLATE`` must be enabled to use this property. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified. You can either specify ``keyPair`` or ``keyName``, not both. Default: - No SSH access will be possible.
        :param max_capacity: Maximum number of instances in the fleet. Default: desiredCapacity
        :param max_instance_lifetime: The maximum amount of time that an instance can be in service. The maximum duration applies to all current and future instances in the group. As an instance approaches its maximum duration, it is terminated and replaced, and cannot be used again. You must specify a value of at least 86,400 seconds (one day). To clear a previously set value, leave this property undefined. Default: none
        :param min_capacity: Minimum number of instances in the fleet. Default: 1
        :param new_instances_protected_from_scale_in: Whether newly-launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. By default, Auto Scaling can terminate an instance at any time after launch when scaling in an Auto Scaling Group, subject to the group's termination policy. However, you may wish to protect newly-launched instances from being scaled in if they are going to run critical applications that should not be prematurely terminated. This flag must be enabled if the Auto Scaling Group will be associated with an ECS Capacity Provider with managed termination protection. Default: false
        :param notifications: Configure autoscaling group to send notifications about fleet changes to an SNS topic(s). Default: - No fleet change notifications will be sent.
        :param signals: Configure waiting for signals during deployment. Use this to pause the CloudFormation deployment to wait for the instances in the AutoScalingGroup to report successful startup during creation and updates. The UserData script needs to invoke ``cfn-signal`` with a success or failure code after it is done setting up the instance. Without waiting for signals, the CloudFormation deployment will proceed as soon as the AutoScalingGroup has been created or updated but before the instances in the group have been started. For example, to have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check verification by using the cfn-init helper script. For an example, see the verify_instance_health command in the Auto Scaling rolling updates sample template: https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/AutoScaling/AutoScalingRollingUpdates.yaml Default: - Do not wait for signals
        :param spot_price: The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: none
        :param ssm_session_permissions: Add SSM session permissions to the instance role. Setting this to ``true`` adds the necessary permissions to connect to the instance using SSM Session Manager. You can do this from the AWS Console. NOTE: Setting this flag to ``true`` may not be enough by itself. You must also use an AMI that comes with the SSM Agent, or install the SSM Agent yourself. See `Working with SSM Agent <https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html>`_ in the SSM Developer Guide. Default: false
        :param termination_policies: A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. Default: - ``TerminationPolicy.DEFAULT``
        :param termination_policy_custom_lambda_function_arn: A lambda function Arn that can be used as a custom termination policy to select the instances to terminate. This property must be specified if the TerminationPolicy.CUSTOM_LAMBDA_FUNCTION is used. Default: - No lambda function Arn will be supplied
        :param update_policy: What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: - ``UpdatePolicy.rollingUpdate()`` if using ``init``, ``UpdatePolicy.none()`` otherwise
        :param vpc_subnets: Where to place instances within the VPC. Default: - All Private subnets.
        :param instance_type: Instance type of the instances to start.
        :param bootstrap_enabled: Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: EKS node bootstrapping options. Default: - none
        :param machine_image_type: Machine image type. Default: MachineImageType.AMAZON_LINUX_2

        :exampleMetadata: infused

        Example::

            cluster = eks.Cluster(self, "SelfManagedCluster",
                version=eks.KubernetesVersion.V1_34
            )
            
            # Add self-managed Auto Scaling Group
            cluster.add_auto_scaling_group_capacity("self-managed-asg",
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
                min_capacity=1,
                max_capacity=5
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if isinstance(bootstrap_options, dict):
            bootstrap_options = BootstrapOptions(**bootstrap_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391f701643a31c9041c2732176c0e9385d97aecf409a768988a75f2f7fbb1f00)
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument auto_scaling_group_name", value=auto_scaling_group_name, expected_type=type_hints["auto_scaling_group_name"])
            check_type(argname="argument az_capacity_distribution_strategy", value=az_capacity_distribution_strategy, expected_type=type_hints["az_capacity_distribution_strategy"])
            check_type(argname="argument block_devices", value=block_devices, expected_type=type_hints["block_devices"])
            check_type(argname="argument capacity_rebalance", value=capacity_rebalance, expected_type=type_hints["capacity_rebalance"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument default_instance_warmup", value=default_instance_warmup, expected_type=type_hints["default_instance_warmup"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument group_metrics", value=group_metrics, expected_type=type_hints["group_metrics"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument health_checks", value=health_checks, expected_type=type_hints["health_checks"])
            check_type(argname="argument ignore_unmodified_size_properties", value=ignore_unmodified_size_properties, expected_type=type_hints["ignore_unmodified_size_properties"])
            check_type(argname="argument instance_monitoring", value=instance_monitoring, expected_type=type_hints["instance_monitoring"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument max_instance_lifetime", value=max_instance_lifetime, expected_type=type_hints["max_instance_lifetime"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument new_instances_protected_from_scale_in", value=new_instances_protected_from_scale_in, expected_type=type_hints["new_instances_protected_from_scale_in"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
            check_type(argname="argument signals", value=signals, expected_type=type_hints["signals"])
            check_type(argname="argument spot_price", value=spot_price, expected_type=type_hints["spot_price"])
            check_type(argname="argument ssm_session_permissions", value=ssm_session_permissions, expected_type=type_hints["ssm_session_permissions"])
            check_type(argname="argument termination_policies", value=termination_policies, expected_type=type_hints["termination_policies"])
            check_type(argname="argument termination_policy_custom_lambda_function_arn", value=termination_policy_custom_lambda_function_arn, expected_type=type_hints["termination_policy_custom_lambda_function_arn"])
            check_type(argname="argument update_policy", value=update_policy, expected_type=type_hints["update_policy"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument bootstrap_enabled", value=bootstrap_enabled, expected_type=type_hints["bootstrap_enabled"])
            check_type(argname="argument bootstrap_options", value=bootstrap_options, expected_type=type_hints["bootstrap_options"])
            check_type(argname="argument machine_image_type", value=machine_image_type, expected_type=type_hints["machine_image_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
        }
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if auto_scaling_group_name is not None:
            self._values["auto_scaling_group_name"] = auto_scaling_group_name
        if az_capacity_distribution_strategy is not None:
            self._values["az_capacity_distribution_strategy"] = az_capacity_distribution_strategy
        if block_devices is not None:
            self._values["block_devices"] = block_devices
        if capacity_rebalance is not None:
            self._values["capacity_rebalance"] = capacity_rebalance
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if default_instance_warmup is not None:
            self._values["default_instance_warmup"] = default_instance_warmup
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if group_metrics is not None:
            self._values["group_metrics"] = group_metrics
        if health_check is not None:
            self._values["health_check"] = health_check
        if health_checks is not None:
            self._values["health_checks"] = health_checks
        if ignore_unmodified_size_properties is not None:
            self._values["ignore_unmodified_size_properties"] = ignore_unmodified_size_properties
        if instance_monitoring is not None:
            self._values["instance_monitoring"] = instance_monitoring
        if key_name is not None:
            self._values["key_name"] = key_name
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if max_instance_lifetime is not None:
            self._values["max_instance_lifetime"] = max_instance_lifetime
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if new_instances_protected_from_scale_in is not None:
            self._values["new_instances_protected_from_scale_in"] = new_instances_protected_from_scale_in
        if notifications is not None:
            self._values["notifications"] = notifications
        if signals is not None:
            self._values["signals"] = signals
        if spot_price is not None:
            self._values["spot_price"] = spot_price
        if ssm_session_permissions is not None:
            self._values["ssm_session_permissions"] = ssm_session_permissions
        if termination_policies is not None:
            self._values["termination_policies"] = termination_policies
        if termination_policy_custom_lambda_function_arn is not None:
            self._values["termination_policy_custom_lambda_function_arn"] = termination_policy_custom_lambda_function_arn
        if update_policy is not None:
            self._values["update_policy"] = update_policy
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if bootstrap_enabled is not None:
            self._values["bootstrap_enabled"] = bootstrap_enabled
        if bootstrap_options is not None:
            self._values["bootstrap_options"] = bootstrap_options
        if machine_image_type is not None:
            self._values["machine_image_type"] = machine_image_type

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether the instances can initiate connections to anywhere by default.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def associate_public_ip_address(self) -> typing.Optional[builtins.bool]:
        '''Whether instances in the Auto Scaling Group should have public IP addresses associated with them.

        ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified

        :default: - Use subnet setting.
        '''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_scaling_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Auto Scaling group.

        This name must be unique per Region per account.

        :default: - Auto generated by CloudFormation
        '''
        result = self._values.get("auto_scaling_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def az_capacity_distribution_strategy(
        self,
    ) -> typing.Optional["_CapacityDistributionStrategy_2393ccfe"]:
        '''The strategy for distributing instances across Availability Zones.

        :default: None
        '''
        result = self._values.get("az_capacity_distribution_strategy")
        return typing.cast(typing.Optional["_CapacityDistributionStrategy_2393ccfe"], result)

    @builtins.property
    def block_devices(self) -> typing.Optional[typing.List["_BlockDevice_0cfc0568"]]:
        '''Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes.

        Each instance that is launched has an associated root device volume,
        either an Amazon EBS volume or an instance store volume.
        You can use block device mappings to specify additional EBS volumes or
        instance store volumes to attach to an instance when it is launched.

        ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified

        :default: - Uses the block device mapping of the AMI

        :see: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html
        '''
        result = self._values.get("block_devices")
        return typing.cast(typing.Optional[typing.List["_BlockDevice_0cfc0568"]], result)

    @builtins.property
    def capacity_rebalance(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether Capacity Rebalancing is enabled.

        When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling
        attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of
        interruption. After launching a new instance, it then terminates an old instance.

        :default: false

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-capacityrebalance
        '''
        result = self._values.get("capacity_rebalance")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cooldown(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''Default scaling cooldown for this AutoScalingGroup.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    @builtins.property
    def default_instance_warmup(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''The amount of time, in seconds, until a newly launched instance can contribute to the Amazon CloudWatch metrics.

        This delay lets an instance finish initializing before Amazon EC2 Auto Scaling aggregates instance metrics,
        resulting in more reliable usage data. Set this value equal to the amount of time that it takes for resource
        consumption to become stable after an instance reaches the InService state.

        To optimize the performance of scaling policies that scale continuously, such as target tracking and
        step scaling policies, we strongly recommend that you enable the default instance warmup, even if its value is set to 0 seconds

        Default instance warmup will not be added if no value is specified

        :default: None

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html
        '''
        result = self._values.get("default_instance_warmup")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional["_DeletionProtection_3beb1830"]:
        '''Deletion protection for the Auto Scaling group.

        :default: DeletionProtection.NONE

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html#asg-deletion-protection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional["_DeletionProtection_3beb1830"], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Initial amount of instances in the fleet.

        If this is set to a number, every deployment will reset the amount of
        instances to this number. It is recommended to leave this value blank.

        :default: minCapacity, and leave unchanged during deployment

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-desiredcapacity
        '''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def group_metrics(self) -> typing.Optional[typing.List["_GroupMetrics_7cdf729b"]]:
        '''Enable monitoring for group metrics, these metrics describe the group rather than any of its instances.

        To report all group metrics use ``GroupMetrics.all()``
        Group metrics are reported in a granularity of 1 minute at no additional charge.

        :default: - no group metrics will be reported
        '''
        result = self._values.get("group_metrics")
        return typing.cast(typing.Optional[typing.List["_GroupMetrics_7cdf729b"]], result)

    @builtins.property
    def health_check(self) -> typing.Optional["_HealthCheck_03a4bd5a"]:
        '''(deprecated) Configuration for health checks.

        :default: - HealthCheck.ec2 with no grace period

        :deprecated: Use ``healthChecks`` instead

        :stability: deprecated
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["_HealthCheck_03a4bd5a"], result)

    @builtins.property
    def health_checks(self) -> typing.Optional["_HealthChecks_b8757873"]:
        '''Configuration for EC2 or additional health checks.

        Even when using ``HealthChecks.withAdditionalChecks()``, the EC2 type is implicitly included.

        :default: - EC2 type with no grace period

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html
        '''
        result = self._values.get("health_checks")
        return typing.cast(typing.Optional["_HealthChecks_b8757873"], result)

    @builtins.property
    def ignore_unmodified_size_properties(self) -> typing.Optional[builtins.bool]:
        '''If the ASG has scheduled actions, don't reset unchanged group sizes.

        Only used if the ASG has scheduled actions (which may scale your ASG up
        or down regardless of cdk deployments). If true, the size of the group
        will only be reset if it has been changed in the CDK app. If false, the
        sizes will always be changed back to what they were in the CDK app
        on deployment.

        :default: true
        '''
        result = self._values.get("ignore_unmodified_size_properties")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_monitoring(self) -> typing.Optional["_Monitoring_50020f91"]:
        '''Controls whether instances in this group are launched with detailed or basic monitoring.

        When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account
        is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes.

        ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified

        :default: - Monitoring.DETAILED

        :see: https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics
        '''
        result = self._values.get("instance_monitoring")
        return typing.cast(typing.Optional["_Monitoring_50020f91"], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Name of SSH keypair to grant access to instances.

        ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified

        You can either specify ``keyPair`` or ``keyName``, not both.

        :default: - No SSH access will be possible.

        :deprecated: - Use ``keyPair`` instead - https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2-readme.html#using-an-existing-ec2-key-pair

        :stability: deprecated
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_pair(self) -> typing.Optional["_IKeyPair_bc344eda"]:
        '''The SSH keypair to grant access to the instance.

        Feature flag ``AUTOSCALING_GENERATE_LAUNCH_TEMPLATE`` must be enabled to use this property.

        ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified.

        You can either specify ``keyPair`` or ``keyName``, not both.

        :default: - No SSH access will be possible.
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional["_IKeyPair_bc344eda"], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of instances in the fleet.

        :default: desiredCapacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_instance_lifetime(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''The maximum amount of time that an instance can be in service.

        The maximum duration applies
        to all current and future instances in the group. As an instance approaches its maximum duration,
        it is terminated and replaced, and cannot be used again.

        You must specify a value of at least 86,400 seconds (one day). To clear a previously set value,
        leave this property undefined.

        :default: none

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html
        '''
        result = self._values.get("max_instance_lifetime")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of instances in the fleet.

        :default: 1
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_instances_protected_from_scale_in(self) -> typing.Optional[builtins.bool]:
        '''Whether newly-launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.

        By default, Auto Scaling can terminate an instance at any time after launch
        when scaling in an Auto Scaling Group, subject to the group's termination
        policy. However, you may wish to protect newly-launched instances from
        being scaled in if they are going to run critical applications that should
        not be prematurely terminated.

        This flag must be enabled if the Auto Scaling Group will be associated with
        an ECS Capacity Provider with managed termination protection.

        :default: false
        '''
        result = self._values.get("new_instances_protected_from_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Optional[typing.List["_NotificationConfiguration_d5911670"]]:
        '''Configure autoscaling group to send notifications about fleet changes to an SNS topic(s).

        :default: - No fleet change notifications will be sent.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-notificationconfigurations
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.List["_NotificationConfiguration_d5911670"]], result)

    @builtins.property
    def signals(self) -> typing.Optional["_Signals_69fbeb6e"]:
        '''Configure waiting for signals during deployment.

        Use this to pause the CloudFormation deployment to wait for the instances
        in the AutoScalingGroup to report successful startup during
        creation and updates. The UserData script needs to invoke ``cfn-signal``
        with a success or failure code after it is done setting up the instance.

        Without waiting for signals, the CloudFormation deployment will proceed as
        soon as the AutoScalingGroup has been created or updated but before the
        instances in the group have been started.

        For example, to have instances wait for an Elastic Load Balancing health check before
        they signal success, add a health-check verification by using the
        cfn-init helper script. For an example, see the verify_instance_health
        command in the Auto Scaling rolling updates sample template:

        https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/AutoScaling/AutoScalingRollingUpdates.yaml

        :default: - Do not wait for signals
        '''
        result = self._values.get("signals")
        return typing.cast(typing.Optional["_Signals_69fbeb6e"], result)

    @builtins.property
    def spot_price(self) -> typing.Optional[builtins.str]:
        '''The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request.

        Spot Instances are
        launched when the price you specify exceeds the current Spot market price.

        ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified

        :default: none
        '''
        result = self._values.get("spot_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssm_session_permissions(self) -> typing.Optional[builtins.bool]:
        '''Add SSM session permissions to the instance role.

        Setting this to ``true`` adds the necessary permissions to connect
        to the instance using SSM Session Manager. You can do this
        from the AWS Console.

        NOTE: Setting this flag to ``true`` may not be enough by itself.
        You must also use an AMI that comes with the SSM Agent, or install
        the SSM Agent yourself. See
        `Working with SSM Agent <https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html>`_
        in the SSM Developer Guide.

        :default: false
        '''
        result = self._values.get("ssm_session_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def termination_policies(
        self,
    ) -> typing.Optional[typing.List["_TerminationPolicy_89633c56"]]:
        '''A policy or a list of policies that are used to select the instances to terminate.

        The policies are executed in the order that you list them.

        :default: - ``TerminationPolicy.DEFAULT``

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html
        '''
        result = self._values.get("termination_policies")
        return typing.cast(typing.Optional[typing.List["_TerminationPolicy_89633c56"]], result)

    @builtins.property
    def termination_policy_custom_lambda_function_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''A lambda function Arn that can be used as a custom termination policy to select the instances to terminate.

        This property must be specified if the TerminationPolicy.CUSTOM_LAMBDA_FUNCTION
        is used.

        :default: - No lambda function Arn will be supplied

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/lambda-custom-termination-policy.html
        '''
        result = self._values.get("termination_policy_custom_lambda_function_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_policy(self) -> typing.Optional["_UpdatePolicy_6dffc7ca"]:
        '''What to do when an AutoScalingGroup's instance configuration is changed.

        This is applied when any of the settings on the ASG are changed that
        affect how the instances should be created (VPC, instance type, startup
        scripts, etc.). It indicates how the existing instances should be
        replaced with new instances matching the new config. By default, nothing
        is done and only new instances are launched with the new config.

        :default: - ``UpdatePolicy.rollingUpdate()`` if using ``init``, ``UpdatePolicy.none()`` otherwise
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional["_UpdatePolicy_6dffc7ca"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional["_SubnetSelection_e57d76df"]:
        '''Where to place instances within the VPC.

        :default: - All Private subnets.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional["_SubnetSelection_e57d76df"], result)

    @builtins.property
    def instance_type(self) -> "_InstanceType_f64915b9":
        '''Instance type of the instances to start.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast("_InstanceType_f64915b9", result)

    @builtins.property
    def bootstrap_enabled(self) -> typing.Optional[builtins.bool]:
        '''Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster.

        If you wish to provide a custom user data script, set this to ``false`` and
        manually invoke ``autoscalingGroup.addUserData()``.

        :default: true
        '''
        result = self._values.get("bootstrap_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bootstrap_options(self) -> typing.Optional["BootstrapOptions"]:
        '''EKS node bootstrapping options.

        :default: - none
        '''
        result = self._values.get("bootstrap_options")
        return typing.cast(typing.Optional["BootstrapOptions"], result)

    @builtins.property
    def machine_image_type(self) -> typing.Optional["MachineImageType"]:
        '''Machine image type.

        :default: MachineImageType.AMAZON_LINUX_2
        '''
        result = self._values.get("machine_image_type")
        return typing.cast(typing.Optional["MachineImageType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingGroupCapacityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.AutoScalingGroupOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bootstrap_enabled": "bootstrapEnabled",
        "bootstrap_options": "bootstrapOptions",
        "machine_image_type": "machineImageType",
    },
)
class AutoScalingGroupOptions:
    def __init__(
        self,
        *,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[typing.Union["BootstrapOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        machine_image_type: typing.Optional["MachineImageType"] = None,
    ) -> None:
        '''Options for adding an AutoScalingGroup as capacity.

        :param bootstrap_enabled: Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: Allows options for node bootstrapping through EC2 user data. Default: - default options
        :param machine_image_type: Allow options to specify different machine image type. Default: MachineImageType.AMAZON_LINUX_2

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            auto_scaling_group_options = eks_v2.AutoScalingGroupOptions(
                bootstrap_enabled=False,
                bootstrap_options=eks_v2.BootstrapOptions(
                    additional_args="additionalArgs",
                    aws_api_retry_attempts=123,
                    dns_cluster_ip="dnsClusterIp",
                    docker_config_json="dockerConfigJson",
                    enable_docker_bridge=False,
                    kubelet_extra_args="kubeletExtraArgs",
                    use_max_pods=False
                ),
                machine_image_type=eks_v2.MachineImageType.AMAZON_LINUX_2
            )
        '''
        if isinstance(bootstrap_options, dict):
            bootstrap_options = BootstrapOptions(**bootstrap_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f16f190b231b77037d63293668740b1890c84350977259ca756c2b3af690340d)
            check_type(argname="argument bootstrap_enabled", value=bootstrap_enabled, expected_type=type_hints["bootstrap_enabled"])
            check_type(argname="argument bootstrap_options", value=bootstrap_options, expected_type=type_hints["bootstrap_options"])
            check_type(argname="argument machine_image_type", value=machine_image_type, expected_type=type_hints["machine_image_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bootstrap_enabled is not None:
            self._values["bootstrap_enabled"] = bootstrap_enabled
        if bootstrap_options is not None:
            self._values["bootstrap_options"] = bootstrap_options
        if machine_image_type is not None:
            self._values["machine_image_type"] = machine_image_type

    @builtins.property
    def bootstrap_enabled(self) -> typing.Optional[builtins.bool]:
        '''Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster.

        If you wish to provide a custom user data script, set this to ``false`` and
        manually invoke ``autoscalingGroup.addUserData()``.

        :default: true
        '''
        result = self._values.get("bootstrap_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bootstrap_options(self) -> typing.Optional["BootstrapOptions"]:
        '''Allows options for node bootstrapping through EC2 user data.

        :default: - default options
        '''
        result = self._values.get("bootstrap_options")
        return typing.cast(typing.Optional["BootstrapOptions"], result)

    @builtins.property
    def machine_image_type(self) -> typing.Optional["MachineImageType"]:
        '''Allow options to specify different machine image type.

        :default: MachineImageType.AMAZON_LINUX_2
        '''
        result = self._values.get("machine_image_type")
        return typing.cast(typing.Optional["MachineImageType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingGroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.BootstrapOptions",
    jsii_struct_bases=[],
    name_mapping={
        "additional_args": "additionalArgs",
        "aws_api_retry_attempts": "awsApiRetryAttempts",
        "dns_cluster_ip": "dnsClusterIp",
        "docker_config_json": "dockerConfigJson",
        "enable_docker_bridge": "enableDockerBridge",
        "kubelet_extra_args": "kubeletExtraArgs",
        "use_max_pods": "useMaxPods",
    },
)
class BootstrapOptions:
    def __init__(
        self,
        *,
        additional_args: typing.Optional[builtins.str] = None,
        aws_api_retry_attempts: typing.Optional[jsii.Number] = None,
        dns_cluster_ip: typing.Optional[builtins.str] = None,
        docker_config_json: typing.Optional[builtins.str] = None,
        enable_docker_bridge: typing.Optional[builtins.bool] = None,
        kubelet_extra_args: typing.Optional[builtins.str] = None,
        use_max_pods: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''EKS node bootstrapping options.

        :param additional_args: Additional command line arguments to pass to the ``/etc/eks/bootstrap.sh`` command. Default: - none
        :param aws_api_retry_attempts: Number of retry attempts for AWS API call (DescribeCluster). Default: 3
        :param dns_cluster_ip: Overrides the IP address to use for DNS queries within the cluster. Default: - 10.100.0.10 or 172.20.0.10 based on the IP address of the primary interface.
        :param docker_config_json: The contents of the ``/etc/docker/daemon.json`` file. Useful if you want a custom config differing from the default one in the EKS AMI. Default: - none
        :param enable_docker_bridge: Restores the docker default bridge network. Default: false
        :param kubelet_extra_args: Extra arguments to add to the kubelet. Useful for adding labels or taints. For example, ``--node-labels foo=bar,goo=far``. Default: - none
        :param use_max_pods: Sets ``--max-pods`` for the kubelet based on the capacity of the EC2 instance. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            bootstrap_options = eks_v2.BootstrapOptions(
                additional_args="additionalArgs",
                aws_api_retry_attempts=123,
                dns_cluster_ip="dnsClusterIp",
                docker_config_json="dockerConfigJson",
                enable_docker_bridge=False,
                kubelet_extra_args="kubeletExtraArgs",
                use_max_pods=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f904654a5122c1c4508d0b1f4fa276f73d101ec61bed458657477c6cfcad2d89)
            check_type(argname="argument additional_args", value=additional_args, expected_type=type_hints["additional_args"])
            check_type(argname="argument aws_api_retry_attempts", value=aws_api_retry_attempts, expected_type=type_hints["aws_api_retry_attempts"])
            check_type(argname="argument dns_cluster_ip", value=dns_cluster_ip, expected_type=type_hints["dns_cluster_ip"])
            check_type(argname="argument docker_config_json", value=docker_config_json, expected_type=type_hints["docker_config_json"])
            check_type(argname="argument enable_docker_bridge", value=enable_docker_bridge, expected_type=type_hints["enable_docker_bridge"])
            check_type(argname="argument kubelet_extra_args", value=kubelet_extra_args, expected_type=type_hints["kubelet_extra_args"])
            check_type(argname="argument use_max_pods", value=use_max_pods, expected_type=type_hints["use_max_pods"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_args is not None:
            self._values["additional_args"] = additional_args
        if aws_api_retry_attempts is not None:
            self._values["aws_api_retry_attempts"] = aws_api_retry_attempts
        if dns_cluster_ip is not None:
            self._values["dns_cluster_ip"] = dns_cluster_ip
        if docker_config_json is not None:
            self._values["docker_config_json"] = docker_config_json
        if enable_docker_bridge is not None:
            self._values["enable_docker_bridge"] = enable_docker_bridge
        if kubelet_extra_args is not None:
            self._values["kubelet_extra_args"] = kubelet_extra_args
        if use_max_pods is not None:
            self._values["use_max_pods"] = use_max_pods

    @builtins.property
    def additional_args(self) -> typing.Optional[builtins.str]:
        '''Additional command line arguments to pass to the ``/etc/eks/bootstrap.sh`` command.

        :default: - none

        :see: https://github.com/awslabs/amazon-eks-ami/blob/master/files/bootstrap.sh
        '''
        result = self._values.get("additional_args")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_api_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''Number of retry attempts for AWS API call (DescribeCluster).

        :default: 3
        '''
        result = self._values.get("aws_api_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dns_cluster_ip(self) -> typing.Optional[builtins.str]:
        '''Overrides the IP address to use for DNS queries within the cluster.

        :default:

        - 10.100.0.10 or 172.20.0.10 based on the IP
        address of the primary interface.
        '''
        result = self._values.get("dns_cluster_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_config_json(self) -> typing.Optional[builtins.str]:
        '''The contents of the ``/etc/docker/daemon.json`` file. Useful if you want a custom config differing from the default one in the EKS AMI.

        :default: - none
        '''
        result = self._values.get("docker_config_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_docker_bridge(self) -> typing.Optional[builtins.bool]:
        '''Restores the docker default bridge network.

        :default: false
        '''
        result = self._values.get("enable_docker_bridge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kubelet_extra_args(self) -> typing.Optional[builtins.str]:
        '''Extra arguments to add to the kubelet. Useful for adding labels or taints.

        For example, ``--node-labels foo=bar,goo=far``.

        :default: - none
        '''
        result = self._values.get("kubelet_extra_args")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_max_pods(self) -> typing.Optional[builtins.bool]:
        '''Sets ``--max-pods`` for the kubelet based on the capacity of the EC2 instance.

        :default: true
        '''
        result = self._values.get("use_max_pods")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BootstrapOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.CapacityType")
class CapacityType(enum.Enum):
    '''Capacity type of the managed node group.'''

    SPOT = "SPOT"
    '''spot instances.'''
    ON_DEMAND = "ON_DEMAND"
    '''on-demand instances.'''
    CAPACITY_BLOCK = "CAPACITY_BLOCK"
    '''capacity block instances.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ClusterAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "cluster_certificate_authority_data": "clusterCertificateAuthorityData",
        "cluster_encryption_config_key_arn": "clusterEncryptionConfigKeyArn",
        "cluster_endpoint": "clusterEndpoint",
        "cluster_security_group_id": "clusterSecurityGroupId",
        "ip_family": "ipFamily",
        "kubectl_provider": "kubectlProvider",
        "kubectl_provider_options": "kubectlProviderOptions",
        "open_id_connect_provider": "openIdConnectProvider",
        "prune": "prune",
        "security_group_ids": "securityGroupIds",
        "vpc": "vpc",
    },
)
class ClusterAttributes:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        cluster_certificate_authority_data: typing.Optional[builtins.str] = None,
        cluster_encryption_config_key_arn: typing.Optional[builtins.str] = None,
        cluster_endpoint: typing.Optional[builtins.str] = None,
        cluster_security_group_id: typing.Optional[builtins.str] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider: typing.Optional["IKubectlProvider"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        open_id_connect_provider: typing.Optional["_IOpenIdConnectProvider_203f0793"] = None,
        prune: typing.Optional[builtins.bool] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
    ) -> None:
        '''Attributes for EKS clusters.

        :param cluster_name: The physical name of the Cluster.
        :param cluster_certificate_authority_data: The certificate-authority-data for your cluster. Default: - if not specified ``cluster.clusterCertificateAuthorityData`` will throw an error
        :param cluster_encryption_config_key_arn: Amazon Resource Name (ARN) or alias of the customer master key (CMK). Default: - if not specified ``cluster.clusterEncryptionConfigKeyArn`` will throw an error
        :param cluster_endpoint: The API Server endpoint URL. Default: - if not specified ``cluster.clusterEndpoint`` will throw an error.
        :param cluster_security_group_id: The cluster security group that was created by Amazon EKS for the cluster. Default: - if not specified ``cluster.clusterSecurityGroupId`` will throw an error
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: - IpFamily.IP_V4
        :param kubectl_provider: KubectlProvider for issuing kubectl commands. Default: - Default CDK provider
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created by default.
        :param open_id_connect_provider: An Open ID Connect provider for this cluster that can be used to configure service accounts. You can either import an existing provider using ``iam.OpenIdConnectProvider.fromProviderArn``, or create a new provider using ``new eks.OpenIdConnectProvider`` Default: - if not specified ``cluster.openIdConnectProvider`` and ``cluster.addServiceAccount`` will throw an error.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param security_group_ids: Additional security groups associated with this cluster. Default: - if not specified, no additional security groups will be considered in ``cluster.connections``.
        :param vpc: The VPC in which this Cluster was created. Default: - if not specified ``cluster.vpc`` will throw an error

        :exampleMetadata: infused

        Example::

            handler_role = iam.Role.from_role_arn(self, "HandlerRole", "arn:aws:iam::123456789012:role/lambda-role")
            # get the serivceToken from the custom resource provider
            function_arn = lambda_.Function.from_function_name(self, "ProviderOnEventFunc", "ProviderframeworkonEvent-XXX").function_arn
            kubectl_provider = eks.KubectlProvider.from_kubectl_provider_attributes(self, "KubectlProvider",
                service_token=function_arn,
                role=handler_role
            )
            
            cluster = eks.Cluster.from_cluster_attributes(self, "Cluster",
                cluster_name="cluster",
                kubectl_provider=kubectl_provider
            )
        '''
        if isinstance(kubectl_provider_options, dict):
            kubectl_provider_options = KubectlProviderOptions(**kubectl_provider_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66e301df415ba7f56900494427b4c395a0ce6d0961cc773754d28d465ecf3b45)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument cluster_certificate_authority_data", value=cluster_certificate_authority_data, expected_type=type_hints["cluster_certificate_authority_data"])
            check_type(argname="argument cluster_encryption_config_key_arn", value=cluster_encryption_config_key_arn, expected_type=type_hints["cluster_encryption_config_key_arn"])
            check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
            check_type(argname="argument cluster_security_group_id", value=cluster_security_group_id, expected_type=type_hints["cluster_security_group_id"])
            check_type(argname="argument ip_family", value=ip_family, expected_type=type_hints["ip_family"])
            check_type(argname="argument kubectl_provider", value=kubectl_provider, expected_type=type_hints["kubectl_provider"])
            check_type(argname="argument kubectl_provider_options", value=kubectl_provider_options, expected_type=type_hints["kubectl_provider_options"])
            check_type(argname="argument open_id_connect_provider", value=open_id_connect_provider, expected_type=type_hints["open_id_connect_provider"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
        }
        if cluster_certificate_authority_data is not None:
            self._values["cluster_certificate_authority_data"] = cluster_certificate_authority_data
        if cluster_encryption_config_key_arn is not None:
            self._values["cluster_encryption_config_key_arn"] = cluster_encryption_config_key_arn
        if cluster_endpoint is not None:
            self._values["cluster_endpoint"] = cluster_endpoint
        if cluster_security_group_id is not None:
            self._values["cluster_security_group_id"] = cluster_security_group_id
        if ip_family is not None:
            self._values["ip_family"] = ip_family
        if kubectl_provider is not None:
            self._values["kubectl_provider"] = kubectl_provider
        if kubectl_provider_options is not None:
            self._values["kubectl_provider_options"] = kubectl_provider_options
        if open_id_connect_provider is not None:
            self._values["open_id_connect_provider"] = open_id_connect_provider
        if prune is not None:
            self._values["prune"] = prune
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The physical name of the Cluster.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_certificate_authority_data(self) -> typing.Optional[builtins.str]:
        '''The certificate-authority-data for your cluster.

        :default:

        - if not specified ``cluster.clusterCertificateAuthorityData`` will
        throw an error
        '''
        result = self._values.get("cluster_certificate_authority_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_encryption_config_key_arn(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) or alias of the customer master key (CMK).

        :default:

        - if not specified ``cluster.clusterEncryptionConfigKeyArn`` will
        throw an error
        '''
        result = self._values.get("cluster_encryption_config_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_endpoint(self) -> typing.Optional[builtins.str]:
        '''The API Server endpoint URL.

        :default: - if not specified ``cluster.clusterEndpoint`` will throw an error.
        '''
        result = self._values.get("cluster_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_security_group_id(self) -> typing.Optional[builtins.str]:
        '''The cluster security group that was created by Amazon EKS for the cluster.

        :default:

        - if not specified ``cluster.clusterSecurityGroupId`` will throw an
        error
        '''
        result = self._values.get("cluster_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: - IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        result = self._values.get("ip_family")
        return typing.cast(typing.Optional["IpFamily"], result)

    @builtins.property
    def kubectl_provider(self) -> typing.Optional["IKubectlProvider"]:
        '''KubectlProvider for issuing kubectl commands.

        :default: - Default CDK provider
        '''
        result = self._values.get("kubectl_provider")
        return typing.cast(typing.Optional["IKubectlProvider"], result)

    @builtins.property
    def kubectl_provider_options(self) -> typing.Optional["KubectlProviderOptions"]:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        If defined, ``kubectlLayer`` is a required property.

        :default: - kubectl provider will not be created by default.
        '''
        result = self._values.get("kubectl_provider_options")
        return typing.cast(typing.Optional["KubectlProviderOptions"], result)

    @builtins.property
    def open_id_connect_provider(
        self,
    ) -> typing.Optional["_IOpenIdConnectProvider_203f0793"]:
        '''An Open ID Connect provider for this cluster that can be used to configure service accounts.

        You can either import an existing provider using ``iam.OpenIdConnectProvider.fromProviderArn``,
        or create a new provider using ``new eks.OpenIdConnectProvider``

        :default: - if not specified ``cluster.openIdConnectProvider`` and ``cluster.addServiceAccount`` will throw an error.
        '''
        result = self._values.get("open_id_connect_provider")
        return typing.cast(typing.Optional["_IOpenIdConnectProvider_203f0793"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned.

        When this is enabled (default), prune labels will be
        allocated and injected to each resource. These labels will then be used
        when issuing the ``kubectl apply`` operation with the ``--prune`` switch.

        :default: true
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional security groups associated with this cluster.

        :default:

        - if not specified, no additional security groups will be
        considered in ``cluster.connections``.
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc(self) -> typing.Optional["_IVpc_f30d5663"]:
        '''The VPC in which this Cluster was created.

        :default: - if not specified ``cluster.vpc`` will throw an error
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["_IVpc_f30d5663"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ClusterCommonOptions",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "alb_controller": "albController",
        "cluster_logging": "clusterLogging",
        "cluster_name": "clusterName",
        "core_dns_compute_type": "coreDnsComputeType",
        "endpoint_access": "endpointAccess",
        "ip_family": "ipFamily",
        "kubectl_provider_options": "kubectlProviderOptions",
        "masters_role": "mastersRole",
        "prune": "prune",
        "remote_node_networks": "remoteNodeNetworks",
        "remote_pod_networks": "remotePodNetworks",
        "removal_policy": "removalPolicy",
        "role": "role",
        "secrets_encryption_key": "secretsEncryptionKey",
        "security_group": "securityGroup",
        "service_ipv4_cidr": "serviceIpv4Cidr",
        "tags": "tags",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class ClusterCommonOptions:
    def __init__(
        self,
        *,
        version: "KubernetesVersion",
        alb_controller: typing.Optional[typing.Union["AlbControllerOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_logging: typing.Optional[typing.Sequence["ClusterLoggingTypes"]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        core_dns_compute_type: typing.Optional["CoreDnsComputeType"] = None,
        endpoint_access: typing.Optional["EndpointAccess"] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        masters_role: typing.Optional["_IRole_235f5d8e"] = None,
        prune: typing.Optional[builtins.bool] = None,
        remote_node_networks: typing.Optional[typing.Sequence[typing.Union["RemoteNodeNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        remote_pod_networks: typing.Optional[typing.Sequence[typing.Union["RemotePodNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        secrets_encryption_key: typing.Optional["_IKeyRef_d4fc6ef3"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
        service_ipv4_cidr: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Options for configuring an EKS cluster.

        :param version: The Kubernetes version to run in the cluster.
        :param alb_controller: Install the AWS Load Balancer Controller onto the cluster. Default: - The controller is not installed.
        :param cluster_logging: The cluster log types which you want to enable. Default: - none
        :param cluster_name: Name for the cluster. Default: - Automatically generated name
        :param core_dns_compute_type: Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS. Default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        :param endpoint_access: Configure access to the Kubernetes API server endpoint.. Default: EndpointAccess.PUBLIC_AND_PRIVATE
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: IpFamily.IP_V4
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created
        :param masters_role: An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - no masters role.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param remote_node_networks: IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster. Default: - none
        :param remote_pod_networks: IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes. Default: - none
        :param removal_policy: The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it; - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it; - The stack is deleted, so CloudFormation stops managing all resources in it. This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC and any other CloudFormation resources managed by this construct. Default: - Resources will be deleted.
        :param role: Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param secrets_encryption_key: KMS secret for envelope encryption for Kubernetes secrets. Default: - By default, Kubernetes stores all secret object data within etcd and all etcd volumes used by Amazon EKS are encrypted at the disk-level using AWS-Managed encryption keys.
        :param security_group: Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param service_ipv4_cidr: The CIDR block to assign Kubernetes service IP addresses from. Default: - Kubernetes assigns addresses from either the 10.100.0.0/16 or 172.20.0.0/16 CIDR blocks
        :param tags: The tags assigned to the EKS cluster. Default: - none
        :param vpc: The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: Where to place EKS Control Plane ENIs. For example, to only select private subnets, supply the following: ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]`` Default: - All public and private subnets

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_eks_v2 as eks_v2
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_lambda as lambda_
            from aws_cdk.interfaces import aws_kms as interfaces_kms
            
            # additional_helm_chart_values: Any
            # alb_controller_version: eks_v2.AlbControllerVersion
            # endpoint_access: eks_v2.EndpointAccess
            # key_ref: interfaces_kms.IKeyRef
            # kubernetes_version: eks_v2.KubernetesVersion
            # layer_version: lambda.LayerVersion
            # policy: Any
            # role: iam.Role
            # security_group: ec2.SecurityGroup
            # size: cdk.Size
            # subnet: ec2.Subnet
            # subnet_filter: ec2.SubnetFilter
            # vpc: ec2.Vpc
            
            cluster_common_options = eks_v2.ClusterCommonOptions(
                version=kubernetes_version,
            
                # the properties below are optional
                alb_controller=eks_v2.AlbControllerOptions(
                    version=alb_controller_version,
            
                    # the properties below are optional
                    additional_helm_chart_values={
                        "additional_helm_chart_values_key": additional_helm_chart_values
                    },
                    overwrite_service_account=False,
                    policy=policy,
                    removal_policy=cdk.RemovalPolicy.DESTROY,
                    repository="repository"
                ),
                cluster_logging=[eks_v2.ClusterLoggingTypes.API],
                cluster_name="clusterName",
                core_dns_compute_type=eks_v2.CoreDnsComputeType.EC2,
                endpoint_access=endpoint_access,
                ip_family=eks_v2.IpFamily.IP_V4,
                kubectl_provider_options=eks_v2.KubectlProviderOptions(
                    kubectl_layer=layer_version,
            
                    # the properties below are optional
                    awscli_layer=layer_version,
                    environment={
                        "environment_key": "environment"
                    },
                    memory=size,
                    private_subnets=[subnet],
                    removal_policy=cdk.RemovalPolicy.DESTROY,
                    role=role,
                    security_group=security_group
                ),
                masters_role=role,
                prune=False,
                remote_node_networks=[eks_v2.RemoteNodeNetwork(
                    cidrs=["cidrs"]
                )],
                remote_pod_networks=[eks_v2.RemotePodNetwork(
                    cidrs=["cidrs"]
                )],
                removal_policy=cdk.RemovalPolicy.DESTROY,
                role=role,
                secrets_encryption_key=key_ref,
                security_group=security_group,
                service_ipv4_cidr="serviceIpv4Cidr",
                tags={
                    "tags_key": "tags"
                },
                vpc=vpc,
                vpc_subnets=[ec2.SubnetSelection(
                    availability_zones=["availabilityZones"],
                    one_per_az=False,
                    subnet_filters=[subnet_filter],
                    subnet_group_name="subnetGroupName",
                    subnets=[subnet],
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                )]
            )
        '''
        if isinstance(alb_controller, dict):
            alb_controller = AlbControllerOptions(**alb_controller)
        if isinstance(kubectl_provider_options, dict):
            kubectl_provider_options = KubectlProviderOptions(**kubectl_provider_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a5ef28766020ab8c83202e5d6dffbece016846b78ba995db3af04cf02e999e)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument alb_controller", value=alb_controller, expected_type=type_hints["alb_controller"])
            check_type(argname="argument cluster_logging", value=cluster_logging, expected_type=type_hints["cluster_logging"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument core_dns_compute_type", value=core_dns_compute_type, expected_type=type_hints["core_dns_compute_type"])
            check_type(argname="argument endpoint_access", value=endpoint_access, expected_type=type_hints["endpoint_access"])
            check_type(argname="argument ip_family", value=ip_family, expected_type=type_hints["ip_family"])
            check_type(argname="argument kubectl_provider_options", value=kubectl_provider_options, expected_type=type_hints["kubectl_provider_options"])
            check_type(argname="argument masters_role", value=masters_role, expected_type=type_hints["masters_role"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument remote_node_networks", value=remote_node_networks, expected_type=type_hints["remote_node_networks"])
            check_type(argname="argument remote_pod_networks", value=remote_pod_networks, expected_type=type_hints["remote_pod_networks"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument secrets_encryption_key", value=secrets_encryption_key, expected_type=type_hints["secrets_encryption_key"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument service_ipv4_cidr", value=service_ipv4_cidr, expected_type=type_hints["service_ipv4_cidr"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if alb_controller is not None:
            self._values["alb_controller"] = alb_controller
        if cluster_logging is not None:
            self._values["cluster_logging"] = cluster_logging
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if core_dns_compute_type is not None:
            self._values["core_dns_compute_type"] = core_dns_compute_type
        if endpoint_access is not None:
            self._values["endpoint_access"] = endpoint_access
        if ip_family is not None:
            self._values["ip_family"] = ip_family
        if kubectl_provider_options is not None:
            self._values["kubectl_provider_options"] = kubectl_provider_options
        if masters_role is not None:
            self._values["masters_role"] = masters_role
        if prune is not None:
            self._values["prune"] = prune
        if remote_node_networks is not None:
            self._values["remote_node_networks"] = remote_node_networks
        if remote_pod_networks is not None:
            self._values["remote_pod_networks"] = remote_pod_networks
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role
        if secrets_encryption_key is not None:
            self._values["secrets_encryption_key"] = secrets_encryption_key
        if security_group is not None:
            self._values["security_group"] = security_group
        if service_ipv4_cidr is not None:
            self._values["service_ipv4_cidr"] = service_ipv4_cidr
        if tags is not None:
            self._values["tags"] = tags
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def version(self) -> "KubernetesVersion":
        '''The Kubernetes version to run in the cluster.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("KubernetesVersion", result)

    @builtins.property
    def alb_controller(self) -> typing.Optional["AlbControllerOptions"]:
        '''Install the AWS Load Balancer Controller onto the cluster.

        :default: - The controller is not installed.

        :see: https://kubernetes-sigs.github.io/aws-load-balancer-controller
        '''
        result = self._values.get("alb_controller")
        return typing.cast(typing.Optional["AlbControllerOptions"], result)

    @builtins.property
    def cluster_logging(self) -> typing.Optional[typing.List["ClusterLoggingTypes"]]:
        '''The cluster log types which you want to enable.

        :default: - none
        '''
        result = self._values.get("cluster_logging")
        return typing.cast(typing.Optional[typing.List["ClusterLoggingTypes"]], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Name for the cluster.

        :default: - Automatically generated name
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_dns_compute_type(self) -> typing.Optional["CoreDnsComputeType"]:
        '''Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS.

        :default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        '''
        result = self._values.get("core_dns_compute_type")
        return typing.cast(typing.Optional["CoreDnsComputeType"], result)

    @builtins.property
    def endpoint_access(self) -> typing.Optional["EndpointAccess"]:
        '''Configure access to the Kubernetes API server endpoint..

        :default: EndpointAccess.PUBLIC_AND_PRIVATE

        :see: https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
        '''
        result = self._values.get("endpoint_access")
        return typing.cast(typing.Optional["EndpointAccess"], result)

    @builtins.property
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        result = self._values.get("ip_family")
        return typing.cast(typing.Optional["IpFamily"], result)

    @builtins.property
    def kubectl_provider_options(self) -> typing.Optional["KubectlProviderOptions"]:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        If defined, ``kubectlLayer`` is a required property.

        :default: - kubectl provider will not be created
        '''
        result = self._values.get("kubectl_provider_options")
        return typing.cast(typing.Optional["KubectlProviderOptions"], result)

    @builtins.property
    def masters_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group.

        :default: - no masters role.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings
        '''
        result = self._values.get("masters_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned.

        When this is enabled (default), prune labels will be
        allocated and injected to each resource. These labels will then be used
        when issuing the ``kubectl apply`` operation with the ``--prune`` switch.

        :default: true
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remote_node_networks(self) -> typing.Optional[typing.List["RemoteNodeNetwork"]]:
        '''IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster.

        :default: - none
        '''
        result = self._values.get("remote_node_networks")
        return typing.cast(typing.Optional[typing.List["RemoteNodeNetwork"]], result)

    @builtins.property
    def remote_pod_networks(self) -> typing.Optional[typing.List["RemotePodNetwork"]]:
        '''IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes.

        :default: - none
        '''
        result = self._values.get("remote_pod_networks")
        return typing.cast(typing.Optional[typing.List["RemotePodNetwork"]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation.

        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it;
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it;
        - The stack is deleted, so CloudFormation stops managing all resources in it.

        This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC
        and any other CloudFormation resources managed by this construct.

        :default: - Resources will be deleted.
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

        :default: - A role is automatically created for you
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def secrets_encryption_key(self) -> typing.Optional["_IKeyRef_d4fc6ef3"]:
        '''KMS secret for envelope encryption for Kubernetes secrets.

        :default:

        - By default, Kubernetes stores all secret object data within etcd and
        all etcd volumes used by Amazon EKS are encrypted at the disk-level
        using AWS-Managed encryption keys.
        '''
        result = self._values.get("secrets_encryption_key")
        return typing.cast(typing.Optional["_IKeyRef_d4fc6ef3"], result)

    @builtins.property
    def security_group(self) -> typing.Optional["_ISecurityGroup_acf8a799"]:
        '''Security Group to use for Control Plane ENIs.

        :default: - A security group is automatically created
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional["_ISecurityGroup_acf8a799"], result)

    @builtins.property
    def service_ipv4_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR block to assign Kubernetes service IP addresses from.

        :default:

        - Kubernetes assigns addresses from either the
        10.100.0.0/16 or 172.20.0.0/16 CIDR blocks

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-serviceIpv4Cidr
        '''
        result = self._values.get("service_ipv4_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags assigned to the EKS cluster.

        :default: - none
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc(self) -> typing.Optional["_IVpc_f30d5663"]:
        '''The VPC in which to create the Cluster.

        :default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["_IVpc_f30d5663"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List["_SubnetSelection_e57d76df"]]:
        '''Where to place EKS Control Plane ENIs.

        For example, to only select private subnets, supply the following:

        ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]``

        :default: - All public and private subnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List["_SubnetSelection_e57d76df"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterCommonOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.ClusterLoggingTypes")
class ClusterLoggingTypes(enum.Enum):
    '''EKS cluster logging types.

    :exampleMetadata: infused

    Example::

        cluster = eks.Cluster(self, "Cluster",
            # ...
            version=eks.KubernetesVersion.V1_34,
            cluster_logging=[eks.ClusterLoggingTypes.API, eks.ClusterLoggingTypes.AUTHENTICATOR, eks.ClusterLoggingTypes.SCHEDULER
            ]
        )
    '''

    API = "API"
    '''Logs pertaining to API requests to the cluster.'''
    AUDIT = "AUDIT"
    '''Logs pertaining to cluster access via the Kubernetes API.'''
    AUTHENTICATOR = "AUTHENTICATOR"
    '''Logs pertaining to authentication requests into the cluster.'''
    CONTROLLER_MANAGER = "CONTROLLER_MANAGER"
    '''Logs pertaining to state of cluster controllers.'''
    SCHEDULER = "SCHEDULER"
    '''Logs pertaining to scheduling decisions.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ClusterProps",
    jsii_struct_bases=[ClusterCommonOptions],
    name_mapping={
        "version": "version",
        "alb_controller": "albController",
        "cluster_logging": "clusterLogging",
        "cluster_name": "clusterName",
        "core_dns_compute_type": "coreDnsComputeType",
        "endpoint_access": "endpointAccess",
        "ip_family": "ipFamily",
        "kubectl_provider_options": "kubectlProviderOptions",
        "masters_role": "mastersRole",
        "prune": "prune",
        "remote_node_networks": "remoteNodeNetworks",
        "remote_pod_networks": "remotePodNetworks",
        "removal_policy": "removalPolicy",
        "role": "role",
        "secrets_encryption_key": "secretsEncryptionKey",
        "security_group": "securityGroup",
        "service_ipv4_cidr": "serviceIpv4Cidr",
        "tags": "tags",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "bootstrap_cluster_creator_admin_permissions": "bootstrapClusterCreatorAdminPermissions",
        "bootstrap_self_managed_addons": "bootstrapSelfManagedAddons",
        "compute": "compute",
        "default_capacity": "defaultCapacity",
        "default_capacity_instance": "defaultCapacityInstance",
        "default_capacity_type": "defaultCapacityType",
        "output_config_command": "outputConfigCommand",
    },
)
class ClusterProps(ClusterCommonOptions):
    def __init__(
        self,
        *,
        version: "KubernetesVersion",
        alb_controller: typing.Optional[typing.Union["AlbControllerOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_logging: typing.Optional[typing.Sequence["ClusterLoggingTypes"]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        core_dns_compute_type: typing.Optional["CoreDnsComputeType"] = None,
        endpoint_access: typing.Optional["EndpointAccess"] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        masters_role: typing.Optional["_IRole_235f5d8e"] = None,
        prune: typing.Optional[builtins.bool] = None,
        remote_node_networks: typing.Optional[typing.Sequence[typing.Union["RemoteNodeNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        remote_pod_networks: typing.Optional[typing.Sequence[typing.Union["RemotePodNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        secrets_encryption_key: typing.Optional["_IKeyRef_d4fc6ef3"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
        service_ipv4_cidr: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]]] = None,
        bootstrap_cluster_creator_admin_permissions: typing.Optional[builtins.bool] = None,
        bootstrap_self_managed_addons: typing.Optional[builtins.bool] = None,
        compute: typing.Optional[typing.Union["ComputeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        default_capacity: typing.Optional[jsii.Number] = None,
        default_capacity_instance: typing.Optional["_InstanceType_f64915b9"] = None,
        default_capacity_type: typing.Optional["DefaultCapacityType"] = None,
        output_config_command: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for configuring a standard EKS cluster (non-Fargate).

        :param version: The Kubernetes version to run in the cluster.
        :param alb_controller: Install the AWS Load Balancer Controller onto the cluster. Default: - The controller is not installed.
        :param cluster_logging: The cluster log types which you want to enable. Default: - none
        :param cluster_name: Name for the cluster. Default: - Automatically generated name
        :param core_dns_compute_type: Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS. Default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        :param endpoint_access: Configure access to the Kubernetes API server endpoint.. Default: EndpointAccess.PUBLIC_AND_PRIVATE
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: IpFamily.IP_V4
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created
        :param masters_role: An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - no masters role.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param remote_node_networks: IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster. Default: - none
        :param remote_pod_networks: IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes. Default: - none
        :param removal_policy: The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it; - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it; - The stack is deleted, so CloudFormation stops managing all resources in it. This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC and any other CloudFormation resources managed by this construct. Default: - Resources will be deleted.
        :param role: Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param secrets_encryption_key: KMS secret for envelope encryption for Kubernetes secrets. Default: - By default, Kubernetes stores all secret object data within etcd and all etcd volumes used by Amazon EKS are encrypted at the disk-level using AWS-Managed encryption keys.
        :param security_group: Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param service_ipv4_cidr: The CIDR block to assign Kubernetes service IP addresses from. Default: - Kubernetes assigns addresses from either the 10.100.0.0/16 or 172.20.0.0/16 CIDR blocks
        :param tags: The tags assigned to the EKS cluster. Default: - none
        :param vpc: The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: Where to place EKS Control Plane ENIs. For example, to only select private subnets, supply the following: ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]`` Default: - All public and private subnets
        :param bootstrap_cluster_creator_admin_permissions: Whether or not IAM principal of the cluster creator was set as a cluster admin access entry during cluster creation time. Changing this value after the cluster has been created will result in the cluster being replaced. Default: true
        :param bootstrap_self_managed_addons: If you set this value to False when creating a cluster, the default networking add-ons will not be installed. The default networking addons include vpc-cni, coredns, and kube-proxy. Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons. Changing this value after the cluster has been created will result in the cluster being replaced. Default: true if the mode is not EKS Auto Mode
        :param compute: Configuration for compute settings in Auto Mode. When enabled, EKS will automatically manage compute resources. Default: - Auto Mode compute disabled
        :param default_capacity: Number of instances to allocate as an initial capacity for this cluster. Instance type can be configured through ``defaultCapacityInstanceType``, which defaults to ``m5.large``. Use ``cluster.addAutoScalingGroupCapacity`` to add additional customized capacity. Set this to ``0`` is you wish to avoid the initial capacity allocation. Default: 2
        :param default_capacity_instance: The instance type to use for the default capacity. This will only be taken into account if ``defaultCapacity`` is > 0. Default: m5.large
        :param default_capacity_type: The default capacity type for the cluster. Default: AUTOMODE
        :param output_config_command: Determines whether a CloudFormation output with the ``aws eks update-kubeconfig`` command will be synthesized. This command will include the cluster name and, if applicable, the ARN of the masters IAM role. Default: true

        :exampleMetadata: infused

        Example::

            cluster = eks.Cluster(self, "ManagedNodeCluster",
                version=eks.KubernetesVersion.V1_34,
                default_capacity_type=eks.DefaultCapacityType.NODEGROUP
            )
            
            # Add a Fargate Profile for specific workloads (e.g., default namespace)
            cluster.add_fargate_profile("FargateProfile",
                selectors=[eks.Selector(namespace="default")
                ]
            )
        '''
        if isinstance(alb_controller, dict):
            alb_controller = AlbControllerOptions(**alb_controller)
        if isinstance(kubectl_provider_options, dict):
            kubectl_provider_options = KubectlProviderOptions(**kubectl_provider_options)
        if isinstance(compute, dict):
            compute = ComputeConfig(**compute)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf0bb0ee5c6865eff515f2fc338ed96f254860f01b55add3f4ea50523d692c0)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument alb_controller", value=alb_controller, expected_type=type_hints["alb_controller"])
            check_type(argname="argument cluster_logging", value=cluster_logging, expected_type=type_hints["cluster_logging"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument core_dns_compute_type", value=core_dns_compute_type, expected_type=type_hints["core_dns_compute_type"])
            check_type(argname="argument endpoint_access", value=endpoint_access, expected_type=type_hints["endpoint_access"])
            check_type(argname="argument ip_family", value=ip_family, expected_type=type_hints["ip_family"])
            check_type(argname="argument kubectl_provider_options", value=kubectl_provider_options, expected_type=type_hints["kubectl_provider_options"])
            check_type(argname="argument masters_role", value=masters_role, expected_type=type_hints["masters_role"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument remote_node_networks", value=remote_node_networks, expected_type=type_hints["remote_node_networks"])
            check_type(argname="argument remote_pod_networks", value=remote_pod_networks, expected_type=type_hints["remote_pod_networks"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument secrets_encryption_key", value=secrets_encryption_key, expected_type=type_hints["secrets_encryption_key"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument service_ipv4_cidr", value=service_ipv4_cidr, expected_type=type_hints["service_ipv4_cidr"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument bootstrap_cluster_creator_admin_permissions", value=bootstrap_cluster_creator_admin_permissions, expected_type=type_hints["bootstrap_cluster_creator_admin_permissions"])
            check_type(argname="argument bootstrap_self_managed_addons", value=bootstrap_self_managed_addons, expected_type=type_hints["bootstrap_self_managed_addons"])
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument default_capacity", value=default_capacity, expected_type=type_hints["default_capacity"])
            check_type(argname="argument default_capacity_instance", value=default_capacity_instance, expected_type=type_hints["default_capacity_instance"])
            check_type(argname="argument default_capacity_type", value=default_capacity_type, expected_type=type_hints["default_capacity_type"])
            check_type(argname="argument output_config_command", value=output_config_command, expected_type=type_hints["output_config_command"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if alb_controller is not None:
            self._values["alb_controller"] = alb_controller
        if cluster_logging is not None:
            self._values["cluster_logging"] = cluster_logging
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if core_dns_compute_type is not None:
            self._values["core_dns_compute_type"] = core_dns_compute_type
        if endpoint_access is not None:
            self._values["endpoint_access"] = endpoint_access
        if ip_family is not None:
            self._values["ip_family"] = ip_family
        if kubectl_provider_options is not None:
            self._values["kubectl_provider_options"] = kubectl_provider_options
        if masters_role is not None:
            self._values["masters_role"] = masters_role
        if prune is not None:
            self._values["prune"] = prune
        if remote_node_networks is not None:
            self._values["remote_node_networks"] = remote_node_networks
        if remote_pod_networks is not None:
            self._values["remote_pod_networks"] = remote_pod_networks
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role
        if secrets_encryption_key is not None:
            self._values["secrets_encryption_key"] = secrets_encryption_key
        if security_group is not None:
            self._values["security_group"] = security_group
        if service_ipv4_cidr is not None:
            self._values["service_ipv4_cidr"] = service_ipv4_cidr
        if tags is not None:
            self._values["tags"] = tags
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if bootstrap_cluster_creator_admin_permissions is not None:
            self._values["bootstrap_cluster_creator_admin_permissions"] = bootstrap_cluster_creator_admin_permissions
        if bootstrap_self_managed_addons is not None:
            self._values["bootstrap_self_managed_addons"] = bootstrap_self_managed_addons
        if compute is not None:
            self._values["compute"] = compute
        if default_capacity is not None:
            self._values["default_capacity"] = default_capacity
        if default_capacity_instance is not None:
            self._values["default_capacity_instance"] = default_capacity_instance
        if default_capacity_type is not None:
            self._values["default_capacity_type"] = default_capacity_type
        if output_config_command is not None:
            self._values["output_config_command"] = output_config_command

    @builtins.property
    def version(self) -> "KubernetesVersion":
        '''The Kubernetes version to run in the cluster.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("KubernetesVersion", result)

    @builtins.property
    def alb_controller(self) -> typing.Optional["AlbControllerOptions"]:
        '''Install the AWS Load Balancer Controller onto the cluster.

        :default: - The controller is not installed.

        :see: https://kubernetes-sigs.github.io/aws-load-balancer-controller
        '''
        result = self._values.get("alb_controller")
        return typing.cast(typing.Optional["AlbControllerOptions"], result)

    @builtins.property
    def cluster_logging(self) -> typing.Optional[typing.List["ClusterLoggingTypes"]]:
        '''The cluster log types which you want to enable.

        :default: - none
        '''
        result = self._values.get("cluster_logging")
        return typing.cast(typing.Optional[typing.List["ClusterLoggingTypes"]], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Name for the cluster.

        :default: - Automatically generated name
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_dns_compute_type(self) -> typing.Optional["CoreDnsComputeType"]:
        '''Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS.

        :default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        '''
        result = self._values.get("core_dns_compute_type")
        return typing.cast(typing.Optional["CoreDnsComputeType"], result)

    @builtins.property
    def endpoint_access(self) -> typing.Optional["EndpointAccess"]:
        '''Configure access to the Kubernetes API server endpoint..

        :default: EndpointAccess.PUBLIC_AND_PRIVATE

        :see: https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
        '''
        result = self._values.get("endpoint_access")
        return typing.cast(typing.Optional["EndpointAccess"], result)

    @builtins.property
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        result = self._values.get("ip_family")
        return typing.cast(typing.Optional["IpFamily"], result)

    @builtins.property
    def kubectl_provider_options(self) -> typing.Optional["KubectlProviderOptions"]:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        If defined, ``kubectlLayer`` is a required property.

        :default: - kubectl provider will not be created
        '''
        result = self._values.get("kubectl_provider_options")
        return typing.cast(typing.Optional["KubectlProviderOptions"], result)

    @builtins.property
    def masters_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group.

        :default: - no masters role.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings
        '''
        result = self._values.get("masters_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned.

        When this is enabled (default), prune labels will be
        allocated and injected to each resource. These labels will then be used
        when issuing the ``kubectl apply`` operation with the ``--prune`` switch.

        :default: true
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remote_node_networks(self) -> typing.Optional[typing.List["RemoteNodeNetwork"]]:
        '''IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster.

        :default: - none
        '''
        result = self._values.get("remote_node_networks")
        return typing.cast(typing.Optional[typing.List["RemoteNodeNetwork"]], result)

    @builtins.property
    def remote_pod_networks(self) -> typing.Optional[typing.List["RemotePodNetwork"]]:
        '''IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes.

        :default: - none
        '''
        result = self._values.get("remote_pod_networks")
        return typing.cast(typing.Optional[typing.List["RemotePodNetwork"]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation.

        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it;
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it;
        - The stack is deleted, so CloudFormation stops managing all resources in it.

        This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC
        and any other CloudFormation resources managed by this construct.

        :default: - Resources will be deleted.
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

        :default: - A role is automatically created for you
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def secrets_encryption_key(self) -> typing.Optional["_IKeyRef_d4fc6ef3"]:
        '''KMS secret for envelope encryption for Kubernetes secrets.

        :default:

        - By default, Kubernetes stores all secret object data within etcd and
        all etcd volumes used by Amazon EKS are encrypted at the disk-level
        using AWS-Managed encryption keys.
        '''
        result = self._values.get("secrets_encryption_key")
        return typing.cast(typing.Optional["_IKeyRef_d4fc6ef3"], result)

    @builtins.property
    def security_group(self) -> typing.Optional["_ISecurityGroup_acf8a799"]:
        '''Security Group to use for Control Plane ENIs.

        :default: - A security group is automatically created
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional["_ISecurityGroup_acf8a799"], result)

    @builtins.property
    def service_ipv4_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR block to assign Kubernetes service IP addresses from.

        :default:

        - Kubernetes assigns addresses from either the
        10.100.0.0/16 or 172.20.0.0/16 CIDR blocks

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-serviceIpv4Cidr
        '''
        result = self._values.get("service_ipv4_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags assigned to the EKS cluster.

        :default: - none
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc(self) -> typing.Optional["_IVpc_f30d5663"]:
        '''The VPC in which to create the Cluster.

        :default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["_IVpc_f30d5663"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List["_SubnetSelection_e57d76df"]]:
        '''Where to place EKS Control Plane ENIs.

        For example, to only select private subnets, supply the following:

        ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]``

        :default: - All public and private subnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List["_SubnetSelection_e57d76df"]], result)

    @builtins.property
    def bootstrap_cluster_creator_admin_permissions(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Whether or not IAM principal of the cluster creator was set as a cluster admin access entry during cluster creation time.

        Changing this value after the cluster has been created will result in the cluster being replaced.

        :default: true
        '''
        result = self._values.get("bootstrap_cluster_creator_admin_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bootstrap_self_managed_addons(self) -> typing.Optional[builtins.bool]:
        '''If you set this value to False when creating a cluster, the default networking add-ons will not be installed.

        The default networking addons include vpc-cni, coredns, and kube-proxy.
        Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons.

        Changing this value after the cluster has been created will result in the cluster being replaced.

        :default: true if the mode is not EKS Auto Mode
        '''
        result = self._values.get("bootstrap_self_managed_addons")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def compute(self) -> typing.Optional["ComputeConfig"]:
        '''Configuration for compute settings in Auto Mode.

        When enabled, EKS will automatically manage compute resources.

        :default: - Auto Mode compute disabled
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional["ComputeConfig"], result)

    @builtins.property
    def default_capacity(self) -> typing.Optional[jsii.Number]:
        '''Number of instances to allocate as an initial capacity for this cluster.

        Instance type can be configured through ``defaultCapacityInstanceType``,
        which defaults to ``m5.large``.

        Use ``cluster.addAutoScalingGroupCapacity`` to add additional customized capacity. Set this
        to ``0`` is you wish to avoid the initial capacity allocation.

        :default: 2
        '''
        result = self._values.get("default_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_capacity_instance(self) -> typing.Optional["_InstanceType_f64915b9"]:
        '''The instance type to use for the default capacity.

        This will only be taken
        into account if ``defaultCapacity`` is > 0.

        :default: m5.large
        '''
        result = self._values.get("default_capacity_instance")
        return typing.cast(typing.Optional["_InstanceType_f64915b9"], result)

    @builtins.property
    def default_capacity_type(self) -> typing.Optional["DefaultCapacityType"]:
        '''The default capacity type for the cluster.

        :default: AUTOMODE
        '''
        result = self._values.get("default_capacity_type")
        return typing.cast(typing.Optional["DefaultCapacityType"], result)

    @builtins.property
    def output_config_command(self) -> typing.Optional[builtins.bool]:
        '''Determines whether a CloudFormation output with the ``aws eks update-kubeconfig`` command will be synthesized.

        This command will include
        the cluster name and, if applicable, the ARN of the masters IAM role.

        :default: true
        '''
        result = self._values.get("output_config_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ComputeConfig",
    jsii_struct_bases=[],
    name_mapping={"node_pools": "nodePools", "node_role": "nodeRole"},
)
class ComputeConfig:
    def __init__(
        self,
        *,
        node_pools: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_role: typing.Optional["_IRole_235f5d8e"] = None,
    ) -> None:
        '''Options for configuring EKS Auto Mode compute settings.

        When enabled, EKS will automatically manage compute resources like node groups and Fargate profiles.

        :param node_pools: Names of nodePools to include in Auto Mode. You cannot modify the built in system and general-purpose node pools. You can only enable or disable them. Node pool values are case-sensitive and must be ``general-purpose`` and/or ``system``. Default: - ['system', 'general-purpose']
        :param node_role: IAM role for the nodePools. Default: - generated by the CDK

        :exampleMetadata: infused

        Example::

            cluster = eks.Cluster(self, "EksAutoCluster",
                version=eks.KubernetesVersion.V1_34,
                default_capacity_type=eks.DefaultCapacityType.AUTOMODE,
                compute=eks.ComputeConfig(
                    node_pools=["system", "general-purpose"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f2276433261f643c13b2562a74d200173c371ac395d946bc5b30974e539c3d8)
            check_type(argname="argument node_pools", value=node_pools, expected_type=type_hints["node_pools"])
            check_type(argname="argument node_role", value=node_role, expected_type=type_hints["node_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if node_pools is not None:
            self._values["node_pools"] = node_pools
        if node_role is not None:
            self._values["node_role"] = node_role

    @builtins.property
    def node_pools(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of nodePools to include in Auto Mode.

        You cannot modify the built in system and general-purpose node pools. You can only enable or disable them.
        Node pool values are case-sensitive and must be ``general-purpose`` and/or ``system``.

        :default: - ['system', 'general-purpose']

        :see: - https://docs.aws.amazon.com/eks/latest/userguide/create-node-pool.html
        '''
        result = self._values.get("node_pools")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def node_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''IAM role for the nodePools.

        :default: - generated by the CDK

        :see: - https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html
        '''
        result = self._values.get("node_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.CoreDnsComputeType")
class CoreDnsComputeType(enum.Enum):
    '''The type of compute resources to use for CoreDNS.'''

    EC2 = "EC2"
    '''Deploy CoreDNS on EC2 instances.'''
    FARGATE = "FARGATE"
    '''Deploy CoreDNS on Fargate-managed instances.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.CpuArch")
class CpuArch(enum.Enum):
    '''CPU architecture.'''

    ARM_64 = "ARM_64"
    '''arm64 CPU type.'''
    X86_64 = "X86_64"
    '''x86_64 CPU type.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.DefaultCapacityType")
class DefaultCapacityType(enum.Enum):
    '''The default capacity type for the cluster.

    :exampleMetadata: infused

    Example::

        cluster = eks.Cluster(self, "HelloEKS",
            version=eks.KubernetesVersion.V1_34,
            default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
            default_capacity=0
        )
        
        cluster.add_nodegroup_capacity("custom-node-group",
            instance_types=[ec2.InstanceType("m5.large")],
            min_size=4,
            disk_size=100
        )
    '''

    NODEGROUP = "NODEGROUP"
    '''managed node group.'''
    EC2 = "EC2"
    '''EC2 autoscaling group.'''
    AUTOMODE = "AUTOMODE"
    '''Auto Mode.'''


@jsii.implements(_IMachineImage_0e8bd50b)
class EksOptimizedImage(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.EksOptimizedImage",
):
    '''Construct an Amazon Linux 2 image from the latest EKS Optimized AMI published in SSM.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eks_v2 as eks_v2
        
        eks_optimized_image = eks_v2.EksOptimizedImage(
            cpu_arch=eks_v2.CpuArch.ARM_64,
            kubernetes_version="kubernetesVersion",
            node_type=eks_v2.NodeType.STANDARD
        )
    '''

    def __init__(
        self,
        *,
        cpu_arch: typing.Optional["CpuArch"] = None,
        kubernetes_version: typing.Optional[builtins.str] = None,
        node_type: typing.Optional["NodeType"] = None,
    ) -> None:
        '''Constructs a new instance of the EcsOptimizedAmi class.

        :param cpu_arch: What cpu architecture to retrieve the image for (arm64 or x86_64). Default: CpuArch.X86_64
        :param kubernetes_version: The Kubernetes version to use. Default: - The latest version
        :param node_type: What instance type to retrieve the image for (standard or GPU-optimized). Default: NodeType.STANDARD
        '''
        props = EksOptimizedImageProps(
            cpu_arch=cpu_arch,
            kubernetes_version=kubernetes_version,
            node_type=node_type,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="getImage")
    def get_image(
        self,
        scope: "_constructs_77d1e7e8.Construct",
    ) -> "_MachineImageConfig_187edaee":
        '''Return the correct image.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2738ba90423201fc12883e08866d0a856feb778d505f172858bfbbce5d08710c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("_MachineImageConfig_187edaee", jsii.invoke(self, "getImage", [scope]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.EksOptimizedImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_arch": "cpuArch",
        "kubernetes_version": "kubernetesVersion",
        "node_type": "nodeType",
    },
)
class EksOptimizedImageProps:
    def __init__(
        self,
        *,
        cpu_arch: typing.Optional["CpuArch"] = None,
        kubernetes_version: typing.Optional[builtins.str] = None,
        node_type: typing.Optional["NodeType"] = None,
    ) -> None:
        '''Properties for EksOptimizedImage.

        :param cpu_arch: What cpu architecture to retrieve the image for (arm64 or x86_64). Default: CpuArch.X86_64
        :param kubernetes_version: The Kubernetes version to use. Default: - The latest version
        :param node_type: What instance type to retrieve the image for (standard or GPU-optimized). Default: NodeType.STANDARD

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            eks_optimized_image_props = eks_v2.EksOptimizedImageProps(
                cpu_arch=eks_v2.CpuArch.ARM_64,
                kubernetes_version="kubernetesVersion",
                node_type=eks_v2.NodeType.STANDARD
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d6369fc46cff5c9662be35163e7c703248821b956be42141437e81db12dcda)
            check_type(argname="argument cpu_arch", value=cpu_arch, expected_type=type_hints["cpu_arch"])
            check_type(argname="argument kubernetes_version", value=kubernetes_version, expected_type=type_hints["kubernetes_version"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_arch is not None:
            self._values["cpu_arch"] = cpu_arch
        if kubernetes_version is not None:
            self._values["kubernetes_version"] = kubernetes_version
        if node_type is not None:
            self._values["node_type"] = node_type

    @builtins.property
    def cpu_arch(self) -> typing.Optional["CpuArch"]:
        '''What cpu architecture to retrieve the image for (arm64 or x86_64).

        :default: CpuArch.X86_64
        '''
        result = self._values.get("cpu_arch")
        return typing.cast(typing.Optional["CpuArch"], result)

    @builtins.property
    def kubernetes_version(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes version to use.

        :default: - The latest version
        '''
        result = self._values.get("kubernetes_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_type(self) -> typing.Optional["NodeType"]:
        '''What instance type to retrieve the image for (standard or GPU-optimized).

        :default: NodeType.STANDARD
        '''
        result = self._values.get("node_type")
        return typing.cast(typing.Optional["NodeType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EksOptimizedImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EndpointAccess(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.EndpointAccess",
):
    '''Endpoint access characteristics.

    :exampleMetadata: infused

    Example::

        cluster = eks.Cluster(self, "hello-eks",
            version=eks.KubernetesVersion.V1_34,
            endpoint_access=eks.EndpointAccess.PRIVATE
        )
    '''

    @jsii.member(jsii_name="onlyFrom")
    def only_from(self, *cidr: builtins.str) -> "EndpointAccess":
        '''Restrict public access to specific CIDR blocks.

        If public access is disabled, this method will result in an error.

        :param cidr: CIDR blocks.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1c8b1b01f47532094dca60e427081322eba78c5885128cf95f25557e7132e2)
            check_type(argname="argument cidr", value=cidr, expected_type=typing.Tuple[type_hints["cidr"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("EndpointAccess", jsii.invoke(self, "onlyFrom", [*cidr]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PRIVATE")
    def PRIVATE(cls) -> "EndpointAccess":
        '''The cluster endpoint is only accessible through your VPC.

        Worker node traffic to the endpoint will stay within your VPC.
        '''
        return typing.cast("EndpointAccess", jsii.sget(cls, "PRIVATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PUBLIC")
    def PUBLIC(cls) -> "EndpointAccess":
        '''The cluster endpoint is accessible from outside of your VPC.

        Worker node traffic will leave your VPC to connect to the endpoint.

        By default, the endpoint is exposed to all adresses. You can optionally limit the CIDR blocks that can access the public endpoint using the ``PUBLIC.onlyFrom`` method.
        If you limit access to specific CIDR blocks, you must ensure that the CIDR blocks that you
        specify include the addresses that worker nodes and Fargate pods (if you use them)
        access the public endpoint from.
        '''
        return typing.cast("EndpointAccess", jsii.sget(cls, "PUBLIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PUBLIC_AND_PRIVATE")
    def PUBLIC_AND_PRIVATE(cls) -> "EndpointAccess":
        '''The cluster endpoint is accessible from outside of your VPC.

        Worker node traffic to the endpoint will stay within your VPC.

        By default, the endpoint is exposed to all adresses. You can optionally limit the CIDR blocks that can access the public endpoint using the ``PUBLIC_AND_PRIVATE.onlyFrom`` method.
        If you limit access to specific CIDR blocks, you must ensure that the CIDR blocks that you
        specify include the addresses that worker nodes and Fargate pods (if you use them)
        access the public endpoint from.
        '''
        return typing.cast("EndpointAccess", jsii.sget(cls, "PUBLIC_AND_PRIVATE"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.FargateClusterProps",
    jsii_struct_bases=[ClusterCommonOptions],
    name_mapping={
        "version": "version",
        "alb_controller": "albController",
        "cluster_logging": "clusterLogging",
        "cluster_name": "clusterName",
        "core_dns_compute_type": "coreDnsComputeType",
        "endpoint_access": "endpointAccess",
        "ip_family": "ipFamily",
        "kubectl_provider_options": "kubectlProviderOptions",
        "masters_role": "mastersRole",
        "prune": "prune",
        "remote_node_networks": "remoteNodeNetworks",
        "remote_pod_networks": "remotePodNetworks",
        "removal_policy": "removalPolicy",
        "role": "role",
        "secrets_encryption_key": "secretsEncryptionKey",
        "security_group": "securityGroup",
        "service_ipv4_cidr": "serviceIpv4Cidr",
        "tags": "tags",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "default_profile": "defaultProfile",
    },
)
class FargateClusterProps(ClusterCommonOptions):
    def __init__(
        self,
        *,
        version: "KubernetesVersion",
        alb_controller: typing.Optional[typing.Union["AlbControllerOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_logging: typing.Optional[typing.Sequence["ClusterLoggingTypes"]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        core_dns_compute_type: typing.Optional["CoreDnsComputeType"] = None,
        endpoint_access: typing.Optional["EndpointAccess"] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        masters_role: typing.Optional["_IRole_235f5d8e"] = None,
        prune: typing.Optional[builtins.bool] = None,
        remote_node_networks: typing.Optional[typing.Sequence[typing.Union["RemoteNodeNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        remote_pod_networks: typing.Optional[typing.Sequence[typing.Union["RemotePodNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        secrets_encryption_key: typing.Optional["_IKeyRef_d4fc6ef3"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
        service_ipv4_cidr: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_profile: typing.Optional[typing.Union["FargateProfileOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Configuration props for EKS Fargate.

        :param version: The Kubernetes version to run in the cluster.
        :param alb_controller: Install the AWS Load Balancer Controller onto the cluster. Default: - The controller is not installed.
        :param cluster_logging: The cluster log types which you want to enable. Default: - none
        :param cluster_name: Name for the cluster. Default: - Automatically generated name
        :param core_dns_compute_type: Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS. Default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        :param endpoint_access: Configure access to the Kubernetes API server endpoint.. Default: EndpointAccess.PUBLIC_AND_PRIVATE
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: IpFamily.IP_V4
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created
        :param masters_role: An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - no masters role.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param remote_node_networks: IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster. Default: - none
        :param remote_pod_networks: IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes. Default: - none
        :param removal_policy: The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it; - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it; - The stack is deleted, so CloudFormation stops managing all resources in it. This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC and any other CloudFormation resources managed by this construct. Default: - Resources will be deleted.
        :param role: Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param secrets_encryption_key: KMS secret for envelope encryption for Kubernetes secrets. Default: - By default, Kubernetes stores all secret object data within etcd and all etcd volumes used by Amazon EKS are encrypted at the disk-level using AWS-Managed encryption keys.
        :param security_group: Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param service_ipv4_cidr: The CIDR block to assign Kubernetes service IP addresses from. Default: - Kubernetes assigns addresses from either the 10.100.0.0/16 or 172.20.0.0/16 CIDR blocks
        :param tags: The tags assigned to the EKS cluster. Default: - none
        :param vpc: The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: Where to place EKS Control Plane ENIs. For example, to only select private subnets, supply the following: ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]`` Default: - All public and private subnets
        :param default_profile: Fargate Profile to create along with the cluster. Default: - A profile called "default" with 'default' and 'kube-system' selectors will be created if this is left undefined.

        :exampleMetadata: infused

        Example::

            cluster = eks.FargateCluster(self, "FargateCluster",
                version=eks.KubernetesVersion.V1_34
            )
        '''
        if isinstance(alb_controller, dict):
            alb_controller = AlbControllerOptions(**alb_controller)
        if isinstance(kubectl_provider_options, dict):
            kubectl_provider_options = KubectlProviderOptions(**kubectl_provider_options)
        if isinstance(default_profile, dict):
            default_profile = FargateProfileOptions(**default_profile)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3435de412248a83f43d99c9de5759414e7750a3260fc08dd8d1d5a7b64555d3)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument alb_controller", value=alb_controller, expected_type=type_hints["alb_controller"])
            check_type(argname="argument cluster_logging", value=cluster_logging, expected_type=type_hints["cluster_logging"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument core_dns_compute_type", value=core_dns_compute_type, expected_type=type_hints["core_dns_compute_type"])
            check_type(argname="argument endpoint_access", value=endpoint_access, expected_type=type_hints["endpoint_access"])
            check_type(argname="argument ip_family", value=ip_family, expected_type=type_hints["ip_family"])
            check_type(argname="argument kubectl_provider_options", value=kubectl_provider_options, expected_type=type_hints["kubectl_provider_options"])
            check_type(argname="argument masters_role", value=masters_role, expected_type=type_hints["masters_role"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument remote_node_networks", value=remote_node_networks, expected_type=type_hints["remote_node_networks"])
            check_type(argname="argument remote_pod_networks", value=remote_pod_networks, expected_type=type_hints["remote_pod_networks"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument secrets_encryption_key", value=secrets_encryption_key, expected_type=type_hints["secrets_encryption_key"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument service_ipv4_cidr", value=service_ipv4_cidr, expected_type=type_hints["service_ipv4_cidr"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument default_profile", value=default_profile, expected_type=type_hints["default_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if alb_controller is not None:
            self._values["alb_controller"] = alb_controller
        if cluster_logging is not None:
            self._values["cluster_logging"] = cluster_logging
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if core_dns_compute_type is not None:
            self._values["core_dns_compute_type"] = core_dns_compute_type
        if endpoint_access is not None:
            self._values["endpoint_access"] = endpoint_access
        if ip_family is not None:
            self._values["ip_family"] = ip_family
        if kubectl_provider_options is not None:
            self._values["kubectl_provider_options"] = kubectl_provider_options
        if masters_role is not None:
            self._values["masters_role"] = masters_role
        if prune is not None:
            self._values["prune"] = prune
        if remote_node_networks is not None:
            self._values["remote_node_networks"] = remote_node_networks
        if remote_pod_networks is not None:
            self._values["remote_pod_networks"] = remote_pod_networks
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role
        if secrets_encryption_key is not None:
            self._values["secrets_encryption_key"] = secrets_encryption_key
        if security_group is not None:
            self._values["security_group"] = security_group
        if service_ipv4_cidr is not None:
            self._values["service_ipv4_cidr"] = service_ipv4_cidr
        if tags is not None:
            self._values["tags"] = tags
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if default_profile is not None:
            self._values["default_profile"] = default_profile

    @builtins.property
    def version(self) -> "KubernetesVersion":
        '''The Kubernetes version to run in the cluster.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("KubernetesVersion", result)

    @builtins.property
    def alb_controller(self) -> typing.Optional["AlbControllerOptions"]:
        '''Install the AWS Load Balancer Controller onto the cluster.

        :default: - The controller is not installed.

        :see: https://kubernetes-sigs.github.io/aws-load-balancer-controller
        '''
        result = self._values.get("alb_controller")
        return typing.cast(typing.Optional["AlbControllerOptions"], result)

    @builtins.property
    def cluster_logging(self) -> typing.Optional[typing.List["ClusterLoggingTypes"]]:
        '''The cluster log types which you want to enable.

        :default: - none
        '''
        result = self._values.get("cluster_logging")
        return typing.cast(typing.Optional[typing.List["ClusterLoggingTypes"]], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Name for the cluster.

        :default: - Automatically generated name
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_dns_compute_type(self) -> typing.Optional["CoreDnsComputeType"]:
        '''Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS.

        :default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        '''
        result = self._values.get("core_dns_compute_type")
        return typing.cast(typing.Optional["CoreDnsComputeType"], result)

    @builtins.property
    def endpoint_access(self) -> typing.Optional["EndpointAccess"]:
        '''Configure access to the Kubernetes API server endpoint..

        :default: EndpointAccess.PUBLIC_AND_PRIVATE

        :see: https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
        '''
        result = self._values.get("endpoint_access")
        return typing.cast(typing.Optional["EndpointAccess"], result)

    @builtins.property
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        result = self._values.get("ip_family")
        return typing.cast(typing.Optional["IpFamily"], result)

    @builtins.property
    def kubectl_provider_options(self) -> typing.Optional["KubectlProviderOptions"]:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        If defined, ``kubectlLayer`` is a required property.

        :default: - kubectl provider will not be created
        '''
        result = self._values.get("kubectl_provider_options")
        return typing.cast(typing.Optional["KubectlProviderOptions"], result)

    @builtins.property
    def masters_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group.

        :default: - no masters role.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings
        '''
        result = self._values.get("masters_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned.

        When this is enabled (default), prune labels will be
        allocated and injected to each resource. These labels will then be used
        when issuing the ``kubectl apply`` operation with the ``--prune`` switch.

        :default: true
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remote_node_networks(self) -> typing.Optional[typing.List["RemoteNodeNetwork"]]:
        '''IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster.

        :default: - none
        '''
        result = self._values.get("remote_node_networks")
        return typing.cast(typing.Optional[typing.List["RemoteNodeNetwork"]], result)

    @builtins.property
    def remote_pod_networks(self) -> typing.Optional[typing.List["RemotePodNetwork"]]:
        '''IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes.

        :default: - none
        '''
        result = self._values.get("remote_pod_networks")
        return typing.cast(typing.Optional[typing.List["RemotePodNetwork"]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation.

        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it;
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it;
        - The stack is deleted, so CloudFormation stops managing all resources in it.

        This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC
        and any other CloudFormation resources managed by this construct.

        :default: - Resources will be deleted.
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

        :default: - A role is automatically created for you
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def secrets_encryption_key(self) -> typing.Optional["_IKeyRef_d4fc6ef3"]:
        '''KMS secret for envelope encryption for Kubernetes secrets.

        :default:

        - By default, Kubernetes stores all secret object data within etcd and
        all etcd volumes used by Amazon EKS are encrypted at the disk-level
        using AWS-Managed encryption keys.
        '''
        result = self._values.get("secrets_encryption_key")
        return typing.cast(typing.Optional["_IKeyRef_d4fc6ef3"], result)

    @builtins.property
    def security_group(self) -> typing.Optional["_ISecurityGroup_acf8a799"]:
        '''Security Group to use for Control Plane ENIs.

        :default: - A security group is automatically created
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional["_ISecurityGroup_acf8a799"], result)

    @builtins.property
    def service_ipv4_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR block to assign Kubernetes service IP addresses from.

        :default:

        - Kubernetes assigns addresses from either the
        10.100.0.0/16 or 172.20.0.0/16 CIDR blocks

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-serviceIpv4Cidr
        '''
        result = self._values.get("service_ipv4_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags assigned to the EKS cluster.

        :default: - none
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc(self) -> typing.Optional["_IVpc_f30d5663"]:
        '''The VPC in which to create the Cluster.

        :default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["_IVpc_f30d5663"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List["_SubnetSelection_e57d76df"]]:
        '''Where to place EKS Control Plane ENIs.

        For example, to only select private subnets, supply the following:

        ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]``

        :default: - All public and private subnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List["_SubnetSelection_e57d76df"]], result)

    @builtins.property
    def default_profile(self) -> typing.Optional["FargateProfileOptions"]:
        '''Fargate Profile to create along with the cluster.

        :default:

        - A profile called "default" with 'default' and 'kube-system'
        selectors will be created if this is left undefined.
        '''
        result = self._values.get("default_profile")
        return typing.cast(typing.Optional["FargateProfileOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_ITaggable_36806126)
class FargateProfile(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.FargateProfile",
):
    '''Fargate profiles allows an administrator to declare which pods run on Fargate.

    This declaration is done through the profile’s selectors. Each
    profile can have up to five selectors that contain a namespace and optional
    labels. You must define a namespace for every selector. The label field
    consists of multiple optional key-value pairs. Pods that match a selector (by
    matching a namespace for the selector and all of the labels specified in the
    selector) are scheduled on Fargate. If a namespace selector is defined
    without any labels, Amazon EKS will attempt to schedule all pods that run in
    that namespace onto Fargate using the profile. If a to-be-scheduled pod
    matches any of the selectors in the Fargate profile, then that pod is
    scheduled on Fargate.

    If a pod matches multiple Fargate profiles, Amazon EKS picks one of the
    matches at random. In this case, you can specify which profile a pod should
    use by adding the following Kubernetes label to the pod specification:
    eks.amazonaws.com/fargate-profile: profile_name. However, the pod must still
    match a selector in that profile in order to be scheduled onto Fargate.

    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        
        eks.FargateProfile(self, "MyProfile",
            cluster=cluster,
            selectors=[eks.Selector(namespace="default")]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "Cluster",
        selectors: typing.Sequence[typing.Union["Selector", typing.Dict[builtins.str, typing.Any]]],
        fargate_profile_name: typing.Optional[builtins.str] = None,
        pod_execution_role: typing.Optional["_IRole_235f5d8e"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnet_selection: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The EKS cluster to apply the Fargate profile to. [disable-awslint:ref-via-interface]
        :param selectors: The selectors to match for pods to use this Fargate profile. Each selector must have an associated namespace. Optionally, you can also specify labels for a namespace. At least one selector is required and you may specify up to five selectors.
        :param fargate_profile_name: The name of the Fargate profile. Default: - generated
        :param pod_execution_role: The pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. Default: - a role will be automatically created
        :param removal_policy: The removal policy applied to the custom resource that manages the Fargate profile. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnet_selection: Select which subnets to launch your pods into. At this time, pods running on Fargate are not assigned public IP addresses, so only private subnets (with no direct route to an Internet Gateway) are allowed. You must specify the VPC to customize the subnet selection Default: - all private subnets of the VPC are selected.
        :param vpc: The VPC from which to select subnets to launch your pods into. By default, all private subnets are selected. You can customize this using ``subnetSelection``. Default: - all private subnets used by the EKS cluster
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff1441149066c392d795ca95a53178129d4e20453a143b0f47b7798a83079d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FargateProfileProps(
            cluster=cluster,
            selectors=selectors,
            fargate_profile_name=fargate_profile_name,
            pod_execution_role=pod_execution_role,
            removal_policy=removal_policy,
            subnet_selection=subnet_selection,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="fargateProfileArn")
    def fargate_profile_arn(self) -> builtins.str:
        '''The full Amazon Resource Name (ARN) of the Fargate profile.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fargateProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="fargateProfileName")
    def fargate_profile_name(self) -> builtins.str:
        '''The name of the Fargate profile.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fargateProfileName"))

    @builtins.property
    @jsii.member(jsii_name="podExecutionRole")
    def pod_execution_role(self) -> "_IRole_235f5d8e":
        '''The pod execution role to use for pods that match the selectors in the Fargate profile.

        The pod execution role allows Fargate infrastructure to
        register with your cluster as a node, and it provides read access to Amazon
        ECR image repositories.
        '''
        return typing.cast("_IRole_235f5d8e", jsii.get(self, "podExecutionRole"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Resource tags.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.FargateProfileOptions",
    jsii_struct_bases=[],
    name_mapping={
        "selectors": "selectors",
        "fargate_profile_name": "fargateProfileName",
        "pod_execution_role": "podExecutionRole",
        "removal_policy": "removalPolicy",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
    },
)
class FargateProfileOptions:
    def __init__(
        self,
        *,
        selectors: typing.Sequence[typing.Union["Selector", typing.Dict[builtins.str, typing.Any]]],
        fargate_profile_name: typing.Optional[builtins.str] = None,
        pod_execution_role: typing.Optional["_IRole_235f5d8e"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnet_selection: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
    ) -> None:
        '''Options for defining EKS Fargate Profiles.

        :param selectors: The selectors to match for pods to use this Fargate profile. Each selector must have an associated namespace. Optionally, you can also specify labels for a namespace. At least one selector is required and you may specify up to five selectors.
        :param fargate_profile_name: The name of the Fargate profile. Default: - generated
        :param pod_execution_role: The pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. Default: - a role will be automatically created
        :param removal_policy: The removal policy applied to the custom resource that manages the Fargate profile. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnet_selection: Select which subnets to launch your pods into. At this time, pods running on Fargate are not assigned public IP addresses, so only private subnets (with no direct route to an Internet Gateway) are allowed. You must specify the VPC to customize the subnet selection Default: - all private subnets of the VPC are selected.
        :param vpc: The VPC from which to select subnets to launch your pods into. By default, all private subnets are selected. You can customize this using ``subnetSelection``. Default: - all private subnets used by the EKS cluster

        :exampleMetadata: infused

        Example::

            cluster = eks.Cluster(self, "ManagedNodeCluster",
                version=eks.KubernetesVersion.V1_34,
                default_capacity_type=eks.DefaultCapacityType.NODEGROUP
            )
            
            # Add a Fargate Profile for specific workloads (e.g., default namespace)
            cluster.add_fargate_profile("FargateProfile",
                selectors=[eks.Selector(namespace="default")
                ]
            )
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = _SubnetSelection_e57d76df(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c42506f4872e7f1d6b355f123ba490e44a15df088f6604e95487339a45279c)
            check_type(argname="argument selectors", value=selectors, expected_type=type_hints["selectors"])
            check_type(argname="argument fargate_profile_name", value=fargate_profile_name, expected_type=type_hints["fargate_profile_name"])
            check_type(argname="argument pod_execution_role", value=pod_execution_role, expected_type=type_hints["pod_execution_role"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "selectors": selectors,
        }
        if fargate_profile_name is not None:
            self._values["fargate_profile_name"] = fargate_profile_name
        if pod_execution_role is not None:
            self._values["pod_execution_role"] = pod_execution_role
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def selectors(self) -> typing.List["Selector"]:
        '''The selectors to match for pods to use this Fargate profile.

        Each selector
        must have an associated namespace. Optionally, you can also specify labels
        for a namespace.

        At least one selector is required and you may specify up to five selectors.
        '''
        result = self._values.get("selectors")
        assert result is not None, "Required property 'selectors' is missing"
        return typing.cast(typing.List["Selector"], result)

    @builtins.property
    def fargate_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Fargate profile.

        :default: - generated
        '''
        result = self._values.get("fargate_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_execution_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The pod execution role to use for pods that match the selectors in the Fargate profile.

        The pod execution role allows Fargate infrastructure to
        register with your cluster as a node, and it provides read access to Amazon
        ECR image repositories.

        :default: - a role will be automatically created

        :see: https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html
        '''
        result = self._values.get("pod_execution_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Fargate profile.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional["_SubnetSelection_e57d76df"]:
        '''Select which subnets to launch your pods into.

        At this time, pods running
        on Fargate are not assigned public IP addresses, so only private subnets
        (with no direct route to an Internet Gateway) are allowed.

        You must specify the VPC to customize the subnet selection

        :default: - all private subnets of the VPC are selected.
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional["_SubnetSelection_e57d76df"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["_IVpc_f30d5663"]:
        '''The VPC from which to select subnets to launch your pods into.

        By default, all private subnets are selected. You can customize this using
        ``subnetSelection``.

        :default: - all private subnets used by the EKS cluster
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["_IVpc_f30d5663"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateProfileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.FargateProfileProps",
    jsii_struct_bases=[FargateProfileOptions],
    name_mapping={
        "selectors": "selectors",
        "fargate_profile_name": "fargateProfileName",
        "pod_execution_role": "podExecutionRole",
        "removal_policy": "removalPolicy",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
        "cluster": "cluster",
    },
)
class FargateProfileProps(FargateProfileOptions):
    def __init__(
        self,
        *,
        selectors: typing.Sequence[typing.Union["Selector", typing.Dict[builtins.str, typing.Any]]],
        fargate_profile_name: typing.Optional[builtins.str] = None,
        pod_execution_role: typing.Optional["_IRole_235f5d8e"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnet_selection: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
        cluster: "Cluster",
    ) -> None:
        '''Configuration props for EKS Fargate Profiles.

        :param selectors: The selectors to match for pods to use this Fargate profile. Each selector must have an associated namespace. Optionally, you can also specify labels for a namespace. At least one selector is required and you may specify up to five selectors.
        :param fargate_profile_name: The name of the Fargate profile. Default: - generated
        :param pod_execution_role: The pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. Default: - a role will be automatically created
        :param removal_policy: The removal policy applied to the custom resource that manages the Fargate profile. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnet_selection: Select which subnets to launch your pods into. At this time, pods running on Fargate are not assigned public IP addresses, so only private subnets (with no direct route to an Internet Gateway) are allowed. You must specify the VPC to customize the subnet selection Default: - all private subnets of the VPC are selected.
        :param vpc: The VPC from which to select subnets to launch your pods into. By default, all private subnets are selected. You can customize this using ``subnetSelection``. Default: - all private subnets used by the EKS cluster
        :param cluster: The EKS cluster to apply the Fargate profile to. [disable-awslint:ref-via-interface]

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            eks.FargateProfile(self, "MyProfile",
                cluster=cluster,
                selectors=[eks.Selector(namespace="default")]
            )
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = _SubnetSelection_e57d76df(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be66b2c09f65387bbc144563f27bb4e976109284f231b60f6fd8c49f0937403f)
            check_type(argname="argument selectors", value=selectors, expected_type=type_hints["selectors"])
            check_type(argname="argument fargate_profile_name", value=fargate_profile_name, expected_type=type_hints["fargate_profile_name"])
            check_type(argname="argument pod_execution_role", value=pod_execution_role, expected_type=type_hints["pod_execution_role"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "selectors": selectors,
            "cluster": cluster,
        }
        if fargate_profile_name is not None:
            self._values["fargate_profile_name"] = fargate_profile_name
        if pod_execution_role is not None:
            self._values["pod_execution_role"] = pod_execution_role
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def selectors(self) -> typing.List["Selector"]:
        '''The selectors to match for pods to use this Fargate profile.

        Each selector
        must have an associated namespace. Optionally, you can also specify labels
        for a namespace.

        At least one selector is required and you may specify up to five selectors.
        '''
        result = self._values.get("selectors")
        assert result is not None, "Required property 'selectors' is missing"
        return typing.cast(typing.List["Selector"], result)

    @builtins.property
    def fargate_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Fargate profile.

        :default: - generated
        '''
        result = self._values.get("fargate_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_execution_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The pod execution role to use for pods that match the selectors in the Fargate profile.

        The pod execution role allows Fargate infrastructure to
        register with your cluster as a node, and it provides read access to Amazon
        ECR image repositories.

        :default: - a role will be automatically created

        :see: https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html
        '''
        result = self._values.get("pod_execution_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Fargate profile.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional["_SubnetSelection_e57d76df"]:
        '''Select which subnets to launch your pods into.

        At this time, pods running
        on Fargate are not assigned public IP addresses, so only private subnets
        (with no direct route to an Internet Gateway) are allowed.

        You must specify the VPC to customize the subnet selection

        :default: - all private subnets of the VPC are selected.
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional["_SubnetSelection_e57d76df"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["_IVpc_f30d5663"]:
        '''The VPC from which to select subnets to launch your pods into.

        By default, all private subnets are selected. You can customize this using
        ``subnetSelection``.

        :default: - all private subnets used by the EKS cluster
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["_IVpc_f30d5663"], result)

    @builtins.property
    def cluster(self) -> "Cluster":
        '''The EKS cluster to apply the Fargate profile to.

        [disable-awslint:ref-via-interface]
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("Cluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.GrantAccessOptions",
    jsii_struct_bases=[],
    name_mapping={"access_entry_type": "accessEntryType"},
)
class GrantAccessOptions:
    def __init__(
        self,
        *,
        access_entry_type: typing.Optional["AccessEntryType"] = None,
    ) -> None:
        '''Options for granting access to a cluster.

        :param access_entry_type: The type of the access entry. Specify ``AccessEntryType.EC2`` for EKS Auto Mode node roles, ``AccessEntryType.HYBRID_LINUX`` for EKS Hybrid Nodes, or ``AccessEntryType.HYPERPOD_LINUX`` for SageMaker HyperPod. Note that EC2, HYBRID_LINUX, and HYPERPOD_LINUX types cannot have access policies attached per AWS EKS API constraints. Default: AccessEntryType.STANDARD - Standard access entry type that supports access policies

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            # node_role: iam.Role
            
            
            # Grant access with EC2 type for Auto Mode node role
            cluster.grant_access("nodeAccess", node_role.role_arn, [
                eks.AccessPolicy.from_access_policy_name("AmazonEKSAutoNodePolicy",
                    access_scope_type=eks.AccessScopeType.CLUSTER
                )
            ], access_entry_type=eks.AccessEntryType.EC2)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e997e86fd860a978b07e581006efa6aba790e360a65c5ddbc81f5d2e030ecc6)
            check_type(argname="argument access_entry_type", value=access_entry_type, expected_type=type_hints["access_entry_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_entry_type is not None:
            self._values["access_entry_type"] = access_entry_type

    @builtins.property
    def access_entry_type(self) -> typing.Optional["AccessEntryType"]:
        '''The type of the access entry.

        Specify ``AccessEntryType.EC2`` for EKS Auto Mode node roles,
        ``AccessEntryType.HYBRID_LINUX`` for EKS Hybrid Nodes, or
        ``AccessEntryType.HYPERPOD_LINUX`` for SageMaker HyperPod.

        Note that EC2, HYBRID_LINUX, and HYPERPOD_LINUX types cannot
        have access policies attached per AWS EKS API constraints.

        :default: AccessEntryType.STANDARD - Standard access entry type that supports access policies
        '''
        result = self._values.get("access_entry_type")
        return typing.cast(typing.Optional["AccessEntryType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantAccessOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HelmChart(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.HelmChart",
):
    '''Represents a helm chart within the Kubernetes system.

    Applies/deletes the resources using ``kubectl`` in sync with the resource.

    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        
        # option 1: use a construct
        eks.HelmChart(self, "MyOCIChart",
            cluster=cluster,
            chart="some-chart",
            repository="oci://${ACCOUNT_ID}.dkr.ecr.${ACCOUNT_REGION}.amazonaws.com/${REPO_NAME}",
            namespace="oci",
            version="0.0.1"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "ICluster",
        atomic: typing.Optional[builtins.bool] = None,
        chart: typing.Optional[builtins.str] = None,
        chart_asset: typing.Optional["_Asset_ac2a7e61"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]
        :param atomic: Whether or not Helm should treat this operation as atomic; if set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used. Default: false
        :param chart: The name of the chart. Either this or ``chartAsset`` must be specified. Default: - No chart name. Implies ``chartAsset`` is used.
        :param chart_asset: The chart in the form of an asset. Either this or ``chart`` must be specified. Default: - No chart asset. Implies ``chart`` is used.
        :param create_namespace: create namespace if not exist. Default: true
        :param namespace: The Kubernetes namespace scope of the requests. Default: default
        :param release: The name of the release. Default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        :param removal_policy: The removal policy applied to the custom resource that manages the Helm chart. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository which contains the chart. For example: https://charts.helm.sh/stable/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param skip_crds: if set, no CRDs will be installed. Default: - CRDs are installed if not already present
        :param timeout: Amount of time to wait for any individual Kubernetes operation. Maximum 15 minutes. Default: Duration.minutes(5)
        :param values: The values to be used by the chart. For nested values use a nested dictionary. For example: values: { installationCRDs: true, webhook: { port: 9443 } } Default: - No values are provided to the chart.
        :param version: The chart version to install. Default: - If this is not specified, the latest version is installed
        :param wait: Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. Default: - Helm will not wait before marking release as successful
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__267bbdf92ec5bdd2c63df8ddabf0ea08b5fb246323ebab2b8602a9feb2b79dc2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HelmChartProps(
            cluster=cluster,
            atomic=atomic,
            chart=chart,
            chart_asset=chart_asset,
            create_namespace=create_namespace,
            namespace=namespace,
            release=release,
            removal_policy=removal_policy,
            repository=repository,
            skip_crds=skip_crds,
            timeout=timeout,
            values=values,
            version=version,
            wait=wait,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_TYPE")
    def RESOURCE_TYPE(cls) -> builtins.str:
        '''The CloudFormation resource type.'''
        return typing.cast(builtins.str, jsii.sget(cls, "RESOURCE_TYPE"))

    @builtins.property
    @jsii.member(jsii_name="atomic")
    def atomic(self) -> typing.Optional[builtins.bool]:
        '''Whether or not Helm should treat this operation as atomic.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "atomic"))

    @builtins.property
    @jsii.member(jsii_name="chart")
    def chart(self) -> typing.Optional[builtins.str]:
        '''The name of the chart.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "chart"))

    @builtins.property
    @jsii.member(jsii_name="chartAsset")
    def chart_asset(self) -> typing.Optional["_Asset_ac2a7e61"]:
        '''The chart in the form of an asset.'''
        return typing.cast(typing.Optional["_Asset_ac2a7e61"], jsii.get(self, "chartAsset"))

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository which contains the chart.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repository"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''The chart version to install.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.HelmChartOptions",
    jsii_struct_bases=[],
    name_mapping={
        "atomic": "atomic",
        "chart": "chart",
        "chart_asset": "chartAsset",
        "create_namespace": "createNamespace",
        "namespace": "namespace",
        "release": "release",
        "removal_policy": "removalPolicy",
        "repository": "repository",
        "skip_crds": "skipCrds",
        "timeout": "timeout",
        "values": "values",
        "version": "version",
        "wait": "wait",
    },
)
class HelmChartOptions:
    def __init__(
        self,
        *,
        atomic: typing.Optional[builtins.bool] = None,
        chart: typing.Optional[builtins.str] = None,
        chart_asset: typing.Optional["_Asset_ac2a7e61"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Helm Chart options.

        :param atomic: Whether or not Helm should treat this operation as atomic; if set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used. Default: false
        :param chart: The name of the chart. Either this or ``chartAsset`` must be specified. Default: - No chart name. Implies ``chartAsset`` is used.
        :param chart_asset: The chart in the form of an asset. Either this or ``chart`` must be specified. Default: - No chart asset. Implies ``chart`` is used.
        :param create_namespace: create namespace if not exist. Default: true
        :param namespace: The Kubernetes namespace scope of the requests. Default: default
        :param release: The name of the release. Default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        :param removal_policy: The removal policy applied to the custom resource that manages the Helm chart. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository which contains the chart. For example: https://charts.helm.sh/stable/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param skip_crds: if set, no CRDs will be installed. Default: - CRDs are installed if not already present
        :param timeout: Amount of time to wait for any individual Kubernetes operation. Maximum 15 minutes. Default: Duration.minutes(5)
        :param values: The values to be used by the chart. For nested values use a nested dictionary. For example: values: { installationCRDs: true, webhook: { port: 9443 } } Default: - No values are provided to the chart.
        :param version: The chart version to install. Default: - If this is not specified, the latest version is installed
        :param wait: Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. Default: - Helm will not wait before marking release as successful

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3_assets as s3_assets
            
            # cluster: eks.Cluster
            
            chart_asset = s3_assets.Asset(self, "ChartAsset",
                path="/path/to/asset"
            )
            
            cluster.add_helm_chart("test-chart",
                chart_asset=chart_asset
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf3e52a6495d221a1058009786322c331c50f98baa602fdf09109f0f6fcffae)
            check_type(argname="argument atomic", value=atomic, expected_type=type_hints["atomic"])
            check_type(argname="argument chart", value=chart, expected_type=type_hints["chart"])
            check_type(argname="argument chart_asset", value=chart_asset, expected_type=type_hints["chart_asset"])
            check_type(argname="argument create_namespace", value=create_namespace, expected_type=type_hints["create_namespace"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument release", value=release, expected_type=type_hints["release"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument skip_crds", value=skip_crds, expected_type=type_hints["skip_crds"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument wait", value=wait, expected_type=type_hints["wait"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if atomic is not None:
            self._values["atomic"] = atomic
        if chart is not None:
            self._values["chart"] = chart
        if chart_asset is not None:
            self._values["chart_asset"] = chart_asset
        if create_namespace is not None:
            self._values["create_namespace"] = create_namespace
        if namespace is not None:
            self._values["namespace"] = namespace
        if release is not None:
            self._values["release"] = release
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if repository is not None:
            self._values["repository"] = repository
        if skip_crds is not None:
            self._values["skip_crds"] = skip_crds
        if timeout is not None:
            self._values["timeout"] = timeout
        if values is not None:
            self._values["values"] = values
        if version is not None:
            self._values["version"] = version
        if wait is not None:
            self._values["wait"] = wait

    @builtins.property
    def atomic(self) -> typing.Optional[builtins.bool]:
        '''Whether or not Helm should treat this operation as atomic;

        if set, upgrade process rolls back changes
        made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used.

        :default: false
        '''
        result = self._values.get("atomic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def chart(self) -> typing.Optional[builtins.str]:
        '''The name of the chart.

        Either this or ``chartAsset`` must be specified.

        :default: - No chart name. Implies ``chartAsset`` is used.
        '''
        result = self._values.get("chart")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def chart_asset(self) -> typing.Optional["_Asset_ac2a7e61"]:
        '''The chart in the form of an asset.

        Either this or ``chart`` must be specified.

        :default: - No chart asset. Implies ``chart`` is used.
        '''
        result = self._values.get("chart_asset")
        return typing.cast(typing.Optional["_Asset_ac2a7e61"], result)

    @builtins.property
    def create_namespace(self) -> typing.Optional[builtins.bool]:
        '''create namespace if not exist.

        :default: true
        '''
        result = self._values.get("create_namespace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes namespace scope of the requests.

        :default: default
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release(self) -> typing.Optional[builtins.str]:
        '''The name of the release.

        :default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        '''
        result = self._values.get("release")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Helm chart.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository which contains the chart.

        For example: https://charts.helm.sh/stable/

        :default: - No repository will be used, which means that the chart needs to be an absolute URL.
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_crds(self) -> typing.Optional[builtins.bool]:
        '''if set, no CRDs will be installed.

        :default: - CRDs are installed if not already present
        '''
        result = self._values.get("skip_crds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''Amount of time to wait for any individual Kubernetes operation.

        Maximum 15 minutes.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The values to be used by the chart.

        For nested values use a nested dictionary. For example:
        values: {
        installationCRDs: true,
        webhook: { port: 9443 }
        }

        :default: - No values are provided to the chart.
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The chart version to install.

        :default: - If this is not specified, the latest version is installed
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait(self) -> typing.Optional[builtins.bool]:
        '''Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful.

        :default: - Helm will not wait before marking release as successful
        '''
        result = self._values.get("wait")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmChartOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.HelmChartProps",
    jsii_struct_bases=[HelmChartOptions],
    name_mapping={
        "atomic": "atomic",
        "chart": "chart",
        "chart_asset": "chartAsset",
        "create_namespace": "createNamespace",
        "namespace": "namespace",
        "release": "release",
        "removal_policy": "removalPolicy",
        "repository": "repository",
        "skip_crds": "skipCrds",
        "timeout": "timeout",
        "values": "values",
        "version": "version",
        "wait": "wait",
        "cluster": "cluster",
    },
)
class HelmChartProps(HelmChartOptions):
    def __init__(
        self,
        *,
        atomic: typing.Optional[builtins.bool] = None,
        chart: typing.Optional[builtins.str] = None,
        chart_asset: typing.Optional["_Asset_ac2a7e61"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
        cluster: "ICluster",
    ) -> None:
        '''Helm Chart properties.

        :param atomic: Whether or not Helm should treat this operation as atomic; if set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used. Default: false
        :param chart: The name of the chart. Either this or ``chartAsset`` must be specified. Default: - No chart name. Implies ``chartAsset`` is used.
        :param chart_asset: The chart in the form of an asset. Either this or ``chart`` must be specified. Default: - No chart asset. Implies ``chart`` is used.
        :param create_namespace: create namespace if not exist. Default: true
        :param namespace: The Kubernetes namespace scope of the requests. Default: default
        :param release: The name of the release. Default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        :param removal_policy: The removal policy applied to the custom resource that manages the Helm chart. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository which contains the chart. For example: https://charts.helm.sh/stable/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param skip_crds: if set, no CRDs will be installed. Default: - CRDs are installed if not already present
        :param timeout: Amount of time to wait for any individual Kubernetes operation. Maximum 15 minutes. Default: Duration.minutes(5)
        :param values: The values to be used by the chart. For nested values use a nested dictionary. For example: values: { installationCRDs: true, webhook: { port: 9443 } } Default: - No values are provided to the chart.
        :param version: The chart version to install. Default: - If this is not specified, the latest version is installed
        :param wait: Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. Default: - Helm will not wait before marking release as successful
        :param cluster: The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            # option 1: use a construct
            eks.HelmChart(self, "MyOCIChart",
                cluster=cluster,
                chart="some-chart",
                repository="oci://${ACCOUNT_ID}.dkr.ecr.${ACCOUNT_REGION}.amazonaws.com/${REPO_NAME}",
                namespace="oci",
                version="0.0.1"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c30fd78e20ace511773a60bd2e380e390d4d44dfd7df73a2899c789cac8234)
            check_type(argname="argument atomic", value=atomic, expected_type=type_hints["atomic"])
            check_type(argname="argument chart", value=chart, expected_type=type_hints["chart"])
            check_type(argname="argument chart_asset", value=chart_asset, expected_type=type_hints["chart_asset"])
            check_type(argname="argument create_namespace", value=create_namespace, expected_type=type_hints["create_namespace"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument release", value=release, expected_type=type_hints["release"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument skip_crds", value=skip_crds, expected_type=type_hints["skip_crds"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument wait", value=wait, expected_type=type_hints["wait"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
        }
        if atomic is not None:
            self._values["atomic"] = atomic
        if chart is not None:
            self._values["chart"] = chart
        if chart_asset is not None:
            self._values["chart_asset"] = chart_asset
        if create_namespace is not None:
            self._values["create_namespace"] = create_namespace
        if namespace is not None:
            self._values["namespace"] = namespace
        if release is not None:
            self._values["release"] = release
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if repository is not None:
            self._values["repository"] = repository
        if skip_crds is not None:
            self._values["skip_crds"] = skip_crds
        if timeout is not None:
            self._values["timeout"] = timeout
        if values is not None:
            self._values["values"] = values
        if version is not None:
            self._values["version"] = version
        if wait is not None:
            self._values["wait"] = wait

    @builtins.property
    def atomic(self) -> typing.Optional[builtins.bool]:
        '''Whether or not Helm should treat this operation as atomic;

        if set, upgrade process rolls back changes
        made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used.

        :default: false
        '''
        result = self._values.get("atomic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def chart(self) -> typing.Optional[builtins.str]:
        '''The name of the chart.

        Either this or ``chartAsset`` must be specified.

        :default: - No chart name. Implies ``chartAsset`` is used.
        '''
        result = self._values.get("chart")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def chart_asset(self) -> typing.Optional["_Asset_ac2a7e61"]:
        '''The chart in the form of an asset.

        Either this or ``chart`` must be specified.

        :default: - No chart asset. Implies ``chart`` is used.
        '''
        result = self._values.get("chart_asset")
        return typing.cast(typing.Optional["_Asset_ac2a7e61"], result)

    @builtins.property
    def create_namespace(self) -> typing.Optional[builtins.bool]:
        '''create namespace if not exist.

        :default: true
        '''
        result = self._values.get("create_namespace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes namespace scope of the requests.

        :default: default
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release(self) -> typing.Optional[builtins.str]:
        '''The name of the release.

        :default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        '''
        result = self._values.get("release")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Helm chart.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository which contains the chart.

        For example: https://charts.helm.sh/stable/

        :default: - No repository will be used, which means that the chart needs to be an absolute URL.
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_crds(self) -> typing.Optional[builtins.bool]:
        '''if set, no CRDs will be installed.

        :default: - CRDs are installed if not already present
        '''
        result = self._values.get("skip_crds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''Amount of time to wait for any individual Kubernetes operation.

        Maximum 15 minutes.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The values to be used by the chart.

        For nested values use a nested dictionary. For example:
        values: {
        installationCRDs: true,
        webhook: { port: 9443 }
        }

        :default: - No values are provided to the chart.
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The chart version to install.

        :default: - If this is not specified, the latest version is installed
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait(self) -> typing.Optional[builtins.bool]:
        '''Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful.

        :default: - Helm will not wait before marking release as successful
        '''
        result = self._values.get("wait")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The EKS cluster to apply this configuration to.

        [disable-awslint:ref-via-interface]
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmChartProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_eks_v2.IAccessEntry")
class IAccessEntry(
    _IResource_c80c4260,
    _IAccessEntryRef_14bb9c0a,
    typing_extensions.Protocol,
):
    '''Represents an access entry in an Amazon EKS cluster.

    An access entry defines the permissions and scope for a user or role to access an Amazon EKS cluster.

    :extends: IResource *
    :interface: IAccessEntry
    :property: {string} accessEntryArn - The Amazon Resource Name (ARN) of the access entry.
    '''

    @builtins.property
    @jsii.member(jsii_name="accessEntryArn")
    def access_entry_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access entry.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="accessEntryName")
    def access_entry_name(self) -> builtins.str:
        '''The name of the access entry.

        :attribute: true
        '''
        ...


class _IAccessEntryProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IAccessEntryRef_14bb9c0a), # type: ignore[misc]
):
    '''Represents an access entry in an Amazon EKS cluster.

    An access entry defines the permissions and scope for a user or role to access an Amazon EKS cluster.

    :extends: IResource *
    :interface: IAccessEntry
    :property: {string} accessEntryArn - The Amazon Resource Name (ARN) of the access entry.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_eks_v2.IAccessEntry"

    @builtins.property
    @jsii.member(jsii_name="accessEntryArn")
    def access_entry_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access entry.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessEntryArn"))

    @builtins.property
    @jsii.member(jsii_name="accessEntryName")
    def access_entry_name(self) -> builtins.str:
        '''The name of the access entry.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessEntryName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessEntry).__jsii_proxy_class__ = lambda : _IAccessEntryProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_eks_v2.IAccessPolicy")
class IAccessPolicy(typing_extensions.Protocol):
    '''Represents an access policy that defines the permissions and scope for a user or role to access an Amazon EKS cluster.

    :interface: IAccessPolicy
    '''

    @builtins.property
    @jsii.member(jsii_name="accessScope")
    def access_scope(self) -> "AccessScope":
        '''The scope of the access policy, which determines the level of access granted.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        '''The access policy itself, which defines the specific permissions.'''
        ...


class _IAccessPolicyProxy:
    '''Represents an access policy that defines the permissions and scope for a user or role to access an Amazon EKS cluster.

    :interface: IAccessPolicy
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_eks_v2.IAccessPolicy"

    @builtins.property
    @jsii.member(jsii_name="accessScope")
    def access_scope(self) -> "AccessScope":
        '''The scope of the access policy, which determines the level of access granted.'''
        return typing.cast("AccessScope", jsii.get(self, "accessScope"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        '''The access policy itself, which defines the specific permissions.'''
        return typing.cast(builtins.str, jsii.get(self, "policy"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPolicy).__jsii_proxy_class__ = lambda : _IAccessPolicyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_eks_v2.IAddon")
class IAddon(_IResource_c80c4260, _IAddonRef_fb5de88c, typing_extensions.Protocol):
    '''Represents an Amazon EKS Add-On.'''

    @builtins.property
    @jsii.member(jsii_name="addonArn")
    def addon_arn(self) -> builtins.str:
        '''ARN of the Add-On.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="addonName")
    def addon_name(self) -> builtins.str:
        '''Name of the Add-On.

        :attribute: true
        '''
        ...


class _IAddonProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IAddonRef_fb5de88c), # type: ignore[misc]
):
    '''Represents an Amazon EKS Add-On.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_eks_v2.IAddon"

    @builtins.property
    @jsii.member(jsii_name="addonArn")
    def addon_arn(self) -> builtins.str:
        '''ARN of the Add-On.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "addonArn"))

    @builtins.property
    @jsii.member(jsii_name="addonName")
    def addon_name(self) -> builtins.str:
        '''Name of the Add-On.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "addonName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAddon).__jsii_proxy_class__ = lambda : _IAddonProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_eks_v2.ICluster")
class ICluster(
    _IResource_c80c4260,
    _IConnectable_10015a05,
    _IClusterRef_5527f448,
    typing_extensions.Protocol,
):
    '''An EKS cluster.'''

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterCertificateAuthorityData")
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''The certificate-authority-data for your cluster.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterEncryptionConfigKeyArn")
    def cluster_encryption_config_key_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) or alias of the customer master key (CMK).

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        '''The API Server endpoint URL.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The physical name of the Cluster.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroup")
    def cluster_security_group(self) -> "_ISecurityGroup_acf8a799":
        '''The cluster security group that was created by Amazon EKS for the cluster.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> builtins.str:
        '''The id of the cluster security group that was created by Amazon EKS for the cluster.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProvider")
    def open_id_connect_provider(self) -> "_IOpenIdConnectProvider_203f0793":
        '''The Open ID Connect Provider of the cluster used to configure Service Accounts.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="prune")
    def prune(self) -> builtins.bool:
        '''Indicates whether Kubernetes resources can be automatically pruned.

        When
        this is enabled (default), prune labels will be allocated and injected to
        each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "_IVpc_f30d5663":
        '''The VPC in which this Cluster was created.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="eksPodIdentityAgent")
    def eks_pod_identity_agent(self) -> typing.Optional["IAddon"]:
        '''The EKS Pod Identity Agent addon for the EKS cluster.

        The EKS Pod Identity Agent is responsible for managing the temporary credentials
        used by pods in the cluster to access AWS resources. It runs as a DaemonSet on
        each node and provides the necessary credentials to the pods based on their
        associated service account.

        This property returns the ``CfnAddon`` resource representing the EKS Pod Identity
        Agent addon. If the addon has not been created yet, it will be created and
        returned.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="ipFamily")
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: - IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="kubectlProvider")
    def kubectl_provider(self) -> typing.Optional["IKubectlProvider"]:
        '''Kubectl Provider for issuing kubectl commands against it.

        If not defined, a default provider will be used
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="kubectlProviderOptions")
    def kubectl_provider_options(self) -> typing.Optional["KubectlProviderOptions"]:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        If defined, ``kubectlLayer`` is a required property.

        :default: - kubectl provider will not be created
        '''
        ...

    @jsii.member(jsii_name="addCdk8sChart")
    def add_cdk8s_chart(
        self,
        id: builtins.str,
        chart: "_constructs_77d1e7e8.Construct",
        *,
        ingress_alb: typing.Optional[builtins.bool] = None,
        ingress_alb_scheme: typing.Optional["AlbScheme"] = None,
        prune: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
    ) -> "KubernetesManifest":
        '''Defines a CDK8s chart in this cluster.

        :param id: logical id of this chart.
        :param chart: the cdk8s chart.
        :param ingress_alb: Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller. Default: false
        :param ingress_alb_scheme: Specify the ALB scheme that should be applied to ``Ingress`` resources. Only applicable if ``ingressAlb`` is set to ``true``. Default: AlbScheme.INTERNAL
        :param prune: When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted. To address this, ``kubectl apply`` has a ``--prune`` option which will query the cluster for all resources with a specific label and will remove all the labeld resources that are not part of the applied manifest. If this option is disabled and a resource is removed, it will become "orphaned" and will not be deleted from the cluster. When this option is enabled (default), the construct will inject a label to all Kubernetes resources included in this manifest which will be used to prune resources when the manifest changes via ``kubectl apply --prune``. The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the 42-char unique address of this construct in the construct tree. Value is empty. Default: - based on the prune option of the cluster, which is ``true`` unless otherwise specified.
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes manifest. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param skip_validation: A flag to signify if the manifest validation should be skipped. Default: false

        :return: a ``KubernetesManifest`` construct representing the chart.
        '''
        ...

    @jsii.member(jsii_name="addHelmChart")
    def add_helm_chart(
        self,
        id: builtins.str,
        *,
        atomic: typing.Optional[builtins.bool] = None,
        chart: typing.Optional[builtins.str] = None,
        chart_asset: typing.Optional["_Asset_ac2a7e61"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
    ) -> "HelmChart":
        '''Defines a Helm chart in this cluster.

        :param id: logical id of this chart.
        :param atomic: Whether or not Helm should treat this operation as atomic; if set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used. Default: false
        :param chart: The name of the chart. Either this or ``chartAsset`` must be specified. Default: - No chart name. Implies ``chartAsset`` is used.
        :param chart_asset: The chart in the form of an asset. Either this or ``chart`` must be specified. Default: - No chart asset. Implies ``chart`` is used.
        :param create_namespace: create namespace if not exist. Default: true
        :param namespace: The Kubernetes namespace scope of the requests. Default: default
        :param release: The name of the release. Default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        :param removal_policy: The removal policy applied to the custom resource that manages the Helm chart. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository which contains the chart. For example: https://charts.helm.sh/stable/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param skip_crds: if set, no CRDs will be installed. Default: - CRDs are installed if not already present
        :param timeout: Amount of time to wait for any individual Kubernetes operation. Maximum 15 minutes. Default: Duration.minutes(5)
        :param values: The values to be used by the chart. For nested values use a nested dictionary. For example: values: { installationCRDs: true, webhook: { port: 9443 } } Default: - No values are provided to the chart.
        :param version: The chart version to install. Default: - If this is not specified, the latest version is installed
        :param wait: Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. Default: - Helm will not wait before marking release as successful

        :return: a ``HelmChart`` construct
        '''
        ...

    @jsii.member(jsii_name="addManifest")
    def add_manifest(
        self,
        id: builtins.str,
        *manifest: typing.Mapping[builtins.str, typing.Any],
    ) -> "KubernetesManifest":
        '''Defines a Kubernetes resource in this cluster.

        The manifest will be applied/deleted using kubectl as needed.

        :param id: logical id of this manifest.
        :param manifest: a list of Kubernetes resource specifications.

        :return: a ``KubernetesManifest`` object.
        '''
        ...

    @jsii.member(jsii_name="addServiceAccount")
    def add_service_account(
        self,
        id: builtins.str,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        identity_type: typing.Optional["IdentityType"] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> "ServiceAccount":
        '''Creates a new service account with corresponding IAM Role (IRSA).

        :param id: logical id of service account.
        :param annotations: Additional annotations of the service account. Default: - no additional annotations
        :param identity_type: The identity type to use for the service account. Default: IdentityType.IRSA
        :param labels: Additional labels of the service account. Default: - no additional labels
        :param name: The name of the service account. The name of a ServiceAccount object must be a valid DNS subdomain name. https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ Default: - If no name is given, it will use the id of the resource.
        :param namespace: The namespace of the service account. All namespace names must be valid RFC 1123 DNS labels. https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns Default: "default"
        :param overwrite_service_account: Overwrite existing service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the service account is created. Otherwise, if there is already a service account in the cluster with the same name, the operation will fail. Default: false
        :param removal_policy: The removal policy applied to the service account resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        '''
        ...

    @jsii.member(jsii_name="connectAutoScalingGroupCapacity")
    def connect_auto_scaling_group_capacity(
        self,
        auto_scaling_group: "_AutoScalingGroup_c547a7b9",
        *,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[typing.Union["BootstrapOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        machine_image_type: typing.Optional["MachineImageType"] = None,
    ) -> None:
        '''Connect capacity in the form of an existing AutoScalingGroup to the EKS cluster.

        The AutoScalingGroup must be running an EKS-optimized AMI containing the
        /etc/eks/bootstrap.sh script. This method will configure Security Groups,
        add the right policies to the instance role, apply the right tags, and add
        the required user data to the instance's launch configuration.

        Prefer to use ``addAutoScalingGroupCapacity`` if possible.

        :param auto_scaling_group: [disable-awslint:ref-via-interface].
        :param bootstrap_enabled: Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: Allows options for node bootstrapping through EC2 user data. Default: - default options
        :param machine_image_type: Allow options to specify different machine image type. Default: MachineImageType.AMAZON_LINUX_2

        :see: https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
        '''
        ...


class _IClusterProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IConnectable_10015a05), # type: ignore[misc]
    jsii.proxy_for(_IClusterRef_5527f448), # type: ignore[misc]
):
    '''An EKS cluster.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_eks_v2.ICluster"

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @builtins.property
    @jsii.member(jsii_name="clusterCertificateAuthorityData")
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''The certificate-authority-data for your cluster.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterCertificateAuthorityData"))

    @builtins.property
    @jsii.member(jsii_name="clusterEncryptionConfigKeyArn")
    def cluster_encryption_config_key_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) or alias of the customer master key (CMK).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterEncryptionConfigKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        '''The API Server endpoint URL.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The physical name of the Cluster.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroup")
    def cluster_security_group(self) -> "_ISecurityGroup_acf8a799":
        '''The cluster security group that was created by Amazon EKS for the cluster.

        :attribute: true
        '''
        return typing.cast("_ISecurityGroup_acf8a799", jsii.get(self, "clusterSecurityGroup"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> builtins.str:
        '''The id of the cluster security group that was created by Amazon EKS for the cluster.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterSecurityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProvider")
    def open_id_connect_provider(self) -> "_IOpenIdConnectProvider_203f0793":
        '''The Open ID Connect Provider of the cluster used to configure Service Accounts.'''
        return typing.cast("_IOpenIdConnectProvider_203f0793", jsii.get(self, "openIdConnectProvider"))

    @builtins.property
    @jsii.member(jsii_name="prune")
    def prune(self) -> builtins.bool:
        '''Indicates whether Kubernetes resources can be automatically pruned.

        When
        this is enabled (default), prune labels will be allocated and injected to
        each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "prune"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "_IVpc_f30d5663":
        '''The VPC in which this Cluster was created.'''
        return typing.cast("_IVpc_f30d5663", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="eksPodIdentityAgent")
    def eks_pod_identity_agent(self) -> typing.Optional["IAddon"]:
        '''The EKS Pod Identity Agent addon for the EKS cluster.

        The EKS Pod Identity Agent is responsible for managing the temporary credentials
        used by pods in the cluster to access AWS resources. It runs as a DaemonSet on
        each node and provides the necessary credentials to the pods based on their
        associated service account.

        This property returns the ``CfnAddon`` resource representing the EKS Pod Identity
        Agent addon. If the addon has not been created yet, it will be created and
        returned.
        '''
        return typing.cast(typing.Optional["IAddon"], jsii.get(self, "eksPodIdentityAgent"))

    @builtins.property
    @jsii.member(jsii_name="ipFamily")
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: - IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        return typing.cast(typing.Optional["IpFamily"], jsii.get(self, "ipFamily"))

    @builtins.property
    @jsii.member(jsii_name="kubectlProvider")
    def kubectl_provider(self) -> typing.Optional["IKubectlProvider"]:
        '''Kubectl Provider for issuing kubectl commands against it.

        If not defined, a default provider will be used
        '''
        return typing.cast(typing.Optional["IKubectlProvider"], jsii.get(self, "kubectlProvider"))

    @builtins.property
    @jsii.member(jsii_name="kubectlProviderOptions")
    def kubectl_provider_options(self) -> typing.Optional["KubectlProviderOptions"]:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        If defined, ``kubectlLayer`` is a required property.

        :default: - kubectl provider will not be created
        '''
        return typing.cast(typing.Optional["KubectlProviderOptions"], jsii.get(self, "kubectlProviderOptions"))

    @jsii.member(jsii_name="addCdk8sChart")
    def add_cdk8s_chart(
        self,
        id: builtins.str,
        chart: "_constructs_77d1e7e8.Construct",
        *,
        ingress_alb: typing.Optional[builtins.bool] = None,
        ingress_alb_scheme: typing.Optional["AlbScheme"] = None,
        prune: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
    ) -> "KubernetesManifest":
        '''Defines a CDK8s chart in this cluster.

        :param id: logical id of this chart.
        :param chart: the cdk8s chart.
        :param ingress_alb: Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller. Default: false
        :param ingress_alb_scheme: Specify the ALB scheme that should be applied to ``Ingress`` resources. Only applicable if ``ingressAlb`` is set to ``true``. Default: AlbScheme.INTERNAL
        :param prune: When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted. To address this, ``kubectl apply`` has a ``--prune`` option which will query the cluster for all resources with a specific label and will remove all the labeld resources that are not part of the applied manifest. If this option is disabled and a resource is removed, it will become "orphaned" and will not be deleted from the cluster. When this option is enabled (default), the construct will inject a label to all Kubernetes resources included in this manifest which will be used to prune resources when the manifest changes via ``kubectl apply --prune``. The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the 42-char unique address of this construct in the construct tree. Value is empty. Default: - based on the prune option of the cluster, which is ``true`` unless otherwise specified.
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes manifest. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param skip_validation: A flag to signify if the manifest validation should be skipped. Default: false

        :return: a ``KubernetesManifest`` construct representing the chart.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff83de86e871d5dc9fcf4c6adc16aedcbec2d949a716c25c5d1a2e0af94d7f97)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument chart", value=chart, expected_type=type_hints["chart"])
        options = KubernetesManifestOptions(
            ingress_alb=ingress_alb,
            ingress_alb_scheme=ingress_alb_scheme,
            prune=prune,
            removal_policy=removal_policy,
            skip_validation=skip_validation,
        )

        return typing.cast("KubernetesManifest", jsii.invoke(self, "addCdk8sChart", [id, chart, options]))

    @jsii.member(jsii_name="addHelmChart")
    def add_helm_chart(
        self,
        id: builtins.str,
        *,
        atomic: typing.Optional[builtins.bool] = None,
        chart: typing.Optional[builtins.str] = None,
        chart_asset: typing.Optional["_Asset_ac2a7e61"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
    ) -> "HelmChart":
        '''Defines a Helm chart in this cluster.

        :param id: logical id of this chart.
        :param atomic: Whether or not Helm should treat this operation as atomic; if set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used. Default: false
        :param chart: The name of the chart. Either this or ``chartAsset`` must be specified. Default: - No chart name. Implies ``chartAsset`` is used.
        :param chart_asset: The chart in the form of an asset. Either this or ``chart`` must be specified. Default: - No chart asset. Implies ``chart`` is used.
        :param create_namespace: create namespace if not exist. Default: true
        :param namespace: The Kubernetes namespace scope of the requests. Default: default
        :param release: The name of the release. Default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        :param removal_policy: The removal policy applied to the custom resource that manages the Helm chart. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository which contains the chart. For example: https://charts.helm.sh/stable/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param skip_crds: if set, no CRDs will be installed. Default: - CRDs are installed if not already present
        :param timeout: Amount of time to wait for any individual Kubernetes operation. Maximum 15 minutes. Default: Duration.minutes(5)
        :param values: The values to be used by the chart. For nested values use a nested dictionary. For example: values: { installationCRDs: true, webhook: { port: 9443 } } Default: - No values are provided to the chart.
        :param version: The chart version to install. Default: - If this is not specified, the latest version is installed
        :param wait: Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. Default: - Helm will not wait before marking release as successful

        :return: a ``HelmChart`` construct
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e91d47c6f3469869f69fbc87b6d30081218e0b6ed8b1b7e87973df9e2d30b3)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = HelmChartOptions(
            atomic=atomic,
            chart=chart,
            chart_asset=chart_asset,
            create_namespace=create_namespace,
            namespace=namespace,
            release=release,
            removal_policy=removal_policy,
            repository=repository,
            skip_crds=skip_crds,
            timeout=timeout,
            values=values,
            version=version,
            wait=wait,
        )

        return typing.cast("HelmChart", jsii.invoke(self, "addHelmChart", [id, options]))

    @jsii.member(jsii_name="addManifest")
    def add_manifest(
        self,
        id: builtins.str,
        *manifest: typing.Mapping[builtins.str, typing.Any],
    ) -> "KubernetesManifest":
        '''Defines a Kubernetes resource in this cluster.

        The manifest will be applied/deleted using kubectl as needed.

        :param id: logical id of this manifest.
        :param manifest: a list of Kubernetes resource specifications.

        :return: a ``KubernetesManifest`` object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c0500823c7aaca8f20a0f9333fed3477a09d69b911373e1dd9617cb7278018)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument manifest", value=manifest, expected_type=typing.Tuple[type_hints["manifest"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("KubernetesManifest", jsii.invoke(self, "addManifest", [id, *manifest]))

    @jsii.member(jsii_name="addServiceAccount")
    def add_service_account(
        self,
        id: builtins.str,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        identity_type: typing.Optional["IdentityType"] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> "ServiceAccount":
        '''Creates a new service account with corresponding IAM Role (IRSA).

        :param id: logical id of service account.
        :param annotations: Additional annotations of the service account. Default: - no additional annotations
        :param identity_type: The identity type to use for the service account. Default: IdentityType.IRSA
        :param labels: Additional labels of the service account. Default: - no additional labels
        :param name: The name of the service account. The name of a ServiceAccount object must be a valid DNS subdomain name. https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ Default: - If no name is given, it will use the id of the resource.
        :param namespace: The namespace of the service account. All namespace names must be valid RFC 1123 DNS labels. https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns Default: "default"
        :param overwrite_service_account: Overwrite existing service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the service account is created. Otherwise, if there is already a service account in the cluster with the same name, the operation will fail. Default: false
        :param removal_policy: The removal policy applied to the service account resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390d49561f44f1197bf5781d054e03a9acb2c7981e79c9c146a535451ecf40fb)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ServiceAccountOptions(
            annotations=annotations,
            identity_type=identity_type,
            labels=labels,
            name=name,
            namespace=namespace,
            overwrite_service_account=overwrite_service_account,
            removal_policy=removal_policy,
        )

        return typing.cast("ServiceAccount", jsii.invoke(self, "addServiceAccount", [id, options]))

    @jsii.member(jsii_name="connectAutoScalingGroupCapacity")
    def connect_auto_scaling_group_capacity(
        self,
        auto_scaling_group: "_AutoScalingGroup_c547a7b9",
        *,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[typing.Union["BootstrapOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        machine_image_type: typing.Optional["MachineImageType"] = None,
    ) -> None:
        '''Connect capacity in the form of an existing AutoScalingGroup to the EKS cluster.

        The AutoScalingGroup must be running an EKS-optimized AMI containing the
        /etc/eks/bootstrap.sh script. This method will configure Security Groups,
        add the right policies to the instance role, apply the right tags, and add
        the required user data to the instance's launch configuration.

        Prefer to use ``addAutoScalingGroupCapacity`` if possible.

        :param auto_scaling_group: [disable-awslint:ref-via-interface].
        :param bootstrap_enabled: Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: Allows options for node bootstrapping through EC2 user data. Default: - default options
        :param machine_image_type: Allow options to specify different machine image type. Default: MachineImageType.AMAZON_LINUX_2

        :see: https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0c9b9d342838868cfdeecd867068960aa4fe89ce221b96f17f94b06c4b55a94)
            check_type(argname="argument auto_scaling_group", value=auto_scaling_group, expected_type=type_hints["auto_scaling_group"])
        options = AutoScalingGroupOptions(
            bootstrap_enabled=bootstrap_enabled,
            bootstrap_options=bootstrap_options,
            machine_image_type=machine_image_type,
        )

        return typing.cast(None, jsii.invoke(self, "connectAutoScalingGroupCapacity", [auto_scaling_group, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICluster).__jsii_proxy_class__ = lambda : _IClusterProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_eks_v2.IKubectlProvider")
class IKubectlProvider(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''Imported KubectlProvider that can be used in place of the default one created by CDK.'''

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''The custom resource provider's service token.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The role of the provider lambda function.

        If undefined,
        you cannot use this provider to deploy helm charts.
        '''
        ...


class _IKubectlProviderProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''Imported KubectlProvider that can be used in place of the default one created by CDK.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_eks_v2.IKubectlProvider"

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''The custom resource provider's service token.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The role of the provider lambda function.

        If undefined,
        you cannot use this provider to deploy helm charts.
        '''
        return typing.cast(typing.Optional["_IRole_235f5d8e"], jsii.get(self, "role"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKubectlProvider).__jsii_proxy_class__ = lambda : _IKubectlProviderProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_eks_v2.INodegroup")
class INodegroup(
    _IResource_c80c4260,
    _INodegroupRef_cac0d8aa,
    typing_extensions.Protocol,
):
    '''NodeGroup interface.'''

    @builtins.property
    @jsii.member(jsii_name="nodegroupName")
    def nodegroup_name(self) -> builtins.str:
        '''Name of the nodegroup.

        :attribute: true
        '''
        ...


class _INodegroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_INodegroupRef_cac0d8aa), # type: ignore[misc]
):
    '''NodeGroup interface.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_eks_v2.INodegroup"

    @builtins.property
    @jsii.member(jsii_name="nodegroupName")
    def nodegroup_name(self) -> builtins.str:
        '''Name of the nodegroup.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "nodegroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INodegroup).__jsii_proxy_class__ = lambda : _INodegroupProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.IdentityType")
class IdentityType(enum.Enum):
    '''Enum representing the different identity types that can be used for a Kubernetes service account.'''

    IRSA = "IRSA"
    '''Use the IAM Roles for Service Accounts (IRSA) identity type.

    IRSA allows you to associate an IAM role with a Kubernetes service account.
    This provides a way to grant permissions to Kubernetes pods by associating an IAM role with a Kubernetes service account.
    The IAM role can then be used to provide AWS credentials to the pods, allowing them to access other AWS resources.

    When enabled, the openIdConnectProvider of the cluster would be created when you create the ServiceAccount.

    :see: https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html
    '''
    POD_IDENTITY = "POD_IDENTITY"
    '''Use the EKS Pod Identities identity type.

    EKS Pod Identities provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles
    provide credentials to Amazon EC2 instances. Instead of creating and distributing your AWS credentials to the containers or using the
    Amazon EC2 instance's role, you associate an IAM role with a Kubernetes service account and configure your Pods to use the service account.

    When enabled, the Pod Identity Agent AddOn of the cluster would be created when you create the ServiceAccount.

    :see: https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.IpFamily")
class IpFamily(enum.Enum):
    '''EKS cluster IP family.'''

    IP_V4 = "IP_V4"
    '''Use IPv4 for pods and services in your cluster.'''
    IP_V6 = "IP_V6"
    '''Use IPv6 for pods and services in your cluster.'''


@jsii.implements(IKubectlProvider)
class KubectlProvider(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.KubectlProvider",
):
    '''Implementation of Kubectl Lambda.

    :exampleMetadata: infused

    Example::

        handler_role = iam.Role.from_role_arn(self, "HandlerRole", "arn:aws:iam::123456789012:role/lambda-role")
        # get the serivceToken from the custom resource provider
        function_arn = lambda_.Function.from_function_name(self, "ProviderOnEventFunc", "ProviderframeworkonEvent-XXX").function_arn
        kubectl_provider = eks.KubectlProvider.from_kubectl_provider_attributes(self, "KubectlProvider",
            service_token=function_arn,
            role=handler_role
        )
        
        cluster = eks.Cluster.from_cluster_attributes(self, "Cluster",
            cluster_name="cluster",
            kubectl_provider=kubectl_provider
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "ICluster",
        kubectl_layer: "_ILayerVersion_5ac127c8",
        awscli_layer: typing.Optional["_ILayerVersion_5ac127c8"] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional["_Size_7b441c34"] = None,
        private_subnets: typing.Optional[typing.Sequence["_ISubnet_d57d1229"]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The cluster to control.
        :param kubectl_layer: An AWS Lambda layer that includes ``kubectl`` and ``helm``.
        :param awscli_layer: An AWS Lambda layer that contains the ``aws`` CLI. Default: - If not defined, a default layer will be used containing the AWS CLI 2.x.
        :param environment: Custom environment variables when running ``kubectl`` against this cluster. Default: - No custom environment variables
        :param memory: The amount of memory allocated to the kubectl provider's lambda function. Default: - 1024
        :param private_subnets: Subnets to host the ``kubectl`` compute resources. If not specified, the k8s endpoint is expected to be accessible publicly. Default: - the k8s is accessible publicly
        :param removal_policy: The removal policy applied to the custom resource that provides kubectl. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param role: An IAM role that can perform kubectl operations against this cluster. The role should be mapped to the ``system:masters`` Kubernetes RBAC role. This role is directly passed to the lambda handler that sends Kube Ctl commands to the cluster. Default: - if not specified, the default role created by a lambda function will be used.
        :param security_group: A security group to use for ``kubectl`` execution. Default: - If not specified, the k8s endpoint is expected to be accessible publicly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aad34a8b7c85b8fafa3a60b89cf1904902b5f18ab4c50ae367481347e5c0b1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KubectlProviderProps(
            cluster=cluster,
            kubectl_layer=kubectl_layer,
            awscli_layer=awscli_layer,
            environment=environment,
            memory=memory,
            private_subnets=private_subnets,
            removal_policy=removal_policy,
            role=role,
            security_group=security_group,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromKubectlProviderAttributes")
    @builtins.classmethod
    def from_kubectl_provider_attributes(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        service_token: builtins.str,
        role: typing.Optional["_IRole_235f5d8e"] = None,
    ) -> "IKubectlProvider":
        '''Import an existing provider.

        :param scope: Construct.
        :param id: an id of resource.
        :param service_token: The kubectl provider lambda arn.
        :param role: The role of the provider lambda function. Only required if you deploy helm charts using this imported provider. Default: - no role.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482e5705a693af11339a7f57c6d0ce81623cec9953281097e3c09cc25d2c6e62)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = KubectlProviderAttributes(service_token=service_token, role=role)

        return typing.cast("IKubectlProvider", jsii.sinvoke(cls, "fromKubectlProviderAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="getKubectlProvider")
    @builtins.classmethod
    def get_kubectl_provider(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        cluster: "ICluster",
    ) -> typing.Optional["IKubectlProvider"]:
        '''Take existing provider on cluster.

        :param scope: Construct.
        :param cluster: k8s cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24a426caec312e2477ccd638d41ff0271e15c86a0c62f06f464e88e5f35fd827)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        return typing.cast(typing.Optional["IKubectlProvider"], jsii.sinvoke(cls, "getKubectlProvider", [scope, cluster]))

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''The custom resource provider's service token.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The IAM execution role of the handler.'''
        return typing.cast(typing.Optional["_IRole_235f5d8e"], jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubectlProviderAttributes",
    jsii_struct_bases=[],
    name_mapping={"service_token": "serviceToken", "role": "role"},
)
class KubectlProviderAttributes:
    def __init__(
        self,
        *,
        service_token: builtins.str,
        role: typing.Optional["_IRole_235f5d8e"] = None,
    ) -> None:
        '''Kubectl Provider Attributes.

        :param service_token: The kubectl provider lambda arn.
        :param role: The role of the provider lambda function. Only required if you deploy helm charts using this imported provider. Default: - no role.

        :exampleMetadata: infused

        Example::

            handler_role = iam.Role.from_role_arn(self, "HandlerRole", "arn:aws:iam::123456789012:role/lambda-role")
            # get the serivceToken from the custom resource provider
            function_arn = lambda_.Function.from_function_name(self, "ProviderOnEventFunc", "ProviderframeworkonEvent-XXX").function_arn
            kubectl_provider = eks.KubectlProvider.from_kubectl_provider_attributes(self, "KubectlProvider",
                service_token=function_arn,
                role=handler_role
            )
            
            cluster = eks.Cluster.from_cluster_attributes(self, "Cluster",
                cluster_name="cluster",
                kubectl_provider=kubectl_provider
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21826c50973a5c6583d4ccfb55d5b9e60e5b35409ed715ada3e709246e16b224)
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_token": service_token,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def service_token(self) -> builtins.str:
        '''The kubectl provider lambda arn.'''
        result = self._values.get("service_token")
        assert result is not None, "Required property 'service_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The role of the provider lambda function.

        Only required if you deploy helm charts using this imported provider.

        :default: - no role.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubectlProviderAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubectlProviderOptions",
    jsii_struct_bases=[],
    name_mapping={
        "kubectl_layer": "kubectlLayer",
        "awscli_layer": "awscliLayer",
        "environment": "environment",
        "memory": "memory",
        "private_subnets": "privateSubnets",
        "removal_policy": "removalPolicy",
        "role": "role",
        "security_group": "securityGroup",
    },
)
class KubectlProviderOptions:
    def __init__(
        self,
        *,
        kubectl_layer: "_ILayerVersion_5ac127c8",
        awscli_layer: typing.Optional["_ILayerVersion_5ac127c8"] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional["_Size_7b441c34"] = None,
        private_subnets: typing.Optional[typing.Sequence["_ISubnet_d57d1229"]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
    ) -> None:
        '''Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster.

        :param kubectl_layer: An AWS Lambda layer that includes ``kubectl`` and ``helm``.
        :param awscli_layer: An AWS Lambda layer that contains the ``aws`` CLI. Default: - If not defined, a default layer will be used containing the AWS CLI 2.x.
        :param environment: Custom environment variables when running ``kubectl`` against this cluster. Default: - No custom environment variables
        :param memory: The amount of memory allocated to the kubectl provider's lambda function. Default: - 1024
        :param private_subnets: Subnets to host the ``kubectl`` compute resources. If not specified, the k8s endpoint is expected to be accessible publicly. Default: - the k8s is accessible publicly
        :param removal_policy: The removal policy applied to the custom resource that provides kubectl. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param role: An IAM role that can perform kubectl operations against this cluster. The role should be mapped to the ``system:masters`` Kubernetes RBAC role. This role is directly passed to the lambda handler that sends Kube Ctl commands to the cluster. Default: - if not specified, the default role created by a lambda function will be used.
        :param security_group: A security group to use for ``kubectl`` execution. Default: - If not specified, the k8s endpoint is expected to be accessible publicly.

        :exampleMetadata: infused

        Example::

            from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer
            
            
            cluster = eks.Cluster(self, "hello-eks",
                version=eks.KubernetesVersion.V1_34,
                kubectl_provider_options=eks.KubectlProviderOptions(
                    kubectl_layer=KubectlV35Layer(self, "kubectl"),
                    environment={
                        "http_proxy": "http://proxy.myproxy.com"
                    }
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db0d43994acd7b6b330a5f26b52341ec27f5672d45b11639c9e406ad65a2134b)
            check_type(argname="argument kubectl_layer", value=kubectl_layer, expected_type=type_hints["kubectl_layer"])
            check_type(argname="argument awscli_layer", value=awscli_layer, expected_type=type_hints["awscli_layer"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument private_subnets", value=private_subnets, expected_type=type_hints["private_subnets"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kubectl_layer": kubectl_layer,
        }
        if awscli_layer is not None:
            self._values["awscli_layer"] = awscli_layer
        if environment is not None:
            self._values["environment"] = environment
        if memory is not None:
            self._values["memory"] = memory
        if private_subnets is not None:
            self._values["private_subnets"] = private_subnets
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group

    @builtins.property
    def kubectl_layer(self) -> "_ILayerVersion_5ac127c8":
        '''An AWS Lambda layer that includes ``kubectl`` and ``helm``.'''
        result = self._values.get("kubectl_layer")
        assert result is not None, "Required property 'kubectl_layer' is missing"
        return typing.cast("_ILayerVersion_5ac127c8", result)

    @builtins.property
    def awscli_layer(self) -> typing.Optional["_ILayerVersion_5ac127c8"]:
        '''An AWS Lambda layer that contains the ``aws`` CLI.

        :default: - If not defined, a default layer will be used containing the AWS CLI 2.x.
        '''
        result = self._values.get("awscli_layer")
        return typing.cast(typing.Optional["_ILayerVersion_5ac127c8"], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom environment variables when running ``kubectl`` against this cluster.

        :default: - No custom environment variables
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def memory(self) -> typing.Optional["_Size_7b441c34"]:
        '''The amount of memory allocated to the kubectl provider's lambda function.

        :default: - 1024
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional["_Size_7b441c34"], result)

    @builtins.property
    def private_subnets(self) -> typing.Optional[typing.List["_ISubnet_d57d1229"]]:
        '''Subnets to host the ``kubectl`` compute resources.

        If not specified, the k8s
        endpoint is expected to be accessible publicly.

        :default: - the k8s is accessible publicly
        '''
        result = self._values.get("private_subnets")
        return typing.cast(typing.Optional[typing.List["_ISubnet_d57d1229"]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that provides kubectl.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''An IAM role that can perform kubectl operations against this cluster.

        The role should be mapped to the ``system:masters`` Kubernetes RBAC role.

        This role is directly passed to the lambda handler that sends Kube Ctl commands to the cluster.

        :default:

        - if not specified, the default role created by a lambda function will
        be used.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def security_group(self) -> typing.Optional["_ISecurityGroup_acf8a799"]:
        '''A security group to use for ``kubectl`` execution.

        :default:

        - If not specified, the k8s endpoint is expected to be accessible
        publicly.
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional["_ISecurityGroup_acf8a799"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubectlProviderOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubectlProviderProps",
    jsii_struct_bases=[KubectlProviderOptions],
    name_mapping={
        "kubectl_layer": "kubectlLayer",
        "awscli_layer": "awscliLayer",
        "environment": "environment",
        "memory": "memory",
        "private_subnets": "privateSubnets",
        "removal_policy": "removalPolicy",
        "role": "role",
        "security_group": "securityGroup",
        "cluster": "cluster",
    },
)
class KubectlProviderProps(KubectlProviderOptions):
    def __init__(
        self,
        *,
        kubectl_layer: "_ILayerVersion_5ac127c8",
        awscli_layer: typing.Optional["_ILayerVersion_5ac127c8"] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional["_Size_7b441c34"] = None,
        private_subnets: typing.Optional[typing.Sequence["_ISubnet_d57d1229"]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
        cluster: "ICluster",
    ) -> None:
        '''Properties for a KubectlProvider.

        :param kubectl_layer: An AWS Lambda layer that includes ``kubectl`` and ``helm``.
        :param awscli_layer: An AWS Lambda layer that contains the ``aws`` CLI. Default: - If not defined, a default layer will be used containing the AWS CLI 2.x.
        :param environment: Custom environment variables when running ``kubectl`` against this cluster. Default: - No custom environment variables
        :param memory: The amount of memory allocated to the kubectl provider's lambda function. Default: - 1024
        :param private_subnets: Subnets to host the ``kubectl`` compute resources. If not specified, the k8s endpoint is expected to be accessible publicly. Default: - the k8s is accessible publicly
        :param removal_policy: The removal policy applied to the custom resource that provides kubectl. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param role: An IAM role that can perform kubectl operations against this cluster. The role should be mapped to the ``system:masters`` Kubernetes RBAC role. This role is directly passed to the lambda handler that sends Kube Ctl commands to the cluster. Default: - if not specified, the default role created by a lambda function will be used.
        :param security_group: A security group to use for ``kubectl`` execution. Default: - If not specified, the k8s endpoint is expected to be accessible publicly.
        :param cluster: The cluster to control.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_eks_v2 as eks_v2
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_lambda as lambda_
            
            # cluster: eks_v2.Cluster
            # layer_version: lambda.LayerVersion
            # role: iam.Role
            # security_group: ec2.SecurityGroup
            # size: cdk.Size
            # subnet: ec2.Subnet
            
            kubectl_provider_props = eks_v2.KubectlProviderProps(
                cluster=cluster,
                kubectl_layer=layer_version,
            
                # the properties below are optional
                awscli_layer=layer_version,
                environment={
                    "environment_key": "environment"
                },
                memory=size,
                private_subnets=[subnet],
                removal_policy=cdk.RemovalPolicy.DESTROY,
                role=role,
                security_group=security_group
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a433dab330d6710bafea4cc09c474eaf4b60af830112e448baa510723d19b0)
            check_type(argname="argument kubectl_layer", value=kubectl_layer, expected_type=type_hints["kubectl_layer"])
            check_type(argname="argument awscli_layer", value=awscli_layer, expected_type=type_hints["awscli_layer"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument private_subnets", value=private_subnets, expected_type=type_hints["private_subnets"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kubectl_layer": kubectl_layer,
            "cluster": cluster,
        }
        if awscli_layer is not None:
            self._values["awscli_layer"] = awscli_layer
        if environment is not None:
            self._values["environment"] = environment
        if memory is not None:
            self._values["memory"] = memory
        if private_subnets is not None:
            self._values["private_subnets"] = private_subnets
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group

    @builtins.property
    def kubectl_layer(self) -> "_ILayerVersion_5ac127c8":
        '''An AWS Lambda layer that includes ``kubectl`` and ``helm``.'''
        result = self._values.get("kubectl_layer")
        assert result is not None, "Required property 'kubectl_layer' is missing"
        return typing.cast("_ILayerVersion_5ac127c8", result)

    @builtins.property
    def awscli_layer(self) -> typing.Optional["_ILayerVersion_5ac127c8"]:
        '''An AWS Lambda layer that contains the ``aws`` CLI.

        :default: - If not defined, a default layer will be used containing the AWS CLI 2.x.
        '''
        result = self._values.get("awscli_layer")
        return typing.cast(typing.Optional["_ILayerVersion_5ac127c8"], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom environment variables when running ``kubectl`` against this cluster.

        :default: - No custom environment variables
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def memory(self) -> typing.Optional["_Size_7b441c34"]:
        '''The amount of memory allocated to the kubectl provider's lambda function.

        :default: - 1024
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional["_Size_7b441c34"], result)

    @builtins.property
    def private_subnets(self) -> typing.Optional[typing.List["_ISubnet_d57d1229"]]:
        '''Subnets to host the ``kubectl`` compute resources.

        If not specified, the k8s
        endpoint is expected to be accessible publicly.

        :default: - the k8s is accessible publicly
        '''
        result = self._values.get("private_subnets")
        return typing.cast(typing.Optional[typing.List["_ISubnet_d57d1229"]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that provides kubectl.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''An IAM role that can perform kubectl operations against this cluster.

        The role should be mapped to the ``system:masters`` Kubernetes RBAC role.

        This role is directly passed to the lambda handler that sends Kube Ctl commands to the cluster.

        :default:

        - if not specified, the default role created by a lambda function will
        be used.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def security_group(self) -> typing.Optional["_ISecurityGroup_acf8a799"]:
        '''A security group to use for ``kubectl`` execution.

        :default:

        - If not specified, the k8s endpoint is expected to be accessible
        publicly.
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional["_ISecurityGroup_acf8a799"], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The cluster to control.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubectlProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesManifest(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesManifest",
):
    '''Represents a manifest within the Kubernetes system.

    Alternatively, you can use ``cluster.addManifest(resource[, resource, ...])``
    to define resources on this cluster.

    Applies/deletes the manifest using ``kubectl``.

    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        
        namespace = cluster.add_manifest("my-namespace", {
            "api_version": "v1",
            "kind": "Namespace",
            "metadata": {"name": "my-app"}
        })
        
        service = cluster.add_manifest("my-service", {
            "metadata": {
                "name": "myservice",
                "namespace": "my-app"
            },
            "spec": {}
        })
        
        service.node.add_dependency(namespace)
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "ICluster",
        manifest: typing.Sequence[typing.Mapping[builtins.str, typing.Any]],
        overwrite: typing.Optional[builtins.bool] = None,
        ingress_alb: typing.Optional[builtins.bool] = None,
        ingress_alb_scheme: typing.Optional["AlbScheme"] = None,
        prune: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The EKS cluster to apply this manifest to. [disable-awslint:ref-via-interface]
        :param manifest: The manifest to apply. Consists of any number of child resources. When the resources are created/updated, this manifest will be applied to the cluster through ``kubectl apply`` and when the resources or the stack is deleted, the resources in the manifest will be deleted through ``kubectl delete``.
        :param overwrite: Overwrite any existing resources. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the resource is created. Otherwise, if there is already a resource in the cluster with the same name, the operation will fail. Default: false
        :param ingress_alb: Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller. Default: false
        :param ingress_alb_scheme: Specify the ALB scheme that should be applied to ``Ingress`` resources. Only applicable if ``ingressAlb`` is set to ``true``. Default: AlbScheme.INTERNAL
        :param prune: When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted. To address this, ``kubectl apply`` has a ``--prune`` option which will query the cluster for all resources with a specific label and will remove all the labeld resources that are not part of the applied manifest. If this option is disabled and a resource is removed, it will become "orphaned" and will not be deleted from the cluster. When this option is enabled (default), the construct will inject a label to all Kubernetes resources included in this manifest which will be used to prune resources when the manifest changes via ``kubectl apply --prune``. The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the 42-char unique address of this construct in the construct tree. Value is empty. Default: - based on the prune option of the cluster, which is ``true`` unless otherwise specified.
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes manifest. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param skip_validation: A flag to signify if the manifest validation should be skipped. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5040cd237de4e6fc90ec31d3e3edb50c772a93243db6531802592e7373b932b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KubernetesManifestProps(
            cluster=cluster,
            manifest=manifest,
            overwrite=overwrite,
            ingress_alb=ingress_alb,
            ingress_alb_scheme=ingress_alb_scheme,
            prune=prune,
            removal_policy=removal_policy,
            skip_validation=skip_validation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_TYPE")
    def RESOURCE_TYPE(cls) -> builtins.str:
        '''The CloudFormation resource type.'''
        return typing.cast(builtins.str, jsii.sget(cls, "RESOURCE_TYPE"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesManifestOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ingress_alb": "ingressAlb",
        "ingress_alb_scheme": "ingressAlbScheme",
        "prune": "prune",
        "removal_policy": "removalPolicy",
        "skip_validation": "skipValidation",
    },
)
class KubernetesManifestOptions:
    def __init__(
        self,
        *,
        ingress_alb: typing.Optional[builtins.bool] = None,
        ingress_alb_scheme: typing.Optional["AlbScheme"] = None,
        prune: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for ``KubernetesManifest``.

        :param ingress_alb: Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller. Default: false
        :param ingress_alb_scheme: Specify the ALB scheme that should be applied to ``Ingress`` resources. Only applicable if ``ingressAlb`` is set to ``true``. Default: AlbScheme.INTERNAL
        :param prune: When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted. To address this, ``kubectl apply`` has a ``--prune`` option which will query the cluster for all resources with a specific label and will remove all the labeld resources that are not part of the applied manifest. If this option is disabled and a resource is removed, it will become "orphaned" and will not be deleted from the cluster. When this option is enabled (default), the construct will inject a label to all Kubernetes resources included in this manifest which will be used to prune resources when the manifest changes via ``kubectl apply --prune``. The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the 42-char unique address of this construct in the construct tree. Value is empty. Default: - based on the prune option of the cluster, which is ``true`` unless otherwise specified.
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes manifest. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param skip_validation: A flag to signify if the manifest validation should be skipped. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_eks_v2 as eks_v2
            
            kubernetes_manifest_options = eks_v2.KubernetesManifestOptions(
                ingress_alb=False,
                ingress_alb_scheme=eks_v2.AlbScheme.INTERNAL,
                prune=False,
                removal_policy=cdk.RemovalPolicy.DESTROY,
                skip_validation=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eb02dba7044365540f72d0cdd546ff96bc7d51d55d23bc2f13b1602b77b3734)
            check_type(argname="argument ingress_alb", value=ingress_alb, expected_type=type_hints["ingress_alb"])
            check_type(argname="argument ingress_alb_scheme", value=ingress_alb_scheme, expected_type=type_hints["ingress_alb_scheme"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument skip_validation", value=skip_validation, expected_type=type_hints["skip_validation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ingress_alb is not None:
            self._values["ingress_alb"] = ingress_alb
        if ingress_alb_scheme is not None:
            self._values["ingress_alb_scheme"] = ingress_alb_scheme
        if prune is not None:
            self._values["prune"] = prune
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if skip_validation is not None:
            self._values["skip_validation"] = skip_validation

    @builtins.property
    def ingress_alb(self) -> typing.Optional[builtins.bool]:
        '''Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller.

        :default: false
        '''
        result = self._values.get("ingress_alb")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ingress_alb_scheme(self) -> typing.Optional["AlbScheme"]:
        '''Specify the ALB scheme that should be applied to ``Ingress`` resources.

        Only applicable if ``ingressAlb`` is set to ``true``.

        :default: AlbScheme.INTERNAL
        '''
        result = self._values.get("ingress_alb_scheme")
        return typing.cast(typing.Optional["AlbScheme"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted.

        To address this, ``kubectl apply`` has a ``--prune`` option which will
        query the cluster for all resources with a specific label and will remove
        all the labeld resources that are not part of the applied manifest. If this
        option is disabled and a resource is removed, it will become "orphaned" and
        will not be deleted from the cluster.

        When this option is enabled (default), the construct will inject a label to
        all Kubernetes resources included in this manifest which will be used to
        prune resources when the manifest changes via ``kubectl apply --prune``.

        The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the
        42-char unique address of this construct in the construct tree. Value is
        empty.

        :default:

        - based on the prune option of the cluster, which is ``true`` unless
        otherwise specified.

        :see: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune-l-your-label
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Kubernetes manifest.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def skip_validation(self) -> typing.Optional[builtins.bool]:
        '''A flag to signify if the manifest validation should be skipped.

        :default: false
        '''
        result = self._values.get("skip_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesManifestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesManifestProps",
    jsii_struct_bases=[KubernetesManifestOptions],
    name_mapping={
        "ingress_alb": "ingressAlb",
        "ingress_alb_scheme": "ingressAlbScheme",
        "prune": "prune",
        "removal_policy": "removalPolicy",
        "skip_validation": "skipValidation",
        "cluster": "cluster",
        "manifest": "manifest",
        "overwrite": "overwrite",
    },
)
class KubernetesManifestProps(KubernetesManifestOptions):
    def __init__(
        self,
        *,
        ingress_alb: typing.Optional[builtins.bool] = None,
        ingress_alb_scheme: typing.Optional["AlbScheme"] = None,
        prune: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
        cluster: "ICluster",
        manifest: typing.Sequence[typing.Mapping[builtins.str, typing.Any]],
        overwrite: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for KubernetesManifest.

        :param ingress_alb: Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller. Default: false
        :param ingress_alb_scheme: Specify the ALB scheme that should be applied to ``Ingress`` resources. Only applicable if ``ingressAlb`` is set to ``true``. Default: AlbScheme.INTERNAL
        :param prune: When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted. To address this, ``kubectl apply`` has a ``--prune`` option which will query the cluster for all resources with a specific label and will remove all the labeld resources that are not part of the applied manifest. If this option is disabled and a resource is removed, it will become "orphaned" and will not be deleted from the cluster. When this option is enabled (default), the construct will inject a label to all Kubernetes resources included in this manifest which will be used to prune resources when the manifest changes via ``kubectl apply --prune``. The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the 42-char unique address of this construct in the construct tree. Value is empty. Default: - based on the prune option of the cluster, which is ``true`` unless otherwise specified.
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes manifest. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param skip_validation: A flag to signify if the manifest validation should be skipped. Default: false
        :param cluster: The EKS cluster to apply this manifest to. [disable-awslint:ref-via-interface]
        :param manifest: The manifest to apply. Consists of any number of child resources. When the resources are created/updated, this manifest will be applied to the cluster through ``kubectl apply`` and when the resources or the stack is deleted, the resources in the manifest will be deleted through ``kubectl delete``.
        :param overwrite: Overwrite any existing resources. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the resource is created. Otherwise, if there is already a resource in the cluster with the same name, the operation will fail. Default: false

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            app_label = {"app": "hello-kubernetes"}
            
            deployment = {
                "api_version": "apps/v1",
                "kind": "Deployment",
                "metadata": {"name": "hello-kubernetes"},
                "spec": {
                    "replicas": 3,
                    "selector": {"match_labels": app_label},
                    "template": {
                        "metadata": {"labels": app_label},
                        "spec": {
                            "containers": [{
                                "name": "hello-kubernetes",
                                "image": "paulbouwer/hello-kubernetes:1.5",
                                "ports": [{"container_port": 8080}]
                            }
                            ]
                        }
                    }
                }
            }
            
            service = {
                "api_version": "v1",
                "kind": "Service",
                "metadata": {"name": "hello-kubernetes"},
                "spec": {
                    "type": "LoadBalancer",
                    "ports": [{"port": 80, "target_port": 8080}],
                    "selector": app_label
                }
            }
            
            # option 1: use a construct
            eks.KubernetesManifest(self, "hello-kub",
                cluster=cluster,
                manifest=[deployment, service]
            )
            
            # or, option2: use `addManifest`
            cluster.add_manifest("hello-kub", service, deployment)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b1104d99f875c1e3595711967bbe93c6dca0a6e48899bd3786b16d96bc081e)
            check_type(argname="argument ingress_alb", value=ingress_alb, expected_type=type_hints["ingress_alb"])
            check_type(argname="argument ingress_alb_scheme", value=ingress_alb_scheme, expected_type=type_hints["ingress_alb_scheme"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument skip_validation", value=skip_validation, expected_type=type_hints["skip_validation"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "manifest": manifest,
        }
        if ingress_alb is not None:
            self._values["ingress_alb"] = ingress_alb
        if ingress_alb_scheme is not None:
            self._values["ingress_alb_scheme"] = ingress_alb_scheme
        if prune is not None:
            self._values["prune"] = prune
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if skip_validation is not None:
            self._values["skip_validation"] = skip_validation
        if overwrite is not None:
            self._values["overwrite"] = overwrite

    @builtins.property
    def ingress_alb(self) -> typing.Optional[builtins.bool]:
        '''Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller.

        :default: false
        '''
        result = self._values.get("ingress_alb")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ingress_alb_scheme(self) -> typing.Optional["AlbScheme"]:
        '''Specify the ALB scheme that should be applied to ``Ingress`` resources.

        Only applicable if ``ingressAlb`` is set to ``true``.

        :default: AlbScheme.INTERNAL
        '''
        result = self._values.get("ingress_alb_scheme")
        return typing.cast(typing.Optional["AlbScheme"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted.

        To address this, ``kubectl apply`` has a ``--prune`` option which will
        query the cluster for all resources with a specific label and will remove
        all the labeld resources that are not part of the applied manifest. If this
        option is disabled and a resource is removed, it will become "orphaned" and
        will not be deleted from the cluster.

        When this option is enabled (default), the construct will inject a label to
        all Kubernetes resources included in this manifest which will be used to
        prune resources when the manifest changes via ``kubectl apply --prune``.

        The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the
        42-char unique address of this construct in the construct tree. Value is
        empty.

        :default:

        - based on the prune option of the cluster, which is ``true`` unless
        otherwise specified.

        :see: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune-l-your-label
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Kubernetes manifest.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def skip_validation(self) -> typing.Optional[builtins.bool]:
        '''A flag to signify if the manifest validation should be skipped.

        :default: false
        '''
        result = self._values.get("skip_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The EKS cluster to apply this manifest to.

        [disable-awslint:ref-via-interface]
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    @builtins.property
    def manifest(self) -> typing.List[typing.Mapping[builtins.str, typing.Any]]:
        '''The manifest to apply.

        Consists of any number of child resources.

        When the resources are created/updated, this manifest will be applied to the
        cluster through ``kubectl apply`` and when the resources or the stack is
        deleted, the resources in the manifest will be deleted through ``kubectl delete``.

        Example::

            [{
                "api_version": "v1",
                "kind": "Pod",
                "metadata": {"name": "mypod"},
                "spec": {
                    "containers": [{"name": "hello", "image": "paulbouwer/hello-kubernetes:1.5", "ports": [{"container_port": 8080}]}]
                }
            }]
        '''
        result = self._values.get("manifest")
        assert result is not None, "Required property 'manifest' is missing"
        return typing.cast(typing.List[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def overwrite(self) -> typing.Optional[builtins.bool]:
        '''Overwrite any existing resources.

        If this is set, we will use ``kubectl apply`` instead of ``kubectl create``
        when the resource is created. Otherwise, if there is already a resource
        in the cluster with the same name, the operation will fail.

        :default: false
        '''
        result = self._values.get("overwrite")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesObjectValue(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesObjectValue",
):
    '''Represents a value of a specific object deployed in the cluster.

    Use this to fetch any information available by the ``kubectl get`` command.

    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        
        # query the load balancer address
        my_service_address = eks.KubernetesObjectValue(self, "LoadBalancerAttribute",
            cluster=cluster,
            object_type="service",
            object_name="my-service",
            json_path=".status.loadBalancer.ingress[0].hostname"
        )
        
        # pass the address to a lambda function
        proxy_function = lambda_.Function(self, "ProxyFunction",
            handler="index.handler",
            code=lambda_.Code.from_inline("my-code"),
            runtime=lambda_.Runtime.NODEJS_LATEST,
            environment={
                "my_service_address": my_service_address.value
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "ICluster",
        json_path: builtins.str,
        object_name: builtins.str,
        object_type: builtins.str,
        object_namespace: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The EKS cluster to fetch attributes from. [disable-awslint:ref-via-interface]
        :param json_path: JSONPath to the specific value.
        :param object_name: The name of the object to query.
        :param object_type: The object type to query. (e.g 'service', 'pod'...)
        :param object_namespace: The namespace the object belongs to. Default: 'default'
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes object value. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param timeout: Timeout for waiting on a value. Default: Duration.minutes(5)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45f73303333592eb76ce2a3a47eb5689f5004712eb9ba9a363083fb711cf2050)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KubernetesObjectValueProps(
            cluster=cluster,
            json_path=json_path,
            object_name=object_name,
            object_type=object_type,
            object_namespace=object_namespace,
            removal_policy=removal_policy,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_TYPE")
    def RESOURCE_TYPE(cls) -> builtins.str:
        '''The CloudFormation resource type.'''
        return typing.cast(builtins.str, jsii.sget(cls, "RESOURCE_TYPE"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The value as a string token.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesObjectValueProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "json_path": "jsonPath",
        "object_name": "objectName",
        "object_type": "objectType",
        "object_namespace": "objectNamespace",
        "removal_policy": "removalPolicy",
        "timeout": "timeout",
    },
)
class KubernetesObjectValueProps:
    def __init__(
        self,
        *,
        cluster: "ICluster",
        json_path: builtins.str,
        object_name: builtins.str,
        object_type: builtins.str,
        object_namespace: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
    ) -> None:
        '''Properties for KubernetesObjectValue.

        :param cluster: The EKS cluster to fetch attributes from. [disable-awslint:ref-via-interface]
        :param json_path: JSONPath to the specific value.
        :param object_name: The name of the object to query.
        :param object_type: The object type to query. (e.g 'service', 'pod'...)
        :param object_namespace: The namespace the object belongs to. Default: 'default'
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes object value. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param timeout: Timeout for waiting on a value. Default: Duration.minutes(5)

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            # query the load balancer address
            my_service_address = eks.KubernetesObjectValue(self, "LoadBalancerAttribute",
                cluster=cluster,
                object_type="service",
                object_name="my-service",
                json_path=".status.loadBalancer.ingress[0].hostname"
            )
            
            # pass the address to a lambda function
            proxy_function = lambda_.Function(self, "ProxyFunction",
                handler="index.handler",
                code=lambda_.Code.from_inline("my-code"),
                runtime=lambda_.Runtime.NODEJS_LATEST,
                environment={
                    "my_service_address": my_service_address.value
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f882ca78f612b80a326720db025bad0ee81c47fc3567e1271454c15f2ee3fa)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument json_path", value=json_path, expected_type=type_hints["json_path"])
            check_type(argname="argument object_name", value=object_name, expected_type=type_hints["object_name"])
            check_type(argname="argument object_type", value=object_type, expected_type=type_hints["object_type"])
            check_type(argname="argument object_namespace", value=object_namespace, expected_type=type_hints["object_namespace"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "json_path": json_path,
            "object_name": object_name,
            "object_type": object_type,
        }
        if object_namespace is not None:
            self._values["object_namespace"] = object_namespace
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The EKS cluster to fetch attributes from.

        [disable-awslint:ref-via-interface]
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    @builtins.property
    def json_path(self) -> builtins.str:
        '''JSONPath to the specific value.

        :see: https://kubernetes.io/docs/reference/kubectl/jsonpath/
        '''
        result = self._values.get("json_path")
        assert result is not None, "Required property 'json_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_name(self) -> builtins.str:
        '''The name of the object to query.'''
        result = self._values.get("object_name")
        assert result is not None, "Required property 'object_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type(self) -> builtins.str:
        '''The object type to query.

        (e.g 'service', 'pod'...)
        '''
        result = self._values.get("object_type")
        assert result is not None, "Required property 'object_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace the object belongs to.

        :default: 'default'
        '''
        result = self._values.get("object_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Kubernetes object value.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''Timeout for waiting on a value.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesObjectValueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesPatch(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesPatch",
):
    '''A CloudFormation resource which applies/restores a JSON patch into a Kubernetes resource.

    :see: https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/
    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        
        eks.KubernetesPatch(self, "hello-kub-deployment-label",
            cluster=cluster,
            resource_name="deployment/hello-kubernetes",
            apply_patch={"spec": {"replicas": 5}},
            restore_patch={"spec": {"replicas": 3}}
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        apply_patch: typing.Mapping[builtins.str, typing.Any],
        cluster: "ICluster",
        resource_name: builtins.str,
        restore_patch: typing.Mapping[builtins.str, typing.Any],
        patch_type: typing.Optional["PatchType"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        resource_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param apply_patch: The JSON object to pass to ``kubectl patch`` when the resource is created/updated.
        :param cluster: The cluster to apply the patch to. [disable-awslint:ref-via-interface]
        :param resource_name: The full name of the resource to patch (e.g. ``deployment/coredns``).
        :param restore_patch: The JSON object to pass to ``kubectl patch`` when the resource is removed.
        :param patch_type: The patch type to pass to ``kubectl patch``. The default type used by ``kubectl patch`` is "strategic". Default: PatchType.STRATEGIC
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes patch. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param resource_namespace: The kubernetes API namespace. Default: "default"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6806e924d7a4b33fb6deb2187dcdc1e376243c3bb4967bd6a7ff20b64bdb4db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KubernetesPatchProps(
            apply_patch=apply_patch,
            cluster=cluster,
            resource_name=resource_name,
            restore_patch=restore_patch,
            patch_type=patch_type,
            removal_policy=removal_policy,
            resource_namespace=resource_namespace,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesPatchProps",
    jsii_struct_bases=[],
    name_mapping={
        "apply_patch": "applyPatch",
        "cluster": "cluster",
        "resource_name": "resourceName",
        "restore_patch": "restorePatch",
        "patch_type": "patchType",
        "removal_policy": "removalPolicy",
        "resource_namespace": "resourceNamespace",
    },
)
class KubernetesPatchProps:
    def __init__(
        self,
        *,
        apply_patch: typing.Mapping[builtins.str, typing.Any],
        cluster: "ICluster",
        resource_name: builtins.str,
        restore_patch: typing.Mapping[builtins.str, typing.Any],
        patch_type: typing.Optional["PatchType"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        resource_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for KubernetesPatch.

        :param apply_patch: The JSON object to pass to ``kubectl patch`` when the resource is created/updated.
        :param cluster: The cluster to apply the patch to. [disable-awslint:ref-via-interface]
        :param resource_name: The full name of the resource to patch (e.g. ``deployment/coredns``).
        :param restore_patch: The JSON object to pass to ``kubectl patch`` when the resource is removed.
        :param patch_type: The patch type to pass to ``kubectl patch``. The default type used by ``kubectl patch`` is "strategic". Default: PatchType.STRATEGIC
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes patch. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param resource_namespace: The kubernetes API namespace. Default: "default"

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            eks.KubernetesPatch(self, "hello-kub-deployment-label",
                cluster=cluster,
                resource_name="deployment/hello-kubernetes",
                apply_patch={"spec": {"replicas": 5}},
                restore_patch={"spec": {"replicas": 3}}
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1fa21e33c8b472af1142c651e669720614ef910d6bc6a0336c7e991204fa178)
            check_type(argname="argument apply_patch", value=apply_patch, expected_type=type_hints["apply_patch"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
            check_type(argname="argument restore_patch", value=restore_patch, expected_type=type_hints["restore_patch"])
            check_type(argname="argument patch_type", value=patch_type, expected_type=type_hints["patch_type"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument resource_namespace", value=resource_namespace, expected_type=type_hints["resource_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apply_patch": apply_patch,
            "cluster": cluster,
            "resource_name": resource_name,
            "restore_patch": restore_patch,
        }
        if patch_type is not None:
            self._values["patch_type"] = patch_type
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if resource_namespace is not None:
            self._values["resource_namespace"] = resource_namespace

    @builtins.property
    def apply_patch(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''The JSON object to pass to ``kubectl patch`` when the resource is created/updated.'''
        result = self._values.get("apply_patch")
        assert result is not None, "Required property 'apply_patch' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The cluster to apply the patch to.

        [disable-awslint:ref-via-interface]
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    @builtins.property
    def resource_name(self) -> builtins.str:
        '''The full name of the resource to patch (e.g. ``deployment/coredns``).'''
        result = self._values.get("resource_name")
        assert result is not None, "Required property 'resource_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restore_patch(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''The JSON object to pass to ``kubectl patch`` when the resource is removed.'''
        result = self._values.get("restore_patch")
        assert result is not None, "Required property 'restore_patch' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    @builtins.property
    def patch_type(self) -> typing.Optional["PatchType"]:
        '''The patch type to pass to ``kubectl patch``.

        The default type used by ``kubectl patch`` is "strategic".

        :default: PatchType.STRATEGIC
        '''
        result = self._values.get("patch_type")
        return typing.cast(typing.Optional["PatchType"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the custom resource that manages the Kubernetes patch.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def resource_namespace(self) -> typing.Optional[builtins.str]:
        '''The kubernetes API namespace.

        :default: "default"
        '''
        result = self._values.get("resource_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesPatchProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.KubernetesVersion",
):
    '''Kubernetes cluster version.

    :see: https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#kubernetes-release-calendar
    :exampleMetadata: infused

    Example::

        cluster = eks.Cluster(self, "ManagedNodeCluster",
            version=eks.KubernetesVersion.V1_34,
            default_capacity_type=eks.DefaultCapacityType.NODEGROUP
        )
        
        # Add a Fargate Profile for specific workloads (e.g., default namespace)
        cluster.add_fargate_profile("FargateProfile",
            selectors=[eks.Selector(namespace="default")
            ]
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, version: builtins.str) -> "KubernetesVersion":
        '''Custom cluster version.

        :param version: custom version number.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211c05e2b989920cd028cf1837789e382429a04d153f1b5b0732ecaf3371f95f)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("KubernetesVersion", jsii.sinvoke(cls, "of", [version]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_25")
    def V1_25(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.25.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV25Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v25``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_25"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_26")
    def V1_26(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.26.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV26Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v26``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_26"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_27")
    def V1_27(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.27.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV27Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v27``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_27"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_28")
    def V1_28(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.28.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV28Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v28``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_28"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_29")
    def V1_29(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.29.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV29Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v29``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_29"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_30")
    def V1_30(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.30.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV30Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v30``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_30"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_31")
    def V1_31(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.31.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV31Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v31``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_31"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_32")
    def V1_32(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.32.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV32Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v32``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_32"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_33")
    def V1_33(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.33.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV33Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v33``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_33"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_34")
    def V1_34(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.34.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV34Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v34``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_34"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_35")
    def V1_35(cls) -> "KubernetesVersion":
        '''Kubernetes version 1.35.

        When creating a ``Cluster`` with this version, you need to also specify the
        ``kubectlLayer`` property with a ``KubectlV35Layer`` from
        ``@aws-cdk/lambda-layer-kubectl-v35``.
        '''
        return typing.cast("KubernetesVersion", jsii.sget(cls, "V1_35"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''cluster version number.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.LaunchTemplateSpec",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "version": "version"},
)
class LaunchTemplateSpec:
    def __init__(
        self,
        *,
        id: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Launch template property specification.

        :param id: The Launch template ID.
        :param version: The launch template version to be used (optional). Default: - the default version of the launch template

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            launch_template_spec = eks_v2.LaunchTemplateSpec(
                id="id",
            
                # the properties below are optional
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__919b48dd57d86167f698cb29b3fa37433baaee3793d480304f510cdb323fce9e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> builtins.str:
        '''The Launch template ID.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The launch template version to be used (optional).

        :default: - the default version of the launch template
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.MachineImageType")
class MachineImageType(enum.Enum):
    '''The machine image type.'''

    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    '''Amazon EKS-optimized Linux AMI.'''
    BOTTLEROCKET = "BOTTLEROCKET"
    '''Bottlerocket AMI.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.NodeType")
class NodeType(enum.Enum):
    '''Whether the worker nodes should support GPU or just standard instances.'''

    STANDARD = "STANDARD"
    '''Standard instances.'''
    GPU = "GPU"
    '''GPU instances.'''
    INFERENTIA = "INFERENTIA"
    '''Inferentia instances.'''
    TRAINIUM = "TRAINIUM"
    '''Trainium instances.'''


@jsii.implements(INodegroup)
class Nodegroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.Nodegroup",
):
    '''The Nodegroup resource class.

    :resource: AWS::EKS::Nodegroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_ec2 as ec2
        from aws_cdk import aws_eks_v2 as eks_v2
        from aws_cdk import aws_iam as iam
        
        # cluster: eks_v2.Cluster
        # instance_type: ec2.InstanceType
        # role: iam.Role
        # security_group: ec2.SecurityGroup
        # subnet: ec2.Subnet
        # subnet_filter: ec2.SubnetFilter
        
        nodegroup = eks_v2.Nodegroup(self, "MyNodegroup",
            cluster=cluster,
        
            # the properties below are optional
            ami_type=eks_v2.NodegroupAmiType.AL2_X86_64,
            capacity_type=eks_v2.CapacityType.SPOT,
            desired_size=123,
            disk_size=123,
            enable_node_auto_repair=False,
            force_update=False,
            instance_types=[instance_type],
            labels={
                "labels_key": "labels"
            },
            launch_template_spec=eks_v2.LaunchTemplateSpec(
                id="id",
        
                # the properties below are optional
                version="version"
            ),
            max_size=123,
            max_unavailable=123,
            max_unavailable_percentage=123,
            min_size=123,
            nodegroup_name="nodegroupName",
            node_role=role,
            release_version="releaseVersion",
            remote_access=eks_v2.NodegroupRemoteAccess(
                ssh_key_name="sshKeyName",
        
                # the properties below are optional
                source_security_groups=[security_group]
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
            subnets=ec2.SubnetSelection(
                availability_zones=["availabilityZones"],
                one_per_az=False,
                subnet_filters=[subnet_filter],
                subnet_group_name="subnetGroupName",
                subnets=[subnet],
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            tags={
                "tags_key": "tags"
            },
            taints=[eks_v2.TaintSpec(
                effect=eks_v2.TaintEffect.NO_SCHEDULE,
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "ICluster",
        ami_type: typing.Optional["NodegroupAmiType"] = None,
        capacity_type: typing.Optional["CapacityType"] = None,
        desired_size: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        enable_node_auto_repair: typing.Optional[builtins.bool] = None,
        force_update: typing.Optional[builtins.bool] = None,
        instance_types: typing.Optional[typing.Sequence["_InstanceType_f64915b9"]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        launch_template_spec: typing.Optional[typing.Union["LaunchTemplateSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
        max_unavailable_percentage: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        nodegroup_name: typing.Optional[builtins.str] = None,
        node_role: typing.Optional["_IRole_235f5d8e"] = None,
        release_version: typing.Optional[builtins.str] = None,
        remote_access: typing.Optional[typing.Union["NodegroupRemoteAccess", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnets: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        taints: typing.Optional[typing.Sequence[typing.Union["TaintSpec", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: Cluster resource.
        :param ami_type: The AMI type for your node group. If you explicitly specify the launchTemplate with custom AMI, do not specify this property, or the node group deployment will fail. In other cases, you will need to specify correct amiType for the nodegroup. Default: - auto-determined from the instanceTypes property when launchTemplateSpec property is not specified
        :param capacity_type: The capacity type of the nodegroup. Default: CapacityType.ON_DEMAND
        :param desired_size: The current number of worker nodes that the managed node group should maintain. If not specified, the nodewgroup will initially create ``minSize`` instances. Default: 2
        :param disk_size: The root device disk size (in GiB) for your node group instances. Default: 20
        :param enable_node_auto_repair: Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default. Default: false
        :param force_update: Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue. If an update fails because pods could not be drained, you can force the update after it fails to terminate the old node whether or not any pods are running on the node. Default: true
        :param instance_types: The instance types to use for your node group. Default: t3.medium will be used according to the cloudformation document.
        :param labels: The Kubernetes labels to be applied to the nodes in the node group when they are created. Default: - None
        :param launch_template_spec: Launch template specification used for the nodegroup. Default: - no launch template
        :param max_size: The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default. Default: - same as desiredSize property
        :param max_unavailable: The maximum number of nodes unavailable at once during a version update. Nodes will be updated in parallel. The maximum number is 100. This value or ``maxUnavailablePercentage`` is required to have a value for custom update configurations to be applied. Default: 1
        :param max_unavailable_percentage: The maximum percentage of nodes unavailable during a version update. This percentage of nodes will be updated in parallel, up to 100 nodes at once. This value or ``maxUnavailable`` is required to have a value for custom update configurations to be applied. Default: undefined - node groups will update instances one at a time
        :param min_size: The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than or equal to zero. Default: 1
        :param nodegroup_name: Name of the Nodegroup. Default: - resource ID
        :param node_role: The IAM role to associate with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. Default: - None. Auto-generated if not specified.
        :param release_version: The AMI version of the Amazon EKS-optimized AMI to use with your node group (for example, ``1.14.7-YYYYMMDD``). Default: - The latest available AMI version for the node group's current Kubernetes version is used.
        :param remote_access: The remote access (SSH) configuration to use with your node group. Disabled by default, however, if you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0) Default: - disabled
        :param removal_policy: The removal policy applied to the managed node group resources. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnets: The subnets to use for the Auto Scaling group that is created for your node group. By specifying the SubnetSelection, the selected subnets will automatically apply required tags i.e. ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared``, where ``CLUSTER_NAME`` is replaced with the name of your cluster. Default: - private subnets
        :param tags: The metadata to apply to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets. Default: None
        :param taints: The Kubernetes taints to be applied to the nodes in the node group when they are created. Default: - None
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62af457a65949e7033d40a53d059be3f6f3a3197f4447681ec062c631bc964ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NodegroupProps(
            cluster=cluster,
            ami_type=ami_type,
            capacity_type=capacity_type,
            desired_size=desired_size,
            disk_size=disk_size,
            enable_node_auto_repair=enable_node_auto_repair,
            force_update=force_update,
            instance_types=instance_types,
            labels=labels,
            launch_template_spec=launch_template_spec,
            max_size=max_size,
            max_unavailable=max_unavailable,
            max_unavailable_percentage=max_unavailable_percentage,
            min_size=min_size,
            nodegroup_name=nodegroup_name,
            node_role=node_role,
            release_version=release_version,
            remote_access=remote_access,
            removal_policy=removal_policy,
            subnets=subnets,
            tags=tags,
            taints=taints,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromNodegroupName")
    @builtins.classmethod
    def from_nodegroup_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        nodegroup_name: builtins.str,
    ) -> "INodegroup":
        '''Import the Nodegroup from attributes.

        :param scope: -
        :param id: -
        :param nodegroup_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca1cb07c5679916253432bb99ab031e94ff8995b6ab160a4d865c1df5203357c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument nodegroup_name", value=nodegroup_name, expected_type=type_hints["nodegroup_name"])
        return typing.cast("INodegroup", jsii.sinvoke(cls, "fromNodegroupName", [scope, id, nodegroup_name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> "ICluster":
        '''the Amazon EKS cluster resource.

        :attribute: ClusterName
        '''
        return typing.cast("ICluster", jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="nodegroupArn")
    def nodegroup_arn(self) -> builtins.str:
        '''ARN of the nodegroup.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "nodegroupArn"))

    @builtins.property
    @jsii.member(jsii_name="nodegroupName")
    def nodegroup_name(self) -> builtins.str:
        '''Nodegroup name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "nodegroupName"))

    @builtins.property
    @jsii.member(jsii_name="nodegroupRef")
    def nodegroup_ref(self) -> "_NodegroupReference_eab944f6":
        '''A reference to a Nodegroup resource.'''
        return typing.cast("_NodegroupReference_eab944f6", jsii.get(self, "nodegroupRef"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> "_IRole_235f5d8e":
        '''IAM role of the instance profile for the nodegroup.'''
        return typing.cast("_IRole_235f5d8e", jsii.get(self, "role"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.NodegroupAmiType")
class NodegroupAmiType(enum.Enum):
    '''The AMI type for your node group.

    GPU instance types should use the ``AL2_x86_64_GPU`` AMI type, which uses the
    Amazon EKS-optimized Linux AMI with GPU support or the ``BOTTLEROCKET_ARM_64_NVIDIA`` or ``BOTTLEROCKET_X86_64_NVIDIA``
    AMI types, which uses the Amazon EKS-optimized Linux AMI with Nvidia-GPU support.

    Non-GPU instances should use the ``AL2_x86_64`` AMI type, which uses the Amazon EKS-optimized Linux AMI.
    '''

    AL2_X86_64 = "AL2_X86_64"
    '''Amazon Linux 2 (x86-64).'''
    AL2_X86_64_GPU = "AL2_X86_64_GPU"
    '''Amazon Linux 2 with GPU support.'''
    AL2_ARM_64 = "AL2_ARM_64"
    '''Amazon Linux 2 (ARM-64).'''
    BOTTLEROCKET_ARM_64 = "BOTTLEROCKET_ARM_64"
    '''Bottlerocket Linux (ARM-64).'''
    BOTTLEROCKET_X86_64 = "BOTTLEROCKET_X86_64"
    '''Bottlerocket (x86-64).'''
    BOTTLEROCKET_ARM_64_NVIDIA = "BOTTLEROCKET_ARM_64_NVIDIA"
    '''Bottlerocket Linux with Nvidia-GPU support (ARM-64).'''
    BOTTLEROCKET_X86_64_NVIDIA = "BOTTLEROCKET_X86_64_NVIDIA"
    '''Bottlerocket with Nvidia-GPU support (x86-64).'''
    BOTTLEROCKET_ARM_64_FIPS = "BOTTLEROCKET_ARM_64_FIPS"
    '''Bottlerocket Linux (ARM-64) with FIPS enabled.'''
    BOTTLEROCKET_X86_64_FIPS = "BOTTLEROCKET_X86_64_FIPS"
    '''Bottlerocket (x86-64) with FIPS enabled.'''
    WINDOWS_CORE_2019_X86_64 = "WINDOWS_CORE_2019_X86_64"
    '''Windows Core 2019 (x86-64).'''
    WINDOWS_CORE_2022_X86_64 = "WINDOWS_CORE_2022_X86_64"
    '''Windows Core 2022 (x86-64).'''
    WINDOWS_FULL_2019_X86_64 = "WINDOWS_FULL_2019_X86_64"
    '''Windows Full 2019 (x86-64).'''
    WINDOWS_FULL_2022_X86_64 = "WINDOWS_FULL_2022_X86_64"
    '''Windows Full 2022 (x86-64).'''
    AL2023_X86_64_STANDARD = "AL2023_X86_64_STANDARD"
    '''Amazon Linux 2023 (x86-64).'''
    AL2023_X86_64_NEURON = "AL2023_X86_64_NEURON"
    '''Amazon Linux 2023 with AWS Neuron drivers (x86-64).'''
    AL2023_X86_64_NVIDIA = "AL2023_X86_64_NVIDIA"
    '''Amazon Linux 2023 with NVIDIA drivers (x86-64).'''
    AL2023_ARM_64_NVIDIA = "AL2023_ARM_64_NVIDIA"
    '''Amazon Linux 2023 with NVIDIA drivers (ARM-64).'''
    AL2023_ARM_64_STANDARD = "AL2023_ARM_64_STANDARD"
    '''Amazon Linux 2023 (ARM-64).'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.NodegroupOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ami_type": "amiType",
        "capacity_type": "capacityType",
        "desired_size": "desiredSize",
        "disk_size": "diskSize",
        "enable_node_auto_repair": "enableNodeAutoRepair",
        "force_update": "forceUpdate",
        "instance_types": "instanceTypes",
        "labels": "labels",
        "launch_template_spec": "launchTemplateSpec",
        "max_size": "maxSize",
        "max_unavailable": "maxUnavailable",
        "max_unavailable_percentage": "maxUnavailablePercentage",
        "min_size": "minSize",
        "nodegroup_name": "nodegroupName",
        "node_role": "nodeRole",
        "release_version": "releaseVersion",
        "remote_access": "remoteAccess",
        "removal_policy": "removalPolicy",
        "subnets": "subnets",
        "tags": "tags",
        "taints": "taints",
    },
)
class NodegroupOptions:
    def __init__(
        self,
        *,
        ami_type: typing.Optional["NodegroupAmiType"] = None,
        capacity_type: typing.Optional["CapacityType"] = None,
        desired_size: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        enable_node_auto_repair: typing.Optional[builtins.bool] = None,
        force_update: typing.Optional[builtins.bool] = None,
        instance_types: typing.Optional[typing.Sequence["_InstanceType_f64915b9"]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        launch_template_spec: typing.Optional[typing.Union["LaunchTemplateSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
        max_unavailable_percentage: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        nodegroup_name: typing.Optional[builtins.str] = None,
        node_role: typing.Optional["_IRole_235f5d8e"] = None,
        release_version: typing.Optional[builtins.str] = None,
        remote_access: typing.Optional[typing.Union["NodegroupRemoteAccess", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnets: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        taints: typing.Optional[typing.Sequence[typing.Union["TaintSpec", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''The Nodegroup Options for addNodeGroup() method.

        :param ami_type: The AMI type for your node group. If you explicitly specify the launchTemplate with custom AMI, do not specify this property, or the node group deployment will fail. In other cases, you will need to specify correct amiType for the nodegroup. Default: - auto-determined from the instanceTypes property when launchTemplateSpec property is not specified
        :param capacity_type: The capacity type of the nodegroup. Default: CapacityType.ON_DEMAND
        :param desired_size: The current number of worker nodes that the managed node group should maintain. If not specified, the nodewgroup will initially create ``minSize`` instances. Default: 2
        :param disk_size: The root device disk size (in GiB) for your node group instances. Default: 20
        :param enable_node_auto_repair: Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default. Default: false
        :param force_update: Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue. If an update fails because pods could not be drained, you can force the update after it fails to terminate the old node whether or not any pods are running on the node. Default: true
        :param instance_types: The instance types to use for your node group. Default: t3.medium will be used according to the cloudformation document.
        :param labels: The Kubernetes labels to be applied to the nodes in the node group when they are created. Default: - None
        :param launch_template_spec: Launch template specification used for the nodegroup. Default: - no launch template
        :param max_size: The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default. Default: - same as desiredSize property
        :param max_unavailable: The maximum number of nodes unavailable at once during a version update. Nodes will be updated in parallel. The maximum number is 100. This value or ``maxUnavailablePercentage`` is required to have a value for custom update configurations to be applied. Default: 1
        :param max_unavailable_percentage: The maximum percentage of nodes unavailable during a version update. This percentage of nodes will be updated in parallel, up to 100 nodes at once. This value or ``maxUnavailable`` is required to have a value for custom update configurations to be applied. Default: undefined - node groups will update instances one at a time
        :param min_size: The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than or equal to zero. Default: 1
        :param nodegroup_name: Name of the Nodegroup. Default: - resource ID
        :param node_role: The IAM role to associate with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. Default: - None. Auto-generated if not specified.
        :param release_version: The AMI version of the Amazon EKS-optimized AMI to use with your node group (for example, ``1.14.7-YYYYMMDD``). Default: - The latest available AMI version for the node group's current Kubernetes version is used.
        :param remote_access: The remote access (SSH) configuration to use with your node group. Disabled by default, however, if you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0) Default: - disabled
        :param removal_policy: The removal policy applied to the managed node group resources. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnets: The subnets to use for the Auto Scaling group that is created for your node group. By specifying the SubnetSelection, the selected subnets will automatically apply required tags i.e. ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared``, where ``CLUSTER_NAME`` is replaced with the name of your cluster. Default: - private subnets
        :param tags: The metadata to apply to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets. Default: None
        :param taints: The Kubernetes taints to be applied to the nodes in the node group when they are created. Default: - None

        :exampleMetadata: infused

        Example::

            cluster = eks.Cluster(self, "HelloEKS",
                version=eks.KubernetesVersion.V1_34,
                default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
                default_capacity=0
            )
            
            cluster.add_nodegroup_capacity("custom-node-group",
                instance_types=[ec2.InstanceType("m5.large")],
                min_size=4,
                disk_size=100
            )
        '''
        if isinstance(launch_template_spec, dict):
            launch_template_spec = LaunchTemplateSpec(**launch_template_spec)
        if isinstance(remote_access, dict):
            remote_access = NodegroupRemoteAccess(**remote_access)
        if isinstance(subnets, dict):
            subnets = _SubnetSelection_e57d76df(**subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4520b68206945b2bfc48c1a6979416f811423e6b7e7b4d017c5b38dfb0d8373e)
            check_type(argname="argument ami_type", value=ami_type, expected_type=type_hints["ami_type"])
            check_type(argname="argument capacity_type", value=capacity_type, expected_type=type_hints["capacity_type"])
            check_type(argname="argument desired_size", value=desired_size, expected_type=type_hints["desired_size"])
            check_type(argname="argument disk_size", value=disk_size, expected_type=type_hints["disk_size"])
            check_type(argname="argument enable_node_auto_repair", value=enable_node_auto_repair, expected_type=type_hints["enable_node_auto_repair"])
            check_type(argname="argument force_update", value=force_update, expected_type=type_hints["force_update"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument launch_template_spec", value=launch_template_spec, expected_type=type_hints["launch_template_spec"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
            check_type(argname="argument max_unavailable_percentage", value=max_unavailable_percentage, expected_type=type_hints["max_unavailable_percentage"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument nodegroup_name", value=nodegroup_name, expected_type=type_hints["nodegroup_name"])
            check_type(argname="argument node_role", value=node_role, expected_type=type_hints["node_role"])
            check_type(argname="argument release_version", value=release_version, expected_type=type_hints["release_version"])
            check_type(argname="argument remote_access", value=remote_access, expected_type=type_hints["remote_access"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taints", value=taints, expected_type=type_hints["taints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ami_type is not None:
            self._values["ami_type"] = ami_type
        if capacity_type is not None:
            self._values["capacity_type"] = capacity_type
        if desired_size is not None:
            self._values["desired_size"] = desired_size
        if disk_size is not None:
            self._values["disk_size"] = disk_size
        if enable_node_auto_repair is not None:
            self._values["enable_node_auto_repair"] = enable_node_auto_repair
        if force_update is not None:
            self._values["force_update"] = force_update
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if labels is not None:
            self._values["labels"] = labels
        if launch_template_spec is not None:
            self._values["launch_template_spec"] = launch_template_spec
        if max_size is not None:
            self._values["max_size"] = max_size
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable
        if max_unavailable_percentage is not None:
            self._values["max_unavailable_percentage"] = max_unavailable_percentage
        if min_size is not None:
            self._values["min_size"] = min_size
        if nodegroup_name is not None:
            self._values["nodegroup_name"] = nodegroup_name
        if node_role is not None:
            self._values["node_role"] = node_role
        if release_version is not None:
            self._values["release_version"] = release_version
        if remote_access is not None:
            self._values["remote_access"] = remote_access
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if subnets is not None:
            self._values["subnets"] = subnets
        if tags is not None:
            self._values["tags"] = tags
        if taints is not None:
            self._values["taints"] = taints

    @builtins.property
    def ami_type(self) -> typing.Optional["NodegroupAmiType"]:
        '''The AMI type for your node group.

        If you explicitly specify the launchTemplate with custom AMI, do not specify this property, or
        the node group deployment will fail. In other cases, you will need to specify correct amiType for the nodegroup.

        :default: - auto-determined from the instanceTypes property when launchTemplateSpec property is not specified
        '''
        result = self._values.get("ami_type")
        return typing.cast(typing.Optional["NodegroupAmiType"], result)

    @builtins.property
    def capacity_type(self) -> typing.Optional["CapacityType"]:
        '''The capacity type of the nodegroup.

        :default: CapacityType.ON_DEMAND
        '''
        result = self._values.get("capacity_type")
        return typing.cast(typing.Optional["CapacityType"], result)

    @builtins.property
    def desired_size(self) -> typing.Optional[jsii.Number]:
        '''The current number of worker nodes that the managed node group should maintain.

        If not specified,
        the nodewgroup will initially create ``minSize`` instances.

        :default: 2
        '''
        result = self._values.get("desired_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''The root device disk size (in GiB) for your node group instances.

        :default: 20
        '''
        result = self._values.get("disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_node_auto_repair(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to enable node auto repair for the node group.

        Node auto repair is disabled by default.

        :default: false

        :see: https://docs.aws.amazon.com/eks/latest/userguide/node-health.html#node-auto-repair
        '''
        result = self._values.get("enable_node_auto_repair")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force_update(self) -> typing.Optional[builtins.bool]:
        '''Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue.

        If an update fails because pods could not be drained, you can force the update after it fails to terminate the old
        node whether or not any pods are
        running on the node.

        :default: true
        '''
        result = self._values.get("force_update")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List["_InstanceType_f64915b9"]]:
        '''The instance types to use for your node group.

        :default: t3.medium will be used according to the cloudformation document.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-instancetypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List["_InstanceType_f64915b9"]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The Kubernetes labels to be applied to the nodes in the node group when they are created.

        :default: - None
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def launch_template_spec(self) -> typing.Optional["LaunchTemplateSpec"]:
        '''Launch template specification used for the nodegroup.

        :default: - no launch template

        :see: https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html
        '''
        result = self._values.get("launch_template_spec")
        return typing.cast(typing.Optional["LaunchTemplateSpec"], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of worker nodes that the managed node group can scale out to.

        Managed node groups can support up to 100 nodes by default.

        :default: - same as desiredSize property
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of nodes unavailable at once during a version update.

        Nodes will be updated in parallel. The maximum number is 100.

        This value or ``maxUnavailablePercentage`` is required to have a value for custom update configurations to be applied.

        :default: 1

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailable
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unavailable_percentage(self) -> typing.Optional[jsii.Number]:
        '''The maximum percentage of nodes unavailable during a version update.

        This percentage of nodes will be updated in parallel, up to 100 nodes at once.

        This value or ``maxUnavailable`` is required to have a value for custom update configurations to be applied.

        :default: undefined - node groups will update instances one at a time

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailablepercentage
        '''
        result = self._values.get("max_unavailable_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of worker nodes that the managed node group can scale in to.

        This number must be greater than or equal to zero.

        :default: 1
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nodegroup_name(self) -> typing.Optional[builtins.str]:
        '''Name of the Nodegroup.

        :default: - resource ID
        '''
        result = self._values.get("nodegroup_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The IAM role to associate with your node group.

        The Amazon EKS worker node kubelet daemon
        makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through
        an IAM instance profile and associated policies. Before you can launch worker nodes and register them
        into a cluster, you must create an IAM role for those worker nodes to use when they are launched.

        :default: - None. Auto-generated if not specified.
        '''
        result = self._values.get("node_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def release_version(self) -> typing.Optional[builtins.str]:
        '''The AMI version of the Amazon EKS-optimized AMI to use with your node group (for example, ``1.14.7-YYYYMMDD``).

        :default: - The latest available AMI version for the node group's current Kubernetes version is used.
        '''
        result = self._values.get("release_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_access(self) -> typing.Optional["NodegroupRemoteAccess"]:
        '''The remote access (SSH) configuration to use with your node group.

        Disabled by default, however, if you
        specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group,
        then port 22 on the worker nodes is opened to the internet (0.0.0.0/0)

        :default: - disabled
        '''
        result = self._values.get("remote_access")
        return typing.cast(typing.Optional["NodegroupRemoteAccess"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the managed node group resources.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def subnets(self) -> typing.Optional["_SubnetSelection_e57d76df"]:
        '''The subnets to use for the Auto Scaling group that is created for your node group.

        By specifying the
        SubnetSelection, the selected subnets will automatically apply required tags i.e.
        ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared``, where ``CLUSTER_NAME`` is replaced with
        the name of your cluster.

        :default: - private subnets
        '''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional["_SubnetSelection_e57d76df"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The metadata to apply to the node group to assist with categorization and organization.

        Each tag consists of
        a key and an optional value, both of which you define. Node group tags do not propagate to any other resources
        associated with the node group, such as the Amazon EC2 instances or subnets.

        :default: None
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def taints(self) -> typing.Optional[typing.List["TaintSpec"]]:
        '''The Kubernetes taints to be applied to the nodes in the node group when they are created.

        :default: - None
        '''
        result = self._values.get("taints")
        return typing.cast(typing.Optional[typing.List["TaintSpec"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodegroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.NodegroupProps",
    jsii_struct_bases=[NodegroupOptions],
    name_mapping={
        "ami_type": "amiType",
        "capacity_type": "capacityType",
        "desired_size": "desiredSize",
        "disk_size": "diskSize",
        "enable_node_auto_repair": "enableNodeAutoRepair",
        "force_update": "forceUpdate",
        "instance_types": "instanceTypes",
        "labels": "labels",
        "launch_template_spec": "launchTemplateSpec",
        "max_size": "maxSize",
        "max_unavailable": "maxUnavailable",
        "max_unavailable_percentage": "maxUnavailablePercentage",
        "min_size": "minSize",
        "nodegroup_name": "nodegroupName",
        "node_role": "nodeRole",
        "release_version": "releaseVersion",
        "remote_access": "remoteAccess",
        "removal_policy": "removalPolicy",
        "subnets": "subnets",
        "tags": "tags",
        "taints": "taints",
        "cluster": "cluster",
    },
)
class NodegroupProps(NodegroupOptions):
    def __init__(
        self,
        *,
        ami_type: typing.Optional["NodegroupAmiType"] = None,
        capacity_type: typing.Optional["CapacityType"] = None,
        desired_size: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        enable_node_auto_repair: typing.Optional[builtins.bool] = None,
        force_update: typing.Optional[builtins.bool] = None,
        instance_types: typing.Optional[typing.Sequence["_InstanceType_f64915b9"]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        launch_template_spec: typing.Optional[typing.Union["LaunchTemplateSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
        max_unavailable_percentage: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        nodegroup_name: typing.Optional[builtins.str] = None,
        node_role: typing.Optional["_IRole_235f5d8e"] = None,
        release_version: typing.Optional[builtins.str] = None,
        remote_access: typing.Optional[typing.Union["NodegroupRemoteAccess", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnets: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        taints: typing.Optional[typing.Sequence[typing.Union["TaintSpec", typing.Dict[builtins.str, typing.Any]]]] = None,
        cluster: "ICluster",
    ) -> None:
        '''NodeGroup properties interface.

        :param ami_type: The AMI type for your node group. If you explicitly specify the launchTemplate with custom AMI, do not specify this property, or the node group deployment will fail. In other cases, you will need to specify correct amiType for the nodegroup. Default: - auto-determined from the instanceTypes property when launchTemplateSpec property is not specified
        :param capacity_type: The capacity type of the nodegroup. Default: CapacityType.ON_DEMAND
        :param desired_size: The current number of worker nodes that the managed node group should maintain. If not specified, the nodewgroup will initially create ``minSize`` instances. Default: 2
        :param disk_size: The root device disk size (in GiB) for your node group instances. Default: 20
        :param enable_node_auto_repair: Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default. Default: false
        :param force_update: Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue. If an update fails because pods could not be drained, you can force the update after it fails to terminate the old node whether or not any pods are running on the node. Default: true
        :param instance_types: The instance types to use for your node group. Default: t3.medium will be used according to the cloudformation document.
        :param labels: The Kubernetes labels to be applied to the nodes in the node group when they are created. Default: - None
        :param launch_template_spec: Launch template specification used for the nodegroup. Default: - no launch template
        :param max_size: The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default. Default: - same as desiredSize property
        :param max_unavailable: The maximum number of nodes unavailable at once during a version update. Nodes will be updated in parallel. The maximum number is 100. This value or ``maxUnavailablePercentage`` is required to have a value for custom update configurations to be applied. Default: 1
        :param max_unavailable_percentage: The maximum percentage of nodes unavailable during a version update. This percentage of nodes will be updated in parallel, up to 100 nodes at once. This value or ``maxUnavailable`` is required to have a value for custom update configurations to be applied. Default: undefined - node groups will update instances one at a time
        :param min_size: The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than or equal to zero. Default: 1
        :param nodegroup_name: Name of the Nodegroup. Default: - resource ID
        :param node_role: The IAM role to associate with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. Default: - None. Auto-generated if not specified.
        :param release_version: The AMI version of the Amazon EKS-optimized AMI to use with your node group (for example, ``1.14.7-YYYYMMDD``). Default: - The latest available AMI version for the node group's current Kubernetes version is used.
        :param remote_access: The remote access (SSH) configuration to use with your node group. Disabled by default, however, if you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0) Default: - disabled
        :param removal_policy: The removal policy applied to the managed node group resources. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnets: The subnets to use for the Auto Scaling group that is created for your node group. By specifying the SubnetSelection, the selected subnets will automatically apply required tags i.e. ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared``, where ``CLUSTER_NAME`` is replaced with the name of your cluster. Default: - private subnets
        :param tags: The metadata to apply to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets. Default: None
        :param taints: The Kubernetes taints to be applied to the nodes in the node group when they are created. Default: - None
        :param cluster: Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_eks_v2 as eks_v2
            from aws_cdk import aws_iam as iam
            
            # cluster: eks_v2.Cluster
            # instance_type: ec2.InstanceType
            # role: iam.Role
            # security_group: ec2.SecurityGroup
            # subnet: ec2.Subnet
            # subnet_filter: ec2.SubnetFilter
            
            nodegroup_props = eks_v2.NodegroupProps(
                cluster=cluster,
            
                # the properties below are optional
                ami_type=eks_v2.NodegroupAmiType.AL2_X86_64,
                capacity_type=eks_v2.CapacityType.SPOT,
                desired_size=123,
                disk_size=123,
                enable_node_auto_repair=False,
                force_update=False,
                instance_types=[instance_type],
                labels={
                    "labels_key": "labels"
                },
                launch_template_spec=eks_v2.LaunchTemplateSpec(
                    id="id",
            
                    # the properties below are optional
                    version="version"
                ),
                max_size=123,
                max_unavailable=123,
                max_unavailable_percentage=123,
                min_size=123,
                nodegroup_name="nodegroupName",
                node_role=role,
                release_version="releaseVersion",
                remote_access=eks_v2.NodegroupRemoteAccess(
                    ssh_key_name="sshKeyName",
            
                    # the properties below are optional
                    source_security_groups=[security_group]
                ),
                removal_policy=cdk.RemovalPolicy.DESTROY,
                subnets=ec2.SubnetSelection(
                    availability_zones=["availabilityZones"],
                    one_per_az=False,
                    subnet_filters=[subnet_filter],
                    subnet_group_name="subnetGroupName",
                    subnets=[subnet],
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
                tags={
                    "tags_key": "tags"
                },
                taints=[eks_v2.TaintSpec(
                    effect=eks_v2.TaintEffect.NO_SCHEDULE,
                    key="key",
                    value="value"
                )]
            )
        '''
        if isinstance(launch_template_spec, dict):
            launch_template_spec = LaunchTemplateSpec(**launch_template_spec)
        if isinstance(remote_access, dict):
            remote_access = NodegroupRemoteAccess(**remote_access)
        if isinstance(subnets, dict):
            subnets = _SubnetSelection_e57d76df(**subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1960828ed0ec52107f2f9d815f5a9edf404b27e19b18ae5dd39b8d5f38f2f8e5)
            check_type(argname="argument ami_type", value=ami_type, expected_type=type_hints["ami_type"])
            check_type(argname="argument capacity_type", value=capacity_type, expected_type=type_hints["capacity_type"])
            check_type(argname="argument desired_size", value=desired_size, expected_type=type_hints["desired_size"])
            check_type(argname="argument disk_size", value=disk_size, expected_type=type_hints["disk_size"])
            check_type(argname="argument enable_node_auto_repair", value=enable_node_auto_repair, expected_type=type_hints["enable_node_auto_repair"])
            check_type(argname="argument force_update", value=force_update, expected_type=type_hints["force_update"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument launch_template_spec", value=launch_template_spec, expected_type=type_hints["launch_template_spec"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
            check_type(argname="argument max_unavailable_percentage", value=max_unavailable_percentage, expected_type=type_hints["max_unavailable_percentage"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument nodegroup_name", value=nodegroup_name, expected_type=type_hints["nodegroup_name"])
            check_type(argname="argument node_role", value=node_role, expected_type=type_hints["node_role"])
            check_type(argname="argument release_version", value=release_version, expected_type=type_hints["release_version"])
            check_type(argname="argument remote_access", value=remote_access, expected_type=type_hints["remote_access"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taints", value=taints, expected_type=type_hints["taints"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
        }
        if ami_type is not None:
            self._values["ami_type"] = ami_type
        if capacity_type is not None:
            self._values["capacity_type"] = capacity_type
        if desired_size is not None:
            self._values["desired_size"] = desired_size
        if disk_size is not None:
            self._values["disk_size"] = disk_size
        if enable_node_auto_repair is not None:
            self._values["enable_node_auto_repair"] = enable_node_auto_repair
        if force_update is not None:
            self._values["force_update"] = force_update
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if labels is not None:
            self._values["labels"] = labels
        if launch_template_spec is not None:
            self._values["launch_template_spec"] = launch_template_spec
        if max_size is not None:
            self._values["max_size"] = max_size
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable
        if max_unavailable_percentage is not None:
            self._values["max_unavailable_percentage"] = max_unavailable_percentage
        if min_size is not None:
            self._values["min_size"] = min_size
        if nodegroup_name is not None:
            self._values["nodegroup_name"] = nodegroup_name
        if node_role is not None:
            self._values["node_role"] = node_role
        if release_version is not None:
            self._values["release_version"] = release_version
        if remote_access is not None:
            self._values["remote_access"] = remote_access
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if subnets is not None:
            self._values["subnets"] = subnets
        if tags is not None:
            self._values["tags"] = tags
        if taints is not None:
            self._values["taints"] = taints

    @builtins.property
    def ami_type(self) -> typing.Optional["NodegroupAmiType"]:
        '''The AMI type for your node group.

        If you explicitly specify the launchTemplate with custom AMI, do not specify this property, or
        the node group deployment will fail. In other cases, you will need to specify correct amiType for the nodegroup.

        :default: - auto-determined from the instanceTypes property when launchTemplateSpec property is not specified
        '''
        result = self._values.get("ami_type")
        return typing.cast(typing.Optional["NodegroupAmiType"], result)

    @builtins.property
    def capacity_type(self) -> typing.Optional["CapacityType"]:
        '''The capacity type of the nodegroup.

        :default: CapacityType.ON_DEMAND
        '''
        result = self._values.get("capacity_type")
        return typing.cast(typing.Optional["CapacityType"], result)

    @builtins.property
    def desired_size(self) -> typing.Optional[jsii.Number]:
        '''The current number of worker nodes that the managed node group should maintain.

        If not specified,
        the nodewgroup will initially create ``minSize`` instances.

        :default: 2
        '''
        result = self._values.get("desired_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''The root device disk size (in GiB) for your node group instances.

        :default: 20
        '''
        result = self._values.get("disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_node_auto_repair(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to enable node auto repair for the node group.

        Node auto repair is disabled by default.

        :default: false

        :see: https://docs.aws.amazon.com/eks/latest/userguide/node-health.html#node-auto-repair
        '''
        result = self._values.get("enable_node_auto_repair")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force_update(self) -> typing.Optional[builtins.bool]:
        '''Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue.

        If an update fails because pods could not be drained, you can force the update after it fails to terminate the old
        node whether or not any pods are
        running on the node.

        :default: true
        '''
        result = self._values.get("force_update")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List["_InstanceType_f64915b9"]]:
        '''The instance types to use for your node group.

        :default: t3.medium will be used according to the cloudformation document.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-instancetypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List["_InstanceType_f64915b9"]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The Kubernetes labels to be applied to the nodes in the node group when they are created.

        :default: - None
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def launch_template_spec(self) -> typing.Optional["LaunchTemplateSpec"]:
        '''Launch template specification used for the nodegroup.

        :default: - no launch template

        :see: https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html
        '''
        result = self._values.get("launch_template_spec")
        return typing.cast(typing.Optional["LaunchTemplateSpec"], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of worker nodes that the managed node group can scale out to.

        Managed node groups can support up to 100 nodes by default.

        :default: - same as desiredSize property
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of nodes unavailable at once during a version update.

        Nodes will be updated in parallel. The maximum number is 100.

        This value or ``maxUnavailablePercentage`` is required to have a value for custom update configurations to be applied.

        :default: 1

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailable
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unavailable_percentage(self) -> typing.Optional[jsii.Number]:
        '''The maximum percentage of nodes unavailable during a version update.

        This percentage of nodes will be updated in parallel, up to 100 nodes at once.

        This value or ``maxUnavailable`` is required to have a value for custom update configurations to be applied.

        :default: undefined - node groups will update instances one at a time

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailablepercentage
        '''
        result = self._values.get("max_unavailable_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of worker nodes that the managed node group can scale in to.

        This number must be greater than or equal to zero.

        :default: 1
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nodegroup_name(self) -> typing.Optional[builtins.str]:
        '''Name of the Nodegroup.

        :default: - resource ID
        '''
        result = self._values.get("nodegroup_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_role(self) -> typing.Optional["_IRole_235f5d8e"]:
        '''The IAM role to associate with your node group.

        The Amazon EKS worker node kubelet daemon
        makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through
        an IAM instance profile and associated policies. Before you can launch worker nodes and register them
        into a cluster, you must create an IAM role for those worker nodes to use when they are launched.

        :default: - None. Auto-generated if not specified.
        '''
        result = self._values.get("node_role")
        return typing.cast(typing.Optional["_IRole_235f5d8e"], result)

    @builtins.property
    def release_version(self) -> typing.Optional[builtins.str]:
        '''The AMI version of the Amazon EKS-optimized AMI to use with your node group (for example, ``1.14.7-YYYYMMDD``).

        :default: - The latest available AMI version for the node group's current Kubernetes version is used.
        '''
        result = self._values.get("release_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_access(self) -> typing.Optional["NodegroupRemoteAccess"]:
        '''The remote access (SSH) configuration to use with your node group.

        Disabled by default, however, if you
        specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group,
        then port 22 on the worker nodes is opened to the internet (0.0.0.0/0)

        :default: - disabled
        '''
        result = self._values.get("remote_access")
        return typing.cast(typing.Optional["NodegroupRemoteAccess"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the managed node group resources.

        The removal policy controls what happens to the resource if it stops being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def subnets(self) -> typing.Optional["_SubnetSelection_e57d76df"]:
        '''The subnets to use for the Auto Scaling group that is created for your node group.

        By specifying the
        SubnetSelection, the selected subnets will automatically apply required tags i.e.
        ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared``, where ``CLUSTER_NAME`` is replaced with
        the name of your cluster.

        :default: - private subnets
        '''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional["_SubnetSelection_e57d76df"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The metadata to apply to the node group to assist with categorization and organization.

        Each tag consists of
        a key and an optional value, both of which you define. Node group tags do not propagate to any other resources
        associated with the node group, such as the Amazon EC2 instances or subnets.

        :default: None
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def taints(self) -> typing.Optional[typing.List["TaintSpec"]]:
        '''The Kubernetes taints to be applied to the nodes in the node group when they are created.

        :default: - None
        '''
        result = self._values.get("taints")
        return typing.cast(typing.Optional[typing.List["TaintSpec"]], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''Cluster resource.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodegroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.NodegroupRemoteAccess",
    jsii_struct_bases=[],
    name_mapping={
        "ssh_key_name": "sshKeyName",
        "source_security_groups": "sourceSecurityGroups",
    },
)
class NodegroupRemoteAccess:
    def __init__(
        self,
        *,
        ssh_key_name: builtins.str,
        source_security_groups: typing.Optional[typing.Sequence["_ISecurityGroup_acf8a799"]] = None,
    ) -> None:
        '''The remote access (SSH) configuration to use with your node group.

        :param ssh_key_name: The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the managed node group.
        :param source_security_groups: The security groups that are allowed SSH access (port 22) to the worker nodes. If you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0). Default: - port 22 on the worker nodes is opened to the internet (0.0.0.0/0)

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_eks_v2 as eks_v2
            
            # security_group: ec2.SecurityGroup
            
            nodegroup_remote_access = eks_v2.NodegroupRemoteAccess(
                ssh_key_name="sshKeyName",
            
                # the properties below are optional
                source_security_groups=[security_group]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f1a56f6e96e735d5421faf302c657e51d067f57405e3a52e02c2f52f620d47)
            check_type(argname="argument ssh_key_name", value=ssh_key_name, expected_type=type_hints["ssh_key_name"])
            check_type(argname="argument source_security_groups", value=source_security_groups, expected_type=type_hints["source_security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ssh_key_name": ssh_key_name,
        }
        if source_security_groups is not None:
            self._values["source_security_groups"] = source_security_groups

    @builtins.property
    def ssh_key_name(self) -> builtins.str:
        '''The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the managed node group.'''
        result = self._values.get("ssh_key_name")
        assert result is not None, "Required property 'ssh_key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_security_groups(
        self,
    ) -> typing.Optional[typing.List["_ISecurityGroup_acf8a799"]]:
        '''The security groups that are allowed SSH access (port 22) to the worker nodes.

        If you specify an Amazon EC2 SSH
        key but do not specify a source security group when you create a managed node group, then port 22 on the worker
        nodes is opened to the internet (0.0.0.0/0).

        :default: - port 22 on the worker nodes is opened to the internet (0.0.0.0/0)
        '''
        result = self._values.get("source_security_groups")
        return typing.cast(typing.Optional[typing.List["_ISecurityGroup_acf8a799"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodegroupRemoteAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OidcProviderNative(
    _OidcProviderNative_18002ae4,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.OidcProviderNative",
):
    '''IAM OIDC identity providers are entities in IAM that describe an external identity provider (IdP) service that supports the OpenID Connect (OIDC) standard, such as Google or Salesforce.

    You use an IAM OIDC identity provider
    when you want to establish trust between an OIDC-compatible IdP and your AWS
    account.

    This implementation uses the native CloudFormation resource and has default
    values for thumbprints and clientIds props that will be compatible with the eks cluster.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html
    :resource: AWS::IAM::OIDCProvider
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        
        # or create a new one using an existing issuer url
        # issuer_url: str
        
        from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer
        
        # you can import an existing provider
        provider = eks.OidcProviderNative.from_oidc_provider_arn(self, "Provider", "arn:aws:iam::123456:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/AB123456ABC")
        provider2 = eks.OidcProviderNative(self, "Provider",
            url=issuer_url
        )
        
        cluster = eks.Cluster.from_cluster_attributes(self, "MyCluster",
            cluster_name="Cluster",
            open_id_connect_provider=provider,
            kubectl_provider_options=eks.KubectlProviderOptions(
                kubectl_layer=KubectlV35Layer(self, "kubectl")
            )
        )
        
        service_account = cluster.add_service_account("MyServiceAccount")
        
        bucket = s3.Bucket(self, "Bucket")
        bucket.grant_read_write(service_account)
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        url: builtins.str,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Defines a native OpenID Connect provider.

        :param scope: The definition scope.
        :param id: Construct ID.
        :param url: The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You can find your OIDC Issuer URL by: aws eks describe-cluster --name %cluster_name% --query "cluster.identity.oidc.issuer" --output text
        :param removal_policy: The removal policy to apply to the OpenID Connect Provider. Default: - RemovalPolicy.DESTROY
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333791b35901664482ab20cd991b904afd4d2ad97fd70d1c8a62237d7f23a02a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = OidcProviderNativeProps(url=url, removal_policy=removal_policy)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


class OpenIdConnectProvider(
    _OpenIdConnectProvider_5cb7bc9f,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.OpenIdConnectProvider",
):
    '''(deprecated) IAM OIDC identity providers are entities in IAM that describe an external identity provider (IdP) service that supports the OpenID Connect (OIDC) standard, such as Google or Salesforce.

    You use an IAM OIDC identity provider
    when you want to establish trust between an OIDC-compatible IdP and your AWS
    account.

    This implementation has default values for thumbprints and clientIds props
    that will be compatible with the eks cluster

    :deprecated: Use ``OidcProviderNative`` instead. This construct will be removed in a future major release.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html
    :stability: deprecated
    :resource: AWS::CloudFormation::CustomResource
    :exampleMetadata: infused

    Example::

        import aws_cdk as cdk
        
        # Step 1: Add retain policy to existing provider
        existing_provider = eks.OpenIdConnectProvider(self, "Provider",
            url="https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLE",
            removal_policy=cdk.RemovalPolicy.RETAIN
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        url: builtins.str,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''(deprecated) Defines an OpenID Connect provider.

        :param scope: The definition scope.
        :param id: Construct ID.
        :param url: The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You can find your OIDC Issuer URL by: aws eks describe-cluster --name %cluster_name% --query "cluster.identity.oidc.issuer" --output text
        :param removal_policy: The removal policy to apply to the OpenID Connect Provider. Default: - RemovalPolicy.DESTROY

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d280f100f41eedf34f0f60af882d5409886185cb49189b059dc5cc7858c939d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = OpenIdConnectProviderProps(url=url, removal_policy=removal_policy)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''(deprecated) Uniquely identifies this class.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.OpenIdConnectProviderProps",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "removal_policy": "removalPolicy"},
)
class OpenIdConnectProviderProps:
    def __init__(
        self,
        *,
        url: builtins.str,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Initialization properties for ``OpenIdConnectProvider``.

        :param url: The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You can find your OIDC Issuer URL by: aws eks describe-cluster --name %cluster_name% --query "cluster.identity.oidc.issuer" --output text
        :param removal_policy: The removal policy to apply to the OpenID Connect Provider. Default: - RemovalPolicy.DESTROY

        :exampleMetadata: infused

        Example::

            import aws_cdk as cdk
            
            # Step 1: Add retain policy to existing provider
            existing_provider = eks.OpenIdConnectProvider(self, "Provider",
                url="https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLE",
                removal_policy=cdk.RemovalPolicy.RETAIN
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3317e0858986f20bc5c548ba58b06e82f8e811e2391f01fe2a8895a53fb685ba)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL of the identity provider.

        The URL must begin with https:// and
        should correspond to the iss claim in the provider's OpenID Connect ID
        tokens. Per the OIDC standard, path components are allowed but query
        parameters are not. Typically the URL consists of only a hostname, like
        https://server.example.org or https://example.com.

        You can find your OIDC Issuer URL by:
        aws eks describe-cluster --name %cluster_name% --query "cluster.identity.oidc.issuer" --output text
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy to apply to the OpenID Connect Provider.

        :default: - RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.PatchType")
class PatchType(enum.Enum):
    '''Values for ``kubectl patch`` --type argument.'''

    JSON = "JSON"
    '''JSON Patch, RFC 6902.'''
    MERGE = "MERGE"
    '''JSON Merge patch.'''
    STRATEGIC = "STRATEGIC"
    '''Strategic merge patch.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.RemoteNodeNetwork",
    jsii_struct_bases=[],
    name_mapping={"cidrs": "cidrs"},
)
class RemoteNodeNetwork:
    def __init__(self, *, cidrs: typing.Sequence[builtins.str]) -> None:
        '''Remote network configuration for hybrid nodes.

        :param cidrs: IPv4 CIDR blocks for the remote node network.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            remote_node_network = eks_v2.RemoteNodeNetwork(
                cidrs=["cidrs"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c060c74a741aec691d27fd934a073aeffa7738efbbf9113e88ed3349b6a279)
            check_type(argname="argument cidrs", value=cidrs, expected_type=type_hints["cidrs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidrs": cidrs,
        }

    @builtins.property
    def cidrs(self) -> typing.List[builtins.str]:
        '''IPv4 CIDR blocks for the remote node network.'''
        result = self._values.get("cidrs")
        assert result is not None, "Required property 'cidrs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemoteNodeNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.RemotePodNetwork",
    jsii_struct_bases=[],
    name_mapping={"cidrs": "cidrs"},
)
class RemotePodNetwork:
    def __init__(self, *, cidrs: typing.Sequence[builtins.str]) -> None:
        '''Remote network configuration for pods on hybrid nodes.

        :param cidrs: IPv4 CIDR blocks for the remote pod network.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            remote_pod_network = eks_v2.RemotePodNetwork(
                cidrs=["cidrs"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c743e611c57394e9752c982811b7678e60ad528d7877cf8ac6ded60a7fae0a77)
            check_type(argname="argument cidrs", value=cidrs, expected_type=type_hints["cidrs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidrs": cidrs,
        }

    @builtins.property
    def cidrs(self) -> typing.List[builtins.str]:
        '''IPv4 CIDR blocks for the remote pod network.'''
        result = self._values.get("cidrs")
        assert result is not None, "Required property 'cidrs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemotePodNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.Selector",
    jsii_struct_bases=[],
    name_mapping={"namespace": "namespace", "labels": "labels"},
)
class Selector:
    def __init__(
        self,
        *,
        namespace: builtins.str,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Fargate profile selector.

        :param namespace: The Kubernetes namespace that the selector should match. You must specify a namespace for a selector. The selector only matches pods that are created in this namespace, but you can create multiple selectors to target multiple namespaces.
        :param labels: The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match. Default: - all pods within the namespace will be selected.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            selector = eks_v2.Selector(
                namespace="namespace",
            
                # the properties below are optional
                labels={
                    "labels_key": "labels"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c29fc574d38fe5b57bd3a9de52666c5ff0e4d6562893c6ff6e42979ba509600d)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace": namespace,
        }
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The Kubernetes namespace that the selector should match.

        You must specify a namespace for a selector. The selector only matches pods
        that are created in this namespace, but you can create multiple selectors
        to target multiple namespaces.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The Kubernetes labels that the selector should match.

        A pod must contain
        all of the labels that are specified in the selector for it to be
        considered a match.

        :default: - all pods within the namespace will be selected.
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Selector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IPrincipal_539bb2fd)
class ServiceAccount(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.ServiceAccount",
):
    '''Service Account.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        
        # or create a new one using an existing issuer url
        # issuer_url: str
        
        from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer
        
        # you can import an existing provider
        provider = eks.OidcProviderNative.from_oidc_provider_arn(self, "Provider", "arn:aws:iam::123456:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/AB123456ABC")
        provider2 = eks.OidcProviderNative(self, "Provider",
            url=issuer_url
        )
        
        cluster = eks.Cluster.from_cluster_attributes(self, "MyCluster",
            cluster_name="Cluster",
            open_id_connect_provider=provider,
            kubectl_provider_options=eks.KubectlProviderOptions(
                kubectl_layer=KubectlV35Layer(self, "kubectl")
            )
        )
        
        service_account = cluster.add_service_account("MyServiceAccount")
        
        bucket = s3.Bucket(self, "Bucket")
        bucket.grant_read_write(service_account)
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster: "ICluster",
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        identity_type: typing.Optional["IdentityType"] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The cluster to apply the patch to.
        :param annotations: Additional annotations of the service account. Default: - no additional annotations
        :param identity_type: The identity type to use for the service account. Default: IdentityType.IRSA
        :param labels: Additional labels of the service account. Default: - no additional labels
        :param name: The name of the service account. The name of a ServiceAccount object must be a valid DNS subdomain name. https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ Default: - If no name is given, it will use the id of the resource.
        :param namespace: The namespace of the service account. All namespace names must be valid RFC 1123 DNS labels. https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns Default: "default"
        :param overwrite_service_account: Overwrite existing service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the service account is created. Otherwise, if there is already a service account in the cluster with the same name, the operation will fail. Default: false
        :param removal_policy: The removal policy applied to the service account resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbaca7b824d909d3e2050c970ff90499375d66f7b3e45708d6e7a0fbb0c1c234)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServiceAccountProps(
            cluster=cluster,
            annotations=annotations,
            identity_type=identity_type,
            labels=labels,
            name=name,
            namespace=namespace,
            overwrite_service_account=overwrite_service_account,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: "_PolicyStatement_0fe33853") -> builtins.bool:
        '''(deprecated) Add to the policy of this principal.

        :param statement: -

        :deprecated: use ``addToPrincipalPolicy()``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc56e7f7009940bf1de62a180e0cb83ac26149eff91c8ceac6aa4b5c0ebfd12a)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: "_PolicyStatement_0fe33853",
    ) -> "_AddToPrincipalPolicyResult_946c9561":
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429486a7c95ed32e038b64ea6b7c83b33565be6e03880fde330aa75f4c68270f)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast("_AddToPrincipalPolicyResult_946c9561", jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> "_IPrincipal_539bb2fd":
        '''The principal to grant permissions to.'''
        return typing.cast("_IPrincipal_539bb2fd", jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> "_PrincipalPolicyFragment_6a855d11":
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast("_PrincipalPolicyFragment_6a855d11", jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> "_IRole_235f5d8e":
        '''The role which is linked to the service account.'''
        return typing.cast("_IRole_235f5d8e", jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountName")
    def service_account_name(self) -> builtins.str:
        '''The name of the service account.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountName"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountNamespace")
    def service_account_namespace(self) -> builtins.str:
        '''The namespace where the service account is located in.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountNamespace"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ServiceAccountOptions",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "identity_type": "identityType",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
        "overwrite_service_account": "overwriteServiceAccount",
        "removal_policy": "removalPolicy",
    },
)
class ServiceAccountOptions:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        identity_type: typing.Optional["IdentityType"] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Options for ``ServiceAccount``.

        :param annotations: Additional annotations of the service account. Default: - no additional annotations
        :param identity_type: The identity type to use for the service account. Default: IdentityType.IRSA
        :param labels: Additional labels of the service account. Default: - no additional labels
        :param name: The name of the service account. The name of a ServiceAccount object must be a valid DNS subdomain name. https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ Default: - If no name is given, it will use the id of the resource.
        :param namespace: The namespace of the service account. All namespace names must be valid RFC 1123 DNS labels. https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns Default: "default"
        :param overwrite_service_account: Overwrite existing service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the service account is created. Otherwise, if there is already a service account in the cluster with the same name, the operation will fail. Default: false
        :param removal_policy: The removal policy applied to the service account resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY

        :exampleMetadata: infused

        Example::

            # cluster: eks.Cluster
            
            # add service account with annotations and labels
            service_account = cluster.add_service_account("MyServiceAccount",
                annotations={
                    "eks.amazonaws.com/sts-regional-endpoints": "false"
                },
                labels={
                    "some-label": "with-some-value"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e60561f7a296f4bf04de0a0c27864a64f49c57d5f2b96cec52694275414918)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument overwrite_service_account", value=overwrite_service_account, expected_type=type_hints["overwrite_service_account"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if identity_type is not None:
            self._values["identity_type"] = identity_type
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if overwrite_service_account is not None:
            self._values["overwrite_service_account"] = overwrite_service_account
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional annotations of the service account.

        :default: - no additional annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def identity_type(self) -> typing.Optional["IdentityType"]:
        '''The identity type to use for the service account.

        :default: IdentityType.IRSA
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional["IdentityType"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional labels of the service account.

        :default: - no additional labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service account.

        The name of a ServiceAccount object must be a valid DNS subdomain name.
        https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

        :default: - If no name is given, it will use the id of the resource.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the service account.

        All namespace names must be valid RFC 1123 DNS labels.
        https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns

        :default: "default"
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_service_account(self) -> typing.Optional[builtins.bool]:
        '''Overwrite existing service account.

        If this is set, we will use ``kubectl apply`` instead of ``kubectl create``
        when the service account is created. Otherwise, if there is already a service account
        in the cluster with the same name, the operation will fail.

        :default: false
        '''
        result = self._values.get("overwrite_service_account")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the service account resources.

        The removal policy controls what happens to the resources if they stop being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAccountOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ServiceAccountProps",
    jsii_struct_bases=[ServiceAccountOptions],
    name_mapping={
        "annotations": "annotations",
        "identity_type": "identityType",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
        "overwrite_service_account": "overwriteServiceAccount",
        "removal_policy": "removalPolicy",
        "cluster": "cluster",
    },
)
class ServiceAccountProps(ServiceAccountOptions):
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        identity_type: typing.Optional["IdentityType"] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        cluster: "ICluster",
    ) -> None:
        '''Properties for defining service accounts.

        :param annotations: Additional annotations of the service account. Default: - no additional annotations
        :param identity_type: The identity type to use for the service account. Default: IdentityType.IRSA
        :param labels: Additional labels of the service account. Default: - no additional labels
        :param name: The name of the service account. The name of a ServiceAccount object must be a valid DNS subdomain name. https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ Default: - If no name is given, it will use the id of the resource.
        :param namespace: The namespace of the service account. All namespace names must be valid RFC 1123 DNS labels. https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns Default: "default"
        :param overwrite_service_account: Overwrite existing service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the service account is created. Otherwise, if there is already a service account in the cluster with the same name, the operation will fail. Default: false
        :param removal_policy: The removal policy applied to the service account resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param cluster: The cluster to apply the patch to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_eks_v2 as eks_v2
            
            # cluster: eks_v2.Cluster
            
            service_account_props = eks_v2.ServiceAccountProps(
                cluster=cluster,
            
                # the properties below are optional
                annotations={
                    "annotations_key": "annotations"
                },
                identity_type=eks_v2.IdentityType.IRSA,
                labels={
                    "labels_key": "labels"
                },
                name="name",
                namespace="namespace",
                overwrite_service_account=False,
                removal_policy=cdk.RemovalPolicy.DESTROY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbdefc85ea927da26d0db8cbc6fa377f201aba1199d5be6929397306c347f4e4)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument overwrite_service_account", value=overwrite_service_account, expected_type=type_hints["overwrite_service_account"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if identity_type is not None:
            self._values["identity_type"] = identity_type
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if overwrite_service_account is not None:
            self._values["overwrite_service_account"] = overwrite_service_account
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional annotations of the service account.

        :default: - no additional annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def identity_type(self) -> typing.Optional["IdentityType"]:
        '''The identity type to use for the service account.

        :default: IdentityType.IRSA
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional["IdentityType"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional labels of the service account.

        :default: - no additional labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service account.

        The name of a ServiceAccount object must be a valid DNS subdomain name.
        https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

        :default: - If no name is given, it will use the id of the resource.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the service account.

        All namespace names must be valid RFC 1123 DNS labels.
        https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns

        :default: "default"
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_service_account(self) -> typing.Optional[builtins.bool]:
        '''Overwrite existing service account.

        If this is set, we will use ``kubectl apply`` instead of ``kubectl create``
        when the service account is created. Otherwise, if there is already a service account
        in the cluster with the same name, the operation will fail.

        :default: false
        '''
        result = self._values.get("overwrite_service_account")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy applied to the service account resources.

        The removal policy controls what happens to the resources if they stop being managed by CloudFormation.
        This can happen in one of three situations:

        - The resource is removed from the template, so CloudFormation stops managing it
        - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it
        - The stack is deleted, so CloudFormation stops managing all resources in it

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    @builtins.property
    def cluster(self) -> "ICluster":
        '''The cluster to apply the patch to.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("ICluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.ServiceLoadBalancerAddressOptions",
    jsii_struct_bases=[],
    name_mapping={"namespace": "namespace", "timeout": "timeout"},
)
class ServiceLoadBalancerAddressOptions:
    def __init__(
        self,
        *,
        namespace: typing.Optional[builtins.str] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
    ) -> None:
        '''Options for fetching a ServiceLoadBalancerAddress.

        :param namespace: The namespace the service belongs to. Default: 'default'
        :param timeout: Timeout for waiting on the load balancer address. Default: Duration.minutes(5)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_eks_v2 as eks_v2
            
            service_load_balancer_address_options = eks_v2.ServiceLoadBalancerAddressOptions(
                namespace="namespace",
                timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f079932823e7c1d90e7a61b8ff67d830b157fa4dc704dbe055655ed3112ca23e)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if namespace is not None:
            self._values["namespace"] = namespace
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace the service belongs to.

        :default: 'default'
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''Timeout for waiting on the load balancer address.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLoadBalancerAddressOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_eks_v2.TaintEffect")
class TaintEffect(enum.Enum):
    '''Effect types of kubernetes node taint.

    Note: These values are specifically for AWS EKS NodeGroups and use the AWS API format.
    When using AWS CLI or API, taint effects must be NO_SCHEDULE, PREFER_NO_SCHEDULE, or NO_EXECUTE.
    When using Kubernetes directly or kubectl, taint effects must be NoSchedule, PreferNoSchedule, or NoExecute.

    For Kubernetes manifests (like Karpenter NodePools), use string literals with PascalCase format:

    - 'NoSchedule' instead of TaintEffect.NO_SCHEDULE
    - 'PreferNoSchedule' instead of TaintEffect.PREFER_NO_SCHEDULE
    - 'NoExecute' instead of TaintEffect.NO_EXECUTE

    :see: https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html
    '''

    NO_SCHEDULE = "NO_SCHEDULE"
    '''NoSchedule.'''
    PREFER_NO_SCHEDULE = "PREFER_NO_SCHEDULE"
    '''PreferNoSchedule.'''
    NO_EXECUTE = "NO_EXECUTE"
    '''NoExecute.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.TaintSpec",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class TaintSpec:
    def __init__(
        self,
        *,
        effect: typing.Optional["TaintEffect"] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Taint interface.

        :param effect: Effect type. Default: - None
        :param key: Taint key. Default: - None
        :param value: Taint value. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eks_v2 as eks_v2
            
            taint_spec = eks_v2.TaintSpec(
                effect=eks_v2.TaintEffect.NO_SCHEDULE,
                key="key",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f2601666139771d5c99f22c408f43ba115a6e7e103efba0fc905c49b8ca186)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def effect(self) -> typing.Optional["TaintEffect"]:
        '''Effect type.

        :default: - None
        '''
        result = self._values.get("effect")
        return typing.cast(typing.Optional["TaintEffect"], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Taint key.

        :default: - None
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Taint value.

        :default: - None
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaintSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAccessEntry)
class AccessEntry(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessEntry",
):
    '''Represents an access entry in an Amazon EKS cluster.

    An access entry defines the permissions and scope for a user or role to access an Amazon EKS cluster.

    :implements: IAccessEntry *
    :resource: AWS::EKS::AccessEntry
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_eks_v2 as eks_v2
        
        # access_policy: eks_v2.AccessPolicy
        # cluster: eks_v2.Cluster
        
        access_entry = eks_v2.AccessEntry(self, "MyAccessEntry",
            access_policies=[access_policy],
            cluster=cluster,
            principal="principal",
        
            # the properties below are optional
            access_entry_name="accessEntryName",
            access_entry_type=eks_v2.AccessEntryType.STANDARD,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        access_policies: typing.Sequence["IAccessPolicy"],
        cluster: "ICluster",
        principal: builtins.str,
        access_entry_name: typing.Optional[builtins.str] = None,
        access_entry_type: typing.Optional["AccessEntryType"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_policies: The access policies that define the permissions and scope for the access entry.
        :param cluster: The Amazon EKS cluster to which the access entry applies.
        :param principal: The Amazon Resource Name (ARN) of the principal (user or role) to associate the access entry with.
        :param access_entry_name: The name of the AccessEntry. Default: - No access entry name is provided
        :param access_entry_type: The type of the AccessEntry. Default: STANDARD
        :param removal_policy: The removal policy applied to the access entry. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdc6127073e756efdb5d14c617b09700f48d54838b27dab13b99f6ee8c7b5c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AccessEntryProps(
            access_policies=access_policies,
            cluster=cluster,
            principal=principal,
            access_entry_name=access_entry_name,
            access_entry_type=access_entry_type,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAccessEntryAttributes")
    @builtins.classmethod
    def from_access_entry_attributes(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        access_entry_arn: builtins.str,
        access_entry_name: builtins.str,
    ) -> "IAccessEntry":
        '''Imports an ``AccessEntry`` from its attributes.

        :param scope: - The parent construct.
        :param id: - The ID of the imported construct.
        :param access_entry_arn: The Amazon Resource Name (ARN) of the access entry.
        :param access_entry_name: The name of the access entry.

        :return: The imported access entry.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5843ba949e2e8e70c545c57e323a169a136e1233a3d21e876a127fb80d7723)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = AccessEntryAttributes(
            access_entry_arn=access_entry_arn, access_entry_name=access_entry_name
        )

        return typing.cast("IAccessEntry", jsii.sinvoke(cls, "fromAccessEntryAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAccessPolicies")
    def add_access_policies(
        self,
        new_access_policies: typing.Sequence["IAccessPolicy"],
    ) -> None:
        '''Add the access policies for this entry.

        :param new_access_policies: - The new access policies to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c74254cbfe0119312b0ccd27b5e4874f7973e094484a1ec1bce54f003b0cc97)
            check_type(argname="argument new_access_policies", value=new_access_policies, expected_type=type_hints["new_access_policies"])
        return typing.cast(None, jsii.invoke(self, "addAccessPolicies", [new_access_policies]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="accessEntryArn")
    def access_entry_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access entry.'''
        return typing.cast(builtins.str, jsii.get(self, "accessEntryArn"))

    @builtins.property
    @jsii.member(jsii_name="accessEntryName")
    def access_entry_name(self) -> builtins.str:
        '''The name of the access entry.'''
        return typing.cast(builtins.str, jsii.get(self, "accessEntryName"))

    @builtins.property
    @jsii.member(jsii_name="accessEntryRef")
    def access_entry_ref(self) -> "_AccessEntryReference_447195cd":
        '''A reference to a AccessEntry resource.'''
        return typing.cast("_AccessEntryReference_447195cd", jsii.get(self, "accessEntryRef"))


@jsii.implements(IAccessPolicy)
class AccessPolicy(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.AccessPolicy",
):
    '''Represents an Amazon EKS Access Policy that implements the IAccessPolicy interface.

    :implements: IAccessPolicy
    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        # node_role: iam.Role
        
        
        # Grant access with EC2 type for Auto Mode node role
        cluster.grant_access("nodeAccess", node_role.role_arn, [
            eks.AccessPolicy.from_access_policy_name("AmazonEKSAutoNodePolicy",
                access_scope_type=eks.AccessScopeType.CLUSTER
            )
        ], access_entry_type=eks.AccessEntryType.EC2)
    '''

    def __init__(
        self,
        *,
        access_scope: typing.Union["AccessScope", typing.Dict[builtins.str, typing.Any]],
        policy: "AccessPolicyArn",
    ) -> None:
        '''Constructs a new instance of the AccessPolicy class.

        :param access_scope: The scope of the access policy, which determines the level of access granted.
        :param policy: The access policy itself, which defines the specific permissions.
        '''
        props = AccessPolicyProps(access_scope=access_scope, policy=policy)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="fromAccessPolicyName")
    @builtins.classmethod
    def from_access_policy_name(
        cls,
        policy_name: builtins.str,
        *,
        access_scope_type: "AccessScopeType",
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "IAccessPolicy":
        '''Import AccessPolicy by name.

        :param policy_name: -
        :param access_scope_type: The scope of the access policy. This determines the level of access granted by the policy.
        :param namespaces: An optional array of Kubernetes namespaces to which the access policy applies. Default: - no specific namespaces for this scope
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ee335ba80e25dde88caafff066ca29c64b71a4600a48104897072f72f9b127c)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        options = AccessPolicyNameOptions(
            access_scope_type=access_scope_type, namespaces=namespaces
        )

        return typing.cast("IAccessPolicy", jsii.sinvoke(cls, "fromAccessPolicyName", [policy_name, options]))

    @builtins.property
    @jsii.member(jsii_name="accessScope")
    def access_scope(self) -> "AccessScope":
        '''The scope of the access policy, which determines the level of access granted.'''
        return typing.cast("AccessScope", jsii.get(self, "accessScope"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        '''The access policy itself, which defines the specific permissions.'''
        return typing.cast(builtins.str, jsii.get(self, "policy"))


@jsii.implements(IAddon)
class Addon(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.Addon",
):
    '''Represents an Amazon EKS Add-On.

    :resource: AWS::EKS::Addon
    :exampleMetadata: infused

    Example::

        # cluster: eks.Cluster
        
        
        eks.Addon(self, "Addon",
            cluster=cluster,
            addon_name="coredns",
            addon_version="v1.11.4-eksbuild.2",
            # whether to preserve the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on.
            preserve_on_delete=False,
            configuration_values={
                "replica_count": 2
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        addon_name: builtins.str,
        cluster: "ICluster",
        addon_version: typing.Optional[builtins.str] = None,
        configuration_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        preserve_on_delete: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Creates a new Amazon EKS Add-On.

        :param scope: The parent construct.
        :param id: The construct ID.
        :param addon_name: Name of the Add-On.
        :param cluster: The EKS cluster the Add-On is associated with.
        :param addon_version: Version of the Add-On. You can check all available versions with describe-addon-versions. For example, this lists all available versions for the ``eks-pod-identity-agent`` addon: $ aws eks describe-addon-versions --addon-name eks-pod-identity-agent --query 'addons[*].addonVersions[*].addonVersion' Default: the latest version.
        :param configuration_values: The configuration values for the Add-on. Default: - Use default configuration.
        :param preserve_on_delete: Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn't removed. Default: true
        :param removal_policy: The removal policy applied to the EKS add-on. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1b17956f5367c24e8d921a4cd124387605b548466a8c8fce1394046132a5b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AddonProps(
            addon_name=addon_name,
            cluster=cluster,
            addon_version=addon_version,
            configuration_values=configuration_values,
            preserve_on_delete=preserve_on_delete,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAddonArn")
    @builtins.classmethod
    def from_addon_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        addon_arn: builtins.str,
    ) -> "IAddon":
        '''Creates an ``IAddon`` from an existing addon ARN.

        :param scope: - The parent construct.
        :param id: - The ID of the construct.
        :param addon_arn: - The ARN of the addon.

        :return: An ``IAddon`` implementation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03634d6d2462cd98d140ea663e2e67722309b40b81399e2b79125a7dbe5e5f85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument addon_arn", value=addon_arn, expected_type=type_hints["addon_arn"])
        return typing.cast("IAddon", jsii.sinvoke(cls, "fromAddonArn", [scope, id, addon_arn]))

    @jsii.member(jsii_name="fromAddonAttributes")
    @builtins.classmethod
    def from_addon_attributes(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        addon_name: builtins.str,
        cluster_name: builtins.str,
    ) -> "IAddon":
        '''Creates an ``IAddon`` instance from the given addon attributes.

        :param scope: - The parent construct.
        :param id: - The construct ID.
        :param addon_name: The name of the addon.
        :param cluster_name: The name of the Amazon EKS cluster the addon is associated with.

        :return: An ``IAddon`` instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c96efbeaaaa15433190608a29071311bab6ef9fd1c1ae38ea9936343adaebb7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = AddonAttributes(addon_name=addon_name, cluster_name=cluster_name)

        return typing.cast("IAddon", jsii.sinvoke(cls, "fromAddonAttributes", [scope, id, attrs]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="addonArn")
    def addon_arn(self) -> builtins.str:
        '''ARN of the Add-On.'''
        return typing.cast(builtins.str, jsii.get(self, "addonArn"))

    @builtins.property
    @jsii.member(jsii_name="addonName")
    def addon_name(self) -> builtins.str:
        '''Name of the addon.'''
        return typing.cast(builtins.str, jsii.get(self, "addonName"))

    @builtins.property
    @jsii.member(jsii_name="addonRef")
    def addon_ref(self) -> "_AddonReference_afb1bd13":
        '''A reference to a Addon resource.'''
        return typing.cast("_AddonReference_afb1bd13", jsii.get(self, "addonRef"))


@jsii.implements(ICluster)
class Cluster(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.Cluster",
):
    '''A Cluster represents a managed Kubernetes Service (EKS).

    This is a fully managed cluster of API Servers (control-plane)
    The user is still required to create the worker nodes.

    :resource: AWS::EKS::Cluster
    :exampleMetadata: infused

    Example::

        cluster = eks.Cluster(self, "ManagedNodeCluster",
            version=eks.KubernetesVersion.V1_34,
            default_capacity_type=eks.DefaultCapacityType.NODEGROUP
        )
        
        # Add a Fargate Profile for specific workloads (e.g., default namespace)
        cluster.add_fargate_profile("FargateProfile",
            selectors=[eks.Selector(namespace="default")
            ]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        bootstrap_cluster_creator_admin_permissions: typing.Optional[builtins.bool] = None,
        bootstrap_self_managed_addons: typing.Optional[builtins.bool] = None,
        compute: typing.Optional[typing.Union["ComputeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        default_capacity: typing.Optional[jsii.Number] = None,
        default_capacity_instance: typing.Optional["_InstanceType_f64915b9"] = None,
        default_capacity_type: typing.Optional["DefaultCapacityType"] = None,
        output_config_command: typing.Optional[builtins.bool] = None,
        version: "KubernetesVersion",
        alb_controller: typing.Optional[typing.Union["AlbControllerOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_logging: typing.Optional[typing.Sequence["ClusterLoggingTypes"]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        core_dns_compute_type: typing.Optional["CoreDnsComputeType"] = None,
        endpoint_access: typing.Optional["EndpointAccess"] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        masters_role: typing.Optional["_IRole_235f5d8e"] = None,
        prune: typing.Optional[builtins.bool] = None,
        remote_node_networks: typing.Optional[typing.Sequence[typing.Union["RemoteNodeNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        remote_pod_networks: typing.Optional[typing.Sequence[typing.Union["RemotePodNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        secrets_encryption_key: typing.Optional["_IKeyRef_d4fc6ef3"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
        service_ipv4_cidr: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Initiates an EKS Cluster with the supplied arguments.

        :param scope: a Construct, most likely a cdk.Stack created.
        :param id: the id of the Construct to create.
        :param bootstrap_cluster_creator_admin_permissions: Whether or not IAM principal of the cluster creator was set as a cluster admin access entry during cluster creation time. Changing this value after the cluster has been created will result in the cluster being replaced. Default: true
        :param bootstrap_self_managed_addons: If you set this value to False when creating a cluster, the default networking add-ons will not be installed. The default networking addons include vpc-cni, coredns, and kube-proxy. Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons. Changing this value after the cluster has been created will result in the cluster being replaced. Default: true if the mode is not EKS Auto Mode
        :param compute: Configuration for compute settings in Auto Mode. When enabled, EKS will automatically manage compute resources. Default: - Auto Mode compute disabled
        :param default_capacity: Number of instances to allocate as an initial capacity for this cluster. Instance type can be configured through ``defaultCapacityInstanceType``, which defaults to ``m5.large``. Use ``cluster.addAutoScalingGroupCapacity`` to add additional customized capacity. Set this to ``0`` is you wish to avoid the initial capacity allocation. Default: 2
        :param default_capacity_instance: The instance type to use for the default capacity. This will only be taken into account if ``defaultCapacity`` is > 0. Default: m5.large
        :param default_capacity_type: The default capacity type for the cluster. Default: AUTOMODE
        :param output_config_command: Determines whether a CloudFormation output with the ``aws eks update-kubeconfig`` command will be synthesized. This command will include the cluster name and, if applicable, the ARN of the masters IAM role. Default: true
        :param version: The Kubernetes version to run in the cluster.
        :param alb_controller: Install the AWS Load Balancer Controller onto the cluster. Default: - The controller is not installed.
        :param cluster_logging: The cluster log types which you want to enable. Default: - none
        :param cluster_name: Name for the cluster. Default: - Automatically generated name
        :param core_dns_compute_type: Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS. Default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        :param endpoint_access: Configure access to the Kubernetes API server endpoint.. Default: EndpointAccess.PUBLIC_AND_PRIVATE
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: IpFamily.IP_V4
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created
        :param masters_role: An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - no masters role.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param remote_node_networks: IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster. Default: - none
        :param remote_pod_networks: IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes. Default: - none
        :param removal_policy: The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it; - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it; - The stack is deleted, so CloudFormation stops managing all resources in it. This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC and any other CloudFormation resources managed by this construct. Default: - Resources will be deleted.
        :param role: Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param secrets_encryption_key: KMS secret for envelope encryption for Kubernetes secrets. Default: - By default, Kubernetes stores all secret object data within etcd and all etcd volumes used by Amazon EKS are encrypted at the disk-level using AWS-Managed encryption keys.
        :param security_group: Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param service_ipv4_cidr: The CIDR block to assign Kubernetes service IP addresses from. Default: - Kubernetes assigns addresses from either the 10.100.0.0/16 or 172.20.0.0/16 CIDR blocks
        :param tags: The tags assigned to the EKS cluster. Default: - none
        :param vpc: The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: Where to place EKS Control Plane ENIs. For example, to only select private subnets, supply the following: ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]`` Default: - All public and private subnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6792a3b69429b43c9b6b098e7633a33fb4c1fab5fd463a43797578ef02f2a82d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterProps(
            bootstrap_cluster_creator_admin_permissions=bootstrap_cluster_creator_admin_permissions,
            bootstrap_self_managed_addons=bootstrap_self_managed_addons,
            compute=compute,
            default_capacity=default_capacity,
            default_capacity_instance=default_capacity_instance,
            default_capacity_type=default_capacity_type,
            output_config_command=output_config_command,
            version=version,
            alb_controller=alb_controller,
            cluster_logging=cluster_logging,
            cluster_name=cluster_name,
            core_dns_compute_type=core_dns_compute_type,
            endpoint_access=endpoint_access,
            ip_family=ip_family,
            kubectl_provider_options=kubectl_provider_options,
            masters_role=masters_role,
            prune=prune,
            remote_node_networks=remote_node_networks,
            remote_pod_networks=remote_pod_networks,
            removal_policy=removal_policy,
            role=role,
            secrets_encryption_key=secrets_encryption_key,
            security_group=security_group,
            service_ipv4_cidr=service_ipv4_cidr,
            tags=tags,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClusterAttributes")
    @builtins.classmethod
    def from_cluster_attributes(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        cluster_certificate_authority_data: typing.Optional[builtins.str] = None,
        cluster_encryption_config_key_arn: typing.Optional[builtins.str] = None,
        cluster_endpoint: typing.Optional[builtins.str] = None,
        cluster_security_group_id: typing.Optional[builtins.str] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider: typing.Optional["IKubectlProvider"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        open_id_connect_provider: typing.Optional["_IOpenIdConnectProvider_203f0793"] = None,
        prune: typing.Optional[builtins.bool] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
    ) -> "ICluster":
        '''Import an existing cluster.

        :param scope: the construct scope, in most cases 'this'.
        :param id: the id or name to import as.
        :param cluster_name: The physical name of the Cluster.
        :param cluster_certificate_authority_data: The certificate-authority-data for your cluster. Default: - if not specified ``cluster.clusterCertificateAuthorityData`` will throw an error
        :param cluster_encryption_config_key_arn: Amazon Resource Name (ARN) or alias of the customer master key (CMK). Default: - if not specified ``cluster.clusterEncryptionConfigKeyArn`` will throw an error
        :param cluster_endpoint: The API Server endpoint URL. Default: - if not specified ``cluster.clusterEndpoint`` will throw an error.
        :param cluster_security_group_id: The cluster security group that was created by Amazon EKS for the cluster. Default: - if not specified ``cluster.clusterSecurityGroupId`` will throw an error
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: - IpFamily.IP_V4
        :param kubectl_provider: KubectlProvider for issuing kubectl commands. Default: - Default CDK provider
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created by default.
        :param open_id_connect_provider: An Open ID Connect provider for this cluster that can be used to configure service accounts. You can either import an existing provider using ``iam.OpenIdConnectProvider.fromProviderArn``, or create a new provider using ``new eks.OpenIdConnectProvider`` Default: - if not specified ``cluster.openIdConnectProvider`` and ``cluster.addServiceAccount`` will throw an error.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param security_group_ids: Additional security groups associated with this cluster. Default: - if not specified, no additional security groups will be considered in ``cluster.connections``.
        :param vpc: The VPC in which this Cluster was created. Default: - if not specified ``cluster.vpc`` will throw an error
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67bdcedf04f32c2e8ab4570349cea73b300650eaf17d233e89978d8ec9050f96)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ClusterAttributes(
            cluster_name=cluster_name,
            cluster_certificate_authority_data=cluster_certificate_authority_data,
            cluster_encryption_config_key_arn=cluster_encryption_config_key_arn,
            cluster_endpoint=cluster_endpoint,
            cluster_security_group_id=cluster_security_group_id,
            ip_family=ip_family,
            kubectl_provider=kubectl_provider,
            kubectl_provider_options=kubectl_provider_options,
            open_id_connect_provider=open_id_connect_provider,
            prune=prune,
            security_group_ids=security_group_ids,
            vpc=vpc,
        )

        return typing.cast("ICluster", jsii.sinvoke(cls, "fromClusterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAutoScalingGroupCapacity")
    def add_auto_scaling_group_capacity(
        self,
        id: builtins.str,
        *,
        instance_type: "_InstanceType_f64915b9",
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[typing.Union["BootstrapOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        machine_image_type: typing.Optional["MachineImageType"] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        associate_public_ip_address: typing.Optional[builtins.bool] = None,
        auto_scaling_group_name: typing.Optional[builtins.str] = None,
        az_capacity_distribution_strategy: typing.Optional["_CapacityDistributionStrategy_2393ccfe"] = None,
        block_devices: typing.Optional[typing.Sequence[typing.Union["_BlockDevice_0cfc0568", typing.Dict[builtins.str, typing.Any]]]] = None,
        capacity_rebalance: typing.Optional[builtins.bool] = None,
        cooldown: typing.Optional["_Duration_4839e8c3"] = None,
        default_instance_warmup: typing.Optional["_Duration_4839e8c3"] = None,
        deletion_protection: typing.Optional["_DeletionProtection_3beb1830"] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        group_metrics: typing.Optional[typing.Sequence["_GroupMetrics_7cdf729b"]] = None,
        health_check: typing.Optional["_HealthCheck_03a4bd5a"] = None,
        health_checks: typing.Optional["_HealthChecks_b8757873"] = None,
        ignore_unmodified_size_properties: typing.Optional[builtins.bool] = None,
        instance_monitoring: typing.Optional["_Monitoring_50020f91"] = None,
        key_name: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional["_IKeyPair_bc344eda"] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_instance_lifetime: typing.Optional["_Duration_4839e8c3"] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        new_instances_protected_from_scale_in: typing.Optional[builtins.bool] = None,
        notifications: typing.Optional[typing.Sequence[typing.Union["_NotificationConfiguration_d5911670", typing.Dict[builtins.str, typing.Any]]]] = None,
        signals: typing.Optional["_Signals_69fbeb6e"] = None,
        spot_price: typing.Optional[builtins.str] = None,
        ssm_session_permissions: typing.Optional[builtins.bool] = None,
        termination_policies: typing.Optional[typing.Sequence["_TerminationPolicy_89633c56"]] = None,
        termination_policy_custom_lambda_function_arn: typing.Optional[builtins.str] = None,
        update_policy: typing.Optional["_UpdatePolicy_6dffc7ca"] = None,
        vpc_subnets: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> "_AutoScalingGroup_c547a7b9":
        '''Add nodes to this EKS cluster.

        The nodes will automatically be configured with the right VPC and AMI
        for the instance type and Kubernetes version.

        Note that if you specify ``updateType: RollingUpdate`` or ``updateType: ReplacingUpdate``, your nodes might be replaced at deploy
        time without notice in case the recommended AMI for your machine image type has been updated by AWS.
        The default behavior for ``updateType`` is ``None``, which means only new instances will be launched using the new AMI.

        :param id: -
        :param instance_type: Instance type of the instances to start.
        :param bootstrap_enabled: Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: EKS node bootstrapping options. Default: - none
        :param machine_image_type: Machine image type. Default: MachineImageType.AMAZON_LINUX_2
        :param allow_all_outbound: Whether the instances can initiate connections to anywhere by default. Default: true
        :param associate_public_ip_address: Whether instances in the Auto Scaling Group should have public IP addresses associated with them. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: - Use subnet setting.
        :param auto_scaling_group_name: The name of the Auto Scaling group. This name must be unique per Region per account. Default: - Auto generated by CloudFormation
        :param az_capacity_distribution_strategy: The strategy for distributing instances across Availability Zones. Default: None
        :param block_devices: Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes. Each instance that is launched has an associated root device volume, either an Amazon EBS volume or an instance store volume. You can use block device mappings to specify additional EBS volumes or instance store volumes to attach to an instance when it is launched. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: - Uses the block device mapping of the AMI
        :param capacity_rebalance: Indicates whether Capacity Rebalancing is enabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. Default: false
        :param cooldown: Default scaling cooldown for this AutoScalingGroup. Default: Duration.minutes(5)
        :param default_instance_warmup: The amount of time, in seconds, until a newly launched instance can contribute to the Amazon CloudWatch metrics. This delay lets an instance finish initializing before Amazon EC2 Auto Scaling aggregates instance metrics, resulting in more reliable usage data. Set this value equal to the amount of time that it takes for resource consumption to become stable after an instance reaches the InService state. To optimize the performance of scaling policies that scale continuously, such as target tracking and step scaling policies, we strongly recommend that you enable the default instance warmup, even if its value is set to 0 seconds Default instance warmup will not be added if no value is specified Default: None
        :param deletion_protection: Deletion protection for the Auto Scaling group. Default: DeletionProtection.NONE
        :param desired_capacity: Initial amount of instances in the fleet. If this is set to a number, every deployment will reset the amount of instances to this number. It is recommended to leave this value blank. Default: minCapacity, and leave unchanged during deployment
        :param group_metrics: Enable monitoring for group metrics, these metrics describe the group rather than any of its instances. To report all group metrics use ``GroupMetrics.all()`` Group metrics are reported in a granularity of 1 minute at no additional charge. Default: - no group metrics will be reported
        :param health_check: (deprecated) Configuration for health checks. Default: - HealthCheck.ec2 with no grace period
        :param health_checks: Configuration for EC2 or additional health checks. Even when using ``HealthChecks.withAdditionalChecks()``, the EC2 type is implicitly included. Default: - EC2 type with no grace period
        :param ignore_unmodified_size_properties: If the ASG has scheduled actions, don't reset unchanged group sizes. Only used if the ASG has scheduled actions (which may scale your ASG up or down regardless of cdk deployments). If true, the size of the group will only be reset if it has been changed in the CDK app. If false, the sizes will always be changed back to what they were in the CDK app on deployment. Default: true
        :param instance_monitoring: Controls whether instances in this group are launched with detailed or basic monitoring. When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: - Monitoring.DETAILED
        :param key_name: (deprecated) Name of SSH keypair to grant access to instances. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified You can either specify ``keyPair`` or ``keyName``, not both. Default: - No SSH access will be possible.
        :param key_pair: The SSH keypair to grant access to the instance. Feature flag ``AUTOSCALING_GENERATE_LAUNCH_TEMPLATE`` must be enabled to use this property. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified. You can either specify ``keyPair`` or ``keyName``, not both. Default: - No SSH access will be possible.
        :param max_capacity: Maximum number of instances in the fleet. Default: desiredCapacity
        :param max_instance_lifetime: The maximum amount of time that an instance can be in service. The maximum duration applies to all current and future instances in the group. As an instance approaches its maximum duration, it is terminated and replaced, and cannot be used again. You must specify a value of at least 86,400 seconds (one day). To clear a previously set value, leave this property undefined. Default: none
        :param min_capacity: Minimum number of instances in the fleet. Default: 1
        :param new_instances_protected_from_scale_in: Whether newly-launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. By default, Auto Scaling can terminate an instance at any time after launch when scaling in an Auto Scaling Group, subject to the group's termination policy. However, you may wish to protect newly-launched instances from being scaled in if they are going to run critical applications that should not be prematurely terminated. This flag must be enabled if the Auto Scaling Group will be associated with an ECS Capacity Provider with managed termination protection. Default: false
        :param notifications: Configure autoscaling group to send notifications about fleet changes to an SNS topic(s). Default: - No fleet change notifications will be sent.
        :param signals: Configure waiting for signals during deployment. Use this to pause the CloudFormation deployment to wait for the instances in the AutoScalingGroup to report successful startup during creation and updates. The UserData script needs to invoke ``cfn-signal`` with a success or failure code after it is done setting up the instance. Without waiting for signals, the CloudFormation deployment will proceed as soon as the AutoScalingGroup has been created or updated but before the instances in the group have been started. For example, to have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check verification by using the cfn-init helper script. For an example, see the verify_instance_health command in the Auto Scaling rolling updates sample template: https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/AutoScaling/AutoScalingRollingUpdates.yaml Default: - Do not wait for signals
        :param spot_price: The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. ``launchTemplate`` and ``mixedInstancesPolicy`` must not be specified when this property is specified Default: none
        :param ssm_session_permissions: Add SSM session permissions to the instance role. Setting this to ``true`` adds the necessary permissions to connect to the instance using SSM Session Manager. You can do this from the AWS Console. NOTE: Setting this flag to ``true`` may not be enough by itself. You must also use an AMI that comes with the SSM Agent, or install the SSM Agent yourself. See `Working with SSM Agent <https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html>`_ in the SSM Developer Guide. Default: false
        :param termination_policies: A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. Default: - ``TerminationPolicy.DEFAULT``
        :param termination_policy_custom_lambda_function_arn: A lambda function Arn that can be used as a custom termination policy to select the instances to terminate. This property must be specified if the TerminationPolicy.CUSTOM_LAMBDA_FUNCTION is used. Default: - No lambda function Arn will be supplied
        :param update_policy: What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: - ``UpdatePolicy.rollingUpdate()`` if using ``init``, ``UpdatePolicy.none()`` otherwise
        :param vpc_subnets: Where to place instances within the VPC. Default: - All Private subnets.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fab71b237eae49d14717c1b7a52d3a7624193c66fd44df3bd384e2bde905f091)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = AutoScalingGroupCapacityOptions(
            instance_type=instance_type,
            bootstrap_enabled=bootstrap_enabled,
            bootstrap_options=bootstrap_options,
            machine_image_type=machine_image_type,
            allow_all_outbound=allow_all_outbound,
            associate_public_ip_address=associate_public_ip_address,
            auto_scaling_group_name=auto_scaling_group_name,
            az_capacity_distribution_strategy=az_capacity_distribution_strategy,
            block_devices=block_devices,
            capacity_rebalance=capacity_rebalance,
            cooldown=cooldown,
            default_instance_warmup=default_instance_warmup,
            deletion_protection=deletion_protection,
            desired_capacity=desired_capacity,
            group_metrics=group_metrics,
            health_check=health_check,
            health_checks=health_checks,
            ignore_unmodified_size_properties=ignore_unmodified_size_properties,
            instance_monitoring=instance_monitoring,
            key_name=key_name,
            key_pair=key_pair,
            max_capacity=max_capacity,
            max_instance_lifetime=max_instance_lifetime,
            min_capacity=min_capacity,
            new_instances_protected_from_scale_in=new_instances_protected_from_scale_in,
            notifications=notifications,
            signals=signals,
            spot_price=spot_price,
            ssm_session_permissions=ssm_session_permissions,
            termination_policies=termination_policies,
            termination_policy_custom_lambda_function_arn=termination_policy_custom_lambda_function_arn,
            update_policy=update_policy,
            vpc_subnets=vpc_subnets,
        )

        return typing.cast("_AutoScalingGroup_c547a7b9", jsii.invoke(self, "addAutoScalingGroupCapacity", [id, options]))

    @jsii.member(jsii_name="addCdk8sChart")
    def add_cdk8s_chart(
        self,
        id: builtins.str,
        chart: "_constructs_77d1e7e8.Construct",
        *,
        ingress_alb: typing.Optional[builtins.bool] = None,
        ingress_alb_scheme: typing.Optional["AlbScheme"] = None,
        prune: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
    ) -> "KubernetesManifest":
        '''Defines a CDK8s chart in this cluster.

        :param id: logical id of this chart.
        :param chart: the cdk8s chart.
        :param ingress_alb: Automatically detect ``Ingress`` resources in the manifest and annotate them so they are picked up by an ALB Ingress Controller. Default: false
        :param ingress_alb_scheme: Specify the ALB scheme that should be applied to ``Ingress`` resources. Only applicable if ``ingressAlb`` is set to ``true``. Default: AlbScheme.INTERNAL
        :param prune: When a resource is removed from a Kubernetes manifest, it no longer appears in the manifest, and there is no way to know that this resource needs to be deleted. To address this, ``kubectl apply`` has a ``--prune`` option which will query the cluster for all resources with a specific label and will remove all the labeld resources that are not part of the applied manifest. If this option is disabled and a resource is removed, it will become "orphaned" and will not be deleted from the cluster. When this option is enabled (default), the construct will inject a label to all Kubernetes resources included in this manifest which will be used to prune resources when the manifest changes via ``kubectl apply --prune``. The label name will be ``aws.cdk.eks/prune-<ADDR>`` where ``<ADDR>`` is the 42-char unique address of this construct in the construct tree. Value is empty. Default: - based on the prune option of the cluster, which is ``true`` unless otherwise specified.
        :param removal_policy: The removal policy applied to the custom resource that manages the Kubernetes manifest. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param skip_validation: A flag to signify if the manifest validation should be skipped. Default: false

        :return: a ``KubernetesManifest`` construct representing the chart.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__616de48bb5e1449e3fd62e9a1f4fd41d7274d3c33d16a1e6df3ce6e7c5fc6a6b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument chart", value=chart, expected_type=type_hints["chart"])
        options = KubernetesManifestOptions(
            ingress_alb=ingress_alb,
            ingress_alb_scheme=ingress_alb_scheme,
            prune=prune,
            removal_policy=removal_policy,
            skip_validation=skip_validation,
        )

        return typing.cast("KubernetesManifest", jsii.invoke(self, "addCdk8sChart", [id, chart, options]))

    @jsii.member(jsii_name="addFargateProfile")
    def add_fargate_profile(
        self,
        id: builtins.str,
        *,
        selectors: typing.Sequence[typing.Union["Selector", typing.Dict[builtins.str, typing.Any]]],
        fargate_profile_name: typing.Optional[builtins.str] = None,
        pod_execution_role: typing.Optional["_IRole_235f5d8e"] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnet_selection: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
    ) -> "FargateProfile":
        '''Adds a Fargate profile to this cluster.

        :param id: the id of this profile.
        :param selectors: The selectors to match for pods to use this Fargate profile. Each selector must have an associated namespace. Optionally, you can also specify labels for a namespace. At least one selector is required and you may specify up to five selectors.
        :param fargate_profile_name: The name of the Fargate profile. Default: - generated
        :param pod_execution_role: The pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. Default: - a role will be automatically created
        :param removal_policy: The removal policy applied to the custom resource that manages the Fargate profile. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnet_selection: Select which subnets to launch your pods into. At this time, pods running on Fargate are not assigned public IP addresses, so only private subnets (with no direct route to an Internet Gateway) are allowed. You must specify the VPC to customize the subnet selection Default: - all private subnets of the VPC are selected.
        :param vpc: The VPC from which to select subnets to launch your pods into. By default, all private subnets are selected. You can customize this using ``subnetSelection``. Default: - all private subnets used by the EKS cluster

        :see: https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52570681f13e680771496b920a1f3bd641b9a3a53d3b27e0173e3d902fd8e879)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = FargateProfileOptions(
            selectors=selectors,
            fargate_profile_name=fargate_profile_name,
            pod_execution_role=pod_execution_role,
            removal_policy=removal_policy,
            subnet_selection=subnet_selection,
            vpc=vpc,
        )

        return typing.cast("FargateProfile", jsii.invoke(self, "addFargateProfile", [id, options]))

    @jsii.member(jsii_name="addHelmChart")
    def add_helm_chart(
        self,
        id: builtins.str,
        *,
        atomic: typing.Optional[builtins.bool] = None,
        chart: typing.Optional[builtins.str] = None,
        chart_asset: typing.Optional["_Asset_ac2a7e61"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        repository: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
    ) -> "HelmChart":
        '''Defines a Helm chart in this cluster.

        :param id: logical id of this chart.
        :param atomic: Whether or not Helm should treat this operation as atomic; if set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be set automatically if --atomic is used. Default: false
        :param chart: The name of the chart. Either this or ``chartAsset`` must be specified. Default: - No chart name. Implies ``chartAsset`` is used.
        :param chart_asset: The chart in the form of an asset. Either this or ``chart`` must be specified. Default: - No chart asset. Implies ``chart`` is used.
        :param create_namespace: create namespace if not exist. Default: true
        :param namespace: The Kubernetes namespace scope of the requests. Default: default
        :param release: The name of the release. Default: - If no release name is given, it will use the last 53 characters of the node's unique id.
        :param removal_policy: The removal policy applied to the custom resource that manages the Helm chart. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param repository: The repository which contains the chart. For example: https://charts.helm.sh/stable/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param skip_crds: if set, no CRDs will be installed. Default: - CRDs are installed if not already present
        :param timeout: Amount of time to wait for any individual Kubernetes operation. Maximum 15 minutes. Default: Duration.minutes(5)
        :param values: The values to be used by the chart. For nested values use a nested dictionary. For example: values: { installationCRDs: true, webhook: { port: 9443 } } Default: - No values are provided to the chart.
        :param version: The chart version to install. Default: - If this is not specified, the latest version is installed
        :param wait: Whether or not Helm should wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. Default: - Helm will not wait before marking release as successful

        :return: a ``HelmChart`` construct
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2efee60e4d961bc101f18bc84a5ff3a7907a13fc2a788fbd44addb7a9c86786)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = HelmChartOptions(
            atomic=atomic,
            chart=chart,
            chart_asset=chart_asset,
            create_namespace=create_namespace,
            namespace=namespace,
            release=release,
            removal_policy=removal_policy,
            repository=repository,
            skip_crds=skip_crds,
            timeout=timeout,
            values=values,
            version=version,
            wait=wait,
        )

        return typing.cast("HelmChart", jsii.invoke(self, "addHelmChart", [id, options]))

    @jsii.member(jsii_name="addManifest")
    def add_manifest(
        self,
        id: builtins.str,
        *manifest: typing.Mapping[builtins.str, typing.Any],
    ) -> "KubernetesManifest":
        '''Defines a Kubernetes resource in this cluster.

        The manifest will be applied/deleted using kubectl as needed.

        :param id: logical id of this manifest.
        :param manifest: a list of Kubernetes resource specifications.

        :return: a ``KubernetesResource`` object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec17920c98f2a13f6d28bdbca1d7c278377a464eac0a7bf72e843185f7165f79)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument manifest", value=manifest, expected_type=typing.Tuple[type_hints["manifest"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("KubernetesManifest", jsii.invoke(self, "addManifest", [id, *manifest]))

    @jsii.member(jsii_name="addNodegroupCapacity")
    def add_nodegroup_capacity(
        self,
        id: builtins.str,
        *,
        ami_type: typing.Optional["NodegroupAmiType"] = None,
        capacity_type: typing.Optional["CapacityType"] = None,
        desired_size: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        enable_node_auto_repair: typing.Optional[builtins.bool] = None,
        force_update: typing.Optional[builtins.bool] = None,
        instance_types: typing.Optional[typing.Sequence["_InstanceType_f64915b9"]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        launch_template_spec: typing.Optional[typing.Union["LaunchTemplateSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
        max_unavailable_percentage: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        nodegroup_name: typing.Optional[builtins.str] = None,
        node_role: typing.Optional["_IRole_235f5d8e"] = None,
        release_version: typing.Optional[builtins.str] = None,
        remote_access: typing.Optional[typing.Union["NodegroupRemoteAccess", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        subnets: typing.Optional[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        taints: typing.Optional[typing.Sequence[typing.Union["TaintSpec", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> "Nodegroup":
        '''Add managed nodegroup to this Amazon EKS cluster.

        This method will create a new managed nodegroup and add into the capacity.

        :param id: The ID of the nodegroup.
        :param ami_type: The AMI type for your node group. If you explicitly specify the launchTemplate with custom AMI, do not specify this property, or the node group deployment will fail. In other cases, you will need to specify correct amiType for the nodegroup. Default: - auto-determined from the instanceTypes property when launchTemplateSpec property is not specified
        :param capacity_type: The capacity type of the nodegroup. Default: CapacityType.ON_DEMAND
        :param desired_size: The current number of worker nodes that the managed node group should maintain. If not specified, the nodewgroup will initially create ``minSize`` instances. Default: 2
        :param disk_size: The root device disk size (in GiB) for your node group instances. Default: 20
        :param enable_node_auto_repair: Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default. Default: false
        :param force_update: Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue. If an update fails because pods could not be drained, you can force the update after it fails to terminate the old node whether or not any pods are running on the node. Default: true
        :param instance_types: The instance types to use for your node group. Default: t3.medium will be used according to the cloudformation document.
        :param labels: The Kubernetes labels to be applied to the nodes in the node group when they are created. Default: - None
        :param launch_template_spec: Launch template specification used for the nodegroup. Default: - no launch template
        :param max_size: The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default. Default: - same as desiredSize property
        :param max_unavailable: The maximum number of nodes unavailable at once during a version update. Nodes will be updated in parallel. The maximum number is 100. This value or ``maxUnavailablePercentage`` is required to have a value for custom update configurations to be applied. Default: 1
        :param max_unavailable_percentage: The maximum percentage of nodes unavailable during a version update. This percentage of nodes will be updated in parallel, up to 100 nodes at once. This value or ``maxUnavailable`` is required to have a value for custom update configurations to be applied. Default: undefined - node groups will update instances one at a time
        :param min_size: The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than or equal to zero. Default: 1
        :param nodegroup_name: Name of the Nodegroup. Default: - resource ID
        :param node_role: The IAM role to associate with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. Default: - None. Auto-generated if not specified.
        :param release_version: The AMI version of the Amazon EKS-optimized AMI to use with your node group (for example, ``1.14.7-YYYYMMDD``). Default: - The latest available AMI version for the node group's current Kubernetes version is used.
        :param remote_access: The remote access (SSH) configuration to use with your node group. Disabled by default, however, if you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0) Default: - disabled
        :param removal_policy: The removal policy applied to the managed node group resources. The removal policy controls what happens to the resource if it stops being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        :param subnets: The subnets to use for the Auto Scaling group that is created for your node group. By specifying the SubnetSelection, the selected subnets will automatically apply required tags i.e. ``kubernetes.io/cluster/CLUSTER_NAME`` with a value of ``shared``, where ``CLUSTER_NAME`` is replaced with the name of your cluster. Default: - private subnets
        :param tags: The metadata to apply to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets. Default: None
        :param taints: The Kubernetes taints to be applied to the nodes in the node group when they are created. Default: - None

        :see: https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a4456e32631812058cf82a0e416af17860a6096439d0ab0ecaa57c3dc3e5fa)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = NodegroupOptions(
            ami_type=ami_type,
            capacity_type=capacity_type,
            desired_size=desired_size,
            disk_size=disk_size,
            enable_node_auto_repair=enable_node_auto_repair,
            force_update=force_update,
            instance_types=instance_types,
            labels=labels,
            launch_template_spec=launch_template_spec,
            max_size=max_size,
            max_unavailable=max_unavailable,
            max_unavailable_percentage=max_unavailable_percentage,
            min_size=min_size,
            nodegroup_name=nodegroup_name,
            node_role=node_role,
            release_version=release_version,
            remote_access=remote_access,
            removal_policy=removal_policy,
            subnets=subnets,
            tags=tags,
            taints=taints,
        )

        return typing.cast("Nodegroup", jsii.invoke(self, "addNodegroupCapacity", [id, options]))

    @jsii.member(jsii_name="addServiceAccount")
    def add_service_account(
        self,
        id: builtins.str,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        identity_type: typing.Optional["IdentityType"] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        overwrite_service_account: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> "ServiceAccount":
        '''Creates a new service account with corresponding IAM Role (IRSA).

        :param id: -
        :param annotations: Additional annotations of the service account. Default: - no additional annotations
        :param identity_type: The identity type to use for the service account. Default: IdentityType.IRSA
        :param labels: Additional labels of the service account. Default: - no additional labels
        :param name: The name of the service account. The name of a ServiceAccount object must be a valid DNS subdomain name. https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ Default: - If no name is given, it will use the id of the resource.
        :param namespace: The namespace of the service account. All namespace names must be valid RFC 1123 DNS labels. https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#namespaces-and-dns Default: "default"
        :param overwrite_service_account: Overwrite existing service account. If this is set, we will use ``kubectl apply`` instead of ``kubectl create`` when the service account is created. Otherwise, if there is already a service account in the cluster with the same name, the operation will fail. Default: false
        :param removal_policy: The removal policy applied to the service account resources. The removal policy controls what happens to the resources if they stop being managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it - The stack is deleted, so CloudFormation stops managing all resources in it Default: RemovalPolicy.DESTROY
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0552883a4f6cd67a9f3ae1baab5b90fa768da6acf35f6b483553285e9044481)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ServiceAccountOptions(
            annotations=annotations,
            identity_type=identity_type,
            labels=labels,
            name=name,
            namespace=namespace,
            overwrite_service_account=overwrite_service_account,
            removal_policy=removal_policy,
        )

        return typing.cast("ServiceAccount", jsii.invoke(self, "addServiceAccount", [id, options]))

    @jsii.member(jsii_name="connectAutoScalingGroupCapacity")
    def connect_auto_scaling_group_capacity(
        self,
        auto_scaling_group: "_AutoScalingGroup_c547a7b9",
        *,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[typing.Union["BootstrapOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        machine_image_type: typing.Optional["MachineImageType"] = None,
    ) -> None:
        '''Connect capacity in the form of an existing AutoScalingGroup to the EKS cluster.

        The AutoScalingGroup must be running an EKS-optimized AMI containing the
        /etc/eks/bootstrap.sh script. This method will configure Security Groups,
        add the right policies to the instance role, apply the right tags, and add
        the required user data to the instance's launch configuration.

        Prefer to use ``addAutoScalingGroupCapacity`` if possible.

        :param auto_scaling_group: [disable-awslint:ref-via-interface].
        :param bootstrap_enabled: Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: Allows options for node bootstrapping through EC2 user data. Default: - default options
        :param machine_image_type: Allow options to specify different machine image type. Default: MachineImageType.AMAZON_LINUX_2

        :see: https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__771327d0ee286335b091dcbf106e6a370539275cdd1b1b98eb7a45a62e441a35)
            check_type(argname="argument auto_scaling_group", value=auto_scaling_group, expected_type=type_hints["auto_scaling_group"])
        options = AutoScalingGroupOptions(
            bootstrap_enabled=bootstrap_enabled,
            bootstrap_options=bootstrap_options,
            machine_image_type=machine_image_type,
        )

        return typing.cast(None, jsii.invoke(self, "connectAutoScalingGroupCapacity", [auto_scaling_group, options]))

    @jsii.member(jsii_name="getIngressLoadBalancerAddress")
    def get_ingress_load_balancer_address(
        self,
        ingress_name: builtins.str,
        *,
        namespace: typing.Optional[builtins.str] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
    ) -> builtins.str:
        '''Fetch the load balancer address of an ingress backed by a load balancer.

        :param ingress_name: The name of the ingress.
        :param namespace: The namespace the service belongs to. Default: 'default'
        :param timeout: Timeout for waiting on the load balancer address. Default: Duration.minutes(5)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e98fd0757ea9554005f809fb1bc299da14609e93be94cd81c68770f0f6037ff7)
            check_type(argname="argument ingress_name", value=ingress_name, expected_type=type_hints["ingress_name"])
        options = IngressLoadBalancerAddressOptions(
            namespace=namespace, timeout=timeout
        )

        return typing.cast(builtins.str, jsii.invoke(self, "getIngressLoadBalancerAddress", [ingress_name, options]))

    @jsii.member(jsii_name="getServiceLoadBalancerAddress")
    def get_service_load_balancer_address(
        self,
        service_name: builtins.str,
        *,
        namespace: typing.Optional[builtins.str] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
    ) -> builtins.str:
        '''Fetch the load balancer address of a service of type 'LoadBalancer'.

        :param service_name: The name of the service.
        :param namespace: The namespace the service belongs to. Default: 'default'
        :param timeout: Timeout for waiting on the load balancer address. Default: Duration.minutes(5)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa784877540d0a561de8adb59e0f66a109778d755a0a136cd88cb66db0391bd)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        options = ServiceLoadBalancerAddressOptions(
            namespace=namespace, timeout=timeout
        )

        return typing.cast(builtins.str, jsii.invoke(self, "getServiceLoadBalancerAddress", [service_name, options]))

    @jsii.member(jsii_name="grantAccess")
    def grant_access(
        self,
        id: builtins.str,
        principal: builtins.str,
        access_policies: typing.Sequence["IAccessPolicy"],
        *,
        access_entry_type: typing.Optional["AccessEntryType"] = None,
    ) -> None:
        '''Grants the specified IAM principal access to the EKS cluster based on the provided access policies.

        This method creates an ``AccessEntry`` construct that grants the specified IAM principal the access permissions
        defined by the provided ``IAccessPolicy`` array. This allows the IAM principal to perform the actions permitted
        by the access policies within the EKS cluster.
        [disable-awslint:no-grants]

        :param id: - The ID of the ``AccessEntry`` construct to be created.
        :param principal: - The IAM principal (role or user) to be granted access to the EKS cluster.
        :param access_policies: - An array of ``IAccessPolicy`` objects that define the access permissions to be granted to the IAM principal.
        :param access_entry_type: The type of the access entry. Specify ``AccessEntryType.EC2`` for EKS Auto Mode node roles, ``AccessEntryType.HYBRID_LINUX`` for EKS Hybrid Nodes, or ``AccessEntryType.HYPERPOD_LINUX`` for SageMaker HyperPod. Note that EC2, HYBRID_LINUX, and HYPERPOD_LINUX types cannot have access policies attached per AWS EKS API constraints. Default: AccessEntryType.STANDARD - Standard access entry type that supports access policies
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a0a8e7a571e2d83fe0d653283d5619dd0847a4feb02f24e52dfd6078c5e5dc8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
        options = GrantAccessOptions(access_entry_type=access_entry_type)

        return typing.cast(None, jsii.invoke(self, "grantAccess", [id, principal, access_policies, options]))

    @jsii.member(jsii_name="grantClusterAdmin")
    def grant_cluster_admin(
        self,
        id: builtins.str,
        principal: builtins.str,
    ) -> "AccessEntry":
        '''Grants the specified IAM principal cluster admin access to the EKS cluster.

        This method creates an ``AccessEntry`` construct that grants the specified IAM principal the cluster admin
        access permissions. This allows the IAM principal to perform the actions permitted
        by the cluster admin acces.
        [disable-awslint:no-grants]

        :param id: - The ID of the ``AccessEntry`` construct to be created.
        :param principal: - The IAM principal (role or user) to be granted access to the EKS cluster.

        :return: the access entry construct
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d480c5ad2387465de28d5136d3a881e299c84073a5087876691da85adb81c52)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        return typing.cast("AccessEntry", jsii.invoke(self, "grantClusterAdmin", [id, principal]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''The AWS generated ARN for the Cluster resource.

        For example, ``arn:aws:eks:us-west-2:666666666666:cluster/prod``
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @builtins.property
    @jsii.member(jsii_name="clusterCertificateAuthorityData")
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''The certificate-authority-data for your cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterCertificateAuthorityData"))

    @builtins.property
    @jsii.member(jsii_name="clusterEncryptionConfigKeyArn")
    def cluster_encryption_config_key_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) or alias of the customer master key (CMK).'''
        return typing.cast(builtins.str, jsii.get(self, "clusterEncryptionConfigKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        '''The endpoint URL for the Cluster.

        This is the URL inside the kubeconfig file to use with kubectl

        For example, ``https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com``
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The Name of the created EKS Cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property
    @jsii.member(jsii_name="clusterOpenIdConnectIssuerUrl")
    def cluster_open_id_connect_issuer_url(self) -> builtins.str:
        '''If this cluster is kubectl-enabled, returns the OpenID Connect issuer url.

        If this cluster is not kubectl-enabled (i.e. uses the
        stock ``CfnCluster``), this is ``undefined``.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterOpenIdConnectIssuerUrl"))

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "_ClusterReference_d6e6b9ff":
        '''A reference to a Cluster resource.'''
        return typing.cast("_ClusterReference_d6e6b9ff", jsii.get(self, "clusterRef"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroup")
    def cluster_security_group(self) -> "_ISecurityGroup_acf8a799":
        '''The cluster security group that was created by Amazon EKS for the cluster.'''
        return typing.cast("_ISecurityGroup_acf8a799", jsii.get(self, "clusterSecurityGroup"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> builtins.str:
        '''The id of the cluster security group that was created by Amazon EKS for the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterSecurityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> "_Connections_0f31fce8":
        '''Manages connection rules (Security Group Rules) for the cluster.

        :memberof: Cluster
        :type: {ec2.Connections}
        '''
        return typing.cast("_Connections_0f31fce8", jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProvider")
    def open_id_connect_provider(self) -> "_IOpenIdConnectProvider_203f0793":
        '''An ``OpenIdConnectProvider`` resource associated with this cluster, and which can be used to link this cluster to AWS IAM.

        A provider will only be defined if this property is accessed (lazy initialization).
        '''
        return typing.cast("_IOpenIdConnectProvider_203f0793", jsii.get(self, "openIdConnectProvider"))

    @builtins.property
    @jsii.member(jsii_name="prune")
    def prune(self) -> builtins.bool:
        '''Determines if Kubernetes resources can be pruned automatically.'''
        return typing.cast(builtins.bool, jsii.get(self, "prune"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> "_IRole_235f5d8e":
        '''IAM role assumed by the EKS Control Plane.'''
        return typing.cast("_IRole_235f5d8e", jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "_IVpc_f30d5663":
        '''The VPC in which this Cluster was created.'''
        return typing.cast("_IVpc_f30d5663", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="albController")
    def alb_controller(self) -> typing.Optional["AlbController"]:
        '''The ALB Controller construct defined for this cluster.

        Will be undefined if ``albController`` wasn't configured.
        '''
        return typing.cast(typing.Optional["AlbController"], jsii.get(self, "albController"))

    @builtins.property
    @jsii.member(jsii_name="defaultCapacity")
    def default_capacity(self) -> typing.Optional["_AutoScalingGroup_c547a7b9"]:
        '''The auto scaling group that hosts the default capacity for this cluster.

        This will be ``undefined`` if the ``defaultCapacityType`` is not ``EC2`` or
        ``defaultCapacityType`` is ``EC2`` but default capacity is set to 0.
        '''
        return typing.cast(typing.Optional["_AutoScalingGroup_c547a7b9"], jsii.get(self, "defaultCapacity"))

    @builtins.property
    @jsii.member(jsii_name="defaultNodegroup")
    def default_nodegroup(self) -> typing.Optional["Nodegroup"]:
        '''The node group that hosts the default capacity for this cluster.

        This will be ``undefined`` if the ``defaultCapacityType`` is ``EC2`` or
        ``defaultCapacityType`` is ``NODEGROUP`` but default capacity is set to 0.
        '''
        return typing.cast(typing.Optional["Nodegroup"], jsii.get(self, "defaultNodegroup"))

    @builtins.property
    @jsii.member(jsii_name="eksPodIdentityAgent")
    def eks_pod_identity_agent(self) -> typing.Optional["IAddon"]:
        '''Retrieves the EKS Pod Identity Agent addon for the EKS cluster.

        The EKS Pod Identity Agent is responsible for managing the temporary credentials
        used by pods in the cluster to access AWS resources. It runs as a DaemonSet on
        each node and provides the necessary credentials to the pods based on their
        associated service account.
        '''
        return typing.cast(typing.Optional["IAddon"], jsii.get(self, "eksPodIdentityAgent"))

    @builtins.property
    @jsii.member(jsii_name="ipFamily")
    def ip_family(self) -> typing.Optional["IpFamily"]:
        '''Specify which IP family is used to assign Kubernetes pod and service IP addresses.

        :default: IpFamily.IP_V4

        :see: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html#AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily
        '''
        return typing.cast(typing.Optional["IpFamily"], jsii.get(self, "ipFamily"))

    @builtins.property
    @jsii.member(jsii_name="kubectlProvider")
    def kubectl_provider(self) -> typing.Optional["IKubectlProvider"]:
        '''KubectlProvider for issuing kubectl commands.'''
        return typing.cast(typing.Optional["IKubectlProvider"], jsii.get(self, "kubectlProvider"))


class FargateCluster(
    Cluster,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eks_v2.FargateCluster",
):
    '''Defines an EKS cluster that runs entirely on AWS Fargate.

    The cluster is created with a default Fargate Profile that matches the
    "default" and "kube-system" namespaces. You can add additional profiles using
    ``addFargateProfile``.

    :exampleMetadata: infused

    Example::

        cluster = eks.FargateCluster(self, "FargateCluster",
            version=eks.KubernetesVersion.V1_34
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        default_profile: typing.Optional[typing.Union["FargateProfileOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        version: "KubernetesVersion",
        alb_controller: typing.Optional[typing.Union["AlbControllerOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_logging: typing.Optional[typing.Sequence["ClusterLoggingTypes"]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        core_dns_compute_type: typing.Optional["CoreDnsComputeType"] = None,
        endpoint_access: typing.Optional["EndpointAccess"] = None,
        ip_family: typing.Optional["IpFamily"] = None,
        kubectl_provider_options: typing.Optional[typing.Union["KubectlProviderOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        masters_role: typing.Optional["_IRole_235f5d8e"] = None,
        prune: typing.Optional[builtins.bool] = None,
        remote_node_networks: typing.Optional[typing.Sequence[typing.Union["RemoteNodeNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        remote_pod_networks: typing.Optional[typing.Sequence[typing.Union["RemotePodNetwork", typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
        role: typing.Optional["_IRole_235f5d8e"] = None,
        secrets_encryption_key: typing.Optional["_IKeyRef_d4fc6ef3"] = None,
        security_group: typing.Optional["_ISecurityGroup_acf8a799"] = None,
        service_ipv4_cidr: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc: typing.Optional["_IVpc_f30d5663"] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union["_SubnetSelection_e57d76df", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default_profile: Fargate Profile to create along with the cluster. Default: - A profile called "default" with 'default' and 'kube-system' selectors will be created if this is left undefined.
        :param version: The Kubernetes version to run in the cluster.
        :param alb_controller: Install the AWS Load Balancer Controller onto the cluster. Default: - The controller is not installed.
        :param cluster_logging: The cluster log types which you want to enable. Default: - none
        :param cluster_name: Name for the cluster. Default: - Automatically generated name
        :param core_dns_compute_type: Controls the "eks.amazonaws.com/compute-type" annotation in the CoreDNS configuration on your cluster to determine which compute type to use for CoreDNS. Default: CoreDnsComputeType.EC2 (for ``FargateCluster`` the default is FARGATE)
        :param endpoint_access: Configure access to the Kubernetes API server endpoint.. Default: EndpointAccess.PUBLIC_AND_PRIVATE
        :param ip_family: Specify which IP family is used to assign Kubernetes pod and service IP addresses. Default: IpFamily.IP_V4
        :param kubectl_provider_options: Options for creating the kubectl provider - a lambda function that executes ``kubectl`` and ``helm`` against the cluster. If defined, ``kubectlLayer`` is a required property. Default: - kubectl provider will not be created
        :param masters_role: An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - no masters role.
        :param prune: Indicates whether Kubernetes resources added through ``addManifest()`` can be automatically pruned. When this is enabled (default), prune labels will be allocated and injected to each resource. These labels will then be used when issuing the ``kubectl apply`` operation with the ``--prune`` switch. Default: true
        :param remote_node_networks: IPv4 CIDR blocks defining the expected address range of hybrid nodes that will join the cluster. Default: - none
        :param remote_pod_networks: IPv4 CIDR blocks for Pods running Kubernetes webhooks on hybrid nodes. Default: - none
        :param removal_policy: The removal policy applied to all CloudFormation resources created by this construct when they are no longer managed by CloudFormation. This can happen in one of three situations: - The resource is removed from the template, so CloudFormation stops managing it; - A change to the resource is made that requires it to be replaced, so CloudFormation stops managing it; - The stack is deleted, so CloudFormation stops managing all resources in it. This affects the EKS cluster itself, associated IAM roles, node groups, security groups, VPC and any other CloudFormation resources managed by this construct. Default: - Resources will be deleted.
        :param role: Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param secrets_encryption_key: KMS secret for envelope encryption for Kubernetes secrets. Default: - By default, Kubernetes stores all secret object data within etcd and all etcd volumes used by Amazon EKS are encrypted at the disk-level using AWS-Managed encryption keys.
        :param security_group: Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param service_ipv4_cidr: The CIDR block to assign Kubernetes service IP addresses from. Default: - Kubernetes assigns addresses from either the 10.100.0.0/16 or 172.20.0.0/16 CIDR blocks
        :param tags: The tags assigned to the EKS cluster. Default: - none
        :param vpc: The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: Where to place EKS Control Plane ENIs. For example, to only select private subnets, supply the following: ``vpcSubnets: [{ subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS }]`` Default: - All public and private subnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a57d359552bec9f56bfd2ab32f38ac52a4ec61ae9a0fb389cdf4cb3245d48296)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FargateClusterProps(
            default_profile=default_profile,
            version=version,
            alb_controller=alb_controller,
            cluster_logging=cluster_logging,
            cluster_name=cluster_name,
            core_dns_compute_type=core_dns_compute_type,
            endpoint_access=endpoint_access,
            ip_family=ip_family,
            kubectl_provider_options=kubectl_provider_options,
            masters_role=masters_role,
            prune=prune,
            remote_node_networks=remote_node_networks,
            remote_pod_networks=remote_pod_networks,
            removal_policy=removal_policy,
            role=role,
            secrets_encryption_key=secrets_encryption_key,
            security_group=security_group,
            service_ipv4_cidr=service_ipv4_cidr,
            tags=tags,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="defaultProfile")
    def default_profile(self) -> "FargateProfile":
        '''Fargate Profile that was created with the cluster.'''
        return typing.cast("FargateProfile", jsii.get(self, "defaultProfile"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.IngressLoadBalancerAddressOptions",
    jsii_struct_bases=[ServiceLoadBalancerAddressOptions],
    name_mapping={"namespace": "namespace", "timeout": "timeout"},
)
class IngressLoadBalancerAddressOptions(ServiceLoadBalancerAddressOptions):
    def __init__(
        self,
        *,
        namespace: typing.Optional[builtins.str] = None,
        timeout: typing.Optional["_Duration_4839e8c3"] = None,
    ) -> None:
        '''Options for fetching an IngressLoadBalancerAddress.

        :param namespace: The namespace the service belongs to. Default: 'default'
        :param timeout: Timeout for waiting on the load balancer address. Default: Duration.minutes(5)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_eks_v2 as eks_v2
            
            ingress_load_balancer_address_options = eks_v2.IngressLoadBalancerAddressOptions(
                namespace="namespace",
                timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a948ced8e6435857118472eef7f15a6176366338511e8d547896d86be919f9)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if namespace is not None:
            self._values["namespace"] = namespace
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace the service belongs to.

        :default: 'default'
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional["_Duration_4839e8c3"]:
        '''Timeout for waiting on the load balancer address.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["_Duration_4839e8c3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressLoadBalancerAddressOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eks_v2.OidcProviderNativeProps",
    jsii_struct_bases=[OpenIdConnectProviderProps],
    name_mapping={"url": "url", "removal_policy": "removalPolicy"},
)
class OidcProviderNativeProps(OpenIdConnectProviderProps):
    def __init__(
        self,
        *,
        url: builtins.str,
        removal_policy: typing.Optional["_RemovalPolicy_9f93c814"] = None,
    ) -> None:
        '''Initialization properties for ``OidcProviderNative``.

        :param url: The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You can find your OIDC Issuer URL by: aws eks describe-cluster --name %cluster_name% --query "cluster.identity.oidc.issuer" --output text
        :param removal_policy: The removal policy to apply to the OpenID Connect Provider. Default: - RemovalPolicy.DESTROY

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            
            # or create a new one using an existing issuer url
            # issuer_url: str
            
            from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer
            
            # you can import an existing provider
            provider = eks.OidcProviderNative.from_oidc_provider_arn(self, "Provider", "arn:aws:iam::123456:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/AB123456ABC")
            provider2 = eks.OidcProviderNative(self, "Provider",
                url=issuer_url
            )
            
            cluster = eks.Cluster.from_cluster_attributes(self, "MyCluster",
                cluster_name="Cluster",
                open_id_connect_provider=provider,
                kubectl_provider_options=eks.KubectlProviderOptions(
                    kubectl_layer=KubectlV35Layer(self, "kubectl")
                )
            )
            
            service_account = cluster.add_service_account("MyServiceAccount")
            
            bucket = s3.Bucket(self, "Bucket")
            bucket.grant_read_write(service_account)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6047d8b2c619283b6ba31c9b2b3e7432baed68657d69d1e9341732d37c0298f8)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL of the identity provider.

        The URL must begin with https:// and
        should correspond to the iss claim in the provider's OpenID Connect ID
        tokens. Per the OIDC standard, path components are allowed but query
        parameters are not. Typically the URL consists of only a hostname, like
        https://server.example.org or https://example.com.

        You can find your OIDC Issuer URL by:
        aws eks describe-cluster --name %cluster_name% --query "cluster.identity.oidc.issuer" --output text
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["_RemovalPolicy_9f93c814"]:
        '''The removal policy to apply to the OpenID Connect Provider.

        :default: - RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["_RemovalPolicy_9f93c814"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OidcProviderNativeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessEntry",
    "AccessEntryAttributes",
    "AccessEntryProps",
    "AccessEntryType",
    "AccessPolicy",
    "AccessPolicyArn",
    "AccessPolicyNameOptions",
    "AccessPolicyProps",
    "AccessScope",
    "AccessScopeType",
    "Addon",
    "AddonAttributes",
    "AddonProps",
    "AlbController",
    "AlbControllerOptions",
    "AlbControllerProps",
    "AlbControllerVersion",
    "AlbScheme",
    "AutoScalingGroupCapacityOptions",
    "AutoScalingGroupOptions",
    "BootstrapOptions",
    "CapacityType",
    "Cluster",
    "ClusterAttributes",
    "ClusterCommonOptions",
    "ClusterLoggingTypes",
    "ClusterProps",
    "ComputeConfig",
    "CoreDnsComputeType",
    "CpuArch",
    "DefaultCapacityType",
    "EksOptimizedImage",
    "EksOptimizedImageProps",
    "EndpointAccess",
    "FargateCluster",
    "FargateClusterProps",
    "FargateProfile",
    "FargateProfileOptions",
    "FargateProfileProps",
    "GrantAccessOptions",
    "HelmChart",
    "HelmChartOptions",
    "HelmChartProps",
    "IAccessEntry",
    "IAccessPolicy",
    "IAddon",
    "ICluster",
    "IKubectlProvider",
    "INodegroup",
    "IdentityType",
    "IngressLoadBalancerAddressOptions",
    "IpFamily",
    "KubectlProvider",
    "KubectlProviderAttributes",
    "KubectlProviderOptions",
    "KubectlProviderProps",
    "KubernetesManifest",
    "KubernetesManifestOptions",
    "KubernetesManifestProps",
    "KubernetesObjectValue",
    "KubernetesObjectValueProps",
    "KubernetesPatch",
    "KubernetesPatchProps",
    "KubernetesVersion",
    "LaunchTemplateSpec",
    "MachineImageType",
    "NodeType",
    "Nodegroup",
    "NodegroupAmiType",
    "NodegroupOptions",
    "NodegroupProps",
    "NodegroupRemoteAccess",
    "OidcProviderNative",
    "OidcProviderNativeProps",
    "OpenIdConnectProvider",
    "OpenIdConnectProviderProps",
    "PatchType",
    "RemoteNodeNetwork",
    "RemotePodNetwork",
    "Selector",
    "ServiceAccount",
    "ServiceAccountOptions",
    "ServiceAccountProps",
    "ServiceLoadBalancerAddressOptions",
    "TaintEffect",
    "TaintSpec",
]

publication.publish()

def _typecheckingstub__74ff0d4e31fc232f50ec6deba77cb81f4fb5845640f58041046e6014a98f5349(
    *,
    access_entry_arn: builtins.str,
    access_entry_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41ffcd9c9b81f2eb3b57e856565badd460fd76ba6e94407016e97fbe71e2e93(
    *,
    access_policies: typing.Sequence[IAccessPolicy],
    cluster: ICluster,
    principal: builtins.str,
    access_entry_name: typing.Optional[builtins.str] = None,
    access_entry_type: typing.Optional[AccessEntryType] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a237b0f2cfab19d79117494ac74e6238ff1b3f480722f7397495ec42935073(
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d82653df0194bb22dd76fc4eece2e78a6f4587af11e18bfb3e9af007005ec909(
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff1b0b387fb8027e6aac0f02cc65e0f2374f9905525c8e2820653e0a2e86ab0(
    *,
    access_scope_type: AccessScopeType,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8865fa4a16d35049e4c14ad235632b968637b3b2ef3009b51b8dbb010dcbaaf(
    *,
    access_scope: typing.Union[AccessScope, typing.Dict[builtins.str, typing.Any]],
    policy: AccessPolicyArn,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f22be5c9e99863839d12fee0ecae363a8a609eb9205801f3ace86534f407e3(
    *,
    type: AccessScopeType,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ada43f0a3b31dd320bd9eff13550c1f471682e5b0bda0a274f68a371bb6d87(
    *,
    addon_name: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d11ec069708c7b4208a323d8379cab46576729e75eb29e4c9e64df4e798fd88(
    *,
    addon_name: builtins.str,
    cluster: ICluster,
    addon_version: typing.Optional[builtins.str] = None,
    configuration_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    preserve_on_delete: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de1a5fab31e27ea56ec8314431ac439667aa7b3a5634280a9817f052982292c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: Cluster,
    version: AlbControllerVersion,
    additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    policy: typing.Any = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d1cff94c29713e5c5b7bb7ba2b00b4278e38ed60ba8a6db024eea79b759762(
    scope: _constructs_77d1e7e8.Construct,
    *,
    cluster: Cluster,
    version: AlbControllerVersion,
    additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    policy: typing.Any = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc3b82a59d8b4ad560f5757657e3397afe031e63d197ae8f3fc25327bece995d(
    *,
    version: AlbControllerVersion,
    additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    policy: typing.Any = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cde38e59a61de7f0bc23764fca6ef8ffc2d9c2007d5c7c13a0350fb7761eeb0(
    *,
    version: AlbControllerVersion,
    additional_helm_chart_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    policy: typing.Any = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
    cluster: Cluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5bc4c0842880bd155fb4ca89e2ad6bd5ba51c35fef2f63867918ecb8a1264c(
    version: builtins.str,
    helm_chart_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391f701643a31c9041c2732176c0e9385d97aecf409a768988a75f2f7fbb1f00(
    *,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    associate_public_ip_address: typing.Optional[builtins.bool] = None,
    auto_scaling_group_name: typing.Optional[builtins.str] = None,
    az_capacity_distribution_strategy: typing.Optional[_CapacityDistributionStrategy_2393ccfe] = None,
    block_devices: typing.Optional[typing.Sequence[typing.Union[_BlockDevice_0cfc0568, typing.Dict[builtins.str, typing.Any]]]] = None,
    capacity_rebalance: typing.Optional[builtins.bool] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    default_instance_warmup: typing.Optional[_Duration_4839e8c3] = None,
    deletion_protection: typing.Optional[_DeletionProtection_3beb1830] = None,
    desired_capacity: typing.Optional[jsii.Number] = None,
    group_metrics: typing.Optional[typing.Sequence[_GroupMetrics_7cdf729b]] = None,
    health_check: typing.Optional[_HealthCheck_03a4bd5a] = None,
    health_checks: typing.Optional[_HealthChecks_b8757873] = None,
    ignore_unmodified_size_properties: typing.Optional[builtins.bool] = None,
    instance_monitoring: typing.Optional[_Monitoring_50020f91] = None,
    key_name: typing.Optional[builtins.str] = None,
    key_pair: typing.Optional[_IKeyPair_bc344eda] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    max_instance_lifetime: typing.Optional[_Duration_4839e8c3] = None,
    min_capacity: typing.Optional[jsii.Number] = None,
    new_instances_protected_from_scale_in: typing.Optional[builtins.bool] = None,
    notifications: typing.Optional[typing.Sequence[typing.Union[_NotificationConfiguration_d5911670, typing.Dict[builtins.str, typing.Any]]]] = None,
    signals: typing.Optional[_Signals_69fbeb6e] = None,
    spot_price: typing.Optional[builtins.str] = None,
    ssm_session_permissions: typing.Optional[builtins.bool] = None,
    termination_policies: typing.Optional[typing.Sequence[_TerminationPolicy_89633c56]] = None,
    termination_policy_custom_lambda_function_arn: typing.Optional[builtins.str] = None,
    update_policy: typing.Optional[_UpdatePolicy_6dffc7ca] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_type: _InstanceType_f64915b9,
    bootstrap_enabled: typing.Optional[builtins.bool] = None,
    bootstrap_options: typing.Optional[typing.Union[BootstrapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    machine_image_type: typing.Optional[MachineImageType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f16f190b231b77037d63293668740b1890c84350977259ca756c2b3af690340d(
    *,
    bootstrap_enabled: typing.Optional[builtins.bool] = None,
    bootstrap_options: typing.Optional[typing.Union[BootstrapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    machine_image_type: typing.Optional[MachineImageType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f904654a5122c1c4508d0b1f4fa276f73d101ec61bed458657477c6cfcad2d89(
    *,
    additional_args: typing.Optional[builtins.str] = None,
    aws_api_retry_attempts: typing.Optional[jsii.Number] = None,
    dns_cluster_ip: typing.Optional[builtins.str] = None,
    docker_config_json: typing.Optional[builtins.str] = None,
    enable_docker_bridge: typing.Optional[builtins.bool] = None,
    kubelet_extra_args: typing.Optional[builtins.str] = None,
    use_max_pods: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e301df415ba7f56900494427b4c395a0ce6d0961cc773754d28d465ecf3b45(
    *,
    cluster_name: builtins.str,
    cluster_certificate_authority_data: typing.Optional[builtins.str] = None,
    cluster_encryption_config_key_arn: typing.Optional[builtins.str] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    cluster_security_group_id: typing.Optional[builtins.str] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider: typing.Optional[IKubectlProvider] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    open_id_connect_provider: typing.Optional[_IOpenIdConnectProvider_203f0793] = None,
    prune: typing.Optional[builtins.bool] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a5ef28766020ab8c83202e5d6dffbece016846b78ba995db3af04cf02e999e(
    *,
    version: KubernetesVersion,
    alb_controller: typing.Optional[typing.Union[AlbControllerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_logging: typing.Optional[typing.Sequence[ClusterLoggingTypes]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    core_dns_compute_type: typing.Optional[CoreDnsComputeType] = None,
    endpoint_access: typing.Optional[EndpointAccess] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    masters_role: typing.Optional[_IRole_235f5d8e] = None,
    prune: typing.Optional[builtins.bool] = None,
    remote_node_networks: typing.Optional[typing.Sequence[typing.Union[RemoteNodeNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    remote_pod_networks: typing.Optional[typing.Sequence[typing.Union[RemotePodNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    secrets_encryption_key: typing.Optional[_IKeyRef_d4fc6ef3] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    service_ipv4_cidr: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf0bb0ee5c6865eff515f2fc338ed96f254860f01b55add3f4ea50523d692c0(
    *,
    version: KubernetesVersion,
    alb_controller: typing.Optional[typing.Union[AlbControllerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_logging: typing.Optional[typing.Sequence[ClusterLoggingTypes]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    core_dns_compute_type: typing.Optional[CoreDnsComputeType] = None,
    endpoint_access: typing.Optional[EndpointAccess] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    masters_role: typing.Optional[_IRole_235f5d8e] = None,
    prune: typing.Optional[builtins.bool] = None,
    remote_node_networks: typing.Optional[typing.Sequence[typing.Union[RemoteNodeNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    remote_pod_networks: typing.Optional[typing.Sequence[typing.Union[RemotePodNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    secrets_encryption_key: typing.Optional[_IKeyRef_d4fc6ef3] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    service_ipv4_cidr: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
    bootstrap_cluster_creator_admin_permissions: typing.Optional[builtins.bool] = None,
    bootstrap_self_managed_addons: typing.Optional[builtins.bool] = None,
    compute: typing.Optional[typing.Union[ComputeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    default_capacity: typing.Optional[jsii.Number] = None,
    default_capacity_instance: typing.Optional[_InstanceType_f64915b9] = None,
    default_capacity_type: typing.Optional[DefaultCapacityType] = None,
    output_config_command: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f2276433261f643c13b2562a74d200173c371ac395d946bc5b30974e539c3d8(
    *,
    node_pools: typing.Optional[typing.Sequence[builtins.str]] = None,
    node_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2738ba90423201fc12883e08866d0a856feb778d505f172858bfbbce5d08710c(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d6369fc46cff5c9662be35163e7c703248821b956be42141437e81db12dcda(
    *,
    cpu_arch: typing.Optional[CpuArch] = None,
    kubernetes_version: typing.Optional[builtins.str] = None,
    node_type: typing.Optional[NodeType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1c8b1b01f47532094dca60e427081322eba78c5885128cf95f25557e7132e2(
    *cidr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3435de412248a83f43d99c9de5759414e7750a3260fc08dd8d1d5a7b64555d3(
    *,
    version: KubernetesVersion,
    alb_controller: typing.Optional[typing.Union[AlbControllerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_logging: typing.Optional[typing.Sequence[ClusterLoggingTypes]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    core_dns_compute_type: typing.Optional[CoreDnsComputeType] = None,
    endpoint_access: typing.Optional[EndpointAccess] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    masters_role: typing.Optional[_IRole_235f5d8e] = None,
    prune: typing.Optional[builtins.bool] = None,
    remote_node_networks: typing.Optional[typing.Sequence[typing.Union[RemoteNodeNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    remote_pod_networks: typing.Optional[typing.Sequence[typing.Union[RemotePodNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    secrets_encryption_key: typing.Optional[_IKeyRef_d4fc6ef3] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    service_ipv4_cidr: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_profile: typing.Optional[typing.Union[FargateProfileOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff1441149066c392d795ca95a53178129d4e20453a143b0f47b7798a83079d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: Cluster,
    selectors: typing.Sequence[typing.Union[Selector, typing.Dict[builtins.str, typing.Any]]],
    fargate_profile_name: typing.Optional[builtins.str] = None,
    pod_execution_role: typing.Optional[_IRole_235f5d8e] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c42506f4872e7f1d6b355f123ba490e44a15df088f6604e95487339a45279c(
    *,
    selectors: typing.Sequence[typing.Union[Selector, typing.Dict[builtins.str, typing.Any]]],
    fargate_profile_name: typing.Optional[builtins.str] = None,
    pod_execution_role: typing.Optional[_IRole_235f5d8e] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be66b2c09f65387bbc144563f27bb4e976109284f231b60f6fd8c49f0937403f(
    *,
    selectors: typing.Sequence[typing.Union[Selector, typing.Dict[builtins.str, typing.Any]]],
    fargate_profile_name: typing.Optional[builtins.str] = None,
    pod_execution_role: typing.Optional[_IRole_235f5d8e] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    cluster: Cluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e997e86fd860a978b07e581006efa6aba790e360a65c5ddbc81f5d2e030ecc6(
    *,
    access_entry_type: typing.Optional[AccessEntryType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__267bbdf92ec5bdd2c63df8ddabf0ea08b5fb246323ebab2b8602a9feb2b79dc2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: ICluster,
    atomic: typing.Optional[builtins.bool] = None,
    chart: typing.Optional[builtins.str] = None,
    chart_asset: typing.Optional[_Asset_ac2a7e61] = None,
    create_namespace: typing.Optional[builtins.bool] = None,
    namespace: typing.Optional[builtins.str] = None,
    release: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
    skip_crds: typing.Optional[builtins.bool] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    version: typing.Optional[builtins.str] = None,
    wait: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf3e52a6495d221a1058009786322c331c50f98baa602fdf09109f0f6fcffae(
    *,
    atomic: typing.Optional[builtins.bool] = None,
    chart: typing.Optional[builtins.str] = None,
    chart_asset: typing.Optional[_Asset_ac2a7e61] = None,
    create_namespace: typing.Optional[builtins.bool] = None,
    namespace: typing.Optional[builtins.str] = None,
    release: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
    skip_crds: typing.Optional[builtins.bool] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    version: typing.Optional[builtins.str] = None,
    wait: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c30fd78e20ace511773a60bd2e380e390d4d44dfd7df73a2899c789cac8234(
    *,
    atomic: typing.Optional[builtins.bool] = None,
    chart: typing.Optional[builtins.str] = None,
    chart_asset: typing.Optional[_Asset_ac2a7e61] = None,
    create_namespace: typing.Optional[builtins.bool] = None,
    namespace: typing.Optional[builtins.str] = None,
    release: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
    skip_crds: typing.Optional[builtins.bool] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    version: typing.Optional[builtins.str] = None,
    wait: typing.Optional[builtins.bool] = None,
    cluster: ICluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff83de86e871d5dc9fcf4c6adc16aedcbec2d949a716c25c5d1a2e0af94d7f97(
    id: builtins.str,
    chart: _constructs_77d1e7e8.Construct,
    *,
    ingress_alb: typing.Optional[builtins.bool] = None,
    ingress_alb_scheme: typing.Optional[AlbScheme] = None,
    prune: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    skip_validation: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e91d47c6f3469869f69fbc87b6d30081218e0b6ed8b1b7e87973df9e2d30b3(
    id: builtins.str,
    *,
    atomic: typing.Optional[builtins.bool] = None,
    chart: typing.Optional[builtins.str] = None,
    chart_asset: typing.Optional[_Asset_ac2a7e61] = None,
    create_namespace: typing.Optional[builtins.bool] = None,
    namespace: typing.Optional[builtins.str] = None,
    release: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
    skip_crds: typing.Optional[builtins.bool] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    version: typing.Optional[builtins.str] = None,
    wait: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c0500823c7aaca8f20a0f9333fed3477a09d69b911373e1dd9617cb7278018(
    id: builtins.str,
    *manifest: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390d49561f44f1197bf5781d054e03a9acb2c7981e79c9c146a535451ecf40fb(
    id: builtins.str,
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    identity_type: typing.Optional[IdentityType] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c9b9d342838868cfdeecd867068960aa4fe89ce221b96f17f94b06c4b55a94(
    auto_scaling_group: _AutoScalingGroup_c547a7b9,
    *,
    bootstrap_enabled: typing.Optional[builtins.bool] = None,
    bootstrap_options: typing.Optional[typing.Union[BootstrapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    machine_image_type: typing.Optional[MachineImageType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aad34a8b7c85b8fafa3a60b89cf1904902b5f18ab4c50ae367481347e5c0b1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: ICluster,
    kubectl_layer: _ILayerVersion_5ac127c8,
    awscli_layer: typing.Optional[_ILayerVersion_5ac127c8] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    memory: typing.Optional[_Size_7b441c34] = None,
    private_subnets: typing.Optional[typing.Sequence[_ISubnet_d57d1229]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482e5705a693af11339a7f57c6d0ce81623cec9953281097e3c09cc25d2c6e62(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    service_token: builtins.str,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a426caec312e2477ccd638d41ff0271e15c86a0c62f06f464e88e5f35fd827(
    scope: _constructs_77d1e7e8.Construct,
    cluster: ICluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21826c50973a5c6583d4ccfb55d5b9e60e5b35409ed715ada3e709246e16b224(
    *,
    service_token: builtins.str,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0d43994acd7b6b330a5f26b52341ec27f5672d45b11639c9e406ad65a2134b(
    *,
    kubectl_layer: _ILayerVersion_5ac127c8,
    awscli_layer: typing.Optional[_ILayerVersion_5ac127c8] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    memory: typing.Optional[_Size_7b441c34] = None,
    private_subnets: typing.Optional[typing.Sequence[_ISubnet_d57d1229]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a433dab330d6710bafea4cc09c474eaf4b60af830112e448baa510723d19b0(
    *,
    kubectl_layer: _ILayerVersion_5ac127c8,
    awscli_layer: typing.Optional[_ILayerVersion_5ac127c8] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    memory: typing.Optional[_Size_7b441c34] = None,
    private_subnets: typing.Optional[typing.Sequence[_ISubnet_d57d1229]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    cluster: ICluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5040cd237de4e6fc90ec31d3e3edb50c772a93243db6531802592e7373b932b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: ICluster,
    manifest: typing.Sequence[typing.Mapping[builtins.str, typing.Any]],
    overwrite: typing.Optional[builtins.bool] = None,
    ingress_alb: typing.Optional[builtins.bool] = None,
    ingress_alb_scheme: typing.Optional[AlbScheme] = None,
    prune: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    skip_validation: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb02dba7044365540f72d0cdd546ff96bc7d51d55d23bc2f13b1602b77b3734(
    *,
    ingress_alb: typing.Optional[builtins.bool] = None,
    ingress_alb_scheme: typing.Optional[AlbScheme] = None,
    prune: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    skip_validation: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b1104d99f875c1e3595711967bbe93c6dca0a6e48899bd3786b16d96bc081e(
    *,
    ingress_alb: typing.Optional[builtins.bool] = None,
    ingress_alb_scheme: typing.Optional[AlbScheme] = None,
    prune: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    skip_validation: typing.Optional[builtins.bool] = None,
    cluster: ICluster,
    manifest: typing.Sequence[typing.Mapping[builtins.str, typing.Any]],
    overwrite: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45f73303333592eb76ce2a3a47eb5689f5004712eb9ba9a363083fb711cf2050(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: ICluster,
    json_path: builtins.str,
    object_name: builtins.str,
    object_type: builtins.str,
    object_namespace: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f882ca78f612b80a326720db025bad0ee81c47fc3567e1271454c15f2ee3fa(
    *,
    cluster: ICluster,
    json_path: builtins.str,
    object_name: builtins.str,
    object_type: builtins.str,
    object_namespace: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6806e924d7a4b33fb6deb2187dcdc1e376243c3bb4967bd6a7ff20b64bdb4db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    apply_patch: typing.Mapping[builtins.str, typing.Any],
    cluster: ICluster,
    resource_name: builtins.str,
    restore_patch: typing.Mapping[builtins.str, typing.Any],
    patch_type: typing.Optional[PatchType] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    resource_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fa21e33c8b472af1142c651e669720614ef910d6bc6a0336c7e991204fa178(
    *,
    apply_patch: typing.Mapping[builtins.str, typing.Any],
    cluster: ICluster,
    resource_name: builtins.str,
    restore_patch: typing.Mapping[builtins.str, typing.Any],
    patch_type: typing.Optional[PatchType] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    resource_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211c05e2b989920cd028cf1837789e382429a04d153f1b5b0732ecaf3371f95f(
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__919b48dd57d86167f698cb29b3fa37433baaee3793d480304f510cdb323fce9e(
    *,
    id: builtins.str,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62af457a65949e7033d40a53d059be3f6f3a3197f4447681ec062c631bc964ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: ICluster,
    ami_type: typing.Optional[NodegroupAmiType] = None,
    capacity_type: typing.Optional[CapacityType] = None,
    desired_size: typing.Optional[jsii.Number] = None,
    disk_size: typing.Optional[jsii.Number] = None,
    enable_node_auto_repair: typing.Optional[builtins.bool] = None,
    force_update: typing.Optional[builtins.bool] = None,
    instance_types: typing.Optional[typing.Sequence[_InstanceType_f64915b9]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    launch_template_spec: typing.Optional[typing.Union[LaunchTemplateSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    max_unavailable: typing.Optional[jsii.Number] = None,
    max_unavailable_percentage: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    nodegroup_name: typing.Optional[builtins.str] = None,
    node_role: typing.Optional[_IRole_235f5d8e] = None,
    release_version: typing.Optional[builtins.str] = None,
    remote_access: typing.Optional[typing.Union[NodegroupRemoteAccess, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    taints: typing.Optional[typing.Sequence[typing.Union[TaintSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca1cb07c5679916253432bb99ab031e94ff8995b6ab160a4d865c1df5203357c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    nodegroup_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4520b68206945b2bfc48c1a6979416f811423e6b7e7b4d017c5b38dfb0d8373e(
    *,
    ami_type: typing.Optional[NodegroupAmiType] = None,
    capacity_type: typing.Optional[CapacityType] = None,
    desired_size: typing.Optional[jsii.Number] = None,
    disk_size: typing.Optional[jsii.Number] = None,
    enable_node_auto_repair: typing.Optional[builtins.bool] = None,
    force_update: typing.Optional[builtins.bool] = None,
    instance_types: typing.Optional[typing.Sequence[_InstanceType_f64915b9]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    launch_template_spec: typing.Optional[typing.Union[LaunchTemplateSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    max_unavailable: typing.Optional[jsii.Number] = None,
    max_unavailable_percentage: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    nodegroup_name: typing.Optional[builtins.str] = None,
    node_role: typing.Optional[_IRole_235f5d8e] = None,
    release_version: typing.Optional[builtins.str] = None,
    remote_access: typing.Optional[typing.Union[NodegroupRemoteAccess, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    taints: typing.Optional[typing.Sequence[typing.Union[TaintSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1960828ed0ec52107f2f9d815f5a9edf404b27e19b18ae5dd39b8d5f38f2f8e5(
    *,
    ami_type: typing.Optional[NodegroupAmiType] = None,
    capacity_type: typing.Optional[CapacityType] = None,
    desired_size: typing.Optional[jsii.Number] = None,
    disk_size: typing.Optional[jsii.Number] = None,
    enable_node_auto_repair: typing.Optional[builtins.bool] = None,
    force_update: typing.Optional[builtins.bool] = None,
    instance_types: typing.Optional[typing.Sequence[_InstanceType_f64915b9]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    launch_template_spec: typing.Optional[typing.Union[LaunchTemplateSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    max_unavailable: typing.Optional[jsii.Number] = None,
    max_unavailable_percentage: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    nodegroup_name: typing.Optional[builtins.str] = None,
    node_role: typing.Optional[_IRole_235f5d8e] = None,
    release_version: typing.Optional[builtins.str] = None,
    remote_access: typing.Optional[typing.Union[NodegroupRemoteAccess, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    taints: typing.Optional[typing.Sequence[typing.Union[TaintSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster: ICluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f1a56f6e96e735d5421faf302c657e51d067f57405e3a52e02c2f52f620d47(
    *,
    ssh_key_name: builtins.str,
    source_security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333791b35901664482ab20cd991b904afd4d2ad97fd70d1c8a62237d7f23a02a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    url: builtins.str,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d280f100f41eedf34f0f60af882d5409886185cb49189b059dc5cc7858c939d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    url: builtins.str,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3317e0858986f20bc5c548ba58b06e82f8e811e2391f01fe2a8895a53fb685ba(
    *,
    url: builtins.str,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c060c74a741aec691d27fd934a073aeffa7738efbbf9113e88ed3349b6a279(
    *,
    cidrs: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c743e611c57394e9752c982811b7678e60ad528d7877cf8ac6ded60a7fae0a77(
    *,
    cidrs: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c29fc574d38fe5b57bd3a9de52666c5ff0e4d6562893c6ff6e42979ba509600d(
    *,
    namespace: builtins.str,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbaca7b824d909d3e2050c970ff90499375d66f7b3e45708d6e7a0fbb0c1c234(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: ICluster,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    identity_type: typing.Optional[IdentityType] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc56e7f7009940bf1de62a180e0cb83ac26149eff91c8ceac6aa4b5c0ebfd12a(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429486a7c95ed32e038b64ea6b7c83b33565be6e03880fde330aa75f4c68270f(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e60561f7a296f4bf04de0a0c27864a64f49c57d5f2b96cec52694275414918(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    identity_type: typing.Optional[IdentityType] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdefc85ea927da26d0db8cbc6fa377f201aba1199d5be6929397306c347f4e4(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    identity_type: typing.Optional[IdentityType] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    cluster: ICluster,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f079932823e7c1d90e7a61b8ff67d830b157fa4dc704dbe055655ed3112ca23e(
    *,
    namespace: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f2601666139771d5c99f22c408f43ba115a6e7e103efba0fc905c49b8ca186(
    *,
    effect: typing.Optional[TaintEffect] = None,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdc6127073e756efdb5d14c617b09700f48d54838b27dab13b99f6ee8c7b5c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_policies: typing.Sequence[IAccessPolicy],
    cluster: ICluster,
    principal: builtins.str,
    access_entry_name: typing.Optional[builtins.str] = None,
    access_entry_type: typing.Optional[AccessEntryType] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5843ba949e2e8e70c545c57e323a169a136e1233a3d21e876a127fb80d7723(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_entry_arn: builtins.str,
    access_entry_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c74254cbfe0119312b0ccd27b5e4874f7973e094484a1ec1bce54f003b0cc97(
    new_access_policies: typing.Sequence[IAccessPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ee335ba80e25dde88caafff066ca29c64b71a4600a48104897072f72f9b127c(
    policy_name: builtins.str,
    *,
    access_scope_type: AccessScopeType,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1b17956f5367c24e8d921a4cd124387605b548466a8c8fce1394046132a5b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    addon_name: builtins.str,
    cluster: ICluster,
    addon_version: typing.Optional[builtins.str] = None,
    configuration_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    preserve_on_delete: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03634d6d2462cd98d140ea663e2e67722309b40b81399e2b79125a7dbe5e5f85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    addon_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c96efbeaaaa15433190608a29071311bab6ef9fd1c1ae38ea9936343adaebb7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    addon_name: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6792a3b69429b43c9b6b098e7633a33fb4c1fab5fd463a43797578ef02f2a82d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bootstrap_cluster_creator_admin_permissions: typing.Optional[builtins.bool] = None,
    bootstrap_self_managed_addons: typing.Optional[builtins.bool] = None,
    compute: typing.Optional[typing.Union[ComputeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    default_capacity: typing.Optional[jsii.Number] = None,
    default_capacity_instance: typing.Optional[_InstanceType_f64915b9] = None,
    default_capacity_type: typing.Optional[DefaultCapacityType] = None,
    output_config_command: typing.Optional[builtins.bool] = None,
    version: KubernetesVersion,
    alb_controller: typing.Optional[typing.Union[AlbControllerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_logging: typing.Optional[typing.Sequence[ClusterLoggingTypes]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    core_dns_compute_type: typing.Optional[CoreDnsComputeType] = None,
    endpoint_access: typing.Optional[EndpointAccess] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    masters_role: typing.Optional[_IRole_235f5d8e] = None,
    prune: typing.Optional[builtins.bool] = None,
    remote_node_networks: typing.Optional[typing.Sequence[typing.Union[RemoteNodeNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    remote_pod_networks: typing.Optional[typing.Sequence[typing.Union[RemotePodNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    secrets_encryption_key: typing.Optional[_IKeyRef_d4fc6ef3] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    service_ipv4_cidr: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67bdcedf04f32c2e8ab4570349cea73b300650eaf17d233e89978d8ec9050f96(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    cluster_certificate_authority_data: typing.Optional[builtins.str] = None,
    cluster_encryption_config_key_arn: typing.Optional[builtins.str] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    cluster_security_group_id: typing.Optional[builtins.str] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider: typing.Optional[IKubectlProvider] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    open_id_connect_provider: typing.Optional[_IOpenIdConnectProvider_203f0793] = None,
    prune: typing.Optional[builtins.bool] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fab71b237eae49d14717c1b7a52d3a7624193c66fd44df3bd384e2bde905f091(
    id: builtins.str,
    *,
    instance_type: _InstanceType_f64915b9,
    bootstrap_enabled: typing.Optional[builtins.bool] = None,
    bootstrap_options: typing.Optional[typing.Union[BootstrapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    machine_image_type: typing.Optional[MachineImageType] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    associate_public_ip_address: typing.Optional[builtins.bool] = None,
    auto_scaling_group_name: typing.Optional[builtins.str] = None,
    az_capacity_distribution_strategy: typing.Optional[_CapacityDistributionStrategy_2393ccfe] = None,
    block_devices: typing.Optional[typing.Sequence[typing.Union[_BlockDevice_0cfc0568, typing.Dict[builtins.str, typing.Any]]]] = None,
    capacity_rebalance: typing.Optional[builtins.bool] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    default_instance_warmup: typing.Optional[_Duration_4839e8c3] = None,
    deletion_protection: typing.Optional[_DeletionProtection_3beb1830] = None,
    desired_capacity: typing.Optional[jsii.Number] = None,
    group_metrics: typing.Optional[typing.Sequence[_GroupMetrics_7cdf729b]] = None,
    health_check: typing.Optional[_HealthCheck_03a4bd5a] = None,
    health_checks: typing.Optional[_HealthChecks_b8757873] = None,
    ignore_unmodified_size_properties: typing.Optional[builtins.bool] = None,
    instance_monitoring: typing.Optional[_Monitoring_50020f91] = None,
    key_name: typing.Optional[builtins.str] = None,
    key_pair: typing.Optional[_IKeyPair_bc344eda] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    max_instance_lifetime: typing.Optional[_Duration_4839e8c3] = None,
    min_capacity: typing.Optional[jsii.Number] = None,
    new_instances_protected_from_scale_in: typing.Optional[builtins.bool] = None,
    notifications: typing.Optional[typing.Sequence[typing.Union[_NotificationConfiguration_d5911670, typing.Dict[builtins.str, typing.Any]]]] = None,
    signals: typing.Optional[_Signals_69fbeb6e] = None,
    spot_price: typing.Optional[builtins.str] = None,
    ssm_session_permissions: typing.Optional[builtins.bool] = None,
    termination_policies: typing.Optional[typing.Sequence[_TerminationPolicy_89633c56]] = None,
    termination_policy_custom_lambda_function_arn: typing.Optional[builtins.str] = None,
    update_policy: typing.Optional[_UpdatePolicy_6dffc7ca] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__616de48bb5e1449e3fd62e9a1f4fd41d7274d3c33d16a1e6df3ce6e7c5fc6a6b(
    id: builtins.str,
    chart: _constructs_77d1e7e8.Construct,
    *,
    ingress_alb: typing.Optional[builtins.bool] = None,
    ingress_alb_scheme: typing.Optional[AlbScheme] = None,
    prune: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    skip_validation: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52570681f13e680771496b920a1f3bd641b9a3a53d3b27e0173e3d902fd8e879(
    id: builtins.str,
    *,
    selectors: typing.Sequence[typing.Union[Selector, typing.Dict[builtins.str, typing.Any]]],
    fargate_profile_name: typing.Optional[builtins.str] = None,
    pod_execution_role: typing.Optional[_IRole_235f5d8e] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2efee60e4d961bc101f18bc84a5ff3a7907a13fc2a788fbd44addb7a9c86786(
    id: builtins.str,
    *,
    atomic: typing.Optional[builtins.bool] = None,
    chart: typing.Optional[builtins.str] = None,
    chart_asset: typing.Optional[_Asset_ac2a7e61] = None,
    create_namespace: typing.Optional[builtins.bool] = None,
    namespace: typing.Optional[builtins.str] = None,
    release: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository: typing.Optional[builtins.str] = None,
    skip_crds: typing.Optional[builtins.bool] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    version: typing.Optional[builtins.str] = None,
    wait: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec17920c98f2a13f6d28bdbca1d7c278377a464eac0a7bf72e843185f7165f79(
    id: builtins.str,
    *manifest: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a4456e32631812058cf82a0e416af17860a6096439d0ab0ecaa57c3dc3e5fa(
    id: builtins.str,
    *,
    ami_type: typing.Optional[NodegroupAmiType] = None,
    capacity_type: typing.Optional[CapacityType] = None,
    desired_size: typing.Optional[jsii.Number] = None,
    disk_size: typing.Optional[jsii.Number] = None,
    enable_node_auto_repair: typing.Optional[builtins.bool] = None,
    force_update: typing.Optional[builtins.bool] = None,
    instance_types: typing.Optional[typing.Sequence[_InstanceType_f64915b9]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    launch_template_spec: typing.Optional[typing.Union[LaunchTemplateSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    max_unavailable: typing.Optional[jsii.Number] = None,
    max_unavailable_percentage: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    nodegroup_name: typing.Optional[builtins.str] = None,
    node_role: typing.Optional[_IRole_235f5d8e] = None,
    release_version: typing.Optional[builtins.str] = None,
    remote_access: typing.Optional[typing.Union[NodegroupRemoteAccess, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    taints: typing.Optional[typing.Sequence[typing.Union[TaintSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0552883a4f6cd67a9f3ae1baab5b90fa768da6acf35f6b483553285e9044481(
    id: builtins.str,
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    identity_type: typing.Optional[IdentityType] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    overwrite_service_account: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771327d0ee286335b091dcbf106e6a370539275cdd1b1b98eb7a45a62e441a35(
    auto_scaling_group: _AutoScalingGroup_c547a7b9,
    *,
    bootstrap_enabled: typing.Optional[builtins.bool] = None,
    bootstrap_options: typing.Optional[typing.Union[BootstrapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    machine_image_type: typing.Optional[MachineImageType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e98fd0757ea9554005f809fb1bc299da14609e93be94cd81c68770f0f6037ff7(
    ingress_name: builtins.str,
    *,
    namespace: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa784877540d0a561de8adb59e0f66a109778d755a0a136cd88cb66db0391bd(
    service_name: builtins.str,
    *,
    namespace: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0a8e7a571e2d83fe0d653283d5619dd0847a4feb02f24e52dfd6078c5e5dc8(
    id: builtins.str,
    principal: builtins.str,
    access_policies: typing.Sequence[IAccessPolicy],
    *,
    access_entry_type: typing.Optional[AccessEntryType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d480c5ad2387465de28d5136d3a881e299c84073a5087876691da85adb81c52(
    id: builtins.str,
    principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a57d359552bec9f56bfd2ab32f38ac52a4ec61ae9a0fb389cdf4cb3245d48296(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_profile: typing.Optional[typing.Union[FargateProfileOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    version: KubernetesVersion,
    alb_controller: typing.Optional[typing.Union[AlbControllerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_logging: typing.Optional[typing.Sequence[ClusterLoggingTypes]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    core_dns_compute_type: typing.Optional[CoreDnsComputeType] = None,
    endpoint_access: typing.Optional[EndpointAccess] = None,
    ip_family: typing.Optional[IpFamily] = None,
    kubectl_provider_options: typing.Optional[typing.Union[KubectlProviderOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    masters_role: typing.Optional[_IRole_235f5d8e] = None,
    prune: typing.Optional[builtins.bool] = None,
    remote_node_networks: typing.Optional[typing.Sequence[typing.Union[RemoteNodeNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    remote_pod_networks: typing.Optional[typing.Sequence[typing.Union[RemotePodNetwork, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    secrets_encryption_key: typing.Optional[_IKeyRef_d4fc6ef3] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    service_ipv4_cidr: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a948ced8e6435857118472eef7f15a6176366338511e8d547896d86be919f9(
    *,
    namespace: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6047d8b2c619283b6ba31c9b2b3e7432baed68657d69d1e9341732d37c0298f8(
    *,
    url: builtins.str,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessEntry, IAccessPolicy, IAddon, ICluster, IKubectlProvider, INodegroup]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
