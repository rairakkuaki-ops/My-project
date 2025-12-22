#Задание 1

print('Определение погоды')

number = int(input('Введиет число от 1 до 12: '))
emoji_1 = str('❄️')
emoji_2 = str('🌈')
emoji_3 = str('☀️')
emoji_4 = str('🌧️')

match number:
    case 1|2|3:
        print(f'{number} зима{emoji_1}')
    case 4|5|6:
        print(f'{number} весна{emoji_2}')
    case 7|8|9:
        print(f'{number} лето{emoji_3}')
    case 10|11|12:
        print(f'{number} осень{emoji_4}')
    case _:
        print('Неизвездная команда')

#Задание 2

print('Простой калькулятор')

number1 = float(input('Введите нужное число: '))
symbol = str(input('Введиет нужный символ операции( +, -, * или /.): '))
number2 = float(input('Введите нужное число: '))

match symbol:
    case '+':
        print(f'{number1} + {number2} = {number1 + number2}')
    case '-':
        print(f'{number1} - {number2} = {number1 - number2}')
    case '*':
        print(f'{number1} * {number2} = {number1 * number2}')
    case '/':
        if number2 != 0:
            print(f'{number1} / {number2} = {number1 / number2}')
        else:
            print('Ошибка: деление на ноль☠️')
    case _:
        print('Неизвестная командам⚠️')