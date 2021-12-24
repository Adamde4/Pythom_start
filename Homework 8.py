# Ex 1
a = 'Hello'
b = 'World'
x = (set(a).intersection(set(b)))
print(x)
y = (set(a) & set(b))
print(y)


# Ex 2
x = []
y = []
z = []
for element in range(1, 91):
    if element % 3 == 0: x.append(element)
    if element % 5 == 0: y.append(element)
print('multiples of 3 = ', x)
print('multiples of 5 = ', y)
x, y = set(x), set(y)
total = x & y
for i in total:
    z.append(i)
print('common num:', total)