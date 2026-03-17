r'''
<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
-->

# cdk-nag

[![PyPI version](https://img.shields.io/pypi/v/cdk-nag)](https://pypi.org/project/cdk-nag/)
[![npm version](https://img.shields.io/npm/v/cdk-nag)](https://www.npmjs.com/package/cdk-nag)
[![Maven version](https://img.shields.io/maven-central/v/io.github.cdklabs/cdknag)](https://search.maven.org/search?q=a:cdknag)
[![NuGet version](https://img.shields.io/nuget/v/Cdklabs.CdkNag)](https://www.nuget.org/packages/Cdklabs.CdkNag)
[![Go version](https://img.shields.io/github/go-mod/go-version/cdklabs/cdk-nag-go?color=blue&filename=cdknag%2Fgo.mod)](https://github.com/cdklabs/cdk-nag-go)

[![View on Construct Hub](https://constructs.dev/badge?package=cdk-nag)](https://constructs.dev/packages/cdk-nag)

Check CDK applications or [CloudFormation templates](#using-on-cloudformation-templates) for best practices using a combination of available rule packs. Inspired by [cfn_nag](https://github.com/stelligent/cfn_nag).

Check out [this blog post](https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/) for a guided overview!

![demo](cdk_nag.gif)

## Available Rules and Packs

See [RULES](./RULES.md) for more information on all the available packs.

1. [AWS Solutions](./RULES.md#awssolutions)
2. [HIPAA Security](./RULES.md#hipaa-security)
3. [NIST 800-53 rev 4](./RULES.md#nist-800-53-rev-4)
4. [NIST 800-53 rev 5](./RULES.md#nist-800-53-rev-5)
5. [PCI DSS 3.2.1](./RULES.md#pci-dss-321)
6. [Serverless](./RULES.md#serverless)

[RULES](./RULES.md) also includes a collection of [additional rules](./RULES.md#additional-rules) that are not currently included in any of the pre-built NagPacks, but are still available for inclusion in custom NagPacks.

Read the [NagPack developer docs](./docs/NagPack.md) if you are interested in creating your own pack.

## Usage

For a full list of options See `NagPackProps` in the [API.md](./API.md#struct-nagpackprops)

<details>
<summary>Including in an application</summary>

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
// Simple rule informational messages using the AWS Solutions Rule pack
Aspects.of(app).add(new AwsSolutionsChecks());
// Multiple rule packs can be run against the same app
Aspects.of(app).add(new NIST80053R5Checks());
// Additional explanations on the purpose of triggered rules
// Aspects.of(stack).add(new AwsSolutionsChecks({ verbose: true }));
```

</details>

## Suppressing a Rule

<details>
  <summary>Example 1) Default Construct</summary>

```python
import { SecurityGroup, Vpc, Peer, Port } from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const test = new SecurityGroup(this, 'test', {
      vpc: new Vpc(this, 'vpc'),
    });
    test.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    NagSuppressions.addResourceSuppressions(test, [
      { id: 'AwsSolutions-EC23', reason: 'lorem ipsum' },
    ]);
  }
}
```

</details><details>
  <summary>Example 2) On Multiple Constructs</summary>

```python
import { SecurityGroup, Vpc, Peer, Port } from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const vpc = new Vpc(this, 'vpc');
    const test1 = new SecurityGroup(this, 'test', { vpc });
    test1.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    const test2 = new SecurityGroup(this, 'test', { vpc });
    test2.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    NagSuppressions.addResourceSuppressions(
      [test1, test2],
      [{ id: 'AwsSolutions-EC23', reason: 'lorem ipsum' }]
    );
  }
}
```

</details><details>
  <summary>Example 3) Child Constructs</summary>

```python
import { User, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const user = new User(this, 'rUser');
    user.addToPolicy(
      new PolicyStatement({
        actions: ['s3:PutObject'],
        resources: ['arn:aws:s3:::bucket_name/*'],
      })
    );
    // Enable adding suppressions to child constructs
    NagSuppressions.addResourceSuppressions(
      user,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'lorem ipsum',
          appliesTo: ['Resource::arn:aws:s3:::bucket_name/*'], // optional
        },
      ],
      true
    );
  }
}
```

</details><details>
  <summary>Example 4) Stack Level </summary>

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks, NagSuppressions } from 'cdk-nag';

const app = new App();
const stack = new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(new AwsSolutionsChecks());
NagSuppressions.addStackSuppressions(stack, [
  { id: 'AwsSolutions-EC23', reason: 'lorem ipsum' },
]);
```

</details><details>
  <summary>Example 5) Construct path</summary>

If you received the following error on synth/deploy

```bash
[Error at /StackName/Custom::CDKBucketDeployment8675309/ServiceRole/Resource] AwsSolutions-IAM4: The IAM user, role, or group uses AWS managed policies
```

```python
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { BucketDeployment } from 'aws-cdk-lib/aws-s3-deployment';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new BucketDeployment(this, 'rDeployment', {
      sources: [],
      destinationBucket: Bucket.fromBucketName(this, 'rBucket', 'foo'),
    });
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/StackName/Custom::CDKBucketDeployment8675309/ServiceRole/Resource',
      [{ id: 'AwsSolutions-IAM4', reason: 'at least 10 characters' }]
    );
  }
}
```

</details><details>
  <summary>Example 6) Granular Suppressions of findings</summary>

Certain rules support granular suppressions of `findings`. If you received the following errors on synth/deploy

```bash
[Error at /StackName/rFirstUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Action::s3:*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
[Error at /StackName/rFirstUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Resource::*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
[Error at /StackName/rSecondUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Action::s3:*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
[Error at /StackName/rSecondUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Resource::*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
```

By applying the following suppressions

```python
import { User } from 'aws-cdk-lib/aws-iam';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const firstUser = new User(this, 'rFirstUser');
    firstUser.addToPolicy(
      new PolicyStatement({
        actions: ['s3:*'],
        resources: ['*'],
      })
    );
    const secondUser = new User(this, 'rSecondUser');
    secondUser.addToPolicy(
      new PolicyStatement({
        actions: ['s3:*'],
        resources: ['*'],
      })
    );
    const thirdUser = new User(this, 'rSecondUser');
    thirdUser.addToPolicy(
      new PolicyStatement({
        actions: ['sqs:CreateQueue'],
        resources: [`arn:aws:sqs:${this.region}:${this.account}:*`],
      })
    );
    NagSuppressions.addResourceSuppressions(
      firstUser,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason:
            "Only suppress AwsSolutions-IAM5 's3:*' finding on First User.",
          appliesTo: ['Action::s3:*'],
        },
      ],
      true
    );
    NagSuppressions.addResourceSuppressions(
      secondUser,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'Suppress all AwsSolutions-IAM5 findings on Second User.',
        },
      ],
      true
    );
    NagSuppressions.addResourceSuppressions(
      thirdUser,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'Suppress AwsSolutions-IAM5 on the SQS resource.',
          appliesTo: [
            {
              regex: '/^Resource::arn:aws:sqs:(.*):\\*$/g',
            },
          ],
        },
      ],
      true
    );
  }
}
```

You would see the following error on synth/deploy

```bash
[Error at /StackName/rFirstUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Resource::*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
```

</details>

## Suppressing Rule Validation Failures

When a rule validation fails it is handled similarly to a rule violation, and can be suppressed in the same manner. The `ID` for a rule failure is `CdkNagValidationFailure`.

If a rule is suppressed in a non-granular manner (i.e. `appliesTo` is not set, see example 1 above) then validation failures on that rule are also suppressed.

Validation failure suppression respects any applied [Suppression Ignore Conditions](#conditionally-ignoring-suppressions)

<details>
  <summary>Example 1) Suppress all Validation Failures on a Resource</summary>

```python
import { SecurityGroup, Vpc, Peer, Port } from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const test = new SecurityGroup(this, 'test', {
      vpc: new Vpc(this, 'vpc'),
    });
    test.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    NagSuppressions.addResourceSuppressions(test, [
      { id: 'CdkNagValidationFailure', reason: 'lorem ipsum' },
    ]);
  }
}
```

</details><details>
  <summary>Example 2) Granular Suppression of Validation Failures</summary>
Validation failures can be suppressed for individual rules by using `appliesTo` to list the desired rules

```python
import { SecurityGroup, Vpc, Peer, Port } from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const test = new SecurityGroup(this, 'test', {
      vpc: new Vpc(this, 'vpc'),
    });
    test.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    NagSuppressions.addResourceSuppressions(test, [
      {
        id: 'CdkNagValidationFailure',
        reason: 'lorem ipsum',
        appliesTo: ['AwsSolutions-L1'],
      },
    ]);
  }
}
```

</details>

## Suppressing `aws-cdk-lib/pipelines` Violations

The [aws-cdk-lib/pipelines.CodePipeline](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.pipelines.CodePipeline.html) construct and its child constructs are not guaranteed to be "Visited" by `Aspects`, as they are not added during the "Construction" phase of the [cdk lifecycle](https://docs.aws.amazon.com/cdk/v2/guide/apps.html#lifecycle). Because of this behavior, you may experience problems such as rule violations not appearing or the inability to suppress violations on these constructs.

You can remediate these rule violation and suppression problems by forcing the pipeline construct creation forward by calling `.buildPipeline()` on your `CodePipeline` object. Otherwise you may see errors such as:

```
Error: Suppression path "/this/construct/path" did not match any resource. This can occur when a resource does not exist or if a suppression is applied before a resource is created.
```

See [this issue](https://github.com/aws/aws-cdk/issues/18440) for more information.

<details>
  <summary>Example) Suppressing Violations in Pipelines</summary>

`example-app.ts`

```python
import { App, Aspects } from 'aws-cdk-lib';
import { AwsSolutionsChecks } from 'cdk-nag';
import { ExamplePipeline } from '../lib/example-pipeline';

const app = new App();
new ExamplePipeline(app, 'example-cdk-pipeline');
Aspects.of(app).add(new AwsSolutionsChecks({ verbose: true }));
app.synth();
```

`example-pipeline.ts`

```python
import { Stack, StackProps } from 'aws-cdk-lib';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import {
  CodePipeline,
  CodePipelineSource,
  ShellStep,
} from 'aws-cdk-lib/pipelines';
import { NagSuppressions } from 'cdk-nag';
import { Construct } from 'constructs';

export class ExamplePipeline extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const exampleSynth = new ShellStep('ExampleSynth', {
      commands: ['yarn build --frozen-lockfile'],
      input: CodePipelineSource.codeCommit(
        new Repository(this, 'ExampleRepo', { repositoryName: 'ExampleRepo' }),
        'main'
      ),
    });

    const ExamplePipeline = new CodePipeline(this, 'ExamplePipeline', {
      synth: exampleSynth,
    });

    // Force the pipeline construct creation forward before applying suppressions.
    // @See https://github.com/aws/aws-cdk/issues/18440
    ExamplePipeline.buildPipeline();

    // The path suppression will error if you comment out "ExamplePipeline.buildPipeline();""
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/example-cdk-pipeline/ExamplePipeline/Pipeline/ArtifactsBucket/Resource',
      [
        {
          id: 'AwsSolutions-S1',
          reason: 'Because I said so',
        },
      ]
    );
  }
}
```

</details>

## Rules and Property Overrides

In some cases L2 Constructs do not have a native option to remediate an issue and must be fixed via [Raw Overrides](https://docs.aws.amazon.com/cdk/latest/guide/cfn_layer.html#cfn_layer_raw). Since raw overrides take place after template synthesis these fixes are not caught by cdk-nag. In this case you should remediate the issue and suppress the issue like in the following example.

<details>
  <summary>Example) Property Overrides</summary>

```python
import {
  Instance,
  InstanceType,
  InstanceClass,
  MachineImage,
  Vpc,
  CfnInstance,
} from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const instance = new Instance(this, 'rInstance', {
      vpc: new Vpc(this, 'rVpc'),
      instanceType: new InstanceType(InstanceClass.T3),
      machineImage: MachineImage.latestAmazonLinux(),
    });
    const cfnIns = instance.node.defaultChild as CfnInstance;
    cfnIns.addPropertyOverride('DisableApiTermination', true);
    NagSuppressions.addResourceSuppressions(instance, [
      {
        id: 'AwsSolutions-EC29',
        reason: 'Remediated through property override.',
      },
    ]);
  }
}
```

</details>

## Conditionally Ignoring Suppressions

You can optionally create a condition that prevents certain rules from being suppressed. You can create conditions for any variety of reasons. Examples include a condition that always ignores a suppression, a condition that ignores a suppression based on the date, a condition that ignores a suppression based on the reason. You can read [the developer docs](./docs/IgnoreSuppressionConditions.md) for more information on creating your own conditions.

<details>
  <summary>Example) Using the pre-built `SuppressionIgnoreErrors` class to ignore suppressions on any `Error` level rules.</summary>

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks, SuppressionIgnoreErrors } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
// Ignore Suppressions on any errors
Aspects.of(app).add(
  new AwsSolutionsChecks({
    suppressionIgnoreCondition: new SuppressionIgnoreErrors(),
  })
);
```

</details>

## Customizing Logging

`NagLogger`s give `NagPack` authors and users the ability to create their own custom reporting mechanisms. All pre-built `NagPacks`come with the `AnnotationsLogger`and the `NagReportLogger` (with CSV reports) enabled by default.

See the [NagLogger](./docs/NagLogger.md) developer docs for more information.

<details>
  <summary>Example) Adding the `ExtremelyHelpfulConsoleLogger` example from the NagLogger docs</summary>

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { ExtremelyHelpfulConsoleLogger } from './docs/NagLogger';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(
  new AwsSolutionsChecks({
    additionalLoggers: [new ExtremelyHelpfulConsoleLogger()],
  })
);
```

</details>

## Using on CloudFormation templates

You can use cdk-nag on existing CloudFormation templates by using the [cloudformation-include](https://docs.aws.amazon.com/cdk/latest/guide/use-cfn-template.html#use-cfn-template-import) module.

<details>
  <summary>Example 1) CloudFormation template with suppression</summary>

Sample CloudFormation template with suppression

```json
{
  "Resources": {
    "rBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "some-bucket-name"
      },
      "Metadata": {
        "cdk_nag": {
          "rules_to_suppress": [
            {
              "id": "AwsSolutions-S1",
              "reason": "at least 10 characters"
            }
          ]
        }
      }
    }
  }
}
```

Sample App

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(new AwsSolutionsChecks());
```

Sample Stack with imported template

```python
import { CfnInclude } from 'aws-cdk-lib/cloudformation-include';
import { NagSuppressions } from 'cdk-nag';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new CfnInclude(this, 'Template', {
      templateFile: 'my-template.json',
    });
    // Add any additional suppressions
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/CdkNagDemo/Template/rBucket',
      [
        {
          id: 'AwsSolutions-S2',
          reason: 'at least 10 characters',
        },
      ]
    );
  }
}
```

</details><details>
  <summary>Example 2) CloudFormation template with granular suppressions</summary>

Sample CloudFormation template with suppression

```json
{
  "Resources": {
    "myPolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyDocument": {
          "Statement": [
            {
              "Action": [
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:Encrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*"
              ],
              "Effect": "Allow",
              "Resource": ["some-key-arn"]
            }
          ],
          "Version": "2012-10-17"
        }
      },
      "Metadata": {
        "cdk_nag": {
          "rules_to_suppress": [
            {
              "id": "AwsSolutions-IAM5",
              "reason": "Allow key data access",
              "applies_to": [
                "Action::kms:ReEncrypt*",
                "Action::kms:GenerateDataKey*"
              ]
            }
          ]
        }
      }
    }
  }
}
```

Sample App

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(new AwsSolutionsChecks());
```

Sample Stack with imported template

```python
import { CfnInclude } from 'aws-cdk-lib/cloudformation-include';
import { NagSuppressions } from 'cdk-nag';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new CfnInclude(this, 'Template', {
      templateFile: 'my-template.json',
    });
    // Add any additional suppressions
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/CdkNagDemo/Template/myPolicy',
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'Allow key data access',
          appliesTo: ['Action::kms:ReEncrypt*', 'Action::kms:GenerateDataKey*'],
        },
      ]
    );
  }
}
```

</details>

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## License

This project is licensed under the Apache-2.0 License.
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

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="cdk-nag.AnnotationLoggerProps",
    jsii_struct_bases=[],
    name_mapping={"log_ignores": "logIgnores", "verbose": "verbose"},
)
class AnnotationLoggerProps:
    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Props for the AnnotationLogger.

        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76f4bc63138756cb580801c06df1ac3a9c0be1a809e326eddd3933e8ccf222c)
            check_type(argname="argument log_ignores", value=log_ignores, expected_type=type_hints["log_ignores"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_ignores is not None:
            self._values["log_ignores"] = log_ignores
        if verbose is not None:
            self._values["verbose"] = verbose

    @builtins.property
    def log_ignores(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to log suppressed rule violations as informational messages (default: false).'''
        result = self._values.get("log_ignores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def verbose(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages.'''
        result = self._values.get("verbose")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnnotationLoggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk-nag.IApplyRule")
class IApplyRule(typing_extensions.Protocol):
    '''Interface for JSII interoperability for passing parameters and the Rule Callback to.

    :applyRule: method.
    '''

    @builtins.property
    @jsii.member(jsii_name="explanation")
    def explanation(self) -> builtins.str:
        '''Why the rule exists.'''
        ...

    @explanation.setter
    def explanation(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> builtins.str:
        '''Why the rule was triggered.'''
        ...

    @info.setter
    def info(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> "NagMessageLevel":
        '''The annotations message level to apply to the rule if triggered.'''
        ...

    @level.setter
    def level(self, value: "NagMessageLevel") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> _aws_cdk_ceddda9d.CfnResource:
        '''The CfnResource to check.'''
        ...

    @node.setter
    def node(self, value: _aws_cdk_ceddda9d.CfnResource) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="ignoreSuppressionCondition")
    def ignore_suppression_condition(self) -> typing.Optional["INagSuppressionIgnore"]:
        '''A condition in which a suppression should be ignored.'''
        ...

    @ignore_suppression_condition.setter
    def ignore_suppression_condition(
        self,
        value: typing.Optional["INagSuppressionIgnore"],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="ruleSuffixOverride")
    def rule_suffix_override(self) -> typing.Optional[builtins.str]:
        '''Override for the suffix of the Rule ID for this rule.'''
        ...

    @rule_suffix_override.setter
    def rule_suffix_override(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @jsii.member(jsii_name="rule")
    def rule(
        self,
        node: _aws_cdk_ceddda9d.CfnResource,
    ) -> typing.Union["NagRuleCompliance", typing.List[builtins.str]]:
        '''The callback to the rule.

        :param node: The CfnResource to check.
        '''
        ...


class _IApplyRuleProxy:
    '''Interface for JSII interoperability for passing parameters and the Rule Callback to.

    :applyRule: method.
    '''

    __jsii_type__: typing.ClassVar[str] = "cdk-nag.IApplyRule"

    @builtins.property
    @jsii.member(jsii_name="explanation")
    def explanation(self) -> builtins.str:
        '''Why the rule exists.'''
        return typing.cast(builtins.str, jsii.get(self, "explanation"))

    @explanation.setter
    def explanation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a23651ea44768b1af733a2b9cef46eced1602c3bca3849419b685c2c8fcba15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "explanation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> builtins.str:
        '''Why the rule was triggered.'''
        return typing.cast(builtins.str, jsii.get(self, "info"))

    @info.setter
    def info(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0a9865d3a20bd3ed9f672903366f8e8197ef53dddebf5ab545d1e84de2ca16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "info", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> "NagMessageLevel":
        '''The annotations message level to apply to the rule if triggered.'''
        return typing.cast("NagMessageLevel", jsii.get(self, "level"))

    @level.setter
    def level(self, value: "NagMessageLevel") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca6380ef48764f27214931f0c5bf28e44b41d002da53939e9265879e403ff9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> _aws_cdk_ceddda9d.CfnResource:
        '''The CfnResource to check.'''
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, jsii.get(self, "node"))

    @node.setter
    def node(self, value: _aws_cdk_ceddda9d.CfnResource) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__123173a6ce5be62d3f85f1d78609032a82004c4807c1cc883736375dfa93eb62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "node", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ignoreSuppressionCondition")
    def ignore_suppression_condition(self) -> typing.Optional["INagSuppressionIgnore"]:
        '''A condition in which a suppression should be ignored.'''
        return typing.cast(typing.Optional["INagSuppressionIgnore"], jsii.get(self, "ignoreSuppressionCondition"))

    @ignore_suppression_condition.setter
    def ignore_suppression_condition(
        self,
        value: typing.Optional["INagSuppressionIgnore"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9288306b38b954b918c055805151abe90063414817d3bb4674cc5456cd6e6619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreSuppressionCondition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleSuffixOverride")
    def rule_suffix_override(self) -> typing.Optional[builtins.str]:
        '''Override for the suffix of the Rule ID for this rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSuffixOverride"))

    @rule_suffix_override.setter
    def rule_suffix_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333cce877f5798931df373ac5d819b402e92f9ac723cf0184c1db35694ca67a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSuffixOverride", value) # pyright: ignore[reportArgumentType]

    @jsii.member(jsii_name="rule")
    def rule(
        self,
        node: _aws_cdk_ceddda9d.CfnResource,
    ) -> typing.Union["NagRuleCompliance", typing.List[builtins.str]]:
        '''The callback to the rule.

        :param node: The CfnResource to check.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__735fc03a45b618e514165f2e218d73e8b7084a45ea15b931267f19e67ef9e8c0)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(typing.Union["NagRuleCompliance", typing.List[builtins.str]], jsii.invoke(self, "rule", [node]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplyRule).__jsii_proxy_class__ = lambda : _IApplyRuleProxy


@jsii.interface(jsii_type="cdk-nag.INagLogger")
class INagLogger(typing_extensions.Protocol):
    '''Interface for creating NagSuppression Ignores.'''

    @jsii.member(jsii_name="onCompliance")
    def on_compliance(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource passes the compliance check for a given rule.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        ...

    @jsii.member(jsii_name="onError")
    def on_error(
        self,
        *,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance.

        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        ...

    @jsii.member(jsii_name="onNonCompliance")
    def on_non_compliance(
        self,
        *,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the the rule violation is not suppressed by the user.

        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        ...

    @jsii.member(jsii_name="onNotApplicable")
    def on_not_applicable(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule does not apply to the given CfnResource.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        ...

    @jsii.member(jsii_name="onSuppressed")
    def on_suppressed(
        self,
        *,
        suppression_reason: builtins.str,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the rule violation is suppressed by the user.

        :param suppression_reason: 
        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        ...

    @jsii.member(jsii_name="onSuppressedError")
    def on_suppressed_error(
        self,
        *,
        error_suppression_reason: builtins.str,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance and the error is suppressed.

        :param error_suppression_reason: 
        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        ...


class _INagLoggerProxy:
    '''Interface for creating NagSuppression Ignores.'''

    __jsii_type__: typing.ClassVar[str] = "cdk-nag.INagLogger"

    @jsii.member(jsii_name="onCompliance")
    def on_compliance(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource passes the compliance check for a given rule.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerComplianceData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onCompliance", [data]))

    @jsii.member(jsii_name="onError")
    def on_error(
        self,
        *,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance.

        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerErrorData(
            error_message=error_message,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onError", [data]))

    @jsii.member(jsii_name="onNonCompliance")
    def on_non_compliance(
        self,
        *,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the the rule violation is not suppressed by the user.

        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerNonComplianceData(
            finding_id=finding_id,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onNonCompliance", [data]))

    @jsii.member(jsii_name="onNotApplicable")
    def on_not_applicable(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule does not apply to the given CfnResource.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerNotApplicableData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onNotApplicable", [data]))

    @jsii.member(jsii_name="onSuppressed")
    def on_suppressed(
        self,
        *,
        suppression_reason: builtins.str,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the rule violation is suppressed by the user.

        :param suppression_reason: 
        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerSuppressedData(
            suppression_reason=suppression_reason,
            finding_id=finding_id,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onSuppressed", [data]))

    @jsii.member(jsii_name="onSuppressedError")
    def on_suppressed_error(
        self,
        *,
        error_suppression_reason: builtins.str,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance and the error is suppressed.

        :param error_suppression_reason: 
        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerSuppressedErrorData(
            error_suppression_reason=error_suppression_reason,
            error_message=error_message,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onSuppressedError", [data]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INagLogger).__jsii_proxy_class__ = lambda : _INagLoggerProxy


@jsii.interface(jsii_type="cdk-nag.INagSuppressionIgnore")
class INagSuppressionIgnore(typing_extensions.Protocol):
    '''Interface for creating NagSuppression Ignores.'''

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: "NagMessageLevel",
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        ...


class _INagSuppressionIgnoreProxy:
    '''Interface for creating NagSuppression Ignores.'''

    __jsii_type__: typing.ClassVar[str] = "cdk-nag.INagSuppressionIgnore"

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: "NagMessageLevel",
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        input = SuppressionIgnoreInput(
            finding_id=finding_id,
            reason=reason,
            resource=resource,
            rule_id=rule_id,
            rule_level=rule_level,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [input]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INagSuppressionIgnore).__jsii_proxy_class__ = lambda : _INagSuppressionIgnoreProxy


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerBaseData",
    jsii_struct_bases=[],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
    },
)
class NagLoggerBaseData:
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Shared data for all INagLogger methods.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b54447c69d32d2c5b63c99983239ae73b9f19d8fdbd1d5f8046701d890f7f5bb)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerBaseData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerComplianceData",
    jsii_struct_bases=[NagLoggerBaseData],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
    },
)
class NagLoggerComplianceData(NagLoggerBaseData):
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Data for onCompliance method of an INagLogger.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2369c97135e6d99b99884b93a52da46d2eaa508b33dd68cf3b232b4c254d8c)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerComplianceData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerErrorData",
    jsii_struct_bases=[NagLoggerBaseData],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
        "error_message": "errorMessage",
    },
)
class NagLoggerErrorData(NagLoggerBaseData):
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
        error_message: builtins.str,
    ) -> None:
        '''Data for onError method of an INagLogger.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        :param error_message: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2cdb757482fd16d0bdc5aec491ea46481898e09304e4cafb215196f81de28c0)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
            check_type(argname="argument error_message", value=error_message, expected_type=type_hints["error_message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
            "error_message": error_message,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_message(self) -> builtins.str:
        result = self._values.get("error_message")
        assert result is not None, "Required property 'error_message' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerErrorData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerNonComplianceData",
    jsii_struct_bases=[NagLoggerBaseData],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
        "finding_id": "findingId",
    },
)
class NagLoggerNonComplianceData(NagLoggerBaseData):
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
        finding_id: builtins.str,
    ) -> None:
        '''Data for onNonCompliance method of an INagLogger.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        :param finding_id: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab29e75d71ea1830fa944b3a77c3025e3a4f8a0742c89c76fbbabc2da83ebf4)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
            "finding_id": finding_id,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_id(self) -> builtins.str:
        result = self._values.get("finding_id")
        assert result is not None, "Required property 'finding_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerNonComplianceData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerNotApplicableData",
    jsii_struct_bases=[NagLoggerBaseData],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
    },
)
class NagLoggerNotApplicableData(NagLoggerBaseData):
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
    ) -> None:
        '''Data for onNotApplicable method of an INagLogger.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c26e4f355c915b68201704e8b383af3e0cea31e8f757660937a73d0473f6e8)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerNotApplicableData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerSuppressedData",
    jsii_struct_bases=[NagLoggerNonComplianceData],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
        "finding_id": "findingId",
        "suppression_reason": "suppressionReason",
    },
)
class NagLoggerSuppressedData(NagLoggerNonComplianceData):
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
        finding_id: builtins.str,
        suppression_reason: builtins.str,
    ) -> None:
        '''Data for onSuppressed method of an INagLogger.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        :param finding_id: 
        :param suppression_reason: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee145b58e321092c41a8ca75ccb9b50bd4d7b06c5b5f303b04fde0fc5335c992)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
            check_type(argname="argument suppression_reason", value=suppression_reason, expected_type=type_hints["suppression_reason"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
            "finding_id": finding_id,
            "suppression_reason": suppression_reason,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_id(self) -> builtins.str:
        result = self._values.get("finding_id")
        assert result is not None, "Required property 'finding_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def suppression_reason(self) -> builtins.str:
        result = self._values.get("suppression_reason")
        assert result is not None, "Required property 'suppression_reason' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerSuppressedData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagLoggerSuppressedErrorData",
    jsii_struct_bases=[NagLoggerErrorData],
    name_mapping={
        "nag_pack_name": "nagPackName",
        "resource": "resource",
        "rule_explanation": "ruleExplanation",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
        "rule_original_name": "ruleOriginalName",
        "error_message": "errorMessage",
        "error_suppression_reason": "errorSuppressionReason",
    },
)
class NagLoggerSuppressedErrorData(NagLoggerErrorData):
    def __init__(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: "NagMessageLevel",
        rule_original_name: builtins.str,
        error_message: builtins.str,
        error_suppression_reason: builtins.str,
    ) -> None:
        '''Data for onSuppressedError method of an INagLogger.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        :param error_message: 
        :param error_suppression_reason: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b97d7febc4da1597477e573081bfba668d6db013a81a05c0c6f6bcd4e5d15e37)
            check_type(argname="argument nag_pack_name", value=nag_pack_name, expected_type=type_hints["nag_pack_name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
            check_type(argname="argument rule_original_name", value=rule_original_name, expected_type=type_hints["rule_original_name"])
            check_type(argname="argument error_message", value=error_message, expected_type=type_hints["error_message"])
            check_type(argname="argument error_suppression_reason", value=error_suppression_reason, expected_type=type_hints["error_suppression_reason"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nag_pack_name": nag_pack_name,
            "resource": resource,
            "rule_explanation": rule_explanation,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
            "rule_original_name": rule_original_name,
            "error_message": error_message,
            "error_suppression_reason": error_suppression_reason,
        }

    @builtins.property
    def nag_pack_name(self) -> builtins.str:
        result = self._values.get("nag_pack_name")
        assert result is not None, "Required property 'nag_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_explanation(self) -> builtins.str:
        result = self._values.get("rule_explanation")
        assert result is not None, "Required property 'rule_explanation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> "NagMessageLevel":
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast("NagMessageLevel", result)

    @builtins.property
    def rule_original_name(self) -> builtins.str:
        result = self._values.get("rule_original_name")
        assert result is not None, "Required property 'rule_original_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_message(self) -> builtins.str:
        result = self._values.get("error_message")
        assert result is not None, "Required property 'error_message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_suppression_reason(self) -> builtins.str:
        result = self._values.get("error_suppression_reason")
        assert result is not None, "Required property 'error_suppression_reason' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagLoggerSuppressedErrorData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk-nag.NagMessageLevel")
class NagMessageLevel(enum.Enum):
    '''The severity level of the rule.'''

    WARN = "WARN"
    ERROR = "ERROR"
    INFO = "INFO"


@jsii.implements(_aws_cdk_ceddda9d.IAspect)
class NagPack(metaclass=jsii.JSIIAbstractClass, jsii_type="cdk-nag.NagPack"):
    '''Base class for all rule packs.'''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence["NagReportFormat"]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="applyRule")
    def _apply_rule(self, params: IApplyRule) -> None:
        '''Create a rule to be used in the NagPack.

        :param params: The.

        :IApplyRule: interface with rule details.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3628e5213d5585ace3e16109c26f8af64546c343c9014c7c1f61edad43c259e)
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
        return typing.cast(None, jsii.invoke(self, "applyRule", [params]))

    @jsii.member(jsii_name="ignoreRule")
    def _ignore_rule(
        self,
        suppressions: typing.Sequence[typing.Union["NagPackSuppression", typing.Dict[builtins.str, typing.Any]]],
        rule_id: builtins.str,
        finding_id: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        level: NagMessageLevel,
        ignore_suppression_condition: typing.Optional[INagSuppressionIgnore] = None,
        validation_failure: typing.Optional[builtins.bool] = None,
    ) -> builtins.str:
        '''Check whether a specific rule should be ignored.

        :param suppressions: The suppressions listed in the cdk-nag metadata.
        :param rule_id: The id of the rule to ignore.
        :param finding_id: The id of the finding that is being checked.
        :param resource: The resource being evaluated.
        :param level: -
        :param ignore_suppression_condition: -
        :param validation_failure: Whether the rule is being checked due to a validation failure.

        :return: The reason the rule was ignored, or an empty string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5c64d28918f6c81ac27ddb1b8fd172dcc8d60b93422df8be15366fbee92a3a)
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument ignore_suppression_condition", value=ignore_suppression_condition, expected_type=type_hints["ignore_suppression_condition"])
            check_type(argname="argument validation_failure", value=validation_failure, expected_type=type_hints["validation_failure"])
        return typing.cast(builtins.str, jsii.invoke(self, "ignoreRule", [suppressions, rule_id, finding_id, resource, level, ignore_suppression_condition, validation_failure]))

    @jsii.member(jsii_name="visit")
    @abc.abstractmethod
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="readPackName")
    def read_pack_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readPackName"))

    @builtins.property
    @jsii.member(jsii_name="loggers")
    def _loggers(self) -> typing.List[INagLogger]:
        return typing.cast(typing.List[INagLogger], jsii.get(self, "loggers"))

    @_loggers.setter
    def _loggers(self, value: typing.List[INagLogger]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5c6b891fc439b6ba962aebfd2ac3f291fad706fc0a6199ca5e2ef180a35b9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="packName")
    def _pack_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packName"))

    @_pack_name.setter
    def _pack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18633cd3423c88500a3be3035af0c083c9c2a61e7358e09d541efac11ba04ecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="packGlobalSuppressionIgnore")
    def _pack_global_suppression_ignore(self) -> typing.Optional[INagSuppressionIgnore]:
        return typing.cast(typing.Optional[INagSuppressionIgnore], jsii.get(self, "packGlobalSuppressionIgnore"))

    @_pack_global_suppression_ignore.setter
    def _pack_global_suppression_ignore(
        self,
        value: typing.Optional[INagSuppressionIgnore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__750990594a653bc50228a510fc9a05a0b77520235ef9cb34eb1dfb6e7f47b9e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packGlobalSuppressionIgnore", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userGlobalSuppressionIgnore")
    def _user_global_suppression_ignore(self) -> typing.Optional[INagSuppressionIgnore]:
        return typing.cast(typing.Optional[INagSuppressionIgnore], jsii.get(self, "userGlobalSuppressionIgnore"))

    @_user_global_suppression_ignore.setter
    def _user_global_suppression_ignore(
        self,
        value: typing.Optional[INagSuppressionIgnore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499426647076f5f9b25fa3802115f4b0187bef15fcfb86478ee847c35a15b0af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGlobalSuppressionIgnore", value) # pyright: ignore[reportArgumentType]


class _NagPackProxy(NagPack):
    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__818a0da55c5cbe0337f1efd54ed9153e54658d7d5a9a1a3d8f93e06baea87360)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, NagPack).__jsii_proxy_class__ = lambda : _NagPackProxy


@jsii.data_type(
    jsii_type="cdk-nag.NagPackProps",
    jsii_struct_bases=[],
    name_mapping={
        "additional_loggers": "additionalLoggers",
        "log_ignores": "logIgnores",
        "report_formats": "reportFormats",
        "reports": "reports",
        "suppression_ignore_condition": "suppressionIgnoreCondition",
        "verbose": "verbose",
    },
)
class NagPackProps:
    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence["NagReportFormat"]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Interface for creating a NagPack.

        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a83ce3fdb1cb0ca96a59694799f0ed3b0090f7d4e437681d969d4c74e7ddab)
            check_type(argname="argument additional_loggers", value=additional_loggers, expected_type=type_hints["additional_loggers"])
            check_type(argname="argument log_ignores", value=log_ignores, expected_type=type_hints["log_ignores"])
            check_type(argname="argument report_formats", value=report_formats, expected_type=type_hints["report_formats"])
            check_type(argname="argument reports", value=reports, expected_type=type_hints["reports"])
            check_type(argname="argument suppression_ignore_condition", value=suppression_ignore_condition, expected_type=type_hints["suppression_ignore_condition"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_loggers is not None:
            self._values["additional_loggers"] = additional_loggers
        if log_ignores is not None:
            self._values["log_ignores"] = log_ignores
        if report_formats is not None:
            self._values["report_formats"] = report_formats
        if reports is not None:
            self._values["reports"] = reports
        if suppression_ignore_condition is not None:
            self._values["suppression_ignore_condition"] = suppression_ignore_condition
        if verbose is not None:
            self._values["verbose"] = verbose

    @builtins.property
    def additional_loggers(self) -> typing.Optional[typing.List[INagLogger]]:
        '''Additional NagLoggers for logging rule validation outputs.'''
        result = self._values.get("additional_loggers")
        return typing.cast(typing.Optional[typing.List[INagLogger]], result)

    @builtins.property
    def log_ignores(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to log suppressed rule violations as informational messages (default: false).'''
        result = self._values.get("log_ignores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def report_formats(self) -> typing.Optional[typing.List["NagReportFormat"]]:
        '''If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).'''
        result = self._values.get("report_formats")
        return typing.cast(typing.Optional[typing.List["NagReportFormat"]], result)

    @builtins.property
    def reports(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).'''
        result = self._values.get("reports")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def suppression_ignore_condition(self) -> typing.Optional[INagSuppressionIgnore]:
        '''Conditionally prevent rules from being suppressed (default: no user provided condition).'''
        result = self._values.get("suppression_ignore_condition")
        return typing.cast(typing.Optional[INagSuppressionIgnore], result)

    @builtins.property
    def verbose(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).'''
        result = self._values.get("verbose")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagPackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagPackSuppression",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "reason": "reason", "applies_to": "appliesTo"},
)
class NagPackSuppression:
    def __init__(
        self,
        *,
        id: builtins.str,
        reason: builtins.str,
        applies_to: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union["RegexAppliesTo", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Interface for creating a rule suppression.

        :param id: The id of the rule to ignore.
        :param reason: The reason to ignore the rule (minimum 10 characters).
        :param applies_to: Rule specific granular suppressions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e488b05b5f3f444467d9eb46090b6726b68fa30596c2566a59974e3b5ccc5f54)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            check_type(argname="argument applies_to", value=applies_to, expected_type=type_hints["applies_to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "reason": reason,
        }
        if applies_to is not None:
            self._values["applies_to"] = applies_to

    @builtins.property
    def id(self) -> builtins.str:
        '''The id of the rule to ignore.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reason(self) -> builtins.str:
        '''The reason to ignore the rule (minimum 10 characters).'''
        result = self._values.get("reason")
        assert result is not None, "Required property 'reason' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def applies_to(
        self,
    ) -> typing.Optional[typing.List[typing.Union[builtins.str, "RegexAppliesTo"]]]:
        '''Rule specific granular suppressions.'''
        result = self._values.get("applies_to")
        return typing.cast(typing.Optional[typing.List[typing.Union[builtins.str, "RegexAppliesTo"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagPackSuppression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk-nag.NagReportFormat")
class NagReportFormat(enum.Enum):
    '''Possible output formats of the NagReport.'''

    CSV = "CSV"
    JSON = "JSON"


@jsii.data_type(
    jsii_type="cdk-nag.NagReportLine",
    jsii_struct_bases=[],
    name_mapping={
        "compliance": "compliance",
        "exception_reason": "exceptionReason",
        "resource_id": "resourceId",
        "rule_id": "ruleId",
        "rule_info": "ruleInfo",
        "rule_level": "ruleLevel",
    },
)
class NagReportLine:
    def __init__(
        self,
        *,
        compliance: builtins.str,
        exception_reason: builtins.str,
        resource_id: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: builtins.str,
    ) -> None:
        '''
        :param compliance: 
        :param exception_reason: 
        :param resource_id: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c6b6029bff770690f88c877bee0f2885b7bc043157258be4815d22b42c13364)
            check_type(argname="argument compliance", value=compliance, expected_type=type_hints["compliance"])
            check_type(argname="argument exception_reason", value=exception_reason, expected_type=type_hints["exception_reason"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compliance": compliance,
            "exception_reason": exception_reason,
            "resource_id": resource_id,
            "rule_id": rule_id,
            "rule_info": rule_info,
            "rule_level": rule_level,
        }

    @builtins.property
    def compliance(self) -> builtins.str:
        result = self._values.get("compliance")
        assert result is not None, "Required property 'compliance' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exception_reason(self) -> builtins.str:
        result = self._values.get("exception_reason")
        assert result is not None, "Required property 'exception_reason' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_info(self) -> builtins.str:
        result = self._values.get("rule_info")
        assert result is not None, "Required property 'rule_info' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> builtins.str:
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagReportLine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INagLogger)
class NagReportLogger(metaclass=jsii.JSIIMeta, jsii_type="cdk-nag.NagReportLogger"):
    '''A NagLogger that creates compliance reports.'''

    def __init__(self, *, formats: typing.Sequence[NagReportFormat]) -> None:
        '''
        :param formats: 
        '''
        props = NagReportLoggerProps(formats=formats)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="getFormatStacks")
    def get_format_stacks(self, format: NagReportFormat) -> typing.List[builtins.str]:
        '''
        :param format: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5258c45d7b5e7a57921e27dd5a7c53e00452a977e1d40530500b345f84a31167)
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getFormatStacks", [format]))

    @jsii.member(jsii_name="initializeStackReport")
    def _initialize_stack_report(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Initialize the report for the rule pack's compliance report for the resource's Stack if it doesn't exist.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerBaseData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "initializeStackReport", [data]))

    @jsii.member(jsii_name="onCompliance")
    def on_compliance(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource passes the compliance check for a given rule.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerComplianceData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onCompliance", [data]))

    @jsii.member(jsii_name="onError")
    def on_error(
        self,
        *,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance.

        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerErrorData(
            error_message=error_message,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onError", [data]))

    @jsii.member(jsii_name="onNonCompliance")
    def on_non_compliance(
        self,
        *,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the the rule violation is not suppressed by the user.

        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerNonComplianceData(
            finding_id=finding_id,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onNonCompliance", [data]))

    @jsii.member(jsii_name="onNotApplicable")
    def on_not_applicable(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule does not apply to the given CfnResource.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerNotApplicableData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onNotApplicable", [data]))

    @jsii.member(jsii_name="onSuppressed")
    def on_suppressed(
        self,
        *,
        suppression_reason: builtins.str,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the rule violation is suppressed by the user.

        :param suppression_reason: 
        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerSuppressedData(
            suppression_reason=suppression_reason,
            finding_id=finding_id,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onSuppressed", [data]))

    @jsii.member(jsii_name="onSuppressedError")
    def on_suppressed_error(
        self,
        *,
        error_suppression_reason: builtins.str,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance and the error is suppressed.

        :param error_suppression_reason: 
        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerSuppressedErrorData(
            error_suppression_reason=error_suppression_reason,
            error_message=error_message,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onSuppressedError", [data]))

    @jsii.member(jsii_name="writeToStackComplianceReport")
    def _write_to_stack_compliance_report(
        self,
        data: typing.Union[NagLoggerBaseData, typing.Dict[builtins.str, typing.Any]],
        compliance: typing.Union["NagRuleCompliance", "NagRulePostValidationStates"],
    ) -> None:
        '''
        :param data: -
        :param compliance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d05cd61c8369866bc8b8765401ea1dfa7ebede0fc2130608a36bb42a8b9448ae)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument compliance", value=compliance, expected_type=type_hints["compliance"])
        return typing.cast(None, jsii.invoke(self, "writeToStackComplianceReport", [data, compliance]))

    @builtins.property
    @jsii.member(jsii_name="formats")
    def formats(self) -> typing.List[NagReportFormat]:
        return typing.cast(typing.List[NagReportFormat], jsii.get(self, "formats"))


@jsii.data_type(
    jsii_type="cdk-nag.NagReportLoggerProps",
    jsii_struct_bases=[],
    name_mapping={"formats": "formats"},
)
class NagReportLoggerProps:
    def __init__(self, *, formats: typing.Sequence[NagReportFormat]) -> None:
        '''Props for the NagReportLogger.

        :param formats: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e3f9aa1b2e641a8748b597a0deb88e437aae2a4f34f10501ac44b0524902a1)
            check_type(argname="argument formats", value=formats, expected_type=type_hints["formats"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "formats": formats,
        }

    @builtins.property
    def formats(self) -> typing.List[NagReportFormat]:
        result = self._values.get("formats")
        assert result is not None, "Required property 'formats' is missing"
        return typing.cast(typing.List[NagReportFormat], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagReportLoggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagReportSchema",
    jsii_struct_bases=[],
    name_mapping={"lines": "lines"},
)
class NagReportSchema:
    def __init__(
        self,
        *,
        lines: typing.Sequence[typing.Union[NagReportLine, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param lines: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d13606a383c679c37ca15873660037b156e8491412ee339c74a414fb2061d8d)
            check_type(argname="argument lines", value=lines, expected_type=type_hints["lines"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lines": lines,
        }

    @builtins.property
    def lines(self) -> typing.List[NagReportLine]:
        result = self._values.get("lines")
        assert result is not None, "Required property 'lines' is missing"
        return typing.cast(typing.List[NagReportLine], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagReportSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk-nag.NagRuleCompliance")
class NagRuleCompliance(enum.Enum):
    '''The compliance level of a resource in relation to a rule.'''

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@jsii.enum(jsii_type="cdk-nag.NagRulePostValidationStates")
class NagRulePostValidationStates(enum.Enum):
    '''Additional states a rule can be in post compliance validation.'''

    SUPPRESSED = "SUPPRESSED"
    UNKNOWN = "UNKNOWN"


class NagRules(metaclass=jsii.JSIIMeta, jsii_type="cdk-nag.NagRules"):
    '''Helper class with methods for rule creation.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="resolveIfPrimitive")
    @builtins.classmethod
    def resolve_if_primitive(
        cls,
        node: _aws_cdk_ceddda9d.CfnResource,
        parameter: typing.Any,
    ) -> typing.Any:
        '''Use in cases where a primitive value must be known to pass a rule.

        https://developer.mozilla.org/en-US/docs/Glossary/Primitive

        :param node: The CfnResource to check.
        :param parameter: The value to attempt to resolve.

        :return: Return a value if resolves to a primitive data type, otherwise throw an error.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8817c32270238bf0dfc84f6218e16b587420567b5bc41a280c177f7ee6cd79f)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolveIfPrimitive", [node, parameter]))

    @jsii.member(jsii_name="resolveResourceFromInstrinsic")
    @builtins.classmethod
    def resolve_resource_from_instrinsic(
        cls,
        node: _aws_cdk_ceddda9d.CfnResource,
        parameter: typing.Any,
    ) -> typing.Any:
        '''
        :param node: The CfnResource to check.
        :param parameter: The value to attempt to resolve.

        :return: Return the Logical resource Id if resolves to a intrinsic function, otherwise the resolved provided value.

        :deprecated:

        Use resolveResourceFromIntrinsic instead

        Use in cases where a token resolves to an intrinsic function and the referenced resource must be known to pass a rule.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2af31e0e8c775eabad30b7da777a2689dbf22e8f31976bf4840dbd2cbbbf939)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolveResourceFromInstrinsic", [node, parameter]))

    @jsii.member(jsii_name="resolveResourceFromIntrinsic")
    @builtins.classmethod
    def resolve_resource_from_intrinsic(
        cls,
        node: _aws_cdk_ceddda9d.CfnResource,
        parameter: typing.Any,
    ) -> typing.Any:
        '''Use in cases where a token resolves to an intrinsic function and the referenced resource must be known to pass a rule.

        :param node: The CfnResource to check.
        :param parameter: The value to attempt to resolve.

        :return: Return the Logical resource Id if resolves to a intrinsic function, otherwise the resolved provided value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31cd67cca34b4963ea5b427552d0ed8190cf2265f4659708bb7d899d8e5fc6cb)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolveResourceFromIntrinsic", [node, parameter]))


class NagSuppressions(metaclass=jsii.JSIIMeta, jsii_type="cdk-nag.NagSuppressions"):
    '''Helper class with methods to add cdk-nag suppressions to cdk resources.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="addResourceSuppressions")
    @builtins.classmethod
    def add_resource_suppressions(
        cls,
        construct: typing.Union[_constructs_77d1e7e8.IConstruct, typing.Sequence[_constructs_77d1e7e8.IConstruct]],
        suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
        apply_to_children: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Add cdk-nag suppressions to a CfnResource and optionally its children.

        :param construct: The IConstruct(s) to apply the suppression to.
        :param suppressions: A list of suppressions to apply to the resource.
        :param apply_to_children: Apply the suppressions to children CfnResources (default:false).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a019ccc6d0325c092e9799383fe39f9bffd3785f51142f30e692e0947937f98e)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument apply_to_children", value=apply_to_children, expected_type=type_hints["apply_to_children"])
        return typing.cast(None, jsii.sinvoke(cls, "addResourceSuppressions", [construct, suppressions, apply_to_children]))

    @jsii.member(jsii_name="addResourceSuppressionsByPath")
    @builtins.classmethod
    def add_resource_suppressions_by_path(
        cls,
        stack: _aws_cdk_ceddda9d.Stack,
        path: typing.Union[builtins.str, typing.Sequence[builtins.str]],
        suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
        apply_to_children: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Add cdk-nag suppressions to a CfnResource and optionally its children via its path.

        :param stack: The Stack the construct belongs to.
        :param path: The path(s) to the construct in the provided stack.
        :param suppressions: A list of suppressions to apply to the resource.
        :param apply_to_children: Apply the suppressions to children CfnResources (default:false).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8e93f68ef8607b6e5a16388f0f7c757ce99057d7e42d5fa1c22db00da355de)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument apply_to_children", value=apply_to_children, expected_type=type_hints["apply_to_children"])
        return typing.cast(None, jsii.sinvoke(cls, "addResourceSuppressionsByPath", [stack, path, suppressions, apply_to_children]))

    @jsii.member(jsii_name="addStackSuppressions")
    @builtins.classmethod
    def add_stack_suppressions(
        cls,
        stack: _aws_cdk_ceddda9d.Stack,
        suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
        apply_to_nested_stacks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Apply cdk-nag suppressions to a Stack and optionally nested stacks.

        :param stack: The Stack to apply the suppression to.
        :param suppressions: A list of suppressions to apply to the stack.
        :param apply_to_nested_stacks: Apply the suppressions to children stacks (default:false).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5c648cedc28d10ee481b251de2f85cde16e2daf0dc2addd3e4c7860c0e5768)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument apply_to_nested_stacks", value=apply_to_nested_stacks, expected_type=type_hints["apply_to_nested_stacks"])
        return typing.cast(None, jsii.sinvoke(cls, "addStackSuppressions", [stack, suppressions, apply_to_nested_stacks]))


class PCIDSS321Checks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.PCIDSS321Checks",
):
    '''Check for PCI DSS 3.2.1 compliance. Based on the PCI DSS 3.2.1 AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-pci-dss.html.'''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813d53d45e9db3648743d0e260e058579163527ffb805ee4e7511408478be1f6)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.data_type(
    jsii_type="cdk-nag.RegexAppliesTo",
    jsii_struct_bases=[],
    name_mapping={"regex": "regex"},
)
class RegexAppliesTo:
    def __init__(self, *, regex: builtins.str) -> None:
        '''A regular expression to apply to matching findings.

        :param regex: An ECMA-262 regex string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8453471acfa85ba5ddf5a90e23aaf4fd9026a9d972c7f9445fcd249f7a656da)
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "regex": regex,
        }

    @builtins.property
    def regex(self) -> builtins.str:
        '''An ECMA-262 regex string.'''
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegexAppliesTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerlessChecks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.ServerlessChecks",
):
    '''Serverless Checks are a compilation of rules to validate infrastructure-as-code template against recommended practices.'''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45822d91dde0925f0c42dd49aa5abb9d5fd6391e1a4d49074f95718261fd8ff8)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.implements(INagSuppressionIgnore)
class SuppressionIgnoreAlways(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.SuppressionIgnoreAlways",
):
    '''Always ignore the suppression.'''

    def __init__(self, trigger_message: builtins.str) -> None:
        '''
        :param trigger_message: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa33f04446bcf1cb8a24a2c7daab296b89d9593c017b8c38f99d9a0d452fa725)
            check_type(argname="argument trigger_message", value=trigger_message, expected_type=type_hints["trigger_message"])
        jsii.create(self.__class__, self, [trigger_message])

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: NagMessageLevel,
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        _input = SuppressionIgnoreInput(
            finding_id=finding_id,
            reason=reason,
            resource=resource,
            rule_id=rule_id,
            rule_level=rule_level,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [_input]))


@jsii.implements(INagSuppressionIgnore)
class SuppressionIgnoreAnd(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.SuppressionIgnoreAnd",
):
    '''Ignore the suppression if all of the given INagSuppressionIgnore return a non-empty message.'''

    def __init__(self, *suppression_ignore_ands: INagSuppressionIgnore) -> None:
        '''
        :param suppression_ignore_ands: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d484956c8730c75e4cf6533596839557423fe7f5ea32dfb4bcbdbb05e4a2d593)
            check_type(argname="argument suppression_ignore_ands", value=suppression_ignore_ands, expected_type=typing.Tuple[type_hints["suppression_ignore_ands"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*suppression_ignore_ands])

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: NagMessageLevel,
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        input = SuppressionIgnoreInput(
            finding_id=finding_id,
            reason=reason,
            resource=resource,
            rule_id=rule_id,
            rule_level=rule_level,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [input]))


@jsii.implements(INagSuppressionIgnore)
class SuppressionIgnoreErrors(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.SuppressionIgnoreErrors",
):
    '''Ignore Suppressions for Rules with a NagMessageLevel.ERROR.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: NagMessageLevel,
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        input = SuppressionIgnoreInput(
            finding_id=finding_id,
            reason=reason,
            resource=resource,
            rule_id=rule_id,
            rule_level=rule_level,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [input]))


@jsii.data_type(
    jsii_type="cdk-nag.SuppressionIgnoreInput",
    jsii_struct_bases=[],
    name_mapping={
        "finding_id": "findingId",
        "reason": "reason",
        "resource": "resource",
        "rule_id": "ruleId",
        "rule_level": "ruleLevel",
    },
)
class SuppressionIgnoreInput:
    def __init__(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: NagMessageLevel,
    ) -> None:
        '''Information about the NagRule and the relevant NagSuppression for the INagSuppressionIgnore.

        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__375fa67002e6963901e2f6603cdb52e9d08e6110fab8ac88ea8031b4f8ca472a)
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
            check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument rule_level", value=rule_level, expected_type=type_hints["rule_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "finding_id": finding_id,
            "reason": reason,
            "resource": resource,
            "rule_id": rule_id,
            "rule_level": rule_level,
        }

    @builtins.property
    def finding_id(self) -> builtins.str:
        result = self._values.get("finding_id")
        assert result is not None, "Required property 'finding_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reason(self) -> builtins.str:
        result = self._values.get("reason")
        assert result is not None, "Required property 'reason' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> _aws_cdk_ceddda9d.CfnResource:
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_aws_cdk_ceddda9d.CfnResource, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_level(self) -> NagMessageLevel:
        result = self._values.get("rule_level")
        assert result is not None, "Required property 'rule_level' is missing"
        return typing.cast(NagMessageLevel, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SuppressionIgnoreInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INagSuppressionIgnore)
class SuppressionIgnoreNever(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.SuppressionIgnoreNever",
):
    '''Don't ignore the suppression.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: NagMessageLevel,
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        _input = SuppressionIgnoreInput(
            finding_id=finding_id,
            reason=reason,
            resource=resource,
            rule_id=rule_id,
            rule_level=rule_level,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [_input]))


@jsii.implements(INagSuppressionIgnore)
class SuppressionIgnoreOr(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.SuppressionIgnoreOr",
):
    '''Ignore the suppression if any of the given INagSuppressionIgnore return a non-empty message.'''

    def __init__(self, *or_suppression_ignores: INagSuppressionIgnore) -> None:
        '''
        :param or_suppression_ignores: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5cc605f87aed5b6dd3b4116e98aa83f86df7e8e4504b2181f2e21b03a184d2)
            check_type(argname="argument or_suppression_ignores", value=or_suppression_ignores, expected_type=typing.Tuple[type_hints["or_suppression_ignores"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*or_suppression_ignores])

    @jsii.member(jsii_name="createMessage")
    def create_message(
        self,
        *,
        finding_id: builtins.str,
        reason: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_id: builtins.str,
        rule_level: NagMessageLevel,
    ) -> builtins.str:
        '''
        :param finding_id: 
        :param reason: 
        :param resource: 
        :param rule_id: 
        :param rule_level: 
        '''
        input = SuppressionIgnoreInput(
            finding_id=finding_id,
            reason=reason,
            resource=resource,
            rule_id=rule_id,
            rule_level=rule_level,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [input]))


@jsii.implements(INagLogger)
class AnnotationLogger(metaclass=jsii.JSIIMeta, jsii_type="cdk-nag.AnnotationLogger"):
    '''A NagLogger that outputs to the CDK Annotations system.'''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages.
        '''
        props = AnnotationLoggerProps(log_ignores=log_ignores, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="createMessage")
    def _create_message(
        self,
        rule_id: builtins.str,
        finding_id: builtins.str,
        rule_info: builtins.str,
        rule_explanation: builtins.str,
        verbose: builtins.bool,
    ) -> builtins.str:
        '''
        :param rule_id: -
        :param finding_id: -
        :param rule_info: -
        :param rule_explanation: -
        :param verbose: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d27003a8b41ff976c7c6fb69915342dff77d036f488f01f27608ce64fb6fc49)
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
            check_type(argname="argument rule_info", value=rule_info, expected_type=type_hints["rule_info"])
            check_type(argname="argument rule_explanation", value=rule_explanation, expected_type=type_hints["rule_explanation"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [rule_id, finding_id, rule_info, rule_explanation, verbose]))

    @jsii.member(jsii_name="onCompliance")
    def on_compliance(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource passes the compliance check for a given rule.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        _data = NagLoggerComplianceData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onCompliance", [_data]))

    @jsii.member(jsii_name="onError")
    def on_error(
        self,
        *,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance.

        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerErrorData(
            error_message=error_message,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onError", [data]))

    @jsii.member(jsii_name="onNonCompliance")
    def on_non_compliance(
        self,
        *,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the the rule violation is not suppressed by the user.

        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerNonComplianceData(
            finding_id=finding_id,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onNonCompliance", [data]))

    @jsii.member(jsii_name="onNotApplicable")
    def on_not_applicable(
        self,
        *,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule does not apply to the given CfnResource.

        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        _data = NagLoggerNotApplicableData(
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onNotApplicable", [_data]))

    @jsii.member(jsii_name="onSuppressed")
    def on_suppressed(
        self,
        *,
        suppression_reason: builtins.str,
        finding_id: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a CfnResource does not pass the compliance check for a given rule and the rule violation is suppressed by the user.

        :param suppression_reason: 
        :param finding_id: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerSuppressedData(
            suppression_reason=suppression_reason,
            finding_id=finding_id,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onSuppressed", [data]))

    @jsii.member(jsii_name="onSuppressedError")
    def on_suppressed_error(
        self,
        *,
        error_suppression_reason: builtins.str,
        error_message: builtins.str,
        nag_pack_name: builtins.str,
        resource: _aws_cdk_ceddda9d.CfnResource,
        rule_explanation: builtins.str,
        rule_id: builtins.str,
        rule_info: builtins.str,
        rule_level: NagMessageLevel,
        rule_original_name: builtins.str,
    ) -> None:
        '''Called when a rule throws an error during while validating a CfnResource for compliance and the error is suppressed.

        :param error_suppression_reason: 
        :param error_message: 
        :param nag_pack_name: 
        :param resource: 
        :param rule_explanation: 
        :param rule_id: 
        :param rule_info: 
        :param rule_level: 
        :param rule_original_name: 
        '''
        data = NagLoggerSuppressedErrorData(
            error_suppression_reason=error_suppression_reason,
            error_message=error_message,
            nag_pack_name=nag_pack_name,
            resource=resource,
            rule_explanation=rule_explanation,
            rule_id=rule_id,
            rule_info=rule_info,
            rule_level=rule_level,
            rule_original_name=rule_original_name,
        )

        return typing.cast(None, jsii.invoke(self, "onSuppressedError", [data]))

    @builtins.property
    @jsii.member(jsii_name="logIgnores")
    def log_ignores(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "logIgnores"))

    @builtins.property
    @jsii.member(jsii_name="verbose")
    def verbose(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "verbose"))

    @builtins.property
    @jsii.member(jsii_name="suppressionId")
    def suppression_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suppressionId"))

    @suppression_id.setter
    def suppression_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e731712efd090983cf7e5c1378ce4a7f327773edbf8f7354ece70984365f5be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressionId", value) # pyright: ignore[reportArgumentType]


class AwsSolutionsChecks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.AwsSolutionsChecks",
):
    '''Check Best practices based on AWS Solutions Security Matrix.'''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96eb46c46eba3538cc66dd2f6fd176af6e483161c98c271e2da09d609cf6f32)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


class HIPAASecurityChecks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.HIPAASecurityChecks",
):
    '''Check for HIPAA Security compliance.

    Based on the HIPAA Security AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-hipaa_security.html
    '''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7befba4c0338ce825c8858ca449ed8639199c568303515244a7e215f1c28061)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


class NIST80053R4Checks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.NIST80053R4Checks",
):
    '''Check for NIST 800-53 rev 4 compliance.

    Based on the NIST 800-53 rev 4 AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-nist-800-53_rev_4.html
    '''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d900825e618c777e4d14e3b2c5357c960a024c352b9c0e3080bf762e9bef6b)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


class NIST80053R5Checks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.NIST80053R5Checks",
):
    '''Check for NIST 800-53 rev 5 compliance.

    Based on the NIST 800-53 rev 5 AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-nist-800-53_rev_5.html
    '''

    def __init__(
        self,
        *,
        additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
        log_ignores: typing.Optional[builtins.bool] = None,
        report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
        reports: typing.Optional[builtins.bool] = None,
        suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_loggers: Additional NagLoggers for logging rule validation outputs.
        :param log_ignores: Whether or not to log suppressed rule violations as informational messages (default: false).
        :param report_formats: If reports are enabled, the output formats of compliance reports in the App's output directory (default: only CSV).
        :param reports: Whether or not to generate compliance reports for applied Stacks in the App's output directory (default: true).
        :param suppression_ignore_condition: Conditionally prevent rules from being suppressed (default: no user provided condition).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(
            additional_loggers=additional_loggers,
            log_ignores=log_ignores,
            report_formats=report_formats,
            reports=reports,
            suppression_ignore_condition=suppression_ignore_condition,
            verbose=verbose,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: _constructs_77d1e7e8.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2e84fa7d4ba03aa7bf298104f9e6a7521c3facd75b8d248d072c42722ecd14)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


__all__ = [
    "AnnotationLogger",
    "AnnotationLoggerProps",
    "AwsSolutionsChecks",
    "HIPAASecurityChecks",
    "IApplyRule",
    "INagLogger",
    "INagSuppressionIgnore",
    "NIST80053R4Checks",
    "NIST80053R5Checks",
    "NagLoggerBaseData",
    "NagLoggerComplianceData",
    "NagLoggerErrorData",
    "NagLoggerNonComplianceData",
    "NagLoggerNotApplicableData",
    "NagLoggerSuppressedData",
    "NagLoggerSuppressedErrorData",
    "NagMessageLevel",
    "NagPack",
    "NagPackProps",
    "NagPackSuppression",
    "NagReportFormat",
    "NagReportLine",
    "NagReportLogger",
    "NagReportLoggerProps",
    "NagReportSchema",
    "NagRuleCompliance",
    "NagRulePostValidationStates",
    "NagRules",
    "NagSuppressions",
    "PCIDSS321Checks",
    "RegexAppliesTo",
    "ServerlessChecks",
    "SuppressionIgnoreAlways",
    "SuppressionIgnoreAnd",
    "SuppressionIgnoreErrors",
    "SuppressionIgnoreInput",
    "SuppressionIgnoreNever",
    "SuppressionIgnoreOr",
]

publication.publish()

def _typecheckingstub__c76f4bc63138756cb580801c06df1ac3a9c0be1a809e326eddd3933e8ccf222c(
    *,
    log_ignores: typing.Optional[builtins.bool] = None,
    verbose: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a23651ea44768b1af733a2b9cef46eced1602c3bca3849419b685c2c8fcba15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0a9865d3a20bd3ed9f672903366f8e8197ef53dddebf5ab545d1e84de2ca16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca6380ef48764f27214931f0c5bf28e44b41d002da53939e9265879e403ff9e(
    value: NagMessageLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123173a6ce5be62d3f85f1d78609032a82004c4807c1cc883736375dfa93eb62(
    value: _aws_cdk_ceddda9d.CfnResource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9288306b38b954b918c055805151abe90063414817d3bb4674cc5456cd6e6619(
    value: typing.Optional[INagSuppressionIgnore],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333cce877f5798931df373ac5d819b402e92f9ac723cf0184c1db35694ca67a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__735fc03a45b618e514165f2e218d73e8b7084a45ea15b931267f19e67ef9e8c0(
    node: _aws_cdk_ceddda9d.CfnResource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54447c69d32d2c5b63c99983239ae73b9f19d8fdbd1d5f8046701d890f7f5bb(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2369c97135e6d99b99884b93a52da46d2eaa508b33dd68cf3b232b4c254d8c(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2cdb757482fd16d0bdc5aec491ea46481898e09304e4cafb215196f81de28c0(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
    error_message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab29e75d71ea1830fa944b3a77c3025e3a4f8a0742c89c76fbbabc2da83ebf4(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
    finding_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c26e4f355c915b68201704e8b383af3e0cea31e8f757660937a73d0473f6e8(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee145b58e321092c41a8ca75ccb9b50bd4d7b06c5b5f303b04fde0fc5335c992(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
    finding_id: builtins.str,
    suppression_reason: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97d7febc4da1597477e573081bfba668d6db013a81a05c0c6f6bcd4e5d15e37(
    *,
    nag_pack_name: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_explanation: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: NagMessageLevel,
    rule_original_name: builtins.str,
    error_message: builtins.str,
    error_suppression_reason: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3628e5213d5585ace3e16109c26f8af64546c343c9014c7c1f61edad43c259e(
    params: IApplyRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5c64d28918f6c81ac27ddb1b8fd172dcc8d60b93422df8be15366fbee92a3a(
    suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
    rule_id: builtins.str,
    finding_id: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    level: NagMessageLevel,
    ignore_suppression_condition: typing.Optional[INagSuppressionIgnore] = None,
    validation_failure: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5c6b891fc439b6ba962aebfd2ac3f291fad706fc0a6199ca5e2ef180a35b9a(
    value: typing.List[INagLogger],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18633cd3423c88500a3be3035af0c083c9c2a61e7358e09d541efac11ba04ecf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750990594a653bc50228a510fc9a05a0b77520235ef9cb34eb1dfb6e7f47b9e7(
    value: typing.Optional[INagSuppressionIgnore],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499426647076f5f9b25fa3802115f4b0187bef15fcfb86478ee847c35a15b0af(
    value: typing.Optional[INagSuppressionIgnore],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__818a0da55c5cbe0337f1efd54ed9153e54658d7d5a9a1a3d8f93e06baea87360(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a83ce3fdb1cb0ca96a59694799f0ed3b0090f7d4e437681d969d4c74e7ddab(
    *,
    additional_loggers: typing.Optional[typing.Sequence[INagLogger]] = None,
    log_ignores: typing.Optional[builtins.bool] = None,
    report_formats: typing.Optional[typing.Sequence[NagReportFormat]] = None,
    reports: typing.Optional[builtins.bool] = None,
    suppression_ignore_condition: typing.Optional[INagSuppressionIgnore] = None,
    verbose: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e488b05b5f3f444467d9eb46090b6726b68fa30596c2566a59974e3b5ccc5f54(
    *,
    id: builtins.str,
    reason: builtins.str,
    applies_to: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union[RegexAppliesTo, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6b6029bff770690f88c877bee0f2885b7bc043157258be4815d22b42c13364(
    *,
    compliance: builtins.str,
    exception_reason: builtins.str,
    resource_id: builtins.str,
    rule_id: builtins.str,
    rule_info: builtins.str,
    rule_level: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5258c45d7b5e7a57921e27dd5a7c53e00452a977e1d40530500b345f84a31167(
    format: NagReportFormat,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d05cd61c8369866bc8b8765401ea1dfa7ebede0fc2130608a36bb42a8b9448ae(
    data: typing.Union[NagLoggerBaseData, typing.Dict[builtins.str, typing.Any]],
    compliance: typing.Union[NagRuleCompliance, NagRulePostValidationStates],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e3f9aa1b2e641a8748b597a0deb88e437aae2a4f34f10501ac44b0524902a1(
    *,
    formats: typing.Sequence[NagReportFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d13606a383c679c37ca15873660037b156e8491412ee339c74a414fb2061d8d(
    *,
    lines: typing.Sequence[typing.Union[NagReportLine, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8817c32270238bf0dfc84f6218e16b587420567b5bc41a280c177f7ee6cd79f(
    node: _aws_cdk_ceddda9d.CfnResource,
    parameter: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2af31e0e8c775eabad30b7da777a2689dbf22e8f31976bf4840dbd2cbbbf939(
    node: _aws_cdk_ceddda9d.CfnResource,
    parameter: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31cd67cca34b4963ea5b427552d0ed8190cf2265f4659708bb7d899d8e5fc6cb(
    node: _aws_cdk_ceddda9d.CfnResource,
    parameter: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a019ccc6d0325c092e9799383fe39f9bffd3785f51142f30e692e0947937f98e(
    construct: typing.Union[_constructs_77d1e7e8.IConstruct, typing.Sequence[_constructs_77d1e7e8.IConstruct]],
    suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
    apply_to_children: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8e93f68ef8607b6e5a16388f0f7c757ce99057d7e42d5fa1c22db00da355de(
    stack: _aws_cdk_ceddda9d.Stack,
    path: typing.Union[builtins.str, typing.Sequence[builtins.str]],
    suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
    apply_to_children: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5c648cedc28d10ee481b251de2f85cde16e2daf0dc2addd3e4c7860c0e5768(
    stack: _aws_cdk_ceddda9d.Stack,
    suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[builtins.str, typing.Any]]],
    apply_to_nested_stacks: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813d53d45e9db3648743d0e260e058579163527ffb805ee4e7511408478be1f6(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8453471acfa85ba5ddf5a90e23aaf4fd9026a9d972c7f9445fcd249f7a656da(
    *,
    regex: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45822d91dde0925f0c42dd49aa5abb9d5fd6391e1a4d49074f95718261fd8ff8(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa33f04446bcf1cb8a24a2c7daab296b89d9593c017b8c38f99d9a0d452fa725(
    trigger_message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d484956c8730c75e4cf6533596839557423fe7f5ea32dfb4bcbdbb05e4a2d593(
    *suppression_ignore_ands: INagSuppressionIgnore,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__375fa67002e6963901e2f6603cdb52e9d08e6110fab8ac88ea8031b4f8ca472a(
    *,
    finding_id: builtins.str,
    reason: builtins.str,
    resource: _aws_cdk_ceddda9d.CfnResource,
    rule_id: builtins.str,
    rule_level: NagMessageLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5cc605f87aed5b6dd3b4116e98aa83f86df7e8e4504b2181f2e21b03a184d2(
    *or_suppression_ignores: INagSuppressionIgnore,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d27003a8b41ff976c7c6fb69915342dff77d036f488f01f27608ce64fb6fc49(
    rule_id: builtins.str,
    finding_id: builtins.str,
    rule_info: builtins.str,
    rule_explanation: builtins.str,
    verbose: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e731712efd090983cf7e5c1378ce4a7f327773edbf8f7354ece70984365f5be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96eb46c46eba3538cc66dd2f6fd176af6e483161c98c271e2da09d609cf6f32(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7befba4c0338ce825c8858ca449ed8639199c568303515244a7e215f1c28061(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d900825e618c777e4d14e3b2c5357c960a024c352b9c0e3080bf762e9bef6b(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2e84fa7d4ba03aa7bf298104f9e6a7521c3facd75b8d248d072c42722ecd14(
    node: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplyRule, INagLogger, INagSuppressionIgnore]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
