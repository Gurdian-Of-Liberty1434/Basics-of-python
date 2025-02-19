import random

while True:
    user_action=input("Enter a choice(Rock,Paper,Scissor):  ")
    possible_actions=["Rock","Paper","Scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\n You chose {user_action} and compute chose {computer_action}. \n")
    if user_action==computer_action:
        print("TIE!")
    elif user_action=="Rock":
        if computer_action=="Scissors":
            print("You win! Rock smashes Scissor")
        else:
            print("You lose! Paper covers Rock")
    elif user_action=="Paper":
        if computer_action=="Rock":
            print("You win! Paper covers Rock")
        else:
            print("You lose! Scissor cuts Paper")
    elif user_action=="Scissor":
        if computer_action=="Paper":
            print("You win! Scissor cuts Paper")
        else:
            print("You lose! Rock smashes Scissor")
    play_again=input("Play again? (y/n): ")
    if play_again !="y":
        break