from enum import Enum

class Workspace:
    class DesktopType(Enum):
        SHARED = "SHARED"
        DEDICATED = "DEDICATED"
    
    class ImageType(Enum):
        gold = "gold"
        private = "private"

    class VolumeType(Enum):
        GPSSD = "GPSSD"
        SAS = "SAS"
        SSD = "SSD"

    class UserGroupType(Enum):
        sudo = "sudo"
        default = "default"
        Administrators = "Administrators"
        users = "users"

    class UserAttachType(Enum):
        GROUP = "GROUP"
        USER = "USER"