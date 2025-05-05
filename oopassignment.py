class Smartphone:
    def __init__(self, model, version, screen_size, battery, camera, name):
        self.model = model
        self.version = version
        self.screen_size = screen_size
        self.battery = battery
        self.camera = camera
        self.name = name

    # Adding method
    def make_call(self, number):
        print(f"{self.name} is calling {number}.")

# Creating a phone and making a call
my_phone = Smartphone("Samsung", 11, 5.6, "5000mAh", "50MP", "Samsung A50")
print(my_phone.name)
print(my_phone.camera)
my_phone.make_call("0708564653")

#Add an inheritance layer to explore polymorphism or encapsulation.
class GamingSmartphone(Smartphone):
    def __init__(self, model, version, screen_size, battery, camera, name, refresh_rate):
        super().__init__(model, version, screen_size, battery, camera, name)
        self.__refresh_rate = refresh_rate  # private attribute

    def show_refresh_rate(self):  # FIXED: now it's inside the class
        print(f"This phone has a {self.__refresh_rate}Hz refresh rate")


        ##Using the gaming Smartphone
my_gaming_phone = GamingSmartphone("ROG", 12, 6.5, "6000mAh", "64MP", "ROG Phone", 144)
my_gaming_phone.make_call("0789123456")
my_gaming_phone.show_refresh_rate()

##Polymorphism Exercise
# Create a Car class
class Car:
    def move(self):
        print("Driving on the road")

# Create a Plane class
class Plane:
    def move(self):
        print("Flying in the sky")

# Create a Boat class
class Boat:
    def move(self):
        print("Sailing on water ")

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()
# Put all in a list
vehicles = [my_car, my_plane, my_boat]

# Loop through them and call move()
for vehicle in vehicles:
    vehicle.move()