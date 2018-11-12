import random
from functools import reduce

N = int(input('Введите количество элементов в списке:')) #вводим цифру для определения количества случайных цифр

numbers = []

while len(numbers)<N:
    x = int(random.randrange(1,10,1))
    numbers.append(x)

print(numbers)

#1 слово

sum = reduce(lambda res, x: res + x, numbers)

multiply = reduce(lambda res, x: res * x, numbers)

union = list(set(numbers))

join = reduce(lambda res, x: 10*res + x, numbers)

reverse = reduce(lambda res, x: [x] + res, numbers, [])

print(union)

#2 слово

negated = list(map(lambda x: x * -1, numbers))

inverted = list(map(lambda x: 1 / x, numbers))

squared = list(map(lambda x: x * x, numbers))

#3 слово

odds = list(filter(lambda x: x % 2 != 0, numbers))

evens = list(filter(lambda x: x % 2 == 0, numbers))

#simples = list(filter(lambda x: x ==, numbers))

print(odds,evens)

func_dict = {"sum":sum,"multiply":multiply,
             "union":union,"join":join,
             "reverse":reverse,"negated":negated,
             "inverted":inverted,"squared":squared,
             "odds":odds,"evens":evens}

action = input("Что будем делать?:")

action_split = action.split()

print(action_split)

x = action_split[0]
y = action_split[1]
z = action_split[2]

func_dict.get(z)

print(x, y, z)

list_a = func_dict.get(z)

list_b = func_dict.get(y)

list_c = func_dict.get(x)