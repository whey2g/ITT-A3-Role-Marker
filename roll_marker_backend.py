#A child class of the python standard Exception class that will parent exception classes for each attribute
#of the Person class. Using the name PersonError as each exception will be related to
#attributes in the Person class and it is good practice to use Error as the final in word in a
#CamelCase class name.
class PersonError(Exception):
    pass

#A child class of the python standard Exception class that will parent exception classes for each attribute
#of the Classroom class. Using the name ClassroomError as each exception will be related to
#attributes in the Classroom class and it is good practice to use Error as the final in word in a
#CamelCase class name.
class ClassroomError(Exception):
    pass

#A component class that defines the Student object. Using the name Student as it is a good
#descriptor of the object.
class Person():
    #
    def__init__(self):
    pass

#A child component class of the Person class that defines the Student object. Using the name
#Student as it is a good descriptor of the object.
class Student(Person):
    #
    def__init__(self):
    pass

#A child component class of the Person class that defines the Teacher object. Using the name
#Teacher as it is a good descriptor of the object.
class Teacher(Person):
    #
    def__init__(self):
    pass

#A child component class of the Person class that defines the EmergencyContact object. Using the name
#EmergencyContact as it is a good descriptor of the object.
class EmergencyContact(Person):
    #
    def__init__(self):
    pass

#A component class that defines the Classroom object. Using the name Classroom as it is a good
#descriptor of the object.
class Classroom():
    #
    def__init__(self):
    pass

#A class that runs the roll marker program backend module methods. Using the name RollMarkerManager as
#it captures the escence of the core purpose of the program.
class RollMarkerManager():
    #
    def__init__(self):
    pass
