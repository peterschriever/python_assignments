# 6: 1/6 + 1/3 + 1/2 + 1/1 = 2, cijfers rechts = 3 + 2 + 1 = 6
# 28: 1/28 + 1/14 + 1/7 + 1/4 + 1/2 + 1/1 = 2 etc..
#
# if 2^P - 1 == a prime number
# 2^P - 1 * (2^P - 1)
# will result in an even perfect number.

# This program and the formula used will only find even perfect numbers.
# At the time of writing this an odd perfect number has yet to be found.
# Thus it falls outside of the scope of this program.
# Notice when talking about prime numbers I reference the Mersenne Primes.

# debugging
import time, re
startTime = time.time()

# Don't look for higher perfect numbers than this.
# The higher the number, the longer execution of the program is
hard_cap = 10000

# empty lists to store the prime/perfectNumbers
primeNumbers = []
perfectNumbers = []

# test with regexp. Results: slower
# def is_prime(n):
#     return not re.match(r'^.?$|^(..+?)\1+$', '1'*n)

# First we need to find some prime number
for p in range(2, hard_cap): # may be able to reduce the loop by a lot here
    # if is_prime(p): primeNumbers.append(p) # regex: slow
    isAPrime = True
    for i in range(2, p):
        if p % i == 0:
            isAPrime = False
            break
    if isAPrime:
        primeNumbers.append(p)

# Loop as long as the hard_cap won't be broken
for P in range(0, hard_cap):
    # Check if (2**P)-1 == a prime
    if ((2**P) - 1) in primeNumbers:
        if ((2**P) -1) == 120:
            print("120 found")

        # Perform perfectNumber formula
        perfectNumber = (2**(P-1)) * ((2**P) - 1)

        # Break if hard_cap is breached
        if perfectNumber >= hard_cap:
            break

        perfectNumbers.append(perfectNumber)

print(perfectNumbers)
print("--- %s seconds ---" % (time.time() - startTime))
