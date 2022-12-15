import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]

# Thought process: [your choice, computer's choice] 
# [0,0] -> Rock, Rock -> DRAW 
# [0,1] -> Rock, Paper -> You lose
# [0,2] -> Rock, Scissors -> You win

decision_matrix = [
  ["It\'s a draw", "You lose", "You win!"],
  ["You win!", "It\'s a draw", "You lose"],
  ["You lose", "You win!", "It\'s a draw"]
]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
if user_choice > 2 or user_choice < 0:
  print("Invalid choice selection, you lose 🤷‍♀️")
  # Otherwise IndexError comes up
else:
  print(choice_list[user_choice])
  # Computer's turn
  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(choice_list[computer_choice])
  
  result = decision_matrix[user_choice][computer_choice]
  print(result)