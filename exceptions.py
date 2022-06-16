class DeviceNotFoundError(Exception):
    pass
class PermissionError(Exception):
    pass
class SerialDisconnectError(Exception):
    pass
class SerialMalfunctionError(Exception):
    pass

__all__ =   ['DeviceNotFoundError',
            'PermissionError',
            'SerialDisconnectError',
            'SerialMalfunctionError']