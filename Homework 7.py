#ed 1
import random
my_list = []
for i in range(10):
    my_list.append(random.randint(1, 5))
resul = {}
for element in my_list:
        num = resul.get(element)
        if num is None:
            resul [element] = 1
        else:
            resul [element] = num + 1
print( my_list)
for key in resul.keys():
    print(key, ' - ', resul[key])

#ed 2
import random
name = ['cat_one', 'cat_two', 'cat_three', 'cat_four', 'cat_five']
cats = []
for i in range(5):
    cat = {
        "name": name[i],
        "age": random.randint(1, 15)
    }
    cats.append(cat)
print(cats)
max_age = cats[0]
for some_cat in cats:
    if some_cat.get('age') > max_age.get('age'):
        max_age = some_cat
print(max_age)

#Task 1
weak = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thuersday', 5: 'Friday', 6: 'Saturday', 7: 'Saturday'}

n = int(input(' enter number = '))
if n > 8 and n < 0:
    print('ancorrect')
else:
    print(weak[n])
# Task 1
my_list = input()
resul = {}
for item in my_list:
    if item in resul:
        resul[item] += 1
    else:
        resul[item] = 1
print(resul)