import time

import project_functions as pf


students_0 = {

}

students_1 = {
     
}

students_2 = {
     
}

students_3 = {
     
}

students_4 = {
     
}


running = True

print("LOADING PROGRAM -------------")
while running:
        student = input("\nEnter the students name: ")
        math = int(input("\nEnter their math score: "))
        physics = int(input("Enter their physics score: "))
        chemistry = int(input("Enter their chemistry score: "))
        biology = int(input("Enter their biology score: "))
        

        average = int((math + physics + chemistry + biology) / 4)

        students_0[student] = average
        students_1[student] = math
        students_2[student] = physics
        students_3[student] = chemistry
        students_4[student] = biology
        
        print(f"{student.title()}'s Performance: ")
        pf.avg(average)

        cont = input(f"Would you like to input another students data?(Y/N)")

        if cont.capitalize() == 'Y':
             continue
        elif cont.capitalize() == 'N':
             break
    
while True:
     scores = input(f"Would you like an overview of the students scores(Y/N)")

     if scores.capitalize() == 'N':
          print(f"Fin")
          break
     elif scores.capitalize() == 'Y':
          for student, average in students_0.items():
               print(f"{student.capitalize()}'s average is: {average}")
          print(f"\n")
          for student, math in students_1.items():
               print(f"{student.capitalize()}'s math score is: {math}")
          print(f"\n")
          for student, physics in students_2.items():
               print(f"{student.capitalize()}'s physics score is: {physics}")
          print(f"\n")
          for student, chemistry in students_3.items():
               print(f"{student.capitalize()}'s chemistry score is: {chemistry}")
          print(f"\n")
          for student, biology in students_4.items():
               print(f"{student.capitalize()}'s biology score is: {biology}")   