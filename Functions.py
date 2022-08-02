# Exercise 2: Create a function with variable length of arguments

def func(*args):
    for i in args:
        print(i)

func(20,30)
func(10,20,40)

# Exercise 3: Return multiple values from a function

def calc(a,b):
    sum = a + b
    sub = a - b
    return sum,sub

res = calc(200,34)

print(res)

# Exercise 4: Create a function with a default argument

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")