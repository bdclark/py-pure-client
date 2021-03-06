from __future__ import absolute_import
import os

from .client import Client
from ...exceptions import PureError
from ...properties import Property, Filter
from ...responses import ValidResponse, ErrorResponse, ApiError, ResponseHeaders

from .models.admin import Admin
from .models.admin_api_token import AdminApiToken
from .models.admin_cache import AdminCache
from .models.admin_patch import AdminPatch
from .models.admin_post import AdminPost
from .models.admin_role import AdminRole
from .models.admin_settings import AdminSettings
from .models.aggregate_replication_performance import AggregateReplicationPerformance
from .models.alert import Alert
from .models.alert_event import AlertEvent
from .models.api_client import ApiClient
from .models.api_client_patch import ApiClientPatch
from .models.api_client_post import ApiClientPost
from .models.api_token import ApiToken
from .models.app import App
from .models.app_node import AppNode
from .models.array import Array
from .models.array_performance import ArrayPerformance
from .models.array_space import ArraySpace
from .models.arrays import Arrays
from .models.audit import Audit
from .models.built_in import BuiltIn
from .models.built_in_relationship import BuiltInRelationship
from .models.built_in_resource_no_id import BuiltInResourceNoId
from .models.chap import Chap
from .models.connection import Connection
from .models.connection2 import Connection2
from .models.connection_post import ConnectionPost
from .models.controller import Controller
from .models.controllers import Controllers
from .models.destroyed_patch_post import DestroyedPatchPost
from .models.directory_service import DirectoryService
from .models.directory_service_management import DirectoryServiceManagement
from .models.directory_service_role import DirectoryServiceRole
from .models.dns import Dns
from .models.dns_patch import DnsPatch
from .models.eula import Eula
from .models.eula_signature import EulaSignature
from .models.fixed_name_resource_no_id import FixedNameResourceNoId
from .models.fixed_reference import FixedReference
from .models.fixed_reference_no_id import FixedReferenceNoId
from .models.hardware import Hardware
from .models.hardware_patch import HardwarePatch
from .models.host import Host
from .models.host2 import Host2
from .models.host_group import HostGroup
from .models.host_group_patch import HostGroupPatch
from .models.host_group_performance import HostGroupPerformance
from .models.host_group_performance_by_array import HostGroupPerformanceByArray
from .models.host_group_space import HostGroupSpace
from .models.host_patch import HostPatch
from .models.host_performance import HostPerformance
from .models.host_performance_by_array import HostPerformanceByArray
from .models.host_port_connectivity import HostPortConnectivity
from .models.host_post import HostPost
from .models.host_space import HostSpace
from .models.kmip import Kmip
from .models.kmip_patch import KmipPatch
from .models.kmip_post import KmipPost
from .models.kmip_test_result import KmipTestResult
from .models.maintenance_window import MaintenanceWindow
from .models.maintenance_window_post import MaintenanceWindowPost
from .models.member import Member
from .models.member_no_id_all import MemberNoIdAll
from .models.member_no_id_group import MemberNoIdGroup
from .models.new_name import NewName
from .models.offload import Offload
from .models.offload_azure import OffloadAzure
from .models.offload_google_cloud import OffloadGoogleCloud
from .models.offload_nfs import OffloadNfs
from .models.offload_post import OffloadPost
from .models.offload_s3 import OffloadS3
from .models.override_check import OverrideCheck
from .models.page_info import PageInfo
from .models.page_info2 import PageInfo2
from .models.performance import Performance
from .models.pod import Pod
from .models.pod2 import Pod2
from .models.pod_array_status import PodArrayStatus
from .models.pod_patch import PodPatch
from .models.pod_patch2 import PodPatch2
from .models.pod_performance import PodPerformance
from .models.pod_performance_by_array import PodPerformanceByArray
from .models.pod_performance_replication import PodPerformanceReplication
from .models.pod_performance_replication_by_array import PodPerformanceReplicationByArray
from .models.pod_post import PodPost
from .models.pod_replica_link import PodReplicaLink
from .models.pod_replica_link_lag import PodReplicaLinkLag
from .models.pod_replica_link_patch import PodReplicaLinkPatch
from .models.pod_replica_link_performance import PodReplicaLinkPerformance
from .models.pod_replica_link_performance_replication import PodReplicaLinkPerformanceReplication
from .models.pod_space import PodSpace
from .models.port import Port
from .models.port_common import PortCommon
from .models.port_initiator import PortInitiator
from .models.protection_group import ProtectionGroup
from .models.protection_group_performance import ProtectionGroupPerformance
from .models.protection_group_performance_array import ProtectionGroupPerformanceArray
from .models.protection_group_performance_by_array import ProtectionGroupPerformanceByArray
from .models.protection_group_snapshot import ProtectionGroupSnapshot
from .models.protection_group_snapshot_patch import ProtectionGroupSnapshotPatch
from .models.protection_group_snapshot_post import ProtectionGroupSnapshotPost
from .models.protection_group_snapshot_transfer import ProtectionGroupSnapshotTransfer
from .models.protection_group_space import ProtectionGroupSpace
from .models.protection_group_target import ProtectionGroupTarget
from .models.qos import Qos
from .models.reference import Reference
from .models.reference_no_id import ReferenceNoId
from .models.remote_pod import RemotePod
from .models.remote_protection_group import RemoteProtectionGroup
from .models.remote_protection_group_snapshot import RemoteProtectionGroupSnapshot
from .models.remote_protection_group_snapshot_transfer import RemoteProtectionGroupSnapshotTransfer
from .models.remote_volume_snapshot import RemoteVolumeSnapshot
from .models.remote_volume_snapshot_transfer import RemoteVolumeSnapshotTransfer
from .models.replica_link_lag import ReplicaLinkLag
from .models.replica_link_performance_replication import ReplicaLinkPerformanceReplication
from .models.replication_performance_with_total import ReplicationPerformanceWithTotal
from .models.replication_schedule import ReplicationSchedule
from .models.resource import Resource
from .models.resource_fixed_non_unique_name import ResourceFixedNonUniqueName
from .models.resource_no_id import ResourceNoId
from .models.resource_performance import ResourcePerformance
from .models.resource_performance_by_array import ResourcePerformanceByArray
from .models.resource_performance_no_id import ResourcePerformanceNoId
from .models.resource_performance_no_id_by_array import ResourcePerformanceNoIdByArray
from .models.resource_pod_space import ResourcePodSpace
from .models.resource_space import ResourceSpace
from .models.resource_space_no_id import ResourceSpaceNoId
from .models.retention_policy import RetentionPolicy
from .models.smis import Smis
from .models.snapshot import Snapshot
from .models.snapshot_schedule import SnapshotSchedule
from .models.software import Software
from .models.software_installation import SoftwareInstallation
from .models.software_installation_patch import SoftwareInstallationPatch
from .models.software_installation_post import SoftwareInstallationPost
from .models.software_installation_step import SoftwareInstallationStep
from .models.software_installation_steps import SoftwareInstallationSteps
from .models.software_installation_steps_checks import SoftwareInstallationStepsChecks
from .models.software_installations import SoftwareInstallations
from .models.space import Space
from .models.start_end_time import StartEndTime
from .models.subnet import Subnet
from .models.subnet_patch import SubnetPatch
from .models.subnet_post import SubnetPost
from .models.support import Support
from .models.support_patch import SupportPatch
from .models.support_remote_assist_paths import SupportRemoteAssistPaths
from .models.tag import Tag
from .models.target_protection_group import TargetProtectionGroup
from .models.target_protection_group_post_patch import TargetProtectionGroupPostPatch
from .models.test_result import TestResult
from .models.test_result_with_resource import TestResultWithResource
from .models.time_window import TimeWindow
from .models.transfer import Transfer
from .models.username import Username
from .models.volume import Volume
from .models.volume2 import Volume2
from .models.volume_common import VolumeCommon
from .models.volume_group import VolumeGroup
from .models.volume_group_performance import VolumeGroupPerformance
from .models.volume_group_post import VolumeGroupPost
from .models.volume_group_space import VolumeGroupSpace
from .models.volume_patch import VolumePatch
from .models.volume_patch2 import VolumePatch2
from .models.volume_performance import VolumePerformance
from .models.volume_performance_by_array import VolumePerformanceByArray
from .models.volume_post import VolumePost
from .models.volume_snapshot import VolumeSnapshot
from .models.volume_snapshot_patch import VolumeSnapshotPatch
from .models.volume_snapshot_post import VolumeSnapshotPost
from .models.volume_snapshot_transfer import VolumeSnapshotTransfer
from .models.volume_space import VolumeSpace


def add_properties(model):
    for name, value in model.attribute_map.items():
        setattr(model, name, Property(value))


CLASSES_TO_ADD_PROPS = [
    Admin,
    AdminApiToken,
    AdminCache,
    AdminPatch,
    AdminPost,
    AdminRole,
    AdminSettings,
    AggregateReplicationPerformance,
    Alert,
    AlertEvent,
    ApiClient,
    ApiClientPatch,
    ApiClientPost,
    ApiToken,
    App,
    AppNode,
    Array,
    ArrayPerformance,
    ArraySpace,
    Arrays,
    Audit,
    BuiltIn,
    BuiltInRelationship,
    BuiltInResourceNoId,
    Chap,
    Connection,
    Connection2,
    ConnectionPost,
    Controller,
    Controllers,
    DestroyedPatchPost,
    DirectoryService,
    DirectoryServiceManagement,
    DirectoryServiceRole,
    Dns,
    DnsPatch,
    Eula,
    EulaSignature,
    FixedNameResourceNoId,
    FixedReference,
    FixedReferenceNoId,
    Hardware,
    HardwarePatch,
    Host,
    Host2,
    HostGroup,
    HostGroupPatch,
    HostGroupPerformance,
    HostGroupPerformanceByArray,
    HostGroupSpace,
    HostPatch,
    HostPerformance,
    HostPerformanceByArray,
    HostPortConnectivity,
    HostPost,
    HostSpace,
    Kmip,
    KmipPatch,
    KmipPost,
    KmipTestResult,
    MaintenanceWindow,
    MaintenanceWindowPost,
    Member,
    MemberNoIdAll,
    MemberNoIdGroup,
    NewName,
    Offload,
    OffloadAzure,
    OffloadGoogleCloud,
    OffloadNfs,
    OffloadPost,
    OffloadS3,
    OverrideCheck,
    PageInfo,
    PageInfo2,
    Performance,
    Pod,
    Pod2,
    PodArrayStatus,
    PodPatch,
    PodPatch2,
    PodPerformance,
    PodPerformanceByArray,
    PodPerformanceReplication,
    PodPerformanceReplicationByArray,
    PodPost,
    PodReplicaLink,
    PodReplicaLinkLag,
    PodReplicaLinkPatch,
    PodReplicaLinkPerformance,
    PodReplicaLinkPerformanceReplication,
    PodSpace,
    Port,
    PortCommon,
    PortInitiator,
    ProtectionGroup,
    ProtectionGroupPerformance,
    ProtectionGroupPerformanceArray,
    ProtectionGroupPerformanceByArray,
    ProtectionGroupSnapshot,
    ProtectionGroupSnapshotPatch,
    ProtectionGroupSnapshotPost,
    ProtectionGroupSnapshotTransfer,
    ProtectionGroupSpace,
    ProtectionGroupTarget,
    Qos,
    Reference,
    ReferenceNoId,
    RemotePod,
    RemoteProtectionGroup,
    RemoteProtectionGroupSnapshot,
    RemoteProtectionGroupSnapshotTransfer,
    RemoteVolumeSnapshot,
    RemoteVolumeSnapshotTransfer,
    ReplicaLinkLag,
    ReplicaLinkPerformanceReplication,
    ReplicationPerformanceWithTotal,
    ReplicationSchedule,
    Resource,
    ResourceFixedNonUniqueName,
    ResourceNoId,
    ResourcePerformance,
    ResourcePerformanceByArray,
    ResourcePerformanceNoId,
    ResourcePerformanceNoIdByArray,
    ResourcePodSpace,
    ResourceSpace,
    ResourceSpaceNoId,
    RetentionPolicy,
    Smis,
    Snapshot,
    SnapshotSchedule,
    Software,
    SoftwareInstallation,
    SoftwareInstallationPatch,
    SoftwareInstallationPost,
    SoftwareInstallationStep,
    SoftwareInstallationSteps,
    SoftwareInstallationStepsChecks,
    SoftwareInstallations,
    Space,
    StartEndTime,
    Subnet,
    SubnetPatch,
    SubnetPost,
    Support,
    SupportPatch,
    SupportRemoteAssistPaths,
    Tag,
    TargetProtectionGroup,
    TargetProtectionGroupPostPatch,
    TestResult,
    TestResultWithResource,
    TimeWindow,
    Transfer,
    Username,
    Volume,
    Volume2,
    VolumeCommon,
    VolumeGroup,
    VolumeGroupPerformance,
    VolumeGroupPost,
    VolumeGroupSpace,
    VolumePatch,
    VolumePatch2,
    VolumePerformance,
    VolumePerformanceByArray,
    VolumePost,
    VolumeSnapshot,
    VolumeSnapshotPatch,
    VolumeSnapshotPost,
    VolumeSnapshotTransfer,
    VolumeSpace
]

if os.environ.get('DOCS_GENERATION') is None:
    for model in CLASSES_TO_ADD_PROPS:
        add_properties(model)
