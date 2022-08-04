# Exercise 1A: Create a string made of the first, middle and last character

str1 = "James"
str2 =  str1[0] + str1[len(str1)//2] + str1[len(str1)-1]
print(str2)

# Exercise 1B: Create a string made of the middle three characters

str1 = "James"
ms = len(str1) // 2
str2 = str1[ms-1:ms+2]
print(str2) 

# Exercise 2: Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"

ms = len(s1) // 2
x = s1[:ms] + s2 + s1[ms:]
print(x)

# Exercise 4: Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"
str2 = ""
for ch in str1:
    if ch.islower():
        str2 = str2 + ch
for ch in str1:
    if ch.isupper():
        str2 = str2 + ch

print(str2)

# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, 
# and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

s1_length = len(s1)
s2_length = len(s2)

length = s1_length if s1_length > s2_length else s2_length
result = ""

s2 = s2[::-1]

for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

# Exercise 7: String characters balance Test

s1 = "Ynf"
s2 = "PYnative"
flag = True
for ch in s1:
    if ch in s2:
        continue
    else:
        flag = False

print(flag)

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"

sub_string = "USA"

temp_str = str1.lower()

count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

# Exercise 9: Calculate the sum and average of the digits present in a string

input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)

# Exercise 11: Reverse a given string

str1 = "PYnative"
print("Original String is:", str1)

str1 = str1[::-1]
print("Reversed String is:", str1)

# Exercise 13: Split a string on hyphens

str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)

# Exercise 16: Remove all characters from a string except integers

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

res = "".join([item for item in str1 if item.isdigit()])

print(res)

