# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
person1 = Person("Sandesh Shrestha", 19)
person2 = Person("Jasmine Thapa", 20)

# Displaying information
person1.display()
person2.display()
