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
from .. import IEnvironmentAware as _IEnvironmentAware_f39049ee


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
        "index_id": "indexId",
    },
)
class DataSourceReference:
    def __init__(
        self,
        *,
        data_source_arn: builtins.str,
        data_source_id: builtins.str,
        index_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param data_source_arn: The ARN of the DataSource resource.
        :param data_source_id: The Id of the DataSource resource.
        :param index_id: The IndexId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            data_source_reference = interfaces_kendra.DataSourceReference(
                data_source_arn="dataSourceArn",
                data_source_id="dataSourceId",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a2266da96cc0a7063425a169455c1a15681197af9c6cf20fadd6cea5b1aef5)
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_arn": data_source_arn,
            "data_source_id": data_source_id,
            "index_id": index_id,
        }

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The ARN of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The Id of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The IndexId of the DataSource resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.FaqReference",
    jsii_struct_bases=[],
    name_mapping={"faq_arn": "faqArn", "faq_id": "faqId", "index_id": "indexId"},
)
class FaqReference:
    def __init__(
        self,
        *,
        faq_arn: builtins.str,
        faq_id: builtins.str,
        index_id: builtins.str,
    ) -> None:
        '''A reference to a Faq resource.

        :param faq_arn: The ARN of the Faq resource.
        :param faq_id: The Id of the Faq resource.
        :param index_id: The IndexId of the Faq resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            faq_reference = interfaces_kendra.FaqReference(
                faq_arn="faqArn",
                faq_id="faqId",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7625e62231fe84325a87668fc4fd70f592af31757a95bd7b6a61041391e98537)
            check_type(argname="argument faq_arn", value=faq_arn, expected_type=type_hints["faq_arn"])
            check_type(argname="argument faq_id", value=faq_id, expected_type=type_hints["faq_id"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "faq_arn": faq_arn,
            "faq_id": faq_id,
            "index_id": index_id,
        }

    @builtins.property
    def faq_arn(self) -> builtins.str:
        '''The ARN of the Faq resource.'''
        result = self._values.get("faq_arn")
        assert result is not None, "Required property 'faq_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def faq_id(self) -> builtins.str:
        '''The Id of the Faq resource.'''
        result = self._values.get("faq_id")
        assert result is not None, "Required property 'faq_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The IndexId of the Faq resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FaqReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IFaqRef")
class IFaqRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Faq.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="faqRef")
    def faq_ref(self) -> "FaqReference":
        '''(experimental) A reference to a Faq resource.

        :stability: experimental
        '''
        ...


class _IFaqRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Faq.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IFaqRef"

    @builtins.property
    @jsii.member(jsii_name="faqRef")
    def faq_ref(self) -> "FaqReference":
        '''(experimental) A reference to a Faq resource.

        :stability: experimental
        '''
        return typing.cast("FaqReference", jsii.get(self, "faqRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFaqRef).__jsii_proxy_class__ = lambda : _IFaqRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IIndexRef")
class IIndexRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        ...


class _IIndexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IIndexRef"

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        return typing.cast("IndexReference", jsii.get(self, "indexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIndexRef).__jsii_proxy_class__ = lambda : _IIndexRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.IndexReference",
    jsii_struct_bases=[],
    name_mapping={"index_arn": "indexArn", "index_id": "indexId"},
)
class IndexReference:
    def __init__(self, *, index_arn: builtins.str, index_id: builtins.str) -> None:
        '''A reference to a Index resource.

        :param index_arn: The ARN of the Index resource.
        :param index_id: The Id of the Index resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            index_reference = interfaces_kendra.IndexReference(
                index_arn="indexArn",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90cd6d290fb63a85515086873543ef20c61d2faa02b3955c1c27c28708e952c4)
            check_type(argname="argument index_arn", value=index_arn, expected_type=type_hints["index_arn"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_arn": index_arn,
            "index_id": index_id,
        }

    @builtins.property
    def index_arn(self) -> builtins.str:
        '''The ARN of the Index resource.'''
        result = self._values.get("index_arn")
        assert result is not None, "Required property 'index_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The Id of the Index resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IndexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataSourceReference",
    "FaqReference",
    "IDataSourceRef",
    "IFaqRef",
    "IIndexRef",
    "IndexReference",
]

publication.publish()

def _typecheckingstub__26a2266da96cc0a7063425a169455c1a15681197af9c6cf20fadd6cea5b1aef5(
    *,
    data_source_arn: builtins.str,
    data_source_id: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7625e62231fe84325a87668fc4fd70f592af31757a95bd7b6a61041391e98537(
    *,
    faq_arn: builtins.str,
    faq_id: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90cd6d290fb63a85515086873543ef20c61d2faa02b3955c1c27c28708e952c4(
    *,
    index_arn: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDataSourceRef, IFaqRef, IIndexRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
