# ed 1
text = 'Hello world 12 ! begin 13now !'
text_two = ''
for element in text:
    if element.isalpha():
        text_two = text_two + element
print(text_two)

# ed 2
text = input("text = ")
letters = []
text = text.upper()
for letter in text:
    if letter.isalpha() and not letter in letters:
        count = 0
        for let in text:
            if let == letter:
                count = count + 1
        letters.append(letter)
        print(letter, ' - ', count)


# Task 1
text = input('Text = ')
count = 0
for element in text:
    if element == 'b':
        count = count + 1
print('count = ', count)

# Task 2
name = input('Name is ')
if name.isalpha() and name.istitle():
    print('correct')
else:
    print('tru agein')

# Task 3
x = input('x = ')
s = 0
for item in x:
    s += ord(item)
print(s)

res = sum(map(ord, x))
print(res)

# Task 4
from math import pi
n = 2
for i in range(10):
    res = f'{pi:.{n}f}'
    print(res)
    n = n + 1

# Task 5
x = input('text = ')
w = 0
i = ' '
for element in x.split():
    if len(element) > w:
        w = len(element)
        i = element
print(i, ' - ', w)