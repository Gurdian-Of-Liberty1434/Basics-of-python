#Write a Python program to create two classes - BMW and Ferrari with similar methods and implement polymorphismPolymorphism on them.
class BMW:
    def move(self):
        print("BMW is moving")
class Ferrari:
    def move(self):
        print("Ferrari is moving")

bmw = BMW()
ferrari = Ferrari()
for car in (bmw,ferrari):
    car.move()
    