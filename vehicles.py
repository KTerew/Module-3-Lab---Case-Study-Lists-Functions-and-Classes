class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType


class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def printCarInfo(self):
        print(f"Vehicle type: {self.vehicleType}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

userInput = input("Please enter vehicle type: ")
userVehicle = Vehicle(userInput)

yearInput = int(input(f"Please enter the {userVehicle.vehicleType}\'s year: "))
makeInput = input(f"Please enter the {userVehicle.vehicleType}\'s make: ")
modelInput = input(f"Please enter the {userVehicle.vehicleType}\'s model: ")
doorInput = int(input(f"Please enter the {userVehicle.vehicleType}\'s number of doors: "))
roofInput = input(f"Please enter the {userVehicle.vehicleType}\'s type of roof: ")

userCar = Automobile(userVehicle.vehicleType, yearInput, makeInput, modelInput, doorInput, roofInput)

userCar.printCarInfo()
