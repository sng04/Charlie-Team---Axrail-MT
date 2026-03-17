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
    jsii_type="aws-cdk-lib.interfaces.aws_location.APIKeyReference",
    jsii_struct_bases=[],
    name_mapping={"api_key_arn": "apiKeyArn", "key_name": "keyName"},
)
class APIKeyReference:
    def __init__(self, *, api_key_arn: builtins.str, key_name: builtins.str) -> None:
        '''A reference to a APIKey resource.

        :param api_key_arn: The ARN of the APIKey resource.
        :param key_name: The KeyName of the APIKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            a_pIKey_reference = interfaces_location.APIKeyReference(
                api_key_arn="apiKeyArn",
                key_name="keyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c29d7290666058d83acadae810c0321e8dd71be129b26f0dfc2518848c5a9aa)
            check_type(argname="argument api_key_arn", value=api_key_arn, expected_type=type_hints["api_key_arn"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key_arn": api_key_arn,
            "key_name": key_name,
        }

    @builtins.property
    def api_key_arn(self) -> builtins.str:
        '''The ARN of the APIKey resource.'''
        result = self._values.get("api_key_arn")
        assert result is not None, "Required property 'api_key_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> builtins.str:
        '''The KeyName of the APIKey resource.'''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "APIKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_location.GeofenceCollectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "collection_name": "collectionName",
        "geofence_collection_arn": "geofenceCollectionArn",
    },
)
class GeofenceCollectionReference:
    def __init__(
        self,
        *,
        collection_name: builtins.str,
        geofence_collection_arn: builtins.str,
    ) -> None:
        '''A reference to a GeofenceCollection resource.

        :param collection_name: The CollectionName of the GeofenceCollection resource.
        :param geofence_collection_arn: The ARN of the GeofenceCollection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            geofence_collection_reference = interfaces_location.GeofenceCollectionReference(
                collection_name="collectionName",
                geofence_collection_arn="geofenceCollectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1625b96f91de82401056da752c57830a97a84b46c36bb3d94e727681756853f4)
            check_type(argname="argument collection_name", value=collection_name, expected_type=type_hints["collection_name"])
            check_type(argname="argument geofence_collection_arn", value=geofence_collection_arn, expected_type=type_hints["geofence_collection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_name": collection_name,
            "geofence_collection_arn": geofence_collection_arn,
        }

    @builtins.property
    def collection_name(self) -> builtins.str:
        '''The CollectionName of the GeofenceCollection resource.'''
        result = self._values.get("collection_name")
        assert result is not None, "Required property 'collection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def geofence_collection_arn(self) -> builtins.str:
        '''The ARN of the GeofenceCollection resource.'''
        result = self._values.get("geofence_collection_arn")
        assert result is not None, "Required property 'geofence_collection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GeofenceCollectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.IAPIKeyRef")
class IAPIKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a APIKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiKeyRef")
    def api_key_ref(self) -> "APIKeyReference":
        '''(experimental) A reference to a APIKey resource.

        :stability: experimental
        '''
        ...


class _IAPIKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a APIKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.IAPIKeyRef"

    @builtins.property
    @jsii.member(jsii_name="apiKeyRef")
    def api_key_ref(self) -> "APIKeyReference":
        '''(experimental) A reference to a APIKey resource.

        :stability: experimental
        '''
        return typing.cast("APIKeyReference", jsii.get(self, "apiKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAPIKeyRef).__jsii_proxy_class__ = lambda : _IAPIKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.IGeofenceCollectionRef")
class IGeofenceCollectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GeofenceCollection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="geofenceCollectionRef")
    def geofence_collection_ref(self) -> "GeofenceCollectionReference":
        '''(experimental) A reference to a GeofenceCollection resource.

        :stability: experimental
        '''
        ...


class _IGeofenceCollectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GeofenceCollection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.IGeofenceCollectionRef"

    @builtins.property
    @jsii.member(jsii_name="geofenceCollectionRef")
    def geofence_collection_ref(self) -> "GeofenceCollectionReference":
        '''(experimental) A reference to a GeofenceCollection resource.

        :stability: experimental
        '''
        return typing.cast("GeofenceCollectionReference", jsii.get(self, "geofenceCollectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGeofenceCollectionRef).__jsii_proxy_class__ = lambda : _IGeofenceCollectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.IMapRef")
class IMapRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Map.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mapRef")
    def map_ref(self) -> "MapReference":
        '''(experimental) A reference to a Map resource.

        :stability: experimental
        '''
        ...


class _IMapRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Map.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.IMapRef"

    @builtins.property
    @jsii.member(jsii_name="mapRef")
    def map_ref(self) -> "MapReference":
        '''(experimental) A reference to a Map resource.

        :stability: experimental
        '''
        return typing.cast("MapReference", jsii.get(self, "mapRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMapRef).__jsii_proxy_class__ = lambda : _IMapRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.IPlaceIndexRef")
class IPlaceIndexRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PlaceIndex.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="placeIndexRef")
    def place_index_ref(self) -> "PlaceIndexReference":
        '''(experimental) A reference to a PlaceIndex resource.

        :stability: experimental
        '''
        ...


class _IPlaceIndexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PlaceIndex.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.IPlaceIndexRef"

    @builtins.property
    @jsii.member(jsii_name="placeIndexRef")
    def place_index_ref(self) -> "PlaceIndexReference":
        '''(experimental) A reference to a PlaceIndex resource.

        :stability: experimental
        '''
        return typing.cast("PlaceIndexReference", jsii.get(self, "placeIndexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlaceIndexRef).__jsii_proxy_class__ = lambda : _IPlaceIndexRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.IRouteCalculatorRef")
class IRouteCalculatorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteCalculator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeCalculatorRef")
    def route_calculator_ref(self) -> "RouteCalculatorReference":
        '''(experimental) A reference to a RouteCalculator resource.

        :stability: experimental
        '''
        ...


class _IRouteCalculatorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteCalculator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.IRouteCalculatorRef"

    @builtins.property
    @jsii.member(jsii_name="routeCalculatorRef")
    def route_calculator_ref(self) -> "RouteCalculatorReference":
        '''(experimental) A reference to a RouteCalculator resource.

        :stability: experimental
        '''
        return typing.cast("RouteCalculatorReference", jsii.get(self, "routeCalculatorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteCalculatorRef).__jsii_proxy_class__ = lambda : _IRouteCalculatorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.ITrackerConsumerRef")
class ITrackerConsumerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrackerConsumer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trackerConsumerRef")
    def tracker_consumer_ref(self) -> "TrackerConsumerReference":
        '''(experimental) A reference to a TrackerConsumer resource.

        :stability: experimental
        '''
        ...


class _ITrackerConsumerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrackerConsumer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.ITrackerConsumerRef"

    @builtins.property
    @jsii.member(jsii_name="trackerConsumerRef")
    def tracker_consumer_ref(self) -> "TrackerConsumerReference":
        '''(experimental) A reference to a TrackerConsumer resource.

        :stability: experimental
        '''
        return typing.cast("TrackerConsumerReference", jsii.get(self, "trackerConsumerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrackerConsumerRef).__jsii_proxy_class__ = lambda : _ITrackerConsumerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_location.ITrackerRef")
class ITrackerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Tracker.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trackerRef")
    def tracker_ref(self) -> "TrackerReference":
        '''(experimental) A reference to a Tracker resource.

        :stability: experimental
        '''
        ...


class _ITrackerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Tracker.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_location.ITrackerRef"

    @builtins.property
    @jsii.member(jsii_name="trackerRef")
    def tracker_ref(self) -> "TrackerReference":
        '''(experimental) A reference to a Tracker resource.

        :stability: experimental
        '''
        return typing.cast("TrackerReference", jsii.get(self, "trackerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrackerRef).__jsii_proxy_class__ = lambda : _ITrackerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_location.MapReference",
    jsii_struct_bases=[],
    name_mapping={"map_arn": "mapArn", "map_name": "mapName"},
)
class MapReference:
    def __init__(self, *, map_arn: builtins.str, map_name: builtins.str) -> None:
        '''A reference to a Map resource.

        :param map_arn: The ARN of the Map resource.
        :param map_name: The MapName of the Map resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            map_reference = interfaces_location.MapReference(
                map_arn="mapArn",
                map_name="mapName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcef94a6744362e1a624a8d7bfa260010b35a87139fd3e9537897bfc9a3b7814)
            check_type(argname="argument map_arn", value=map_arn, expected_type=type_hints["map_arn"])
            check_type(argname="argument map_name", value=map_name, expected_type=type_hints["map_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_arn": map_arn,
            "map_name": map_name,
        }

    @builtins.property
    def map_arn(self) -> builtins.str:
        '''The ARN of the Map resource.'''
        result = self._values.get("map_arn")
        assert result is not None, "Required property 'map_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_name(self) -> builtins.str:
        '''The MapName of the Map resource.'''
        result = self._values.get("map_name")
        assert result is not None, "Required property 'map_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MapReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_location.PlaceIndexReference",
    jsii_struct_bases=[],
    name_mapping={"index_name": "indexName", "place_index_arn": "placeIndexArn"},
)
class PlaceIndexReference:
    def __init__(
        self,
        *,
        index_name: builtins.str,
        place_index_arn: builtins.str,
    ) -> None:
        '''A reference to a PlaceIndex resource.

        :param index_name: The IndexName of the PlaceIndex resource.
        :param place_index_arn: The ARN of the PlaceIndex resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            place_index_reference = interfaces_location.PlaceIndexReference(
                index_name="indexName",
                place_index_arn="placeIndexArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdccdd950b00dc4272c43d70bc115004ce00a81fcccf4dd10211eee9fc01752a)
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument place_index_arn", value=place_index_arn, expected_type=type_hints["place_index_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_name": index_name,
            "place_index_arn": place_index_arn,
        }

    @builtins.property
    def index_name(self) -> builtins.str:
        '''The IndexName of the PlaceIndex resource.'''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def place_index_arn(self) -> builtins.str:
        '''The ARN of the PlaceIndex resource.'''
        result = self._values.get("place_index_arn")
        assert result is not None, "Required property 'place_index_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlaceIndexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_location.RouteCalculatorReference",
    jsii_struct_bases=[],
    name_mapping={
        "calculator_name": "calculatorName",
        "route_calculator_arn": "routeCalculatorArn",
    },
)
class RouteCalculatorReference:
    def __init__(
        self,
        *,
        calculator_name: builtins.str,
        route_calculator_arn: builtins.str,
    ) -> None:
        '''A reference to a RouteCalculator resource.

        :param calculator_name: The CalculatorName of the RouteCalculator resource.
        :param route_calculator_arn: The ARN of the RouteCalculator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            route_calculator_reference = interfaces_location.RouteCalculatorReference(
                calculator_name="calculatorName",
                route_calculator_arn="routeCalculatorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb97f3bca552e2842a19f1fa398f9f372b6092b67f47dd32b2d6d5e0b9a6e23d)
            check_type(argname="argument calculator_name", value=calculator_name, expected_type=type_hints["calculator_name"])
            check_type(argname="argument route_calculator_arn", value=route_calculator_arn, expected_type=type_hints["route_calculator_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "calculator_name": calculator_name,
            "route_calculator_arn": route_calculator_arn,
        }

    @builtins.property
    def calculator_name(self) -> builtins.str:
        '''The CalculatorName of the RouteCalculator resource.'''
        result = self._values.get("calculator_name")
        assert result is not None, "Required property 'calculator_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_calculator_arn(self) -> builtins.str:
        '''The ARN of the RouteCalculator resource.'''
        result = self._values.get("route_calculator_arn")
        assert result is not None, "Required property 'route_calculator_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteCalculatorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_location.TrackerConsumerReference",
    jsii_struct_bases=[],
    name_mapping={"consumer_arn": "consumerArn", "tracker_name": "trackerName"},
)
class TrackerConsumerReference:
    def __init__(
        self,
        *,
        consumer_arn: builtins.str,
        tracker_name: builtins.str,
    ) -> None:
        '''A reference to a TrackerConsumer resource.

        :param consumer_arn: The ConsumerArn of the TrackerConsumer resource.
        :param tracker_name: The TrackerName of the TrackerConsumer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            tracker_consumer_reference = interfaces_location.TrackerConsumerReference(
                consumer_arn="consumerArn",
                tracker_name="trackerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a724199fd8d3d2f5effc88a45a26c498f879bf4a9c3c42d03dd8ce49e615c590)
            check_type(argname="argument consumer_arn", value=consumer_arn, expected_type=type_hints["consumer_arn"])
            check_type(argname="argument tracker_name", value=tracker_name, expected_type=type_hints["tracker_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumer_arn": consumer_arn,
            "tracker_name": tracker_name,
        }

    @builtins.property
    def consumer_arn(self) -> builtins.str:
        '''The ConsumerArn of the TrackerConsumer resource.'''
        result = self._values.get("consumer_arn")
        assert result is not None, "Required property 'consumer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracker_name(self) -> builtins.str:
        '''The TrackerName of the TrackerConsumer resource.'''
        result = self._values.get("tracker_name")
        assert result is not None, "Required property 'tracker_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrackerConsumerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_location.TrackerReference",
    jsii_struct_bases=[],
    name_mapping={"tracker_arn": "trackerArn", "tracker_name": "trackerName"},
)
class TrackerReference:
    def __init__(
        self,
        *,
        tracker_arn: builtins.str,
        tracker_name: builtins.str,
    ) -> None:
        '''A reference to a Tracker resource.

        :param tracker_arn: The ARN of the Tracker resource.
        :param tracker_name: The TrackerName of the Tracker resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_location as interfaces_location
            
            tracker_reference = interfaces_location.TrackerReference(
                tracker_arn="trackerArn",
                tracker_name="trackerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41c2a2f9d3ee6d88f6fbff2fbd32c71f7dc8719f50618a2e3e8758d744775da7)
            check_type(argname="argument tracker_arn", value=tracker_arn, expected_type=type_hints["tracker_arn"])
            check_type(argname="argument tracker_name", value=tracker_name, expected_type=type_hints["tracker_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tracker_arn": tracker_arn,
            "tracker_name": tracker_name,
        }

    @builtins.property
    def tracker_arn(self) -> builtins.str:
        '''The ARN of the Tracker resource.'''
        result = self._values.get("tracker_arn")
        assert result is not None, "Required property 'tracker_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracker_name(self) -> builtins.str:
        '''The TrackerName of the Tracker resource.'''
        result = self._values.get("tracker_name")
        assert result is not None, "Required property 'tracker_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrackerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "APIKeyReference",
    "GeofenceCollectionReference",
    "IAPIKeyRef",
    "IGeofenceCollectionRef",
    "IMapRef",
    "IPlaceIndexRef",
    "IRouteCalculatorRef",
    "ITrackerConsumerRef",
    "ITrackerRef",
    "MapReference",
    "PlaceIndexReference",
    "RouteCalculatorReference",
    "TrackerConsumerReference",
    "TrackerReference",
]

publication.publish()

def _typecheckingstub__5c29d7290666058d83acadae810c0321e8dd71be129b26f0dfc2518848c5a9aa(
    *,
    api_key_arn: builtins.str,
    key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1625b96f91de82401056da752c57830a97a84b46c36bb3d94e727681756853f4(
    *,
    collection_name: builtins.str,
    geofence_collection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcef94a6744362e1a624a8d7bfa260010b35a87139fd3e9537897bfc9a3b7814(
    *,
    map_arn: builtins.str,
    map_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdccdd950b00dc4272c43d70bc115004ce00a81fcccf4dd10211eee9fc01752a(
    *,
    index_name: builtins.str,
    place_index_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb97f3bca552e2842a19f1fa398f9f372b6092b67f47dd32b2d6d5e0b9a6e23d(
    *,
    calculator_name: builtins.str,
    route_calculator_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a724199fd8d3d2f5effc88a45a26c498f879bf4a9c3c42d03dd8ce49e615c590(
    *,
    consumer_arn: builtins.str,
    tracker_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41c2a2f9d3ee6d88f6fbff2fbd32c71f7dc8719f50618a2e3e8758d744775da7(
    *,
    tracker_arn: builtins.str,
    tracker_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAPIKeyRef, IGeofenceCollectionRef, IMapRef, IPlaceIndexRef, IRouteCalculatorRef, ITrackerConsumerRef, ITrackerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
