# Exercise 1: Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

print('\n')

# Exercise 4: Unpack the tuple into 4 variables

tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

print('\n')

# Exercise 5: Swap two tuples in Python

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)

print('\n')

# Exercise 7: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

print('\n')

# Exercise 8: Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

print('\n')

# Exercise 9: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

print('\n')
