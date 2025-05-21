class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+'(  '+self.meaning+'  )'

flashcards = []
print("Welcome to the flashcard creator!")
while (True):
    word = input("Enter a word: ")
    meaning = input("Enter its meaning: ")
    flashcard = Flashcard(word, meaning)
    flashcards.append(flashcard)
    choice = input("Do you want to add another flashcard? (yes/no): ")
    if choice.lower() != "yes":
        break

for flashcard in flashcards:
    print(flashcard)

while True:
    choice = input("Do you want to see the flashcards again? (yes/no): ")
    if choice.lower() == "yes":
        for flashcard in flashcards:
            print(flashcard)
    else:
        break
