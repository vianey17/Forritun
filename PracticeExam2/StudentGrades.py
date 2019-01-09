"""
Write a Python program that manages grades for 4 students. 
Each student has a unique name and 3 grades.

The user should be able to input the name of each student and the corresponding grades for each student.
Next the program should print the names of each student in alphabetical order along with their grades.
Finally, the program should print the name of the student with the highest average grade along with 
he student's average grade. The average grade should be printed with 2 digits after the decimal point.

If two or more students have the same average grade the student that appears first in the alphabetical order should be printed.
"""

class Student(object):
    def __init__(self,name):
        self.name = name
        self.grades_list = []
    
    def __str__(self):
        return "{}: {}".format(self.name,self.grades_list)
    
    def __lt__(self,other):
        return self.name < other.name
    
    def get_name(self):
        return self.name
    
    def add_grade(self):
        cardinal = len(self.grades_list) + 1
        try:
            grade = float(input("Input grade number {}: ".format(cardinal)))
            self.grades_list.append(grade)
            return self.grades_list
        except:
            print("Enter digits only")
            return self.add_grade()
    
    def gpa(self):
        gpa = sum(self.grades_list)/len(self.grades_list)
        return gpa
    
def print_student_with_highest_grade(students):
    highest_gpa = 0
    student_name = ""

    for student in students:
        if student.gpa() > highest_gpa:
            highest_gpa = student.gpa()
            student_name = student.get_name()
    
    print("\nStudent with highest average grade:")
    print("{} has an average grade of {:.2f}".format(student_name,highest_gpa))



def main():
    class_size = 4  # Number of students
    number_of_grades = 3  # How many assignments?
    students = []  # List will contain student classes

    for i in range(0,class_size):
        student_name = input("Input student name: ")
        student = Student(student_name)
        for j in range(0,number_of_grades):
            student.add_grade()
        students.append(student)
    students.sort()
    
    print("Student list")
    for student in students:
        print(student)
    
    print_student_with_highest_grade(students)



main()