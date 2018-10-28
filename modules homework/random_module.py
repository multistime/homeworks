import random

x = int(random.randrange(1,11,1))

y = -1

print('Hi, it\'s me, your computer. What do you think, what number did I make?')

while y != x:
    y = int(input('Input your number [1-10]>>>'))
    if y == x:
        print('Nice shoot!')
    else:
        print(str(y)+'?....No. Try again.')