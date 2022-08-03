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