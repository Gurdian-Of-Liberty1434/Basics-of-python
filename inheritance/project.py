#create a bus child class that inherits from the vehicle class to calculate the total fare

class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class bus(vehicle):
    def __init__(self,name,max_speed,mileage):
        super().__init__(name,max_speed,mileage)

    def fare(self):
        return self.capacity*100

school_bus=bus("School Volvo",180,12)
print("Vehicle Name:",school_bus.name,"Vehicle Max Speed:",school_bus.max_speed,"Vehicle Mileage:",school_bus.mileage)