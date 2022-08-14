# 1

number1 = 20
number2 = 30

p = number1 * number2

if p < 1000:
  print(p)
else:
  print(number1 + number2)
  
print('\n')

# 2

for i in range(0,10):
  if(i>0):
    x = i + i - 1
  if(i==0):
    x = 0
  print(x)
  
print('\n')

# 3 

str = "H"

for i in range(0, len(str), 2):
  print(str[i])

print('\n')

# 4

def remove_char(st,n):
  x = st[n:]
  print(x)

remove_char("Hrithik",3)
print('\n')


# 8

n = 5

for i in range(n):
  for j in range(i):
    print(i, end = "")
  print("")

print('\n')

# 9 

o = 6556
n = o
s = 0
while n > 0:
  x = n % 10
  n = n // 10
  s = s * 10 + x

if n == s:
  print("palindrome", s)
else:
  print("not plaindrome", s)
print('\n')

# 13 

for i in range(1,11):
  for j in range(1,11):
    print(i*j, end = " ")
  print(" ")
print('\n')

# 14

for i in range(5,0,-1):
  for j in range(0,i):
    print('*', end = " ")
  print(" ")

print('\n')
