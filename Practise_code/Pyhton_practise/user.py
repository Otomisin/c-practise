#!/usr/bin/python3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight/(height**2)
if BMI <= 18.5:
     print("Your BMI is 18, you are underweight.")
elif BMI > 18.5 and BMI < 25:
     print("Your BMI is 22, you have a normal weight.")
elif BMI > 25 and BMI < 30:
     print("Your BMI is 28, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
     print ("Your BMI is 33, you are obese.")
else:
     print ("Your BMI is 40, you are clinically obese.")
