import tkinter as tk
from random import choice

class RockPaperScissor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissor")
        self.window.geometry("300x200")

        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.window, text="Player Score: 0", font=("Arial", 12))
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0", font=("Arial", 12))
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.result_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=self.rock)
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=self.paper)
        self.paper_button.pack()

        self.scissor_button = tk.Button(self.window, text="Scissor", command=self.scissor)
        self.scissor_button.pack()

    def computer_choice(self):
        return choice(["rock", "paper", "scissor"])

    def rock(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.result_label.config(text="It's a tie!")
        elif computer == "paper":
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
            self.result_label.config(text="Paper covers rock! Computer wins!")
        else:
            self.player_score += 1
            self.player_score_label.config(text=f"Player Score: {self.player_score}")
            self.result_label.config(text="Rock smashes scissor! Player wins!")

    def paper(self):
        computer = self.computer_choice()
        if computer == "paper":
            self.result_label.config(text="It's a tie!")
        elif computer == "scissor":
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
            self.result_label.config(text="Scissor cuts paper! Computer wins!")
        else:
            self.player_score += 1
            self.player_score_label.config(text=f"Player Score: {self.player_score}")
            self.result_label.config(text="Paper covers rock! Player wins!")

    def scissor(self):
        computer = self.computer_choice()
        if computer == "scissor":
            self.result_label.config(text="It's a tie!")
        elif computer == "rock":
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
            self.result_label.config(text="Rock smashes scissor! Computer wins!")
        else:
            self.player_score += 1
            self.player_score_label.config(text=f"Player Score: {self.player_score}")
            self.result_label.config(text="Scissor cuts paper! Player wins!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissor()
    game.run()