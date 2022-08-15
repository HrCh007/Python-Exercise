# Exercise 1: Print First 10 natural numbers using while loop

i = 1
while i <= 10:
    print(i)
    i+=1

print('\n')

# Exercise 2: Print the following pattern


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = '') 
    print('')

print('\n')

# Exercise 3: Calculate the sum of all numbers from 1 to a given number

n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)

print('\n')

# Exercise 7: Print the following pattern


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end = '') 
    print('')

print('\n')

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

print('\n')

# Exercise 11: Write a program to display all prime numbers within a range

# range
start = 25
end = 50

for i in range(start,end):
    temp = 1
    for j in range(2,i//2):
        if i % j == 0:
            temp = 0
            break
    if temp:
        print(i)

print('\n')

#Exercise 14: Reverse a given integer number

x = 66374
n = 0
while x > 0:
    t = x % 10
    n = n*10 + t
    x = x // 10

print(n)

print('\n')

# Exercise 15: Use a loop to display elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

ll = len(my_list)

for i in range(ll):
    if i % 2 == 1:
        print(my_list[i], end = " ")

print('\n')

# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n = 5
num = 0
sum = 0
for i in range(1,n+1):
    num = num * 10 + 2
    sum = sum + num

print(sum)

print('\n')

# Exercise 18: Print the following pattern
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
n = 5

for i in range(1,n+1):
    for j in range(i):
        print('*', end = " ")
    print("")

for i in range(n-1,0,-1):
    for j in range(i):
        print("*", end = " ")
    print("")

print('\n')