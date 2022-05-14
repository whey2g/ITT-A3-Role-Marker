#A child class of the python standard Exception class that will parent exception classes for each attribute
#of the Student class. Using the name StudentError as each exception will be related to
#attributes in the Student class and it is good practice to use Error as the final in word in a
#CamelCase class name.
class StudentError(Exception):
    pass

#A child class of the python standard Exception class that will parent exception classes for each attribute
#of the Teacher class. Using the name TeacherError as each exception will be related to
#attributes in the Teacher class and it is good practice to use Error as the final in word in a
#CamelCase class name.
class TeacherError(Exception):
    pass

#A component class that defines the Student object. Using the name Student as it is a good
#descriptor of the object.
class Student():
    #
    def__init__(self):
    pass

#A component class that defines the Teacher object. Using the name Teacher as it is a good
#descriptor of the object.
class Teacher():
    #
    def__init__(self):
    pass

#A class that runs the roll marker program backend module methods. Using the name RollMarkerManager as
#it captures the escence of the core purpose of the program.
class RollMarkerManager():
    #
    def__init__(self):
    pass
