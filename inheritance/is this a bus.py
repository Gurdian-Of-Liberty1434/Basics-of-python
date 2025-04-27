class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle): 
    pass
school_bus=bus("School Volvo",180,12)
print("Vehicle Name:",school_bus.name,"Vehicle Max Speed:",school_bus.max_speed,"Vehicle Mileage:",school_bus.mileage)