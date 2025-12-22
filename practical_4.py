#Задание 1

import  math
num = float(input('Введите не целое число x: '))
print(round(num) + math.ceil(num))

#Задание 2

print(f'Определение евклидово расстояние между двумя точками\n')

import math
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
distance = (math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2)))
print(distance)

#Задание 3

print(f'Программа для нахождения цифр четырёхзначного числа\n')

user_number = str(input('Введите четырёх значное число: '))
print('Цифра в позиции тысяч равна:', user_number[0])
print('Цифра в позиции сотен равна:', user_number[1])
print('Цифра в позиции десятков равна:', user_number[2])
print('Цифра в позиции единиц равна:', user_number[3])

#Задание 4

print(f'Школьники делят между собой мандарины\n')

n = int(input('Введите количество школьников: '))
k = int(input('Введите количество мандарин: '))
print('Количество мандарин у школьника: ', k//n)
print('Количество мандарин в корзине: ', k%n)

#Задание 5

print(f'Пересчёт величины временного интервала\n')

time = int(input('Введите количество минут: '))
print(time,'мин - это', time//60, 'час', time%60,'минут')

#Задание 6

print(f'Вычисление тригонометрического выражения\n')

import math
x = int(input('Введите  градус: '))
r = (math.radians(x))
summ = (math.sin(r)+math.cos(r)+math.tan(1)**2*r)
print('Тригонометрическое значение:',round(summ))

#Задание 7

print(f'Какое купе\n')

number = int(input('Введите номер своего места: '))

coupe = (number + 3) // 4


print('Ваше купе под номером: ',coupe)

