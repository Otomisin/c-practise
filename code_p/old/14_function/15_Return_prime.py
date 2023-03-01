# ---------- RETURN A LIST OF PRIMES ----------
# A prime can only be divided by 1 and itself
# 5 is prime because 1 and 5 are its only positive factors
# 6 is a composite because it is divisible by 1, 2, 3 and 6

# We'll receive a request for primes up to the input value
# We'll then use a for loop and check if modulus == 0 for
# every value up to the number to check
# If modulus == 0 that means the number isn't prime

def isprime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):

        # If any division has no remainder we know it
        # isn't a prime number
        if (num % i) == 0:
            return False
    return True


def getPrimes(max_number):
    # Create a list to hold primes
    list_of_primes = []

    # This for loop cycles through primes from 2 to
    # the maximum value requested
    for num1 in range(2, max_number):

        if isprime(num1):
            list_of_primes.append(num1)

    return list_of_primes


max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)