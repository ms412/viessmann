
import json
import viessmann.base.base as base

class Circuits(base.ViBase):

    def getSensorTempSupply(self):
        try:
            return self.getProperty("heating.circuits.1.sensors.temperature.supply")["properties"]["value"]["value"]
        except KeyError:
            return "error"