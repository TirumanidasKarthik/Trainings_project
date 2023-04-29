
class Course:
    def __init__(self, name : str):
        self._modules = []
        self._trainings = []
        self._name = name
    
    def getModules(self):
        return self._modules
    
    def setModules(self, modules : list):
        self._modules = []
        for module in modules:
            self._modules.append(module)
    
    def addModule(self, module):
        self._modules.append(module)
    
    def getTrainings(self):
        return self._trainings
    
    def setTrainings(self, trainings : list):
        self._trainings = []
        for training in trainings:
            self._trainings.append(training)


    def addTraining(self, training):
        self._trainings.append(training)

    def setName(self, name: str):
        self._name = name
    
    def getName(self):
        return self._name
    