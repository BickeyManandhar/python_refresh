import random

def play_scissor_paper_rock():
    user = int(input("Enter your choice (0 for scissor, 1 for paper, 2 for rock): "))
    dict_choices = {0: "scissor", 1: "paper", 2: "rock"}
    computer = random.randint(0, 2)
    try:
      print(computer)
      print(f"You chose: {dict_choices[user]}")
      print(f"Computer chose: {dict_choices[computer]}")
      if user == computer:
          print("It's a draw!")
      elif (user == 0 and computer == 1) or \
          (user == 1 and computer == 2) or \
          (user == 2 and computer == 0):
          print("You win!")
      else:
          print("Computer wins!")     
    except KeyError:
      print("Invalid input! Please enter 0, 1, or 2.")

play_scissor_paper_rock()