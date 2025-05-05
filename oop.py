# Defining a class in Python
# A class is a blueprint for creating objects
class Car:
    color = "red"
    model = "Toyota"

     # Method/behaviour to display car details
    def drive(self):
            print("The car is driving")

my_car = Car() # Create an instance of the Car class         
my_car.drive() # Call the drive method on the instance
print(my_car.color) # Access the color attribute of the instance

# The __init__ method is a special method that initializes the object when it is created
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

        def personDetails(self):
            print(f"Name: {self.name}, Age: {self.age}")

    def myperson(name, age):
        personName = name
        personName = age

        myPerson(print("Name: ", "20"))

        print("Person details: ", personName, personAge)