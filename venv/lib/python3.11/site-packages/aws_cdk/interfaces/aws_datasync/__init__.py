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
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.AgentReference",
    jsii_struct_bases=[],
    name_mapping={"agent_arn": "agentArn"},
)
class AgentReference:
    def __init__(self, *, agent_arn: builtins.str) -> None:
        '''A reference to a Agent resource.

        :param agent_arn: The AgentArn of the Agent resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            agent_reference = interfaces_datasync.AgentReference(
                agent_arn="agentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5fa969d10bd09ef8595e91a48f2e6117fe6648db183d1d917cf0cfdaa229f38)
            check_type(argname="argument agent_arn", value=agent_arn, expected_type=type_hints["agent_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arn": agent_arn,
        }

    @builtins.property
    def agent_arn(self) -> builtins.str:
        '''The AgentArn of the Agent resource.'''
        result = self._values.get("agent_arn")
        assert result is not None, "Required property 'agent_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.IAgentRef")
class IAgentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Agent.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentRef")
    def agent_ref(self) -> "AgentReference":
        '''(experimental) A reference to a Agent resource.

        :stability: experimental
        '''
        ...


class _IAgentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Agent.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.IAgentRef"

    @builtins.property
    @jsii.member(jsii_name="agentRef")
    def agent_ref(self) -> "AgentReference":
        '''(experimental) A reference to a Agent resource.

        :stability: experimental
        '''
        return typing.cast("AgentReference", jsii.get(self, "agentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentRef).__jsii_proxy_class__ = lambda : _IAgentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationAzureBlobRef")
class ILocationAzureBlobRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationAzureBlob.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationAzureBlobRef")
    def location_azure_blob_ref(self) -> "LocationAzureBlobReference":
        '''(experimental) A reference to a LocationAzureBlob resource.

        :stability: experimental
        '''
        ...


class _ILocationAzureBlobRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationAzureBlob.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationAzureBlobRef"

    @builtins.property
    @jsii.member(jsii_name="locationAzureBlobRef")
    def location_azure_blob_ref(self) -> "LocationAzureBlobReference":
        '''(experimental) A reference to a LocationAzureBlob resource.

        :stability: experimental
        '''
        return typing.cast("LocationAzureBlobReference", jsii.get(self, "locationAzureBlobRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationAzureBlobRef).__jsii_proxy_class__ = lambda : _ILocationAzureBlobRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationEFSRef")
class ILocationEFSRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationEFS.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationEfsRef")
    def location_efs_ref(self) -> "LocationEFSReference":
        '''(experimental) A reference to a LocationEFS resource.

        :stability: experimental
        '''
        ...


class _ILocationEFSRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationEFS.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationEFSRef"

    @builtins.property
    @jsii.member(jsii_name="locationEfsRef")
    def location_efs_ref(self) -> "LocationEFSReference":
        '''(experimental) A reference to a LocationEFS resource.

        :stability: experimental
        '''
        return typing.cast("LocationEFSReference", jsii.get(self, "locationEfsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationEFSRef).__jsii_proxy_class__ = lambda : _ILocationEFSRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationFSxLustreRef")
class ILocationFSxLustreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxLustre.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationFSxLustreRef")
    def location_f_sx_lustre_ref(self) -> "LocationFSxLustreReference":
        '''(experimental) A reference to a LocationFSxLustre resource.

        :stability: experimental
        '''
        ...


class _ILocationFSxLustreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxLustre.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationFSxLustreRef"

    @builtins.property
    @jsii.member(jsii_name="locationFSxLustreRef")
    def location_f_sx_lustre_ref(self) -> "LocationFSxLustreReference":
        '''(experimental) A reference to a LocationFSxLustre resource.

        :stability: experimental
        '''
        return typing.cast("LocationFSxLustreReference", jsii.get(self, "locationFSxLustreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationFSxLustreRef).__jsii_proxy_class__ = lambda : _ILocationFSxLustreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationFSxONTAPRef")
class ILocationFSxONTAPRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxONTAP.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationFSxOntapRef")
    def location_f_sx_ontap_ref(self) -> "LocationFSxONTAPReference":
        '''(experimental) A reference to a LocationFSxONTAP resource.

        :stability: experimental
        '''
        ...


class _ILocationFSxONTAPRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxONTAP.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationFSxONTAPRef"

    @builtins.property
    @jsii.member(jsii_name="locationFSxOntapRef")
    def location_f_sx_ontap_ref(self) -> "LocationFSxONTAPReference":
        '''(experimental) A reference to a LocationFSxONTAP resource.

        :stability: experimental
        '''
        return typing.cast("LocationFSxONTAPReference", jsii.get(self, "locationFSxOntapRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationFSxONTAPRef).__jsii_proxy_class__ = lambda : _ILocationFSxONTAPRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationFSxOpenZFSRef")
class ILocationFSxOpenZFSRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxOpenZFS.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationFSxOpenZfsRef")
    def location_f_sx_open_zfs_ref(self) -> "LocationFSxOpenZFSReference":
        '''(experimental) A reference to a LocationFSxOpenZFS resource.

        :stability: experimental
        '''
        ...


class _ILocationFSxOpenZFSRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxOpenZFS.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationFSxOpenZFSRef"

    @builtins.property
    @jsii.member(jsii_name="locationFSxOpenZfsRef")
    def location_f_sx_open_zfs_ref(self) -> "LocationFSxOpenZFSReference":
        '''(experimental) A reference to a LocationFSxOpenZFS resource.

        :stability: experimental
        '''
        return typing.cast("LocationFSxOpenZFSReference", jsii.get(self, "locationFSxOpenZfsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationFSxOpenZFSRef).__jsii_proxy_class__ = lambda : _ILocationFSxOpenZFSRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationFSxWindowsRef")
class ILocationFSxWindowsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxWindows.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationFSxWindowsRef")
    def location_f_sx_windows_ref(self) -> "LocationFSxWindowsReference":
        '''(experimental) A reference to a LocationFSxWindows resource.

        :stability: experimental
        '''
        ...


class _ILocationFSxWindowsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationFSxWindows.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationFSxWindowsRef"

    @builtins.property
    @jsii.member(jsii_name="locationFSxWindowsRef")
    def location_f_sx_windows_ref(self) -> "LocationFSxWindowsReference":
        '''(experimental) A reference to a LocationFSxWindows resource.

        :stability: experimental
        '''
        return typing.cast("LocationFSxWindowsReference", jsii.get(self, "locationFSxWindowsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationFSxWindowsRef).__jsii_proxy_class__ = lambda : _ILocationFSxWindowsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationHDFSRef")
class ILocationHDFSRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationHDFS.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationHdfsRef")
    def location_hdfs_ref(self) -> "LocationHDFSReference":
        '''(experimental) A reference to a LocationHDFS resource.

        :stability: experimental
        '''
        ...


class _ILocationHDFSRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationHDFS.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationHDFSRef"

    @builtins.property
    @jsii.member(jsii_name="locationHdfsRef")
    def location_hdfs_ref(self) -> "LocationHDFSReference":
        '''(experimental) A reference to a LocationHDFS resource.

        :stability: experimental
        '''
        return typing.cast("LocationHDFSReference", jsii.get(self, "locationHdfsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationHDFSRef).__jsii_proxy_class__ = lambda : _ILocationHDFSRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationNFSRef")
class ILocationNFSRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationNFS.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationNfsRef")
    def location_nfs_ref(self) -> "LocationNFSReference":
        '''(experimental) A reference to a LocationNFS resource.

        :stability: experimental
        '''
        ...


class _ILocationNFSRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationNFS.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationNFSRef"

    @builtins.property
    @jsii.member(jsii_name="locationNfsRef")
    def location_nfs_ref(self) -> "LocationNFSReference":
        '''(experimental) A reference to a LocationNFS resource.

        :stability: experimental
        '''
        return typing.cast("LocationNFSReference", jsii.get(self, "locationNfsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationNFSRef).__jsii_proxy_class__ = lambda : _ILocationNFSRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationObjectStorageRef"
)
class ILocationObjectStorageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationObjectStorage.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationObjectStorageRef")
    def location_object_storage_ref(self) -> "LocationObjectStorageReference":
        '''(experimental) A reference to a LocationObjectStorage resource.

        :stability: experimental
        '''
        ...


class _ILocationObjectStorageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationObjectStorage.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationObjectStorageRef"

    @builtins.property
    @jsii.member(jsii_name="locationObjectStorageRef")
    def location_object_storage_ref(self) -> "LocationObjectStorageReference":
        '''(experimental) A reference to a LocationObjectStorage resource.

        :stability: experimental
        '''
        return typing.cast("LocationObjectStorageReference", jsii.get(self, "locationObjectStorageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationObjectStorageRef).__jsii_proxy_class__ = lambda : _ILocationObjectStorageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationS3Ref")
class ILocationS3Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationS3.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationS3Ref")
    def location_s3_ref(self) -> "LocationS3Reference":
        '''(experimental) A reference to a LocationS3 resource.

        :stability: experimental
        '''
        ...


class _ILocationS3RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationS3.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationS3Ref"

    @builtins.property
    @jsii.member(jsii_name="locationS3Ref")
    def location_s3_ref(self) -> "LocationS3Reference":
        '''(experimental) A reference to a LocationS3 resource.

        :stability: experimental
        '''
        return typing.cast("LocationS3Reference", jsii.get(self, "locationS3Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationS3Ref).__jsii_proxy_class__ = lambda : _ILocationS3RefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ILocationSMBRef")
class ILocationSMBRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocationSMB.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationSmbRef")
    def location_smb_ref(self) -> "LocationSMBReference":
        '''(experimental) A reference to a LocationSMB resource.

        :stability: experimental
        '''
        ...


class _ILocationSMBRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocationSMB.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ILocationSMBRef"

    @builtins.property
    @jsii.member(jsii_name="locationSmbRef")
    def location_smb_ref(self) -> "LocationSMBReference":
        '''(experimental) A reference to a LocationSMB resource.

        :stability: experimental
        '''
        return typing.cast("LocationSMBReference", jsii.get(self, "locationSmbRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationSMBRef).__jsii_proxy_class__ = lambda : _ILocationSMBRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datasync.ITaskRef")
class ITaskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Task.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="taskRef")
    def task_ref(self) -> "TaskReference":
        '''(experimental) A reference to a Task resource.

        :stability: experimental
        '''
        ...


class _ITaskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Task.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datasync.ITaskRef"

    @builtins.property
    @jsii.member(jsii_name="taskRef")
    def task_ref(self) -> "TaskReference":
        '''(experimental) A reference to a Task resource.

        :stability: experimental
        '''
        return typing.cast("TaskReference", jsii.get(self, "taskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITaskRef).__jsii_proxy_class__ = lambda : _ITaskRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationAzureBlobReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationAzureBlobReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationAzureBlob resource.

        :param location_arn: The LocationArn of the LocationAzureBlob resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_azure_blob_reference = interfaces_datasync.LocationAzureBlobReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffac249f62ebc114c4f912db619444bbf040bd9efdeacbb153177f22893d348f)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationAzureBlob resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationAzureBlobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationEFSReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationEFSReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationEFS resource.

        :param location_arn: The LocationArn of the LocationEFS resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_eFSReference = interfaces_datasync.LocationEFSReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462aeba30bb567b993af9e6f3044acf172bf05c19984476a0fa00b33f292f728)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationEFS resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationEFSReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationFSxLustreReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationFSxLustreReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationFSxLustre resource.

        :param location_arn: The LocationArn of the LocationFSxLustre resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_fSx_lustre_reference = interfaces_datasync.LocationFSxLustreReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652bfd868f9d53f316e84811447f071dabfacce3cf493be8bc06c66871251a1a)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationFSxLustre resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationFSxLustreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationFSxONTAPReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationFSxONTAPReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationFSxONTAP resource.

        :param location_arn: The LocationArn of the LocationFSxONTAP resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_fSx_oNTAPReference = interfaces_datasync.LocationFSxONTAPReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abefad40453e6fae4e079c8389d02020533a746fb7cfd51f43ca093529933855)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationFSxONTAP resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationFSxONTAPReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationFSxOpenZFSReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationFSxOpenZFSReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationFSxOpenZFS resource.

        :param location_arn: The LocationArn of the LocationFSxOpenZFS resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_fSx_open_zFSReference = interfaces_datasync.LocationFSxOpenZFSReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a73dca9dd8fbef60fcf74d08fe4dd28f76f8177c98e57c4192f8445ae888ca5)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationFSxOpenZFS resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationFSxOpenZFSReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationFSxWindowsReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationFSxWindowsReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationFSxWindows resource.

        :param location_arn: The LocationArn of the LocationFSxWindows resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_fSx_windows_reference = interfaces_datasync.LocationFSxWindowsReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ba67bbf99d6b631954a46dc7ddc43687e75ba161e2f1abd76208ac57be0ef2c)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationFSxWindows resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationFSxWindowsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationHDFSReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationHDFSReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationHDFS resource.

        :param location_arn: The LocationArn of the LocationHDFS resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_hDFSReference = interfaces_datasync.LocationHDFSReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff28b0373aa978e9dcc778f341010d6e147987ec60ce53cdf88bd5332b65e7a)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationHDFS resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationHDFSReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationNFSReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationNFSReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationNFS resource.

        :param location_arn: The LocationArn of the LocationNFS resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_nFSReference = interfaces_datasync.LocationNFSReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__099a4de669c3bc4ce0315a83a72682c7ebc3256870cc90cb3176e19d317a7267)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationNFS resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationNFSReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationObjectStorageReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationObjectStorageReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationObjectStorage resource.

        :param location_arn: The LocationArn of the LocationObjectStorage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_object_storage_reference = interfaces_datasync.LocationObjectStorageReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc30dc7d20bef33ce08d021e7377b43e0ff9ab77621b3ec5b5ff38aa83916fda)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationObjectStorage resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationObjectStorageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationS3Reference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationS3Reference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationS3 resource.

        :param location_arn: The LocationArn of the LocationS3 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_s3_reference = interfaces_datasync.LocationS3Reference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d282cd1893f55554f026c97243ef7dec30e29bda583e5dc92f2ef19ec4c4b52e)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationS3 resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationS3Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.LocationSMBReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn"},
)
class LocationSMBReference:
    def __init__(self, *, location_arn: builtins.str) -> None:
        '''A reference to a LocationSMB resource.

        :param location_arn: The LocationArn of the LocationSMB resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            location_sMBReference = interfaces_datasync.LocationSMBReference(
                location_arn="locationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d183e904452d2128ca7cbe0f0d4b81e6fa240d21df23459ea5f6ae6fdc085a3c)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The LocationArn of the LocationSMB resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationSMBReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datasync.TaskReference",
    jsii_struct_bases=[],
    name_mapping={"task_arn": "taskArn"},
)
class TaskReference:
    def __init__(self, *, task_arn: builtins.str) -> None:
        '''A reference to a Task resource.

        :param task_arn: The TaskArn of the Task resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datasync as interfaces_datasync
            
            task_reference = interfaces_datasync.TaskReference(
                task_arn="taskArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be5ec9cf6fc52294db8458f3ffb93c8d7084262b91b4c55790907c0ebe7112fa)
            check_type(argname="argument task_arn", value=task_arn, expected_type=type_hints["task_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_arn": task_arn,
        }

    @builtins.property
    def task_arn(self) -> builtins.str:
        '''The TaskArn of the Task resource.'''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentReference",
    "IAgentRef",
    "ILocationAzureBlobRef",
    "ILocationEFSRef",
    "ILocationFSxLustreRef",
    "ILocationFSxONTAPRef",
    "ILocationFSxOpenZFSRef",
    "ILocationFSxWindowsRef",
    "ILocationHDFSRef",
    "ILocationNFSRef",
    "ILocationObjectStorageRef",
    "ILocationS3Ref",
    "ILocationSMBRef",
    "ITaskRef",
    "LocationAzureBlobReference",
    "LocationEFSReference",
    "LocationFSxLustreReference",
    "LocationFSxONTAPReference",
    "LocationFSxOpenZFSReference",
    "LocationFSxWindowsReference",
    "LocationHDFSReference",
    "LocationNFSReference",
    "LocationObjectStorageReference",
    "LocationS3Reference",
    "LocationSMBReference",
    "TaskReference",
]

publication.publish()

def _typecheckingstub__f5fa969d10bd09ef8595e91a48f2e6117fe6648db183d1d917cf0cfdaa229f38(
    *,
    agent_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffac249f62ebc114c4f912db619444bbf040bd9efdeacbb153177f22893d348f(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462aeba30bb567b993af9e6f3044acf172bf05c19984476a0fa00b33f292f728(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652bfd868f9d53f316e84811447f071dabfacce3cf493be8bc06c66871251a1a(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abefad40453e6fae4e079c8389d02020533a746fb7cfd51f43ca093529933855(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a73dca9dd8fbef60fcf74d08fe4dd28f76f8177c98e57c4192f8445ae888ca5(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ba67bbf99d6b631954a46dc7ddc43687e75ba161e2f1abd76208ac57be0ef2c(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff28b0373aa978e9dcc778f341010d6e147987ec60ce53cdf88bd5332b65e7a(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__099a4de669c3bc4ce0315a83a72682c7ebc3256870cc90cb3176e19d317a7267(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc30dc7d20bef33ce08d021e7377b43e0ff9ab77621b3ec5b5ff38aa83916fda(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d282cd1893f55554f026c97243ef7dec30e29bda583e5dc92f2ef19ec4c4b52e(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d183e904452d2128ca7cbe0f0d4b81e6fa240d21df23459ea5f6ae6fdc085a3c(
    *,
    location_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5ec9cf6fc52294db8458f3ffb93c8d7084262b91b4c55790907c0ebe7112fa(
    *,
    task_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentRef, ILocationAzureBlobRef, ILocationEFSRef, ILocationFSxLustreRef, ILocationFSxONTAPRef, ILocationFSxOpenZFSRef, ILocationFSxWindowsRef, ILocationHDFSRef, ILocationNFSRef, ILocationObjectStorageRef, ILocationS3Ref, ILocationSMBRef, ITaskRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
