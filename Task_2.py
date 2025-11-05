#Задание 1
import  math
num1 = float(input('Введите не целое число x1: '))
num2 = float(input('Введите не целое число x2: '))
print(round(num1) + round(num2))

#Задание 2
import math
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
summ = (math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2)))
print(summ)

#Задание 3
num = str(input('Введите четырёх значное число: '))
print('Цифра в позиции тысяч равна ',num[0])
print('Цифра в позиции сотен равна ', num[1])
print('Цифра в позиции десятков равна ', num[2])
print('Цифра в позиции единиц равна ', num[3])

#Задание 4
n = int(input('Введите количество школьников: '))
k = int(input('Введите количество мандарин: '))
print('Количество мандарин у школьника: ', k//n)
print('Количество мандарин в корзине: ', k%n)

#Задание 5
time = int(input('Введите количество минут: '))
print(time,'мин - это', time//60, 'час', time%60,'минут')

#Задание 6
import math
x = int(input('Введите градус(x): '))
r = (math.radians(x))
summ = (math.sin(r)+math.sin(r)+math.tan(1)**2*r)
print(summ)

#Задание 7
number = int(input('Введите номер своего места: '))
if number <= 3:
    print('Номер вашего купе:', 1)
elif number <= 7:
    print('Номер вашего купе:', 2)
elif number <= 11:
    print('Номер вашего купе:', 3)
elif number <= 15:
    print('Номер вашего купе:', 4)
elif number <= 20:
    print('Номер вашего купе:', 5)
elif number <= 24:
    print('Номер вашего купе:', 6)
elif number <= 28:
    print('Номер вашего купе:', 7)
elif number <= 32:
    print('Номер вашего купе:', 8)
elif number <= 35:
    print('Номер вашего купе:',9)
else:
    print('Нету такого места')
