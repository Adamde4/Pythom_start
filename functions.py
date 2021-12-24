# 1 variant
def filter (x, func):
    res = []
    for element in x:
        if func(element):
            res.append(element)
    return res

def is_neg(element):
    if element < 0:
        return element

def is_pos(element):
    if element > 0:
        return element


x = [1, 5, - 10, - 15, 20]
print(filter(x, is_neg))
print(filter(x, is_pos))

# 2 variant
def filter (x, func):
    res = []
    for element in x:
        if func(element):
            res.append(element)
    return res

x = [1, 5, - 10, - 15, 20]
print(filter(x, lambda element: element < 0))
print(filter(x, lambda element: element > 0))
print(filter(x, lambda element: element % 2 == 0))
print(filter(x, lambda element: element % 2 != 0))

# calc
calc = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

x, y = int(input('enter x = ')), int(input('enter y = '))
op = input('enter operation ')
print(calc[op] (x, y))

#stepin
def step(a, b):
    if b == 0:
        return 1
    return a * step(a, b - 1)

print(step(5, 3))

