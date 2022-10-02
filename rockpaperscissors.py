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
game_images = [rock, paper, scissors]
print("Welcome to rock, paper, scissors online!\n")
player = int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

random = random.randint(0, 2)

print(f"Computer choose:\n {game_images[random]}\n")

if player == 0:
  if random == 0:
    print("Tie.")
  elif random == 1:
    print("You lose.")
  else:
    print("You win!")
elif player == 1:
  if random == 0:
    print("You win!")
  elif random == 1:
    print("Tie.")
  else:
    print("You lose.")
else:
  if random == 0:
    print("You lose.")
  elif random == 1:
    print("You win!")
  else:
    print("Tie.")
