

from viessmann.api.heating import Heating
from viessmann.api.sensors import Sensors
from viessmann.api.circuits import Circuits
from viessmann.api.device import Device

class viApi(Heating,
            Sensors,
            Circuits,
            Device):

    pass
