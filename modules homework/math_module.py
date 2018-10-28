import math
from math import cos,sin,acos,degrees


print('Введите длины сторон треугольника:')

a=float(input('Длина стороны a:'))

b=float(input('Длина стороны b:'))

c=float(input('Длина стороны c:'))

print('Сумма сторон:')
print(a+b+c)

print('Вы строите треугольник со сторонами:')
print(a)
print(b)
print(c)

if a+b>c and a+c>b and b+c>a:
    print('есть такой треугольник')
else:
    print('нет такого треугольника')

x = (b**2+c**2-a**2)/(2*b*c)
y = (a**2+c**2-b**2)/(2*a*c)
z = degrees(acos(x))+degrees(acos(y))

print(degrees(acos(x)))
print(degrees(acos(y)))
print(180-z)

print(x+y+z)