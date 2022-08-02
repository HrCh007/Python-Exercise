# Exercise 1: Print First 10 natural numbers using while loop

i = 1
while i <= 10:
    print(i)
    i+=1

# Exercise 2: Print the following pattern


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = '') 
    print('')

# Exercise 3: Calculate the sum of all numbers from 1 to a given number

n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)

# Exercise 7: Print the following pattern


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end = '') 
    print('')

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)


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
