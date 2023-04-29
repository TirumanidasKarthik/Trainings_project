
class Training:
    def __init__(self, trainer, course):
        self._trainer = trainer
        self._trainees = []
        self._course = course

    def getTrainer(self):
        return self._trainer
    
    def setTrainer(self, trainer):
        self._trainer = trainer

    def getNumOfTrainees(self):
        return len(self._trainees)
    
    def getTrainees(self):
        return self._trainees
    
    def setTrainees(self, trainees : list):
        self._trainees = []
        for trainee in trainees:
            self._trainees.append(trainee)
        
    
    def addTrainee(self, trainee):
        self._trainees.append(trainee)
    
    def getCourse(self):
        return self._course
    
    def setCourse(self, course):
        self._course = course

    def getTrainingOrganizationName(self):
        return self.getTrainer().getOrganization()

    def getTrainingDurationInHrs(self):
        course = self.getCourse()
        duration = 0
        for module in course.getModules():
            for unit in module.getUnits():
                duration += unit.getDurationHrs()
        return duration
