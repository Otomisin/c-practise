"""
SEQUENCE UNPACKING:
You can assign the individual elements of a sequence to multiple variables.
This is known as sequence unpacking and it is handy in many situations.
https://learnbyexample.github.io/tips/python-tip-14/#:~:text=2022%2D08%2D03,is%20handy%20in%20many%20situations.
"""

details = ['2018-10-25', 'car', 2345]
purchase_date, vehicle, qty = details

print(purchase_date)
