# Task 1
a, b, c, d = int(input('a = ')), int(input('b = ')), int(input('c= ')), int(input('d = '))
print(max(a, b, c, d))
if a > b and a > c and a > d:
    print(a)
elif b > c and b > d:
    print (b)
elif c > d:
    print(c)
else:
    print(d)

# Task 2
FLOORS = 9
Num_flats = 4
ENTERANCE = 4
flat = int(input('Enter number = ')) - 1
enterance = (flat // (Num_flats * FLOORS)) + 1
floor = flat // Num_flats - (enterance - 1) * FLOORS + 1
num_flat_in_the_floors = flat % Num_flats + 1
print( 'floor = ', floor, 'num_flat_in_the_floors = ', num_flat_in_the_floors, 'enterance = ', enterance, 'flat =', flat + 1)

# Task 3
year = int(input('year is '))
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0
    print(True)
else:
    print(False)