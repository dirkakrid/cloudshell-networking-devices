from cloudshell.shell.core.exceptions import BaseVisibleException


class InvalidSNMPParams(BaseVisibleException):
    """SNMP parameters aren't valid"""
    pass


class SetupCLISessionException(BaseVisibleException):
    """Failed to get CLI session"""
    pass
