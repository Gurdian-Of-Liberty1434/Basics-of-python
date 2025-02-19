import random
playing=True
number=str(random.randint(10,30))



while playing:
    print("I will generate a number from 10 to 30. You have to guess the number")
    guess=input("USE YOUR BRAIN! \n")
    if number==guess:
        print("YOUR ANSWER IS CORRECT! YOU WIN!")
        print("The number was",number)
        break
    else:
        print("incorrect, pls try again \n")
