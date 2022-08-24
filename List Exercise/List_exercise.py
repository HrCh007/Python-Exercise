# Exercise 2: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

print('\n')

# Exercise 3: Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]

squares = [ i * i for i in numbers]
print(squares)

print('\n')

# Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i + j)

print(list3)

print('\n')

# Exercise 5: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

print('\n')

# Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res = list(filter(None, list1))
print(res)

print('\n')

# Exercise 7: Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

print('\n')

# Exercise 10: Remove all occurrences of a specific item from a list.

val = 20
list1 = [5, 20, 15, 20, 25, 50, 20]

res = [ i for i in list1 if i != val]
print(res)

print('\n')

