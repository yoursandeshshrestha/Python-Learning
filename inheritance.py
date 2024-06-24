# Parent class
class Animal:
    def speak(self):
        return "Animal makes a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Dog says Woof!"

dog = Dog()

print(dog.speak())  # Output: Dog says Woof!
