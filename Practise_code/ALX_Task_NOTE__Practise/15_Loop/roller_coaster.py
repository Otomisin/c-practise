# !/usr/bin/python3

print("Welcome to the rollercoater!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
     print ("You can ride the rollercoaster!")
     age = int(input("What is your age? "))
     if age < 12:
          bill = 5
          print("Please pay extra $5 and you.")
     elif age <= 18:
          bill = 7
          print("please pay $7.")
     else:
          bill = 12
          print("Please pay $12.")

     #Ask if they want photos 
     photo = input("Do you want a photo  take? Y or N.")
     if photo == "Y":
          bill += 3
          print(f"You will be paying {bill}")
     else:
          print(f"Your bill is {bill}")

else:
     print("You can't ride a rollercoaster")
