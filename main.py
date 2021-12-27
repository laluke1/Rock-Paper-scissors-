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
choices = [rock, paper, scissors]

Com_c = random.randint(0, 2)

player_c = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))

print(f"\nComputer\'s choice: \n{choices[Com_c]}")
print(f"\nPlayer\'s choice:")
if player_c < 0 or player_c >= 3:
  print("Invalid number, You lose.")
else:
  print(choices[player_c])
  if player_c == Com_c:
    print("It's a draw... try again")
  else:
    if player_c == 0 and Com_c == 1:
      print("You Lose!!!")
    elif player_c == 0 and Com_c == 2:
      print("You Win!!!")
    elif player_c == 1 and Com_c == 0:
      print("You Win!!!")
    elif player_c == 1 and Com_c == 2:
      print("You lose!!!")
    elif player_c == 2 and Com_c == 0:
      print("You lose!!!")
    elif player_c == 2 and Com_c == 1:
      print("You Win!!!")


