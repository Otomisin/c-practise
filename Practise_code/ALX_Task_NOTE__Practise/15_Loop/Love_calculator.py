#!/usr/bin/python3

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bothNamesc = name1 + name2
bothNames = bothNamesc.lower()

t = bothNames.count("t")
r = bothNames.count("r")
u = bothNames.count("u")
e = bothNames.count("e")
true = t+r+u+e

l = bothNames.count("l")
o = bothNames.count("o")
v = bothNames.count("v")
e = bothNames.count("e")

love = l+o+v+e

total_score = int(str(true) + str(love))

if (total_score < 10) or (total_score > 90):
     print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 90):
    print(f"Your score is {total_score}, you are alright together.")
else:
     print(f"Your score is {total_score}.")
