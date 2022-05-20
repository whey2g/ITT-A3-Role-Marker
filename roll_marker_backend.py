import sys
import datetime

#A child class of the python standard Exception class that will parent exception classes for each
#attribute of the AttendanceRecord class. Using the name AttendanceRecord as each exception will be
#related to attributes in the AttendanceRecord class and it is good practice to use Error as the final
#in word in a CamelCase class name.
class AttendanceRecordError(Exception):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name IdError as it is an Exception class that relates to the AttendanceRecordError attribute id.
class IdError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name FirstNameError as it is an Exception class that relates to the AttendanceRecordError attribute first_name.
class FirstNameError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name LastNameError as it is an Exception class that relates to the AttendanceRecordError attribute last_name.
class LastNameError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name GenderError as it is an Exception class that relates to the AttendanceRecordError attribute gender.
class GenderError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name PhoneError as it is an Exception class that relates to the AttendanceRecordError attribute phone.
class PhoneError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name CommentsError as it is an Exception class that relates to the AttendanceRecordError attribute comments.
class CommentsError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name ClassroomNameError as it is an Exception class that relates to the AttendanceRecordError attribute
#classroom_name.
class ClassroomNameError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name ClassroomStatusError as it is an Exception class that relates to the AttendanceRecordError attribute
#classroom_status.
class ClassroomStatusError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name ClassroomDateError as it is an Exception class that relates to the AttendanceRecordError attribute
#classroom_date.
class ClassroomDateError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name ClassroomDayError as it is an Exception class that relates to the AttendanceRecordError attribute
#classroom_dat.
class ClassroomDayError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name StudentStatusError as it is an Exception class that relates to the AttendanceRecordError attribute
#student_status.
class StudentStatusError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name AttendanceCountError as it is an Exception class that relates to the AttendanceRecordError attribute
#attendance_count.
class AttendanceCountError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name AttendanceRateError as it is an Exception class that relates to the AttendanceRecordError attribute
#attendance_rate.
class AttendanceRateError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name TitleError as it is an Exception class that relates to the AttendanceRecordError attribute
#title.
class TitleError(AttendanceRecordError):
    pass

#A child of the AttendanceRecordError class, through inheritance this will also be an Exception class. Using
#the name RelationshipError as it is an Exception class that relates to the AttendanceRecordError attribute
#relationship.
class RelationshipError(AttendanceRecordError):
    pass

#A component class that defines the AttendanceRecord object. Using the name AttendanceRecord as it is a good
#descriptor of the object.
class AttendanceRecord():
    #An attribute of the AttendanceRecord class. Using the name student_id as it refers directly to a field
    #in the external dataset.
    __student_id=None
    #An attribute of the AttendanceRecord class. Using the name student_first_name as it refers directly to a field
    #in the external dataset.
    __student_first_name=None
    #An attribute of the AttendanceRecord class. Using the name student_last_name as it refers directly to a field
    #in the external dataset.
    __student_last_name=None
    #An attribute of the AttendanceRecord class. Using the name student_gender as it refers directly to a field
    #in the external dataset.
    __student_gender=None
    #An attribute of the AttendanceRecord class. Using the name student_phone as it refers directly to a field
    #in the external dataset.
    __student_phone=None
    #An attribute of the AttendanceRecord class. Using the name student_comments as it refers directly to a field
    #in the external dataset.
    __student_comments=None
    #An attribute of the AttendanceRecord class. Using the name student_status as it refers directly to a field
    #in the external dataset.
    __student_status=None
    #An attribute of the AttendanceRecord class. Using the name attendance_count as it refers directly to a field
    #in the external dataset.
    __attendance_count=None
    #An attribute of the AttendanceRecord class. Using the name attendance_rate as it refers directly to a field
    #in the external dataset.
    __attendance_rate=None
    #An attribute of the AttendanceRecord class. Using the name teacher_id as it refers directly to a field
    #in the external dataset.
    __teacher_id=None
    #An attribute of the AttendanceRecord class. Using the name teacher_title as it refers directly to a field
    #in the external dataset.
    __teacher_title=None
    #An attribute of the AttendanceRecord class. Using the name teacher_first_name as it refers directly to a field
    #in the external dataset.
    __teacher_first_name=None
    #An attribute of the AttendanceRecord class. Using the name teacher_last_name as it refers directly to a field
    #in the external dataset.
    __teacher_last_name=None
    #An attribute of the AttendanceRecord class. Using the name teacher_phone as it refers directly to a field
    #in the external dataset.
    __teacher_phone=None
    #An attribute of the AttendanceRecord class. Using the name e_contact_id as it refers directly to a field
    #in the external dataset.
    __e_contact_id=None
    #An attribute of the AttendanceRecord class. Using the name e_contact_first_name as it refers directly to a field
    #in the external dataset.
    __e_contact_first_name=None
    #An attribute of the AttendanceRecord class. Using the name e_contact_last_name as it refers directly to a field
    #in the external dataset.
    __e_contact_last_name=None
    #An attribute of the AttendanceRecord class. Using the name e_contact_phone as it refers directly to a field
    #in the external dataset.
    __e_contact_phone=None
    #An attribute of the AttendanceRecord class. Using the name e_contact_comments as it refers directly to a field
    #in the external dataset.
    __e_contact_comments=None
    #An attribute of the AttendanceRecord class. Using the name e_contact_relationship as it refers directly to
    #a field in the external dataset.
    __e_contact_relationship=None
    #An attribute of the AttendanceRecord class. Using the name classroom_name as it refers directly to
    #a field in the external dataset
    __classroom_name=None
    #An attribute of the AttendanceRecord class. Using the name classroom_status as it refers directly to
    #a field in the external dataset.
    __classroom_status=None
    #An attribute of the AttendanceRecord class. Using the name classroom_name as it refers directly to
    #a field in the external dataset.
    __classroom_date=None
    #An attribute of the AttendanceRecord class. Using the name classroom_name as it refers directly to
    #a field in the external dataset.
    __classroom_day=None

    #A constructor method called on creation of the AttendanceRecord class that takes several arguments
    #that relate directly to fields in an external dataset.
    def __init__(self,student_id,student_first_name,student_last_name,student_gender,student_phone,student_comments,student_status,attendance_count,attendance_rate,teacher_id,teacher_title,teacher_first_name,teacher_last_name,teacher_phone,e_contact_id,e_contact_first_name,e_contact_last_name,e_contact_phone,e_contact_comments,e_contact_relationship,classroom_name,classroom_status,classroom_date,classroom_day):
        self.student_id=student_id
        self.student_first_name=student_first_name
        self.student_last_name=student_last_name
        self.student_gender=student_gender
        self.student_phone=student_phone
        self.student_comments=student_comments
        self.student_status=student_status
        self.attendance_count=attendance_count
        self.attendance_rate=attendance_rate
        self.teacher_id=teacher_id
        self.teacher_title=teacher_title
        self.teacher_first_name=teacher_first_name
        self.teacher_last_name=teacher_last_name
        self.teacher_phone=teacher_phone
        self.e_contact_id=e_contact_id
        self.e_contact_first_name=e_contact_first_name
        self.e_contact_last_name=e_contact_last_name
        self.e_contact_phone=e_contact_phone
        self.e_contact_comments=e_contact_comments
        self.e_contact_relationship=e_contact_relationship
        self.classroom_name=classroom_name
        self.classroom_status=classroom_status
        self.classroom_date=classroom_date
        self.classroom_day=classroom_day

    #A getter accessor method to allow read-only access to the student_id attribute from outside of the AttendanceRecord
    #class.
    @property
    def student_id(self):
        return self.__student_id

    #A setter mutator method that will produce an error if a negative value or a string is passed to
    #the student_id attribute.
    @student_id.setter
    def student_id(self,value):
    #    if (value==None):
    #        raise IdError("Value cannot be None")
    #    elif (not isinstance(value,str)):
    #        raise IdError("Value cannot be string")
    #    elif (len(value.strip())<=0):
    #        raise IdError("Value cannt be an empty string")
        self.__student_id=value

    #A getter accessor method to allow read-only access to the student_first_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def student_first_name(self):
        return self.__student_first_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #student_first_name attribute.
    @student_first_name.setter
    def student_first_name(self,value):
    #    if (type(value)!=str):
    #        raise FirstNameError("Value must be a string.")
        self.__student_first_name=value

    #A getter accessor method to allow read-only access to the student_last_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def student_last_name(self):
        return self.__student_last_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #student_last_name attribute.
    @student_last_name.setter
    def student_last_name(self,value):
    #    if (type(value)!=str):
    #        raise LastNameError("Value must be a string.")
        self.__student_last_name=value

    #A getter accessor method to allow read-only access to the student_gender attribute from outside of the
    #AttendanceRecord class.
    @property
    def student_gender(self):
        return self.__student_gender

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #student_gender attribute.
    @student_gender.setter
    def student_gender(self,value):
    #    if (type(value)!=str):
    #        raise GenderError("Value must be a string.")
        self.__student_gender=value

    #A getter accessor method to allow read-only access to the student_phone attribute from outside of the
    #AttendanceRecord class.
    @property
    def student_phone(self):
        return self.__student_phone

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #student_phone attribute.
    @student_phone.setter
    def student_phone(self,value):
    #    if (type(value)!=str):
    #        raise PhoneError("Value must be a string.")
        self.__student_phone=value

    #A getter accessor method to allow read-only access to the student_comments attribute from outside of the
    #AttendanceRecord class.
    @property
    def student_comments(self):
        return self.__student_comments

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #student_comments attribute.
    @student_comments.setter
    def student_comments(self,value):
    #    if (type(value)!=str):
    #        raise CommentsError("Value must be a string.")
        self.__student_comments=value

    #A getter accessor method to allow read-only access to the student_status attribute from outside of
    #the AttendanceRecord class.
    @property
    def student_status(self):
        return self.__student_status

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #student_status attribute.
    @student_status.setter
    def student_status(self,value):
    #    if (type(value)!=str):
    #        raise StudentStatusError("Value must be a string.")
        self.__student_status=value

    #A getter accessor method to allow read-only access to the attendance_count attribute from outside
    #of the AttendanceRecord class.
    @property
    def attendance_count(self):
        return self.__attendance_count

    #A setter mutator method that will produce an error if a negative value or a string is passed to
    #the attendance_count attribute.
    @attendance_count.setter
    def attendance_count(self,value):
    #    if (value==None):
    #        raise AttendanceCountError("Value cannot be None")
    #    elif (not isinstance(value,str)):
    #        raise AttendanceCountError("Value cannot be string")
    #    elif (len(value.strip())<=0):
    #        raise AttendanceCountError("Value cannt be an empty string")
        self.__attendance_count=value

    #A getter accessor method to allow read-only access to the attendance_rate attribute from outside
    #of the AttendanceRecord class.
    @property
    def attendance_rate(self):
        return self.__attendance_rate

    #A setter mutator method that will produce an error if a negative value or a string is passed to
    #the attendance_rate attribute.
    @attendance_rate.setter
    def attendance_rate(self,value):
    #    if (type(value)!=str):
    #        raise AttendanceRateError("Value must be a string.")
        self.__attendance_rate=value

    #A getter accessor method to allow read-only access to the teacher_id attribute from outside of the AttendanceRecord
    #class.
    @property
    def teacher_id(self):
        return self.__teacher_id

    #A setter mutator method that will produce an error if a negative value or a string is passed to
    #the teacher_id attribute.
    @teacher_id.setter
    def teacher_id(self,value):
    #    if (value==None):
    #        raise IdError("Value cannot be None")
    #    elif (not isinstance(value,str)):
    #        raise IdError("Value cannot be string")
    #    elif (len(value.strip())<=0):
    #        raise IdError("Value cannt be an empty string")
        self.__teacher_id=value

    #A getter accessor method to allow read-only access to the teacher_title attribute from outside of the
    #AttendanceRecord class.
    @property
    def teacher_title(self):
        return self.__teacher_title

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #teacher_title attribute.
    @teacher_title.setter
    def teacher_title(self,value):
    #    if (type(value)!=str):
    #        raise TitleError("Value must be a string.")
        self.__teacher_title=value

    #A getter accessor method to allow read-only access to the teacher_first_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def teacher_first_name(self):
        return self.__teacher_first_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #teacher_first_name attribute.
    @teacher_first_name.setter
    def teacher_first_name(self,value):
    #    if (type(value)!=str):
    #        raise FirstNameError("Value must be a string.")
        self.__teacher_first_name=value

    #A getter accessor method to allow read-only access to the teacher_last_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def teacher_last_name(self):
        return self.__teacher_last_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #teacher_last_name attribute.
    @teacher_last_name.setter
    def teacher_last_name(self,value):
    #    if (type(value)!=str):
    #        raise LastNameError("Value must be a string.")
        self.__teacher_last_name=value

    #A getter accessor method to allow read-only access to the teacher_phone attribute from outside of the
    #AttendanceRecord class.
    @property
    def teacher_phone(self):
        return self.__teacher_phone

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #teacher_phone attribute.
    @teacher_phone.setter
    def teacher_phone(self,value):
    #    if (type(value)!=str):
    #        raise PhoneError("Value must be a string.")
        self.__teacher_phone=value

    #A getter accessor method to allow read-only access to the e_contact_id attribute from outside of the AttendanceRecord
    #class.
    @property
    def e_contact_id(self):
        return self.__e_contact_id

    #A setter mutator method that will produce an error if a negative value or a string is passed to
    #the e_contact_id attribute.
    @e_contact_id.setter
    def e_contact_id(self,value):
    #    if (value==None):
    #        raise IdError("Value cannot be None")
    #    elif (not isinstance(value,str)):
    #        raise IdError("Value cannot be string")
    #    elif (len(value.strip())<=0):
    #        raise IdError("Value cannt be an empty string")
        self.__e_contact_id=value

    #A getter accessor method to allow read-only access to the e_contact_first_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def e_contact_first_name(self):
        return self.__e_contact_first_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #e_contact_first_name attribute.
    @e_contact_first_name.setter
    def e_contact_first_name(self,value):
    #    if (type(value)!=str):
    #        raise FirstNameError("Value must be a string.")
        self.__e_contact_first_name=value

    #A getter accessor method to allow read-only access to the e_contact_last_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def e_contact_last_name(self):
        return self.__e_contact_last_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #e_contact_last_name attribute.
    @e_contact_last_name.setter
    def e_contact_last_name(self,value):
    #    if (type(value)!=str):
    #        raise LastNameError("Value must be a string.")
        self.__e_contact_last_name=value

    #A getter accessor method to allow read-only access to the e_contact_phone attribute from outside of the
    #AttendanceRecord class.
    @property
    def e_contact_phone(self):
        return self.__e_contact_phone

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #e_contact_phone attribute.
    @e_contact_phone.setter
    def e_contact_phone(self,value):
    #    if (type(value)!=str):
    #        raise PhoneError("Value must be a string.")
        self.__e_contact_phone=value

    #A getter accessor method to allow read-only access to the e_contact_comments attribute from outside of the
    #AttendanceRecord class.
    @property
    def e_contact_comments(self):
        return self.__e_contact_comments

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #e_contact_comments attribute.
    @e_contact_comments.setter
    def e_contact_comments(self,value):
    #    if (type(value)!=str):
    #        raise CommentsError("Value must be a string.")
        self.__e_contact_comments=value

    #A getter accessor method to allow read-only access to the e_contact_relationship attribute from outside of the
    #AttendanceRecord class.
    @property
    def e_contact_relationship(self):
        return self.__e_contact_relationship

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #e_contact_relationship attribute.
    @e_contact_relationship.setter
    def e_contact_relationship(self,value):
    #    if (type(value)!=str):
    #        raise RelationshipError("Value must be a string.")
        self.__e_contact_relationship=value

    #A getter accessor method to allow read-only access to the classroom_name attribute from outside of the
    #AttendanceRecord class.
    @property
    def classroom_name(self):
        return self.__classroom_name

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #classroom_name attribute.
    @classroom_name.setter
    def classroom_name(self,value):
    #    if (type(value)!=str):
    #        raise ClassroomNameError("Value must be a string.")
        self.__classroom_name=value

    #A getter accessor method to allow read-only access to the classroom_status attribute from outside of the
    #AttendanceRecord class.
    @property
    def classroom_status(self):
        return self.__classroom_status

    #A setter mutator method that will produce an error if a string data type is not passed to the
    #classroom_status attribute.
    @classroom_status.setter
    def classroom_status(self,value):
    #    if (type(value)!=str):
    #        raise ClassroomStatusError("Value must be a string.")
        self.__classroom_status=value

    #A getter accessor method to allow read-only access to the classroom_date attribute from outside of the
    #AttendanceRecord class.
    @property
    def classroom_date(self):
        return self.__classroom_date

    #A setter mutator method that will produce an error if a the date is not passed to the
    #classroom_date attribute in the correct format.
    @classroom_date.setter
    def classroom_date(self,value):
    #    try:
    #        self.__classroom_date=datetime.datetime.strptime(value,"%Y-%m-%d")
    #    except:
    #        raise ClassroomDateError(value+" must be in the format YYYY-MM-DD")
        self.__classroom_date=value

    #A getter accessor method to allow read-only access to the classroom_day attribute from outside of the
    #AttendanceRecord class.
    @property
    def classroom_day(self):
        return self.__classroom_day

    #A setter mutator method that will produce an error if a negative value or a string is passed to
    #the classroom_day attribute.
    @classroom_day.setter
    def classroom_day(self,value):
    #    if (value==None):
    #        raise ClassroomDayError("Value cannot be None")
    #    elif (not isinstance(value,str)):
    #        raise ClassroomDayError("Value cannot be string")
    #    elif (len(value.strip())<=0):
    #        raise ClassroomDayError("Value cannt be an empty string")
        self.__classroom_day=value

#A class that runs the roll marker program backend module methods. Using the name RollMarkerManager as
#it captures the escence of the core purpose of the program.
class RollMarkerManager:
    def __init__(self):
        #A variable to store a list of data. Using the name attendance_records as it is a good descriptor of
        #the data being stored.
        self.attendance_records=[]

    #A method that accepts several arguments to append newly entered records to the attendance_records list.
    #Using the name add_attendance_record as it is a suitable verb followed by the description of the method of
    #adding an attendance record to the list.
    def add_attendance_record(self,student_id,student_first_name,student_last_name,student_gender,student_phone,student_comments,student_status,attendance_count,attendance_rate,teacher_id,teacher_title,teacher_first_name,teacher_last_name,teacher_phone,e_contact_id,e_contact_first_name,e_contact_last_name,e_contact_phone,e_contact_comments,e_contact_relationship,classroom_name,classroom_status,classroom_date,classroom_day):
        #A variable to store the the data passed to the method by the arguments. Using the name new_record
        #as it represents new attendance record that will be appended to an exisiting list of records.
        new_record=None
        new_record=AttendanceRecord(student_id,student_first_name,student_last_name,student_gender,student_phone,student_comments,student_status,attendance_count,attendance_rate,teacher_id,teacher_title,teacher_first_name,teacher_last_name,teacher_phone,e_contact_id,e_contact_first_name,e_contact_last_name,e_contact_phone,e_contact_comments,e_contact_relationship,classroom_name,classroom_status,classroom_date,classroom_day)
        self.attendance_records.append(new_record)

    #A method that accepts an argument of a partial classroom name to search the attendance_records list for.
    #matching classroom names. The method than yeilds the results of that search.
    def get_matching_classroom(self,classroom_name_partial):
        #A variable to store a partical classroom name that can be used to search the attendance_record list.
        classroom_name_partial=classroom_name_partial.lower()
        for c in self.attendance_records:
            if classroom_name_partial in c.classroom_name.lower():
                yield c

    #A method that accepts an argument of a partial student name to search the attendance_records list for.
    #matching student names. The method than yeilds the results of that search.
    def get_matching_student(self,student_name_partial):
        #A variable to store a partical student name that can be used to search the attendance_record list.
        student_name_partial=student_name_partial.lower()
        for s in self.attendance_records:
            if student_name_partial in s.student_first_name.lower():
                yield s

    #A method that can be called from the frontend module that accepts the argument file_name and reads data from
    #the external data file given to it by the variable file_name. Using the name load_from_file as it is a
    #suitable verb followed by a description of what the function is doing, loading data from a file.
    def load_data(self,file_name):
        #A variable that is being assigned the function of opening and closing an external file in order to read
        #data to the external file. Using the name file_object as it is a good descriptor of the file object.
        file_object=open(file_name,"r")
        #A variable to store the data that is being read from each line of the external file. Using the name
        #line as it is a good descriptor of what is being captured, a line of data from the external file.
        line=file_object.readline()

        line=file_object.readline()
        while(line!=""):
            fields=line.strip().split(",")
            student_id=fields[0]
            student_first_name=fields[1]
            student_last_name=fields[2]
            student_gender=fields[3]
            student_phone=fields[4]
            student_comments=fields[5]
            student_status=fields[6]
            attendance_count=fields[7]
            attendance_rate=fields[8]
            teacher_id=fields[9]
            teacher_title=fields[10]
            teacher_first_name=fields[11]
            teacher_last_name=fields[12]
            teacher_phone=fields[13]
            e_contact_id=fields[14]
            e_contact_first_name=fields[15]
            e_contact_last_name=fields[16]
            e_contact_phone=fields[17]
            e_contact_comments=fields[18]
            e_contact_relationship=fields[19]
            classroom_name=fields[20]
            classroom_status=fields[21]
            classroom_date=fields[22]
            classroom_day=fields[23]
            self.add_attendance_record(student_id,student_first_name,student_last_name,student_gender,student_phone,student_comments,student_status,attendance_count,attendance_rate,teacher_id,teacher_title,teacher_first_name,teacher_last_name,teacher_phone,e_contact_id,e_contact_first_name,e_contact_last_name,e_contact_phone,e_contact_comments,e_contact_relationship,classroom_name,classroom_status,classroom_date,classroom_day)
            line=file_object.readline()
        file_object.close()

    #A method that that can be called from the frontend module that accepts the argument file_name and writes
    #data to the external data file given to it by the variable file_name. Using the name save_data as it is
    #a suiable verb followed by a description of what the function is doing, saving data to a file.
    def save_data(self,file_name):
        #A variable to capture the length of the attendance_records lists to use in a while loop. Using the name
        #num_records as it is a good descriptor of what the variable is being used for.
        num_records=len(self.attendance_records)
        #A variable to capture a summary of data that can be written to an external file. Using
        #the name summary as it is providing a summary of the data that can be written to file.
        summary="Student ID,Student First Name,Student Last Name,Student Gender,Student Phone,Student Comments,Student Status,Attendance Count,Attendance Rate,Teacher ID,Teacher Title,Teacher First Name,Teacher Last Name,Teacher Phone,E Contact ID,E Contact First Name,E Contact Last Name,E Contact Phone,E Contact Comments,E Contact Relationship,Classroom Name,Classroom Status,Classroom Date,Classroom Day\n"
        #A variable to index the lines of data in the opportunities list starting at 0. This will be used in a
        #while loop to ensure that whilst the index is less than the number of opportunities in the list, the loop
        #will display a summary of that line of data. Using the name i as it is a good descriptor of what
        #it is being used for, to index the list of opportunities.
        i=0
        while(i<num_records):
            summary+=str(self.attendance_records[i].student_id)
            summary+=","+str(self.attendance_records[i].student_first_name)
            summary+=","+str(self.attendance_records[i].student_last_name)
            summary+=","+str(self.attendance_records[i].student_gender)
            summary+=","+str(self.attendance_records[i].student_phone)
            summary+=","+str(self.attendance_records[i].student_comments)
            summary+=","+str(self.attendance_records[i].student_status)
            summary+=","+str(self.attendance_records[i].attendance_count)
            summary+=","+str(self.attendance_records[i].attendance_rate)
            summary+=","+str(self.attendance_records[i].teacher_id)
            summary+=","+str(self.attendance_records[i].teacher_title)
            summary+=","+str(self.attendance_records[i].teacher_first_name)
            summary+=","+str(self.attendance_records[i].teacher_last_name)
            summary+=","+str(self.attendance_records[i].teacher_phone)
            summary+=","+str(self.attendance_records[i].e_contact_id)
            summary+=","+str(self.attendance_records[i].e_contact_first_name)
            summary+=","+str(self.attendance_records[i].e_contact_last_name)
            summary+=","+str(self.attendance_records[i].e_contact_phone)
            summary+=","+str(self.attendance_records[i].e_contact_comments)
            summary+=","+str(self.attendance_records[i].e_contact_relationship)
            summary+=","+str(self.attendance_records[i].classroom_name)
            summary+=","+str(self.attendance_records[i].classroom_status)
            summary+=","+str(self.attendance_records[i].classroom_date)
            summary+=","+str(self.attendance_records[i].classroom_day)+"\n"
            i+=1
        #A variable that is being assigned the function of opening and closing an external file in order to write
        #data to the external file. Using the name file_object as it is a good descriptor of the file object.
        file_object=open(file_name,"w")
        file_object.write(summary)
        file_object.close()
