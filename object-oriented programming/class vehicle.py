class vehicle:
    def __init__(self, max_speed, milleage):
        self.max_speed = max_speed
        self.millage = milleage

modelX = vehicle(240, 18)
print("Model max speed:",modelX.max_speed)
print("Model milleage:",modelX.millage)