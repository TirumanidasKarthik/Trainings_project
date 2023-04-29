
class Trainer:
    def __init__(self, name : str, organization : object):
        self._name = name
        self._organization = organization
        self._trainees = []
        self._trainings = []
    
    def getName(self):
        return self._name
    
    def setName(self, name : str):
        self._name = name

    def getOrganization(self):
        return self._organization.getName()
    
    def setOrganization(self, organization : object):
        self._organization = organization

    def getTrainees(self):
        return self._trainees
    
    def setTrainees(self, trainees : list):
        self._trainees = []
        for trainee in trainees:
            self._trainees.append(trainee)
    
    def addTrainee(self, trainee : object):
        self._trainees.append(trainee)
    
    def getTrainings(self):
        return self._trainings
    
    def setTrainings(self, trainings : list):
        self._trainings = []
        for training in trainings:
            self._trainings.append(training)
    
    def addTraining(self, training : object):
        self._trainings.append(training)

    