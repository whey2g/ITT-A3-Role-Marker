import sys
import datetime
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


    #A method used to reduce code throughout the program that requests user input and returns a
    #string. Using the name get_string as it is a suitable verb followed by the description of the method
    #of getting a string data type.
    def get_string(self,prompt):
        """Takes user input and returns a string.
        """
        sys.stdout.write(prompt)
        sys.stdout.flush()
        #A variable to capture user input. Using the name input_string as it is a suitable verb followed by
        #a description of what data type is being input.
        input_string = sys.stdin.readline().strip()
        while(len(input_string)==0):
            sys.stdout.write("Input cannot be blank. Please try again: ")
            sys.stdout.flush()
            value=sys.stdin.readline().strip()
        return input_string

    #A method used to reduce code throughout the program that requests user input and returns a
    #float. Using the name get_float as it is a suitable verb followed by the description of the
    #method of getting an float data type.
    def get_float(self,prompt):
        """Takes user input and returns a float.
        """
        #A variable to capture user input. User the name input_float as it is a suitable verb followed by
        #a description of what data type is being input.
        input_float=None
        while(input_float==None):
            try:
                input_float=float(self.get_string(prompt))
            except:
                prompt="Invalid entry. Please try again: "
        return input_float

    #A method used to reduce code throughout the program that requests user input and returns a
    #positive float. Using the name get_positive_float as it is a suitable verb followed by the description of the
    #method of getting a positive float data type.
    def get_positive_float(self,prompt):
        """Takes user input and returns a positive float.
        """
        #A variable to capture user input. User the name input_float as it is a suitable verb follwed by
        #a description of what data type is being input.
        input_positive_float=self.get_float(prompt)
        while(input_positive_float<0):
            input_positive_float=self.get_float("Invalid entry. Please enter a positive number: ")
        return input_positive_float

    def output_error(self,message):
        sys.stderr.write("Problem! "+message+"\n")

    def add_class_attendance_via_menu(self):
        pass

    def display_classroom_list_via_menu(self):
        sys.stdout.write("-------------\n")
        sys.stdout.write("Display Class\n")
        sys.stdout.write("-------------\n")
        sys.stdout.write("Enter partial class name to find ie. 1st: ")
        sys.stdout.flush()
        search_target=sys.stdin.readline().strip()

        self.search_and_display_matching_classroom(search_target)

    def find_student_via_menu(self):
        sys.stdout.write("------------\n")
        sys.stdout.write("Find Student\n")
        sys.stdout.write("------------\n")
        sys.stdout.write("Enter partial record name to find: ")
        sys.stdout.flush()
        search_target=sys.stdin.readline().strip()

        self.search_and_display_matching_students(search_target)

    def search_and_display_matching_classroom(self,search_target):
        sys.stdout.write("\n")
        #A variable to capture a summary of formatted data to be displayed on screen. Using the name
        #summary as it is providing a summary of the data that can be displayed.
        summary ="|-----------------------------------------Classroom Summary----------------------------------------|\n"
        summary+="|Student ID|Name                     |Gender |Phone       |Comments       |Status  |Attendance Rate|\n"
        sys.stdout.write(summary)

        num_matching_records=0
        for r in self.roll_marker.get_matching_classroom(search_target):
            #A variable to capture a rows of matched data to be displayed on screen. Using the name
            #row_text as it is providing a row of data that can be displayed.
            row_text="|"
            row_text+=(str(r.student_id)).ljust(10)+"|"
            row_text+=(str(r.student_first_name)).ljust(12)+" "+(str(r.student_last_name)).ljust(12)+"|"
            row_text+=(str(r.student_gender)).ljust(7)+"|"
            row_text+=(str(r.student_phone)).ljust(12)+"|"
            row_text+=(str(r.student_comments)).ljust(15)+"|"
            row_text+=(str(r.student_status)).ljust(8)+"|"
            row_text+=(str(r.attendance_rate)).ljust(15)+"|"
            num_matching_records+=1
            sys.stdout.write(row_text)
            sys.stdout.write("\n")

    def search_and_display_matching_students(self,search_target):
        sys.stdout.write("\n")
        #A variable to capture a summary of formatted data to be displayed on screen. Using the name
        #summary as it is providing a summary of the data that can be displayed.
        summary ="|---------------------------------------------------------------Student Summary---------------------------------------------------------------|\n"
        summary+="|Student ID|Name                     |Attendance Rate|Teacher           |Emergency Contact        |Phone       |Comments       |Relationship  |\n"
        sys.stdout.write(summary)

        num_matching_records=0
        for r in self.roll_marker.get_matching_student(search_target):
            #A variable to capture a rows of matched data to be displayed on screen. Using the name
            #row_text as it is providing a row of data that can be displayed.
            row_text="|"
            row_text+=(str(r.student_id)).ljust(10)+"|"
            row_text+=(str(r.student_first_name)).ljust(12)+" "+(str(r.student_last_name)).ljust(12)+"|"
            row_text+=(str(r.attendance_rate)).ljust(15)+"|"
            row_text+=(str(r.teacher_title)).ljust(5)+" "+(str(r.teacher_last_name)).ljust(12)+"|"
            row_text+=(str(r.e_contact_first_name)).ljust(12)+" "+(str(r.e_contact_last_name)).ljust(12)+"|"
            row_text+=(str(r.e_contact_phone)).ljust(12)+"|"
            row_text+=(str(r.e_contact_comments)).ljust(15)+"|"
            row_text+=(str(r.e_contact_relationship)).ljust(14)+"|"
            num_matching_records+=1
            sys.stdout.write(row_text)
            sys.stdout.write("\n")

home_roll_marker = RollMarkerUI()
home_roll_marker.run_roll_marker()
