

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

game_image = [rock, paper, scissors]
# Collect user input number
users_choice = int(input("What do you choose? 0 for rock, 1 for paper and 2 for Scissors "))
if users_choice >= 3 or users_choice < 0:
     print(f"You typed an invalid number {users_choice} : ")
else:
     print (f"You choose {users_choice} {game_image[users_choice]}")

# Computer random number
     import random
     com_choice = random.randint(0, 2)
     print(f"Computer choose {com_choice} {game_image[com_choice]}")

     if users_choice == 0 and com_choice == 2:
          print()
          print ("You win! ")
     elif com_choice == 0 and users_choice == 2:
          print ("You lose")
     elif users_choice > com_choice:
          print(f"You win")
     elif com_choice > users_choice:
          print (f"You lose")
     elif users_choice == com_choice:
          print("It's a draw")
     else:
          print(f" You lose")
