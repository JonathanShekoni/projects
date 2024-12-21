class EmptyRosterError(Exception):
    def __str__(self):
        return "Exception: Course Roster is Empty"


class StudentNotFoundError(Exception):
    def __init__(self, student_id):
        self.message = f"Exception: Student ({student_id}) not found"

    def __str__(self):
        return self.message


class GradeItemNotFoundError(Exception):  
    def __init__(self, grade_item_name):
        self.message = f"Exception: Grade Item ({grade_item_name}) not found"

    def __str__(self):
        return self.message


class Student:
    #Initialize Student Class
    def __init__(self,first_name,last_name,student_id):
        self.fname = first_name
        self.lname = last_name
        self.student_id = student_id

    def get_last_name(self):
        return self.lname
        
    def get_first_name(self):
        return self.fname
    
    def get_student_id(self):
        return self.student_id


class GradeItem:
    #Initialize GradeItem Class
    def __init__(self,assignment_name,total_points,grades):
        self.name = assignment_name
        self.points = total_points
        self.grades = grades

    def get_name(self):
        return self.name
    
    def get_total_points(self):
        return self.points

    def add_student_grade(self,student_id,grade):
        self.grades[student_id] = grade

    def get_student_grade(self,student_id):
        return self.grades.get(student_id,None)


class Course:
    #roster contains a list of student objects
    #grade_items contains a list of GradeItem objects
    #Initialize Course Class
    def __init__(self):
        self.roster = []
        self.grade_items = []

    def add_student(self,student):
        self.roster.append(student)

    def add_grade_item(self,gradeitem):
        self.grade_items.append(gradeitem)

    def add_student_grade(self,grade_item_name,student_id,grade):

        if not self.roster:
            raise EmptyRosterError()
        

        for grade_item in self.grade_items:
            if grade_item.get_name() == grade_item_name:
                for student in self.roster:
                    if student.get_student_id() == student_id:
                        grade_item.add_student_grade(student_id, grade)
                        return
                raise StudentNotFoundError(student_id)
        raise GradeItemNotFoundError(grade_item_name)
            
    def print_student_grade(self,student_id):
        if not self.roster:
            raise EmptyRosterError()

        for student in self.roster:
            if student.get_student_id() == student_id:
                id = student.get_student_id()
                fname = student.get_first_name()
                lname = student.get_last_name()
                print(f"{lname}, {fname} ({id})", end = ' | ')

                for grade_item in self.grade_items:
                    grade = grade_item.get_student_grade(student_id)
                    if grade is None:
                        grade = "N/A"
                    print(f"{grade_item.get_name()}: {grade} ({grade_item.get_total_points()})", end = ' | ')
                print()
                return
        raise StudentNotFoundError(student_id)
    
    def print_roster(self):
        if not self.roster:
            raise EmptyRosterError()
        print("Class Roster")
        for student in self.roster:
            id = student.get_student_id()
            fname = student.get_first_name()
            lname = student.get_last_name()
            print(f"{lname}, {fname} ({id})")


    def print_class_grades(self):
        if not self.roster:
            raise EmptyRosterError()

        for student in self.roster:
            id = student.get_student_id()
            fname = student.get_first_name()
            lname = student.get_last_name()
            print(f"{lname}, {fname} ({id})", end=' | ')

            for grade_item in self.grade_items:
                grade = grade_item.get_student_grade(id)
                if grade is None:
                    grade = "N/A"
                print(f"{grade_item.get_name()}: {grade} ({grade_item.get_total_points()})", end=' | ')
            print()



        
course = Course()
print("""Welcome to CSC/DSCI 1301: Principles in CS/DS 1
Please choose one of the following options (Enter 'quit' or 'q' to exit).""")
print("1)Add a Student.\n2)Add a Grade Item.\n3)Add a Student's Grade.\n4)Print a Studen's Grades.")
print("5)Print Course Roster.\n6)Print Class Grades.\n")


while True:
    print()
    choice = input()
    if choice == '1':
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        try:
            id = int(input("Enter Student ID: "))
            student = Student(first_name, last_name, str(id))
            course.add_student(student)
        except ValueError:
            print("Error: Student ID must be a number.")
    elif choice == '2':
        assignment_name = input("Enter grade item name: ")
        try:
            total_points = int(input("Enter the total amount of points for the grade item: "))
            grade = GradeItem(assignment_name, total_points, {})
            course.add_grade_item(grade)
        except ValueError:
            print("Error: Total points must be a number.")
    elif choice == '3':
        grade_item = input("Enter grade item name: ")
        try:
            id = int(input("Enter Student ID: "))
            student_grade = int(input("Enter Student Grade: "))
            course.add_student_grade(grade_item, str(id), student_grade)
        except ValueError:
            print("Error: Student ID and grade must be numbers.")
        except EmptyRosterError as e:
            print(e)
        except StudentNotFoundError as e:
            print(e)
        except GradeItemNotFoundError as e:
            print(e)
    elif choice == '4':
        try:
            id = int(input("Enter Student ID: "))
            course.print_student_grade(str(id))
        except ValueError:
            print("Error: Student ID must be a number.")
        except EmptyRosterError as e:
            print(e)
        except StudentNotFoundError as e:
            print(e)
    elif choice == '5':
        try:
            course.print_roster()
        except EmptyRosterError as e:
            print(e)
    elif choice == '6':
        try:
            print("Class Grades:")
            course.print_class_grades()
        except EmptyRosterError as e:
            print(e)
    elif choice.lower() in ('quit', 'q'):
        break
    else:
        print("Error: Invalid choice. Please select a valid option.")