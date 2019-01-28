
import json
import viessmann.base.base as base

class Device(base.ViBase):

    def getDevice(self):
        try:
           # return self.getProperty("heating.circuits.1.operating.programs")["entities"][9]["properties"]["components"]
            return self.getProperty("heating.device.time")["properties"]["value"]["value"]
        except KeyError:
            return "error"