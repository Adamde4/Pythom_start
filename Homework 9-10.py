# Task 1
import random

def max_num(a):
    num = 0
    for element in a:
        if element > num:
            num = element
    return num

a = []
for element in range(5):
    a.append(random.randint(0, 90))
print(max_num(a))
print(a)

#task 2
def fun(a, b, s):
    if isinstance(a, int) and isinstance(b, int) and isinstance(s, str):
        return (a + b), s
    return None

print(fun(5, 3, 5))
