
class Module:
    def __init__(self, name : str):
        self._units = []
        self._name = name
    
    def getUnits(self):
        return self._units
    
    def setUnits(self, units : list):
        self._units = []
        for unit in units:
            self._units.append(unit)
    
    def addUnit(self, unit):
        self._units.append(unit)
    
    def getName(self):
        return self._name
    
    def setName(self, name: str):
        self._name = name

