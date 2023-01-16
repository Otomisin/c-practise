
word_list = ["ardvark", "baboon", "camel"]
# using random.choice() to
# get a random number

import random
chosen_word = random.choice(word_list)
# print(word_list)

# for letter in chosen_word:
#      if letter == guess:
#           print("Right")
#      else:
#           print("Wrong")

# Check if the user letter is one of the choocen words

display  = []
word_len = range(len(chosen_word))
for _ in word_len:
     display += "_"
print (f"{display}\n")


end_of_game = False

while not end_of_game:
     guess = input('Guess an alphabet? ').lower()
     # change the postion of the choose n word with the "_"
     for position in word_len:
          letter = chosen_word[position]
          if letter == guess:
               display[position] = letter

     print(display)
if "_" not in display:
     end_of_game = True
     print ("All Gmaes guessed")

# display  = []
# for letter in word_list:
#      display += "_"
# print (display)

# print(displays)
