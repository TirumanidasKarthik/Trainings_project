
class Unit:
    def __init__(self, name : str, durationHrs : int):
        self._name = name
        self._durationHrs = durationHrs
        self._topics = []

    def getName(self):
        return self._name
    
    def setName(self, name : str):
        self._name = name
    
    
    def getDurationHrs(self):
        return self._durationHrs
    
    def setDurationHrs(self, durationHrs : int):
        self._durationHrs = durationHrs

    def getTopics(self):
        return self._topics
    
    def setTopics(self, topics : list):
        self._topics = []
        for topic in topics:
            self._topics.append(topic)
    
    def addTopic(self, topic):
        self._topics.append(topic)