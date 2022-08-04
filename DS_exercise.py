# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

res = []

res = l1[1::2] + l2[0::2]

print(res)

# Exercise 4: Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Exercise 5: Create a Python set such that it shows the element from both lists in a pair

print("Printing count of each item  ", count_dict)

first_list = [2, 3, 4, 5, 6, 7, 8]

second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)

# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

speed_list = list()

for item in speed.values():
    if item not in speed_list:
        speed_list.append(item)

print(speed_list)