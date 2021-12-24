# Task 1
x= '123'
print(x)
y= float(x)
print(y)

# Task 2
x= float(123)
print(x)
y= int(x)
print(y)

# Task 3
x = float(123.45)
print(x)
y= int(x)
print(y)

# Task 4
card_number= input('enter card number =')
card_number= int(card_number)
print(card_number % 1000)

# Task 5
x= int(input('three number ='))
print(x // 100 + x // 10 %10 + x % 10)

# Task 6
a = float(input('a ='))
b = float(input('b='))
c = float(input('c ='))
p = (a + b + c) / 2
print('p =', p)
area = (p * (p - a) * (p - b) * (p - c)) **0.5
print('area =', area)