# Task 1
x= input('Enter four num = ')
print(x)
if  x[0] + x[1] == x[2] + x[3]:
    print('lucky')
else:
    print('false')

# Task 2
x= input('Enter num = ')
list(x)
if x == x[::-1]:
    print('palindrome')
else:
    print('false')

# Task 3
x, y, r = int(input('x = ')), int(input('y = ')), int(input('radius = '))
if a**2 + b**2 <= r**2:
    print('true')
else:
    print('false')