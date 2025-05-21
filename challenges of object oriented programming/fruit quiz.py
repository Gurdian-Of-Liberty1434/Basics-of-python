import random

class FruitQuiz:
    def __init__(self, fruits):
        self.fruits = fruits

    def play(self):
        fruit = random.choice(list(self.fruits.keys()))
        color = input("What is the color of the {}? ".format(fruit))
        if color.lower() == self.fruits[fruit].lower():
            print("Correct!")
        else:
            print("Incorrect. The correct color is {}.".format(self.fruits[fruit]))

fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grape": "purple",
    "kiwi": "green"
}

quiz = FruitQuiz(fruits)
quiz.play()
