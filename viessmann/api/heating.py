
import json
import viessmann.base.base as base

class Heating(base.ViBase):
    """ Set the active mode
    Parameters
    ----------
    mode : str
        Valid mode can be obtained using getModes()
    Returns
    -------
    result: json
        json representation of the answer
    """
    def setMode(self,mode):
        r=self.setProperty("heating.circuits.0.operating.modes.active","setMode","{\"mode\":\""+mode+"\"}")
        return r

    # Works for normal, reduced, comfort
    # active has no action
    # exetenral , standby no action
    # holiday, sheculde and unscheduled
    # activate, decativate comfort,eco
    """ Set the target temperature for the target program
    Parameters
    ----------
    program : str
        Can be normal, reduced or comfort
    temperature: int
        target temperature
    Returns
    -------
    result: json
        json representation of the answer
    """
    def setProgramTemperature(self,program: str,temperature :int):
        return self.setProperty("heating.circuits.0.operating.programs."+program,"setTemperature","{\"targetTemperature\":"+str(temperature)+"}")

    def setReducedTemperature(self,temperature):
        return self.setProgramTemperature("reduced",temperature)

    def setComfortTemperature(self,temperature):
        return self.setProgramTemperature("comfort",temperature)

    def setNormalTemperature(self,temperature):
        return self.setProgramTemperature("normal",temperature)

    """ Activate a program
        NOTE
        DEVICE_COMMUNICATION_ERROR can just mean that the program is already on
    Parameters
    ----------
    program : str
        Appears to work only for comfort
    Returns
    -------
    result: json
        json representation of the answer
    """
    # optional temperature parameter could be passed (but not done)
    def activateProgram(self,program):
        return self.setProperty("heating.circuits.0.operating.programs."+program,"activate","{}")

    def activateComfort(self):
        return self.activateProgram("comfort")
    """ Deactivate a program
    Parameters
    ----------
    program : str
        Appears to work only for comfort and eco (coming from normal, can be reached only by deactivating another state)
    Returns
    -------
    result: json
        json representation of the answer
    """
    def deactivateProgram(self,program):
        return self.setProperty("heating.circuits.0.operating.programs."+program,"deactivate","{}")
    def deactivateComfort(self):
        return self.deactivateProgram("comfort")

    """ Set the target temperature for domestic host water
    Parameters
    ----------
    temperature : int
        Target temperature
    Returns
    -------
    result: json
        json representation of the answer
    """
    def setDomesticHotWaterTemperature(self,temperature):
        return self.setProperty("heating.dhw.temperature","setTargetTemperature","{\"temperature\":"+str(temperature)+"}")

    def getMonthSinceLastService(self):
        try:
            return self.getProperty("heating.service.timeBased")["properties"]["activeMonthSinceLastService"]["value"]
        except KeyError:
            return "error"

    def getLastServiceDate(self):
        try:
            return self.getProperty("heating.service.timeBased")["properties"]["lastService"]["value"]
        except KeyError:
            return "error"

    def getOutsideTemperature(self):
        try:
            return self.getProperty("heating.sensors.temperature.outside")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getSupplyTemperature(self):
        try:
            return self.getProperty("heating.circuits.0.sensors.temperature.supply")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getRoomTemperature(self):
        try:
            return self.getProperty("heating.circuits.0.sensors.temperature.room")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getModes(self):
        try:
            return self.getProperty("heating.circuits.0.operating.modes.active")["actions"][0]["fields"][0]["enum"]
        except KeyError:
            return "error"

    def getActiveMode(self):
        try:
            return self.getProperty("heating.circuits.0.operating.modes.active")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getHeatingCurveShift(self):
        try:
            return self.getProperty("heating.circuits.0.heating.curve")["properties"]["shift"]["value"]
        except KeyError:
            return "error"

    def getHeatingCurveSlope(self):
        try:
            return self.getProperty("heating.circuits.0.heating.curve")["properties"]["slope"]["value"]
        except KeyError:
            return "error"

    def getBoilerTemperature(self):
        try:
            return self.getProperty("heating.boiler.sensors.temperature.main")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getActiveProgram(self):
        try:
            return self.getProperty("heating.circuits.0.operating.programs.active")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getPrograms(self):
        try:
            return self.getProperty("heating.circuits.0.operating.programs")["entities"][9]["properties"]["components"]
        except KeyError:
            return "error"

    def getDesiredTemperatureForProgram(self , program):
        try:
            return self.getProperty("heating.circuits.0.operating.programs."+program)["properties"]["temperature"]["value"]
        except KeyError:
            return "error"

    def getCurrentDesiredTemperature(self):
        try:
            return self.getProperty("heating.circuits.0.operating.programs."+self.getActiveProgram())["properties"]["temperature"]["value"]
        except KeyError:
            return "error"

    def getDomesticHotWaterConfiguredTemperature(self):
        try:
            return self.getProperty("heating.dhw.temperature")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getDomesticHotWaterStorageTemperature(self):
        try:
            return self.getProperty("heating.dhw.sensors.temperature.hotWaterStorage")["properties"]["value"]["value"]
        except KeyError:
            return "error"

    def getDomesticHotWaterMaxTemperature(self):
        try:
            return self.getProperty("heating.dhw.temperature")["actions"][0]["fields"][0]["max"]
        except KeyError:
            return "error"

    def getDomesticHotWaterMinTemperature(self):
        try:
            return self.getProperty("heating.dhw.temperature")["actions"][0]["fields"][0]["min"]
        except KeyError:
            return "error"

    def getGasConsumptionHeatingDays(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['day']['value']
        except KeyError:
            return "error"

    def getGasConsumptionHeatingToday(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['day']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionHeatingWeeks(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['week']['value']
        except KeyError:
            return "error"

    def getGasConsumptionHeatingThisWeek(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['week']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionHeatingMonths(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['month']['value']
        except KeyError:
            return "error"

    def getGasConsumptionHeatingThisMonth(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['month']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionHeatingYears(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['year']['value']
        except KeyError:
            return "error"

    def getGasConsumptionHeatingThisYear(self):
        try:
            return self.getProperty('heating.gas.consumption.heating')['properties']['year']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterDays(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['day']['value']
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterToday(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['day']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterWeeks(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['week']['value']
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterThisWeek(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['week']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterMonths(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['month']['value']
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterThisMonth(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['month']['value'][0]
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterYears(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['year']['value']
        except KeyError:
            return "error"

    def getGasConsumptionDomesticHotWaterThisYear(self):
        try:
            return self.getProperty('heating.gas.consumption.dhw')['properties']['year']['value'][0]
        except KeyError:
            return "error"
