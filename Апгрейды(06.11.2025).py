#РАУНД 1
number = int(input('Введите место: '))
print("Номер Вашего купе:", (number-1) // 4 + 1)

#РАУНД 2.1
number = int(input('Введите место: '))
Kol_mest=4
print("Номер Вашего купе:", (number-1) // Kol_mest + 1)

#РАУНД 2.2
import math
x1, y1 = map(float, input('Введите x1, y1: ').split())
x2, y2 = map(float, input('Введите x2, y2: ').split())
summ = (math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2)))
print(summ)

#РАУНД 2.3

import math
x1, y1 = map(float, input('Введите x1, y1: ').split())
x2, y2 = map(float, input('Введите x2, y2: ').split())
summ = (math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2)))
print(f"Расстояние между точками: {summ:.2f}")

#РАУНД 3

import math
x1, y1 = map(float, input('Введите x1, y1: ').split())
x2, y2 = map(float, input('Введите x2, y2: ').split())
def koordinaty(x1, x2, y1, y2):
    summ = (math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
    return summ
print(koordinaty(x1, x2, y1, y2))
