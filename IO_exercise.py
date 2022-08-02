# Exercise 3: Convert Decimal number to octal using print() output formatting

num = 8
print('%o' % num)

#Exercise 5: Accept a list of 5 float numbers as an input from the user

numbers = []

for i in range(0,5):
    item = float(input("Enter number :"))
    numbers.append(item)

print(numbers)


# Exercise 6: Write all content of a given file into a new file by skipping line number 5

with open('test.txt', 'r') as ft:
    lines = ft.readlines()

with open('new_test.txt', 'w') as fnt:
    count = 0
    for line in lines:
        if count == 4:
            count+=1
            continue
        else:
            fnt.write(line)
        count+=1

with open('new_test.txt', 'r') as fnt:
    print(fnt.read())


# Exercise 7: Accept any three string from one input() call

str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)



# Exercise 8: Format variables using a string.format() method

totalMoney = 1000
quantity = 3
price = 450

print('I have {0} dollars so I can buy {1} football for {2:.2f} dollars.'.format(totalMoney, quantity, price))

# Exercise 9: Check file is empty or not

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')

# Exercise 10: Read line number 4 from the following file

with open('test.txt', 'r') as ft:
    lines = ft.readlines()
    print(lines[3])

