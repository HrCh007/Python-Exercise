# Exercise 2: Create a function with variable length of arguments

def func(*args):
    for i in args:
        print(i)

func(20,30)
func(10,20,40)

print('\n')

# Exercise 3: Return multiple values from a function

def calc(a,b):
    sum = a + b
    sub = a - b
    return sum,sub

res = calc(200,34)

print('\n')

print(res)

# Exercise 4: Create a function with a default argument

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

print('\n')

# Exercise 7: Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

showStudent = display_student

showStudent("Emma", 26)

print('\n')

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

list1 = list(range(4,30,2))
print(list1)

print('\n')

# Exercise 9: Find the largest item from a given list

x = [4, 6, 8, 24, 12, 2]
print(max(x))

print('\n')