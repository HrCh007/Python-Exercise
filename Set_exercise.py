# Exercise 1: Add a list of elements to a set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

# Exercise 2: Return a new set of identical items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

# Exercise 3: Get Only unique items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))

# Exercise 4: Update the first set with items that don’t exist in the second set

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.difference_update(set2))