"""
LEARN TO PROGRAM 2
https://www.youtube.com/watch?v=swQEbZ6ez1I&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=2&ab_channel=DerekBanas

"""
# Have a user  enter their investment amount and expected interest
# Ask for the invested  and interest rate
money = input("How much is your initial Investment? ")
interest_rate = input('How much is th interest rate? ')

# Convert value to float and round the percentage rate by 2
money = float(money)
interest_rate = float(interest_rate) * .01

# Cycle through the 10 years
for i in range(10):
    money = money + (money * interest_rate)
print("Interest after 10 years: {:.2f}".format(money))
