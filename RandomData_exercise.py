import random
import string

# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

for i in range(3):
    print(random.randrange(100,999,5), end = ", ")

print('\n')

# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

lottery_list = []

for i in range(100):
    lottery_list.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_list, 2)

print(winners)
print('\n')

# Exercise 3: Generate 6 digit random secure OTP

import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("Secure random OTP is ", otp,'\n')

# Exercise 4: Pick a random character from a given String

name = 'pynative'
char = random.choice(name)
print("random char is ", char, '\n')

# Exercise 5: Generate random String of length 5

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString(5) , '\n')

# Exercise 6: Generate a random Password which meets the following conditions
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Password is ", randomPassword(), '\n')

# Exercise 7: Calculate multiplication of two random float numbers

num1  = random.uniform(0.1,1)
print("First Random float is ", num1)
num2 = random.uniform(9.5, 99.5)
print("Second Random float is ", num2)

num3 = num1 * num2
print("Multiplication is ", num3)

# Exercise 8: Generate random secure token of 64 bytes and random URL

print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

# Exercise 9: Roll dice in such a way that every time you get the same number

dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))

# 