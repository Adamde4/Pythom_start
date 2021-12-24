#ed 1
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('spamm egg')
    elif i % 3 == 0:
        print ('spamm')
    elif i % 5 == 0:
        print('egg')
    print(i)
    i = i + 1

# ed 2
num = int(input('Enter num = '))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print('*', end = ' ')
        j = j + 1
    print()
    i = i + 1

# ed 3
import random
my_list = []
for i in range (10):
    my_list.append(random.randint(1, 10))
print(my_list)
summa = 0
count = 0
for element in my_list:
    if element % 2 != 1:
        summa = summa + element
        count = count + 1
x = summa / count
print(summa)
print(count)
print(x)

# ed 4
import random
my_matrix = []
for i in range(5):
    lis = []
    for j in range(5):
        lis.append(random.randint(0, 10))
    my_matrix.append(lis)
for element in my_matrix:
    print(element)
summa = 0
for i in range(len(my_matrix)):
    summa = summa + my_matrix[i] [i]
print('Summa = ', summa)
#____________________________________________
# Task 1
for i in range(1, 101):
    if i % 7 ==0:
        print(i)

# Task 2
import math
x, y = 4, 16
i = 1
while i <= x:
    i = i + 1
    while x < i < y:
        print(str(i) + '! =', math.factorial(i))
        i = i + 1

# task 3
num = 5
while num <= 5:
    i = 1
    while i <= 10:
        prod = num * i
        print(num, ' * ', i, ' = ', prod)
        i = i + 1
    num = num + 1

# Task 4
w = int(input('Enter width = '))
h = int(input('Enter higt = '))
i = 1
while i <= h:
    j = 1
    while j <= w:
        print('*', end=' ')
        j = j + 1
    print()
    i = i + 1
print( )
print('* ' * w )
for i in range(h - 2):
    print('* ', ' ' * (w - 2), '*', sep=' ')
print('* ' * w )

# Task 5
x = [0, 5, 2, 4, 7, 1, 3, 19]
i = 0
while i < len(x):
    print((x[i] % 2 == 1))
    i = i + 1
print(sum(x[i]))

# Task 6
import random
first_list = [random.randint(0, 20) for i in range(5)]
print(first_list)
second_list = list.copy(first_list)
for j in range(len(second_list)):
    second_list[j] = second_list[j] * 2
print(first_list + second_list)

# Task 7
import random
list = [random.randint(7500, 15000) for i in range(12)]
print(list)
print('Total summa = ', sum(list), '$')
print('1 month = ', sum(list) // len(list), "$")

# Task 8
import random
my_matrix = []
for i in range(2):
    lis = [random.randint(0, 9) for j in range(2)]
    my_matrix.append(lis)
for i in my_matrix:
    print(i)
summa = 0
for i in my_matrix:
    summa += sum(i)
print('Summa = ', summa)

# Task 9
for list in range(2, 101):
    for i in range(2, list):
        if list % i == 0:
            break
    else:
        print(list)

# Task 10
w = int(input('Enter whild = '))

j = 0
for i in range(w, 0, -2):
    print(' ' * j, '*' * i, sep='')
    j += 1

j -= 1
for i in range(3, w + 1, 2):
    j -= 1
    print(' ' * j, '*' * i, sep='')

# task 11
import random
s = [random.randint(0, 20) for i in range(5)]
print(s)
print(s[::-1])