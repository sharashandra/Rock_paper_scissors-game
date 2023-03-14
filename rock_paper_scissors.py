import random


def rock_paper_scissor():
  if user == computer:
    print("Tie")
  elif user == "Rock":
    if computer == "scissors":
      print("Rock Smashes Scissors, You Win..!")
    else:
      print("Paper Covers Rock, You lose..!")
  elif user == "paper":
    if computer == "Rock":
      print("Paper covers rock, You Win..!")
    else:
      print("Scissors cut Paper, You Lose..!")
  elif user == "scissors":
    if computer == "paper":
      print("Scissors cuts paper, You Win..!")
    else:
      print("Rock Smaches Scissors, You Lose..!")


user = input("Enter a choice (rock, paper, scissors) : ")
possible_actions = ["Rock", "paper", "scissors"]
computer = random.choice(possible_actions)
rock_paper_scissor()
