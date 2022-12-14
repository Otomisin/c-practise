
# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1

def factorial(num):
    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:

        result = num * factorial(num - 1)
        return result


print(factorial(4))

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2

# ---------- PROBLEM : CALCULATE FIBONACCI NUMBERS ----------
# To calculate Fibonacci numbers we sum the 2 previous
# values to calculate the next item in the list like this
# 1, 1, 2, 3, 5, 8 ...

# The Fibonacci sequence is defined by:
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

'''
Sample Run Though to Help
print(fib(3))

# 1st : result = fib(2) + fib(1) : 2 + 1
# 2nd : result = (fib(1) + fib(0)) + (fib(0)) : 1 + 0
# 3rd : result = fib(2) + fib(1)

print(fib(4))

# 1st : result = fib(3) + fib(2) : 3 + 2
# 2nd : result = (fib(2) + fib(1)) + (fib(1) + fib(0)) : 2 + 1
# 3rd : result = (fib(1) + fib(0)) + fib(0) : 1 + 0
'''


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        result = fib(n - 1) + fib(n - 2)
        return result


print(fib(3))

print(fib(4))