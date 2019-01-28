

import json
import viessmann.base.base as base

class Sensors(base.ViBase):

    def getSensorsTemp(self):
        try:
            return self.getProperty("heating.sensors.temperature")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getSensorsTempOutside(self):
        try:
            return self.getProperty("heating.sensors.temperature.outside")["properties"]["value"]["value"]
        except KeyError:
            return "error"