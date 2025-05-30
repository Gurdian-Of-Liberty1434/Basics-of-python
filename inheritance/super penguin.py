#Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.

class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("penguin")
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()