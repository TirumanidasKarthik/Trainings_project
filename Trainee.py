
class Trainee:
    def __init__(self, name : str, trainer : object):
        self._name = name
        self._trainer = trainer
        self._trainings = []
    
    def getName(self):
        return self._name
    
    def setName(self, name : str):
        self._name = name

    def getTrainer(self):
        return self._trainer
    
    def setTrainer(self, trainer : object):
        self._trainer = trainer

    def getTrainings(self):
        return self._trainings
    
    def setTraining(self, trainings : list):
        self._trainings = []
        for training in trainings:
            self._trainings.append(training)
    
    def addTraining(self, training : object):
        self._trainings.append(training)
       