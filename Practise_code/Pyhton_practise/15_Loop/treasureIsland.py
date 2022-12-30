#!/usr/bin/python3

"""
ASCII Art
https://ascii.co.uk/art
"""
print('''
        888     d8b                                      
        888     Y8P                                      
        888                                              
 .d8888b88888b. 88888888b.d88b. 88888b.  .d88b. 888  888 
d88P"   888 "88b888888 "888 "88b888 "88bd8P  Y8b888  888 
888     888  888888888  888  888888  88888888888888  888 
Y88b.   888  888888888  888  888888  888Y8b.    Y88b 888 
 "Y8888P888  888888888  888  888888  888 "Y8888  "Y88888 
                                                     888 
                                                Y8b d88P 
                                                 "Y88P" 
''')

print ("Welcome to chimmy games ##################### ")
print ("Your mission is to find the lost treasure")

decide = input("you\'re at a cross road, where do you want to go? Type Right or left ").lower()
if decide == "right":
     print("Congratulations, you can continue\n ")
     swimWait = input('You\' come to a lake. There is an island in the middle of the lake. Type "wait" to wait for  boat and type "swim" to swim \n').lower()
     if swimWait == "wait":
          print("Wellldone, you're waiting\n ")
          door = input("You arrived at an island unharmed. There is a house with 3 doors. One is red, one is yellow and one blue. which colour do you choose? : \n").lower()
          if door == "red":
               print("It's a room full of fire. Game over. ")
          elif door == "yellow":
               print("You found the treaure! You win!")
          elif door == "blue":
               print("You got attacked by an antry trout. Game over. ")
          else:
               print("You fell into a hole :( ")
     else: 
          print ("You got attacked by an angry trout. Game over. ")


else:     
     print("You fell into a hole, game over ")



