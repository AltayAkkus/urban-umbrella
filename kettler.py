from os.path import exists
import os
from exceptions import *
import serial, inspect

class Kettler:
    def __init__(self, serialDevice = "/dev/ttyUSB0", baud = 9600, debug = False):
        """Init for Kettler Class
        @serialDevice: Full path to serial device (string)
        @baud: Baud-Rate (numeric)
        """
        self.baud = baud
        self.serialDevice = serialDevice
        self.ser = None
        self.debug = debug
        self.checkSerialDevice()

    def connect(self):
        self.ser = serial.Serial(self.serialDevice)
        return self.ser

    def checkSerialDevice(self):
        if not os.access(self.serialDevice, os.F_OK):
            raise DeviceNotFoundError(self.serialDevice)
        print(os.access(self.serialDevice, os.R_OK))
        print(os.access(self.serialDevice, os.W_OK))
        if not os.access(self.serialDevice, os.R_OK) and  not os.access(self.serialDevice, os.W_OK):
            try:
                os.chmod(self.serialDevice, 600)
            except:
                raise PermissionError('Cannot set chmod of ' + self.serialDevice + ' to 600')

    def debugLog(self, var):
        if self.debug:
            print('------------- DEBUG BLOCK -------------')
            print(inspect.stack()[1][3])
            print(var)
            print(type(var))
    def checkConnectionActive(self):
        if self.ser:
            self.ser.write(b'SB\r\n')
            resp = self.ser.readline()
            resp = resp.decode('utf-8')
            self.debugLog(resp)
            if not resp == "ACK\r\n":
                raise SerialMalfunctionError('Serial is connected and working, but SB command returned no acknowledgment.')
        else:
            raise SerialDisconnectError('Serial not connected. Try to reconnect.')

    def checkConnection(self):
        if not self.ser:
            raise SerialDisconnectError('Serial not connected. Try to reconnect.')
        else: 
            return True
    
    def getStatus(self):
        if self.checkConnection():
            self.ser.write(b'ST\r\n')
            resp = self.ser.readline()
            resp = resp.decode('utf-8')
            resp = resp.replace('\r\n','')
            status = resp.split('\t')
            return status