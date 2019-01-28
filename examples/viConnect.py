
import sys
import time
import viessmann
from configobj import ConfigObj
from library.loghandler import loghandler


class viConnect(object):
    def __init__(self,configfile):

        self._configfile = configfile
        self._log = None

        self._viess = None

    def readConfig(self):
        print('READCONFIG',self._configfile)
        _cfg = ConfigObj(self._configfile)

        if bool(_cfg) is False:
            print('ERROR config file not found', self._configfile)
            sys.exit()

        self._cfg_log = _cfg.get('LOGGING', None)
        self._cfg_viess = _cfg.get('VIESSMANN',None)
        return True

    def startLogger(self):
        self._log = loghandler()
        self._log.handle(self._cfg_log.get('LOGMODE'), self._cfg_log)
        self._log.level(self._cfg_log.get('LOGLEVEL', 'DEBUG'))
        return True

    def connect(self):
        _user = self._cfg_viess.get('USER','admin')
        _password = self._cfg_viess.get('PASSWORD',None)
        print('TEST',viessmann)
        self._viess = viessmann.viApi()
        self._viess.connect(_user,_password)

    def calls(self):
        print('Month since Last Service: ',self._viess.getMonthSinceLastService())
        print('Outside Temperature: ', self._viess.getSensorsTempOutside())
        print('Sensore Temperature: ',self._viess.getSensorTempSupply())
        print('Device: ',self._viess.getDevice())

    def run(self):
        self.readConfig()
        self.startLogger()
        self.connect()
        self.calls()

if __name__ == "__main__":
    vi = viConnect('./viConnect.cfg')
    print(vi)
    vi.run()


