"""This module contains the general information for SecurityEncryptionEpFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SecurityEncryptionEpFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_NOP = "nop"
    NAME_UPDATE_ENCRYPTION_EP_BEGIN = "updateEncryptionEpBegin"
    NAME_UPDATE_ENCRYPTION_EP_CONFIGURE_LOCAL = "updateEncryptionEpConfigureLocal"
    NAME_UPDATE_ENCRYPTION_EP_CONFIGURE_PEER = "updateEncryptionEpConfigurePeer"
    NAME_UPDATE_ENCRYPTION_EP_DELETE_AFTER_CONFIG_LOCAL = "updateEncryptionEpDeleteAfterConfigLocal"
    NAME_UPDATE_ENCRYPTION_EP_DELETE_AFTER_CONFIG_PEER = "updateEncryptionEpDeleteAfterConfigPeer"
    NAME_UPDATE_ENCRYPTION_EP_FAIL = "updateEncryptionEpFail"
    NAME_UPDATE_ENCRYPTION_EP_SUCCESS = "updateEncryptionEpSuccess"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class SecurityEncryptionEpFsmStage(ManagedObject):
    """This is SecurityEncryptionEpFsmStage class."""

    consts = SecurityEncryptionEpFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SecurityEncryptionEpFsmStage", "securityEncryptionEpFsmStage", "stage-[name]", VersionMeta.Version435a, "OutputOnly", 0xf, [], [""], ['securityEncryptionEpFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version435a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version435a, MoPropertyMeta.NAMING, None, None, None, None, ["nop", "updateEncryptionEpBegin", "updateEncryptionEpConfigureLocal", "updateEncryptionEpConfigurePeer", "updateEncryptionEpDeleteAfterConfigLocal", "updateEncryptionEpDeleteAfterConfigPeer", "updateEncryptionEpFail", "updateEncryptionEpSuccess"], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version435a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "SecurityEncryptionEpFsmStage", parent_mo_or_dn, **kwargs)
