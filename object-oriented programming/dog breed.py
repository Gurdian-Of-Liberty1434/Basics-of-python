#Write a program to create a dog class with one class variable and two instance variables, and display the details of dogs of two different breed

class Dog:
    species="german shepherd"
    def __init__(self,name,age):
        self.name=name
        self.age=age

minky = Dog("Minky", 5)
wooly = Dog("Wooly", 8)

print("Minky is a {}".format(minky.__class__.species))
print("Wooly is also a {}".format(wooly.__class__.species))

print("{} is {} years old".format(minky.name, minky.age))
print("{} is {} years old".format(wooly.name, wooly.age))
