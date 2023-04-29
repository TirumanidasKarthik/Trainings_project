from Organization import Organization
from Trainer import Trainer
from Trainee import Trainee
from Course import Course
from Training import Training
from Module import Module
from Unit import Unit
from Topic import Topic

def main():
    org = Organization('tcs')
    trainer1 = Trainer('karthik', org)
    trainees = []
    trainees.append(Trainee('nicky', trainer1))
    trainees.append(Trainee('yedla', trainer1))
    trainer1.setTrainees(trainees)
    course = Course('python')
    training = Training(trainer1, course)
    training.setTrainees(trainees)
    modules = []
    modules.append(Module('m1'))
    modules.append(Module('m2'))
    course.setModules(modules)
    units = []
    units.append(Unit('u1', 2))
    units.append(Unit('u2', 5))
    modules[0].setUnits(units)
    modules[1].setUnits(units)

    topics = []
    topics.append(Topic('topic1'))
    topics.append(Topic('topic2'))

    units[0].setTopics(topics)
    units[1].setTopics(topics)

    print(f'number of trainees {training.getNumOfTrainees()}')
    print(f'training organization name is {training.getTrainingOrganizationName()}')
    print(f'training duration is {training.getTrainingDurationInHrs()}')





main()