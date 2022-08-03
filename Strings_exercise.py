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

