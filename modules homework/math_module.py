import math

print('Введите длины сторон треугольника:')

a=int(input('Длина стороны a:'))
b=int(input('Длина стороны b:'))
c=int(input('Длина стороны c:'))

print('Треугольник со сторонами:'+a+b+c)

cos_a=(math.pow(b, 2)+math.pow(c, 2)-math.pow(a, 2))/2*b*c