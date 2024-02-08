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

#Write your code below this line 👇
import random

game = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if player == 0:
    print(game[0])
elif player == 1:
    print(game[1])
elif player == 2:
    print(game[2])
else:
    print("Wrong number or letter")

computer = random.randint(0, 2)
computer_pick = game[computer]
print(f"Computer chose: {computer_pick} ")
if player == computer:
    print("Draw")
elif player == 0 and computer == 2:
    print("You win")
elif player == 1 and computer == 0:
    print("You win")
elif player == 2 and computer == 1:
    print("You win")
else:
    print("You lose")
