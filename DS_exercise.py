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