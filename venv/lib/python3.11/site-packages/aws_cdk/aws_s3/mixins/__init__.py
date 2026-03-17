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

from ..._jsii import *

import constructs as _constructs_77d1e7e8
from .. import BlockPublicAccess as _BlockPublicAccess_f5d5d483
from ... import Mixin as _Mixin_d3d231df
from ...aws_iam import PolicyStatement as _PolicyStatement_0fe33853


class BucketAutoDeleteObjects(
    _Mixin_d3d231df,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3.mixins.BucketAutoDeleteObjects",
):
    '''S3-specific Mixin to automatically delete all objects from a bucket when the bucket is removed from the stack or when the stack is deleted.

    Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``.

    Apply this mixin to a bucket will add ``s3:PutBucketPolicy`` to the
    bucket policy. This is because during bucket deletion, the custom resource provider
    needs to update the bucket policy by adding a deny policy for ``s3:PutObject`` to
    prevent race conditions with external bucket writers.

    :exampleMetadata: fixture=README-mixins infused

    Example::

        # Apply mixins fluently with .with()
        s3.CfnBucket(scope, "MyL1Bucket").with(BucketBlockPublicAccess()).with(BucketAutoDeleteObjects())
        
        # Apply multiple mixins to the same construct
        s3.CfnBucket(scope, "MyL1Bucket").with(BucketBlockPublicAccess(), BucketAutoDeleteObjects())
        
        # Mixins work with all types of constructs:
        # L1, L2 and even custom constructs
        s3.Bucket(stack, "MyL2Bucket").with(BucketBlockPublicAccess())
        CustomBucket(stack, "MyCustomBucket").with(BucketBlockPublicAccess())
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, construct: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba562fe062bba531ffca978f38501ea81f6347d7ecc74681f7a93978f2f89275)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [construct]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d89ec4ef035e2178fef36bcf1e95f70394ab469955bdee9eefb395eb9aec8b4)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


class BucketBlockPublicAccess(
    _Mixin_d3d231df,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3.mixins.BucketBlockPublicAccess",
):
    '''S3-specific mixin for blocking public-access.

    :exampleMetadata: fixture=README-mixins infused

    Example::

        # Apply mixins fluently with .with()
        s3.CfnBucket(scope, "MyL1Bucket").with(BucketBlockPublicAccess()).with(BucketAutoDeleteObjects())
        
        # Apply multiple mixins to the same construct
        s3.CfnBucket(scope, "MyL1Bucket").with(BucketBlockPublicAccess(), BucketAutoDeleteObjects())
        
        # Mixins work with all types of constructs:
        # L1, L2 and even custom constructs
        s3.Bucket(stack, "MyL2Bucket").with(BucketBlockPublicAccess())
        CustomBucket(stack, "MyCustomBucket").with(BucketBlockPublicAccess())
    '''

    def __init__(
        self,
        public_access_config: typing.Optional["_BlockPublicAccess_f5d5d483"] = None,
    ) -> None:
        '''
        :param public_access_config: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__094c7ee211134c22bdc897a9daeaf0513f39d5d55a7c06dd6e7b8be450bcd156)
            check_type(argname="argument public_access_config", value=public_access_config, expected_type=type_hints["public_access_config"])
        jsii.create(self.__class__, self, [public_access_config])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, construct: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b0ce170eadec3336c23203ebb0d64868283cb31a34324dd49e7b543acdf944a)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [construct]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0297c075ca9c8b509ab19f1bd7a7e1f8d5e3c3c7cf688a671c24856a3d93e7b)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


class BucketPolicyStatements(
    _Mixin_d3d231df,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3.mixins.BucketPolicyStatements",
):
    '''Adds statements to a bucket policy.

    :exampleMetadata: infused

    Example::

        s3.CfnBucketPolicy(self, "Policy",
            bucket=s3.CfnBucket(self, "Bucket").ref,
            policy_document=iam.PolicyDocument()
        ).with(s3.mixins.BucketPolicyStatements([
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=["*"],
                principals=[iam.AnyPrincipal()]
            )
        ]))
    '''

    def __init__(
        self,
        statements: typing.Sequence["_PolicyStatement_0fe33853"],
    ) -> None:
        '''
        :param statements: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa3de63e08c7cbf73b3caf34d2c40c53a0aec2f6039c3d938eeca53b4fb4320)
            check_type(argname="argument statements", value=statements, expected_type=type_hints["statements"])
        jsii.create(self.__class__, self, [statements])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, policy: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param policy: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09cc95ae82e7f8a84fa1184cba34c2e4d8d78464c6b2836356c9d95f831fe48c)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [policy]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc5d2eaf91262ba99cc465e651653c0269391f4cb12ecabc25157e1027a330b6)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


class BucketVersioning(
    _Mixin_d3d231df,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3.mixins.BucketVersioning",
):
    '''S3-specific mixin for enabling versioning.

    :exampleMetadata: infused

    Example::

        s3.CfnBucket(self, "Bucket").with(s3.mixins.BucketVersioning())
    '''

    def __init__(self, enabled: typing.Optional[builtins.bool] = None) -> None:
        '''
        :param enabled: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e1f10b10b0c9f72889bd2c9f53b49943aa8686d3fdbf176335602465f1b4560)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        jsii.create(self.__class__, self, [enabled])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, construct: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b42e2ea4a56f1eceee37f332dc934222f116480deb7b4937ae789d84529cf30d)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [construct]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__000391283ea3d62a1411865ec3b953ca9213ea9c76c6b2f4c777e4f1514b8574)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


__all__ = [
    "BucketAutoDeleteObjects",
    "BucketBlockPublicAccess",
    "BucketPolicyStatements",
    "BucketVersioning",
]

publication.publish()

def _typecheckingstub__ba562fe062bba531ffca978f38501ea81f6347d7ecc74681f7a93978f2f89275(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d89ec4ef035e2178fef36bcf1e95f70394ab469955bdee9eefb395eb9aec8b4(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094c7ee211134c22bdc897a9daeaf0513f39d5d55a7c06dd6e7b8be450bcd156(
    public_access_config: typing.Optional[_BlockPublicAccess_f5d5d483] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0ce170eadec3336c23203ebb0d64868283cb31a34324dd49e7b543acdf944a(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0297c075ca9c8b509ab19f1bd7a7e1f8d5e3c3c7cf688a671c24856a3d93e7b(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa3de63e08c7cbf73b3caf34d2c40c53a0aec2f6039c3d938eeca53b4fb4320(
    statements: typing.Sequence[_PolicyStatement_0fe33853],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09cc95ae82e7f8a84fa1184cba34c2e4d8d78464c6b2836356c9d95f831fe48c(
    policy: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5d2eaf91262ba99cc465e651653c0269391f4cb12ecabc25157e1027a330b6(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1f10b10b0c9f72889bd2c9f53b49943aa8686d3fdbf176335602465f1b4560(
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b42e2ea4a56f1eceee37f332dc934222f116480deb7b4937ae789d84529cf30d(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000391283ea3d62a1411865ec3b953ca9213ea9c76c6b2f4c777e4f1514b8574(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass
