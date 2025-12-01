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
num = input('Введите четырёх значное число: ')
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

n1 = number % 2 or number != 0
number = number <= 4

n2 = number % 2 or number != 0
number = number <= 7

n3 = number % 2 or number != 0
number = number <= 11

n4 = number % 2 or number != 0
number = number <= 16

n5 = number % 2 or number != 0
number = number <= 20

n6 = number % 2 or number != 0
number = number <= 24

n7 = number % 2 or number != 0
number = number <= 28

n8 = number % 2 or number != 0
number = number <= 32

n9 = number % 2 or number != 0
number = number <= 36

print(f'Номер вашего купе: 1, место:{n1}')
print(f'Номер вашего купе: 2, место:{n2}')
print(f'Номер вашего купе: 3, место:{n3}')
print(f'Номер вашего купе: 4, место:{n4}')
print(f'Номер вашего купе: 5, место:{n5}')
print(f'Номер вашего купе: 6, место:{n6}')
print(f'Номер вашего купе: 7, место:{n7}')
print(f'Номер вашего купе: 8, место:{n8}')
print(f'Номер вашего купе: 9, место:{n9}')

