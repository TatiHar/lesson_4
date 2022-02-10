#задание 1
def wage():
    try:
        time = float(input('time: '))
        rate = int(input('rate: '))
        bonus = int(input('bonus: '))
        return time * rate + bonus
    except ValueError:
        print('это не число. выходим')
wage()

#задание 2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [j for i, j in zip(list, list[1:]) if j > i]
print(new_list)

# задание 3
new_list = [el for el in range(20, 241) if el%20==0]
print(new_list)

new_list = [el for el in range(20, 241) if el%21==0]
print(new_list)

#задание 4
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in list if list.count(el)==1]
print(new)

#задание 5
from functools import reduce
new_list = (el for el in range(100,1001) if el%2 == 0)
sum_all = reduce(lambda x, y: x + y, new_list)
print(sum_all)

#задание 6
from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle
с = 0
for el in cycle("156"):
    if с > 10:
        break
    print(el)
    с +=1

#задание 7
from itertools import count
from math import factorial
def gen():
    for el in count(1):
        yield factorial(el)
g = gen()
n = 0
for i in g:
    if n < 10:
        print(i)
        n += 1
    else:
        break
