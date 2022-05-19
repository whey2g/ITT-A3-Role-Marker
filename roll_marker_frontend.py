import sys
import roll_marker_backend

#A class that runs the roll marker program, writing and displaying menus, calling and
#accepting user input. Using the name RollMarkerUI as RollMarker captures the escence of the core
#purpose of the program, UI stands for User Interface which is the role of this class.
class RollMarkerUI():
    #A variable that is being assigned the class RollMarkerManager from the backend module to reduce code
    #throughout the program. Using the name roll_marker as it calling a roll_marker (manager) class
    #from the backend module.
    roll_marker = roll_marker_backend.RollMarkerManager()

    def run_roll_marker(self):
        #A variable that takes the file name passed to it by the constructor method. using the name
        #file_name as it is a good descriptor of what is being stored.
        data_file_name="dataset_day5.csv"
        try:
            self.roll_marker.load_data(data_file_name)
        except Exception as e:
            self.output_error(str(e)+". Could not load from file "+data_file_name)
        #A variable to capture and store a users selection from the provided menu options.
        choice=self.get_menu_choice()
        while(choice!="x"):
            sys.stdout.write("\n")
            if choice=="a":
                self.add_class_attendance_via_menu()
            elif choice=="d":
                self.display_classroom_list_via_menu()
            elif choice=="f":
                self.find_student_via_menu()
                choice=self.get_menu_choice()
        try:
            self.roll_marker.save_data(data_file_name)
        except Exception as e:
            self.output_error(str(e)+". could not save to file "+data_file_name)

    def get_menu_choice(self):
        menu="\n|------------------------------|\n"
        menu +="|---------Roll Marker----------|\n"
        menu +="|---------by Cloud 11----------|\n"
        menu +="|------------------------------|\n"
        menu +="|[A]dd Class Attendance        |\n"
        menu +="|[D]isplay Classroom List      |\n"
        menu +="|[F]ind Student                |\n"
        menu +="|E[x]it                        |\n"
        menu +="|------------------------------|\n"

        sys.stdout.write(menu)

        menu=menu.lower()
        choice=self.get_string("Enter choice: ").lower()
        while not "["+choice+"]" in menu:
            choice=self.get_string(choice+" was an invalid choice. Please try again: ").lower()
        return choice


    #A static method used to reduce code throughout the program that requests user input and returns a
    #string. Using the name get_string as it is a suitable verb followed by the description of the method
    #of getting a string data type.
    @staticmethod
    def get_string(prompt:str)->str:
        """Takes user input and returns a string.
        """
        sys.stdout.write(prompt)
        #A variable to capture user input. Using the name input_string as it is a suitable verb followed by
        #a description of what data type is being input.
        input_string = sys.stdin.readline().strip()
        return input_string

    #A static method used to reduce code throughout the program that requests user input and returns an
    #integer. Using the name get_integer as it is a suitable verb followed by the description of the
    #method of getting an integer data type.
    @staticmethod
    def get_integer(prompt:str)->int:
        """Takes user input and returns an integer.
        """
        #A variable to capture error message. Using the name error_message as it will deliver an error
        #message to the user should the user input an invalid entry.
        error_message = ""
        #A variable to capture user input. User the name input_integer as it is a suitable verb follwed by
        #a description of what data type is being input.
        input_integer = None
        while(input_integer==None):
            try:
                input_integer=int(RollMarkerUI.get_string(error_message+prompt))
            except:
                error_message="Invalid entry. Please enter a whole number.\n"
        return input_integer

    #A static method used to reduce code throughout the program that requests user input and returns a
    #float. Using the name get_float as it is a suitable verb followed by the description of the
    #method of getting an float data type.
    @staticmethod
    def get_float(prompt:str)->float:
        """Takes user input and returns a float.
        """
        #A variable to capture error message. Using the name error_message as it will deliver an error
        #message to the user should the user input an invalid entry.
        error_message = ""
        #A variable to capture user input. User the name input_float as it is a suitable verb followed by
        #a description of what data type is being input.
        input_float = None
        while(input_float==None):
            try:
                input_float=float(RollMarkerUI.get_string(error_message+prompt))
            except:
                error_message="Invalid entry. Please enter a number.\n"
        return input_float

    #A static method used to reduce code throughout the program that requests user input and returns a
    #positive float. Using the name get_positive_float as it is a suitable verb followed by the description of the
    #method of getting a positive float data type.
    @staticmethod
    def get_positive_float(prompt:float)->float:
        """Takes user input and returns a positive float.
        """
        #A variable to capture error message. Using the name error_message as it will deliver an error
        #message to the user should the user input an invalid entry.
        error_message = ""
        #A variable to capture user input. User the name input_float as it is a suitable verb follwed by
        #a description of what data type is being input.
        input_positive_float = RollMarkerUI.get_float(prompt)
        while(input_positive_float<0):
            try:
                input_positive_float=float(RollMarkerUI.get_float(error_message+prompt))
            except:
                error_message="Invalid entry. Please enter a positive number.\n"
        return input_positive_float

    def output_error(self,message):
        sys.stderr.write("Problem! "+message+"\n")

    def add_class_attendance_via_menu():
        pass

    def display_classroom_list_via_menu():
        pass

    def find_student_via_menu():
        pass

home_roll_marker = RollMarkerUI()
home_roll_marker.run_roll_marker()
