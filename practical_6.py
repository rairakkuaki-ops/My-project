#Задание 1

print(f'Диагностика состояния здоровья\n')

temperature = float(input('Введите температура(°C): '))
pressure = float(input('Введите давление(верхнее): '))
pulse = float(input('Введите пульс(уд/мин): '))

TEMP_NORMAL_MAX = 37
TEMP_NORMAL_MIN = 36
TEMP_MILD_MAX = 38
TEMP_MILD_MIN = 35

PRESSURE_NORMAL_MAX = 130
PRESSURE_NORMAL_MIN = 110
PRESSURE_MILD_MAX = 140
PRESSURE_MILD_MIN = 105

PULSE_NORMAL_MAX = 100
PULSE_NORMAL_MIN = 60
PULSE_MILD_MAX = 110
PULSE_MILD_MIN = 55

if (TEMP_NORMAL_MIN <= temperature <= TEMP_NORMAL_MAX) and (PRESSURE_NORMAL_MIN <= pressure <= PRESSURE_NORMAL_MAX ) and (PULSE_NORMAL_MIN <= pulse <= PULSE_NORMAL_MAX ):
    print('Нормальное состояни')
elif ( TEMP_MILD_MIN <= temperature <= TEMP_NORMAL_MIN) or (TEMP_NORMAL_MAX  <= temperature <= TEMP_MILD_MAX) or (PRESSURE_MILD_MIN <= pressure <= PRESSURE_NORMAL_MIN ) or (PRESSURE_NORMAL_MAX <= pressure <= PRESSURE_MILD_MAX ) or (PULSE_MILD_MIN <= pulse <= PULSE_NORMAL_MIN) or (PULSE_NORMAL_MAX <= pulse <= PULSE_MILD_MAX):
    print('Легкое недомогание')
elif (temperature < TEMP_MILD_MIN) or (temperature > TEMP_MILD_MAX) or (pressure < PRESSURE_MILD_MIN) or (pressure > PRESSURE_MILD_MAX) or (pulse < PULSE_MILD_MIN) or (pulse > PULSE_MILD_MAX):
    print('Требуется врач!')
else:
    print('Неизвестная команда')


#Задание 2

print(f'Цвета колеса рулетки\n')

number = int(input('Введиет номер кармана: '))

RULLETE_RANGE_POINT1 = 15
RULLETE_RANGE_POINT2 = 19
RULLETE_RANGE_POINT3 = 30
RULLETE_RANGE_POINT4 = 42

if number == 0:
    print('Зелёный')
elif ((1 <= number <= RULLETE_RANGE_POINT1) or (RULLETE_RANGE_POINT2+1 <= number <= RULLETE_RANGE_POINT3)) and number % 2 == 0:
    print('Чёрный')
elif ((1 <= number <= RULLETE_RANGE_POINT1) or (RULLETE_RANGE_POINT2+1 <= number <= RULLETE_RANGE_POINT3)) and number % 2 == 1:
    print('Красный')
elif ((RULLETE_RANGE_POINT1+1 <= number <= RULLETE_RANGE_POINT2) or (RULLETE_RANGE_POINT3+1 <= number <= RULLETE_RANGE_POINT4)) and number % 2 == 0:
    print('Красный')
elif ((RULLETE_RANGE_POINT1+1 <= number <= RULLETE_RANGE_POINT2) or (RULLETE_RANGE_POINT3+1 <= number <= RULLETE_RANGE_POINT4)) and number % 2 == 1:
    print('Чёрный')
else:
    print('Ошибка ввода')


#Задание 3

print(f'Шахматная доска\n')

Cell_horizontally1 = int(input('Введите число для первой клетки по горизонтали(от 1 до 8): '))
Cell_vertically1 = int(input('Введите число для первой клетки по вертекали(от 1 до 8): '))
Cell_horizontally2 = int(input('Введите число для второй клетки по горизонтали(от 1 до 8): '))
Cell_vertically2 = int(input('Введите число для второй клетки по вертекали(от 1 до 8): '))

if (1 <= Cell_horizontally1 <= 8) and (1 <= Cell_vertically1 <= 8) and (1 <= Cell_horizontally2 <= 8) and (1 <= Cell_vertically2 <= 8):

    sum1 = (Cell_horizontally1 + Cell_vertically1) % 2
    sum2 = (Cell_horizontally2 + Cell_vertically2) % 2

    if sum1 == sum2:
        print('YES')
    elif sum1 != sum2:
        print('NO')
    else:
        print('Неизвестная команда')
else:
    print('Нельзя число больше 8!')


#Задание 4

print(f'Ход слона\n')

Cell_horizontally1 = int(input('Введите число для первой клетки по горизонтали(от 1 до 8): '))
Cell_vertically1 = int(input('Введите число для первой клетки по вертекали(от 1 до 8): '))
Cell_horizontally2 = int(input('Введите число для второй клетки по горизонтали(от 1 до 8): '))
Cell_vertically2 = int(input('Введите число для второй клетки по вертекали(от 1 до 8): '))

if (1 <= Cell_horizontally1 <= 8) and (1 <= Cell_vertically1 <= 8) and (1 <= Cell_horizontally2 <= 8) and (1 <= Cell_vertically2 <= 8):

    sum1 = (Cell_horizontally1 - Cell_horizontally2)
    sum2 = (Cell_vertically1  - Cell_vertically2)

    if abs(sum1) == abs(sum2):
        print('YES')
    else:
        print('NO')
else:
    print('Нельзя число больше 8!')

