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
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.DetectorReference",
    jsii_struct_bases=[],
    name_mapping={"detector_arn": "detectorArn"},
)
class DetectorReference:
    def __init__(self, *, detector_arn: builtins.str) -> None:
        '''A reference to a Detector resource.

        :param detector_arn: The Arn of the Detector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            detector_reference = interfaces_frauddetector.DetectorReference(
                detector_arn="detectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10aba78fb6a583487340005852bd45707768042280a628a3b955c26276a840e)
            check_type(argname="argument detector_arn", value=detector_arn, expected_type=type_hints["detector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_arn": detector_arn,
        }

    @builtins.property
    def detector_arn(self) -> builtins.str:
        '''The Arn of the Detector resource.'''
        result = self._values.get("detector_arn")
        assert result is not None, "Required property 'detector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DetectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.EntityTypeReference",
    jsii_struct_bases=[],
    name_mapping={"entity_type_arn": "entityTypeArn"},
)
class EntityTypeReference:
    def __init__(self, *, entity_type_arn: builtins.str) -> None:
        '''A reference to a EntityType resource.

        :param entity_type_arn: The Arn of the EntityType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            entity_type_reference = interfaces_frauddetector.EntityTypeReference(
                entity_type_arn="entityTypeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a874e002d5d140029c663d4ca81beea6e2977cca2b42bad2e09dc45e5d99613)
            check_type(argname="argument entity_type_arn", value=entity_type_arn, expected_type=type_hints["entity_type_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_type_arn": entity_type_arn,
        }

    @builtins.property
    def entity_type_arn(self) -> builtins.str:
        '''The Arn of the EntityType resource.'''
        result = self._values.get("entity_type_arn")
        assert result is not None, "Required property 'entity_type_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EntityTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.EventTypeReference",
    jsii_struct_bases=[],
    name_mapping={"event_type_arn": "eventTypeArn"},
)
class EventTypeReference:
    def __init__(self, *, event_type_arn: builtins.str) -> None:
        '''A reference to a EventType resource.

        :param event_type_arn: The Arn of the EventType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            event_type_reference = interfaces_frauddetector.EventTypeReference(
                event_type_arn="eventTypeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722772f7a1afa3c5be85402ef6b6bc301fb73e5a37deb350011398aa75228db4)
            check_type(argname="argument event_type_arn", value=event_type_arn, expected_type=type_hints["event_type_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_type_arn": event_type_arn,
        }

    @builtins.property
    def event_type_arn(self) -> builtins.str:
        '''The Arn of the EventType resource.'''
        result = self._values.get("event_type_arn")
        assert result is not None, "Required property 'event_type_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.IDetectorRef")
class IDetectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Detector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="detectorRef")
    def detector_ref(self) -> "DetectorReference":
        '''(experimental) A reference to a Detector resource.

        :stability: experimental
        '''
        ...


class _IDetectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Detector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.IDetectorRef"

    @builtins.property
    @jsii.member(jsii_name="detectorRef")
    def detector_ref(self) -> "DetectorReference":
        '''(experimental) A reference to a Detector resource.

        :stability: experimental
        '''
        return typing.cast("DetectorReference", jsii.get(self, "detectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDetectorRef).__jsii_proxy_class__ = lambda : _IDetectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.IEntityTypeRef")
class IEntityTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EntityType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="entityTypeRef")
    def entity_type_ref(self) -> "EntityTypeReference":
        '''(experimental) A reference to a EntityType resource.

        :stability: experimental
        '''
        ...


class _IEntityTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EntityType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.IEntityTypeRef"

    @builtins.property
    @jsii.member(jsii_name="entityTypeRef")
    def entity_type_ref(self) -> "EntityTypeReference":
        '''(experimental) A reference to a EntityType resource.

        :stability: experimental
        '''
        return typing.cast("EntityTypeReference", jsii.get(self, "entityTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEntityTypeRef).__jsii_proxy_class__ = lambda : _IEntityTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.IEventTypeRef")
class IEventTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventTypeRef")
    def event_type_ref(self) -> "EventTypeReference":
        '''(experimental) A reference to a EventType resource.

        :stability: experimental
        '''
        ...


class _IEventTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.IEventTypeRef"

    @builtins.property
    @jsii.member(jsii_name="eventTypeRef")
    def event_type_ref(self) -> "EventTypeReference":
        '''(experimental) A reference to a EventType resource.

        :stability: experimental
        '''
        return typing.cast("EventTypeReference", jsii.get(self, "eventTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventTypeRef).__jsii_proxy_class__ = lambda : _IEventTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.ILabelRef")
class ILabelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Label.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="labelRef")
    def label_ref(self) -> "LabelReference":
        '''(experimental) A reference to a Label resource.

        :stability: experimental
        '''
        ...


class _ILabelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Label.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.ILabelRef"

    @builtins.property
    @jsii.member(jsii_name="labelRef")
    def label_ref(self) -> "LabelReference":
        '''(experimental) A reference to a Label resource.

        :stability: experimental
        '''
        return typing.cast("LabelReference", jsii.get(self, "labelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILabelRef).__jsii_proxy_class__ = lambda : _ILabelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.IListRef")
class IListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a List.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="listRef")
    def list_ref(self) -> "ListReference":
        '''(experimental) A reference to a List resource.

        :stability: experimental
        '''
        ...


class _IListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a List.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.IListRef"

    @builtins.property
    @jsii.member(jsii_name="listRef")
    def list_ref(self) -> "ListReference":
        '''(experimental) A reference to a List resource.

        :stability: experimental
        '''
        return typing.cast("ListReference", jsii.get(self, "listRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListRef).__jsii_proxy_class__ = lambda : _IListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.IOutcomeRef")
class IOutcomeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Outcome.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="outcomeRef")
    def outcome_ref(self) -> "OutcomeReference":
        '''(experimental) A reference to a Outcome resource.

        :stability: experimental
        '''
        ...


class _IOutcomeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Outcome.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.IOutcomeRef"

    @builtins.property
    @jsii.member(jsii_name="outcomeRef")
    def outcome_ref(self) -> "OutcomeReference":
        '''(experimental) A reference to a Outcome resource.

        :stability: experimental
        '''
        return typing.cast("OutcomeReference", jsii.get(self, "outcomeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOutcomeRef).__jsii_proxy_class__ = lambda : _IOutcomeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.IVariableRef")
class IVariableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Variable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="variableRef")
    def variable_ref(self) -> "VariableReference":
        '''(experimental) A reference to a Variable resource.

        :stability: experimental
        '''
        ...


class _IVariableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Variable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_frauddetector.IVariableRef"

    @builtins.property
    @jsii.member(jsii_name="variableRef")
    def variable_ref(self) -> "VariableReference":
        '''(experimental) A reference to a Variable resource.

        :stability: experimental
        '''
        return typing.cast("VariableReference", jsii.get(self, "variableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVariableRef).__jsii_proxy_class__ = lambda : _IVariableRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.LabelReference",
    jsii_struct_bases=[],
    name_mapping={"label_arn": "labelArn"},
)
class LabelReference:
    def __init__(self, *, label_arn: builtins.str) -> None:
        '''A reference to a Label resource.

        :param label_arn: The Arn of the Label resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            label_reference = interfaces_frauddetector.LabelReference(
                label_arn="labelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3f1f4b873e67b6b03f0a42b26e707c803d5c9b5bd23ebbee82075e6fd7ea0c1)
            check_type(argname="argument label_arn", value=label_arn, expected_type=type_hints["label_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label_arn": label_arn,
        }

    @builtins.property
    def label_arn(self) -> builtins.str:
        '''The Arn of the Label resource.'''
        result = self._values.get("label_arn")
        assert result is not None, "Required property 'label_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.ListReference",
    jsii_struct_bases=[],
    name_mapping={"list_arn": "listArn"},
)
class ListReference:
    def __init__(self, *, list_arn: builtins.str) -> None:
        '''A reference to a List resource.

        :param list_arn: The Arn of the List resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            list_reference = interfaces_frauddetector.ListReference(
                list_arn="listArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c73f6b8e780054e3bd1cff533a3910d154e827c646b5208f186268d5817a60da)
            check_type(argname="argument list_arn", value=list_arn, expected_type=type_hints["list_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "list_arn": list_arn,
        }

    @builtins.property
    def list_arn(self) -> builtins.str:
        '''The Arn of the List resource.'''
        result = self._values.get("list_arn")
        assert result is not None, "Required property 'list_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.OutcomeReference",
    jsii_struct_bases=[],
    name_mapping={"outcome_arn": "outcomeArn"},
)
class OutcomeReference:
    def __init__(self, *, outcome_arn: builtins.str) -> None:
        '''A reference to a Outcome resource.

        :param outcome_arn: The Arn of the Outcome resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            outcome_reference = interfaces_frauddetector.OutcomeReference(
                outcome_arn="outcomeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575ac3789446585263aa91e4dd7a9c50509a9bf7c12b5da779bceb94e277b86b)
            check_type(argname="argument outcome_arn", value=outcome_arn, expected_type=type_hints["outcome_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "outcome_arn": outcome_arn,
        }

    @builtins.property
    def outcome_arn(self) -> builtins.str:
        '''The Arn of the Outcome resource.'''
        result = self._values.get("outcome_arn")
        assert result is not None, "Required property 'outcome_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutcomeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_frauddetector.VariableReference",
    jsii_struct_bases=[],
    name_mapping={"variable_arn": "variableArn"},
)
class VariableReference:
    def __init__(self, *, variable_arn: builtins.str) -> None:
        '''A reference to a Variable resource.

        :param variable_arn: The Arn of the Variable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_frauddetector as interfaces_frauddetector
            
            variable_reference = interfaces_frauddetector.VariableReference(
                variable_arn="variableArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d3bd3f3a3765172f813fc1094bbb93c5a21da845791a1afbf4071e8d0af5237)
            check_type(argname="argument variable_arn", value=variable_arn, expected_type=type_hints["variable_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "variable_arn": variable_arn,
        }

    @builtins.property
    def variable_arn(self) -> builtins.str:
        '''The Arn of the Variable resource.'''
        result = self._values.get("variable_arn")
        assert result is not None, "Required property 'variable_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VariableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DetectorReference",
    "EntityTypeReference",
    "EventTypeReference",
    "IDetectorRef",
    "IEntityTypeRef",
    "IEventTypeRef",
    "ILabelRef",
    "IListRef",
    "IOutcomeRef",
    "IVariableRef",
    "LabelReference",
    "ListReference",
    "OutcomeReference",
    "VariableReference",
]

publication.publish()

def _typecheckingstub__d10aba78fb6a583487340005852bd45707768042280a628a3b955c26276a840e(
    *,
    detector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a874e002d5d140029c663d4ca81beea6e2977cca2b42bad2e09dc45e5d99613(
    *,
    entity_type_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722772f7a1afa3c5be85402ef6b6bc301fb73e5a37deb350011398aa75228db4(
    *,
    event_type_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f1f4b873e67b6b03f0a42b26e707c803d5c9b5bd23ebbee82075e6fd7ea0c1(
    *,
    label_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c73f6b8e780054e3bd1cff533a3910d154e827c646b5208f186268d5817a60da(
    *,
    list_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575ac3789446585263aa91e4dd7a9c50509a9bf7c12b5da779bceb94e277b86b(
    *,
    outcome_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3bd3f3a3765172f813fc1094bbb93c5a21da845791a1afbf4071e8d0af5237(
    *,
    variable_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDetectorRef, IEntityTypeRef, IEventTypeRef, ILabelRef, IListRef, IOutcomeRef, IVariableRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
