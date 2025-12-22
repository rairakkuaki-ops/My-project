#Задание 1

print(f'Калькулятор налогов\n')

income = float(input('Введите годовой доход(одно число): '))
TAX_RATE = 0.13
print(income)
print('Налоговая ставка = 13%')
print(f'{income/TAX_RATE:.2f}')

#Задание 2

print(f'Калькулятор ИМТ\n')

weight,heigt = map(float, input('Введите свой вес(в кг) и рост(в метрах): ').split())
calculations = weight/heigt*heigt
print(calculations)

#Задание 3
print(f'Конвертер валют\n')

def convert_usd_to_rub(amount_usd):
    """
        Конвертирует введённую сумму долларов в рубли.
    Args:
        amount_usd (float): введённая сумма в долларах
    Returns:
        float: перевод из долларов в рубли
    """
    convert = amount_usd * 95.50
    return convert

help(convert_usd_to_rub)

usd_amount = float(input('Введите сумму в долларах: '))
rub_amoumt = convert_usd_to_rub(usd_amount)
print(f'Сумма в рублях: {rub_amoumt}')


#Задание 4

print('Универсальный калькулятор площади')

def calculate_rectangel_area(width, height):
    """
    Считает площадь прямоугольника.

    Args:
        width(float): введённая ширина
        height (float): введённая высота
    Returns:
        float: нахождение площади прямоугольника
    """
    area = width * height
    return area

help(calculate_rectangel_area)

def calculate_circle_area(radius):
    """

    Считает площадь круга.

    Args:
        radius (float): радиус круга
        3.14 (float): число пи
        radius ** 2 (float): возведение во вторую степень радиус
    Returns:
        float: нахождение площади круга
    """
    calculate_radius = 3.14 * radius ** 2
    return calculate_radius

help(calculate_circle_area)

width = float(input('Введите ширину прямоугольника: '))
height = float(input('Введите высоту прямоугольника: '))
s = calculate_rectangel_area(width, height)
print(f'Площадь прямоугольника является: {s}')

radius = float(input('Введите радиус круга: '))
r = calculate_circle_area(radius)
print(f'Радиус круга является: {r}')


#Задание 5

print('Банкомат')

B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

deposit_money = int(input('Введите сумму которую хотите снять(кратное 100): '))

count_5000 = deposit_money // B5000
deposit_money = deposit_money % B5000

count_2000 = deposit_money // B2000
deposit_money = deposit_money % B2000

count_1000 = deposit_money // B1000
deposit_money = deposit_money % B1000

count_500 = deposit_money // B500
deposit_money = deposit_money % B500

count_200 = deposit_money // B200
deposit_money = deposit_money % B200

count_100 = deposit_money // B100
deposit_money = deposit_money % B100

print(f'Количество 5000: {count_5000}')
print(f'Количество 2000: {count_2000}')
print(f'Количество 1000: {count_1000}')
print(f'Количество 500: {count_500}')
print(f'Количество 200: {count_200}')
print(f'Количество 100: {count_100}')

#Задание 6

print('Площадь треугольника по координатам')

import math

def calculate_distance(x1, y1, x2, y2):
    """
    Вычисление координат

    Args:
        x1, y1 (float): координаты первой точки
        x2, y2 (float): координаты второй точки
    Returns:
        float: расстояния между точками
    """
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance
help(calculate_distance)

def calculate_triangle_area(a, b, c):
    """
    Вычисление площади треугольника

    Args:
      a (float): одна сторона треугольника
      b (float): вторая сторона треугольника
      c (float): третья сторона треугольника
    Returns:
        float: площадь
    """
    p = (a + b + c) / 2
    area = math.sqrt(p*(p - a) * (p - b) * (p - c))
    return area

help(calculate_triangle_area)

x1_str, y1_str = input('Введите координату точки A(x и y): ').split()
x2_str, y2_str = input('Введите координату точки B(x и y): ').split()
x3_str, y3_str = input('Введите координату точки C(x и y): ').split()

x1, y1 = float(x1_str), float(y1_str)
x2, y2 = float(x2_str), float(y2_str)
x3, y3 = float(x3_str), float(y3_str)

side_ab = calculate_distance(x1, y1, x2, y2)
side_bc = calculate_distance(x2, y2, x3, y3)
side_ac = calculate_distance(x1, y1, x3, y3)
area_of_a_triangle = calculate_triangle_area(side_ab, side_bc, side_ac)

print(round(area_of_a_triangle))

#Задание 7

def calculate_fuel_consumption(distance_km, fuel_per_100km):
    """
    Вычисление поездок на такси
    Args:
        distance_km (float): какое растояние проехал
        fuel_per_100km (float): сколько литров потратил
    Returns:
        float: общий расход топлива в литрах
    """
    calculate_rides = distance_km * (fuel_per_100km/100)
    return calculate_rides

help(calculate_fuel_consumption)

distance = float(input('Введите какое количество км проехали: '))
fuel = float(input('Введите какоЙ расход топлива(л/100 км): '))
FUEL_COST= 49.5
calculate_distance = calculate_fuel_consumption(distance, fuel)
calculate_cost = calculate_distance * FUEL_COST
print(f'Количество необходимого бензина: {calculate_distance}')
print(f'Стоимость: {calculate_cost:.2f}')