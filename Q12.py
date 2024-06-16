class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}")

class CollegeStudent(Student):
    def __init__(self, name, roll_no, college):
        super().__init__(name, roll_no)
        self.college = college

    def display(self):
        super().display()
        print(f"College: {self.college}")

# Creating objects and displaying information
student1 = CollegeStudent("Sandesh Shrestha", 12345, "Inspiria Knowledge Campus")
student1.display()
