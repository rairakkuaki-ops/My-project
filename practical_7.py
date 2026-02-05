#Задание 1

print('Система рейтинга продуктов')

number = int(input('Введиет число от 1 до 10: '))
match number:
    case 1|2:
        print(f'✎Рейтинг {number} → "Плохой продукт! 💩 Рискните здоровьем"')
    case 3|4:
        print(f'✎Рейтинг {number} → "Средний продукт 🤔 Стоит ли оно того?"')
    case 5|6|7:
        print(f'✎Рейтинг {number} → "Хороший продукт ⭐ Обязательно попробуйте"')
    case 8|9|10:
        print(f'✎Рейтинг {number} → "Отличный продукт! 🎇 Это великолепно"')
    case _:
        print('✎Неизвездная команда')

#Задача 2

print('Отслеживание заказов')

status = str(input('Введиет статус заказа: '))

print('-', '=' * 40)
print('         📦СТАТУС ВАШЕГО ЗАКАЗА📦')
print('-','=' * 40)

match status:
    case 'pending'|'Pending':
        print(f'Статус: в ожидании🦖\nОписание: Ваш заказ в пути\nВремя ожидания: 10-15\nРекомендации: следите за уведомлениями')
    case 'processing'|'Processing':
        print(f'Статус: в обработке🧘\nОписание: Ваш заказ собирается\nВремя ожидания: собирается\nРекомендации: ожидайде когда собирется')
    case 'shipped'|'Shipped':
        print(f'Статус: отправлено✈️\nОписание: Ваш заказ отправлен на пункт выдачи\nВремя ожидания: 2-5 дней\nРекомендации: следите за поступающими уведомлениями')
    case 'devlivered'|'Devlivered':
        print(f'Статус: доставлено🎉\nОписание: Ваш заказ в пункте выдачи и ожидает Вас\nВремя ожидания: прибыл\nРекомендации: забрать заказ')
    case 'cancelled'|'Cancelled':
        print(f'Статус: отменено🤚\nОписание: Ваш заказ был отменен\nВремя ожидания: отмена\nРекомендации: Вы либо отменили заказ или роизошла ошибка в приложении напишите в поддержку')
    case _:
        print(f'❌Ошибка: Неизвестный статус "invalid_status"\nДопустимые статусы: pending, processing, shipped, devlivered, cancelled')

#Задание 3

print(f'Интерактивное меню кафе\n')
print('=' * 40)
print('1. Кофе - 120 руб')
print('2. Чай - 80 руб')
print('3. Сок - 100 руб')
print('4. Вода - 50 руб')
print('5. Лимонад - 90 руб')
print(f'=' * 40)
print(f'\n')
drink = input('Введите номер напитка или название: ')
number_of_servings = int(input('Введите количество порций: '))
discount = input('Введите промакод(при наличии): ')

COFFEE = 120
TEA = 80
JUICE = 100
WATER = 50
LEMONADE = 90

STUDENT = 0.2

coffee_price = COFFEE * number_of_servings
tea_price = TEA * number_of_servings
juice_price = JUICE * number_of_servings
water_price = WATER * number_of_servings
lemonade_price = LEMONADE * number_of_servings

match drink:
    case '1'|'Кофе':
        print(f'Товар: Кофе☕\nЦена за порцию:{COFFEE} руб\nКоличество: {number_of_servings}\nСумма: {coffee_price} руб')
    case '2'|'Чай':
        print(f'Товар: Чай🍵\nЦена за порцию:{TEA} руб\nКоличество: {number_of_servings}\nСумма: {tea_price} руб')
    case '3'|'Сок':
        print(f'Товар: Сок🧃\nЦена за порцию:{JUICE} руб\nКоличество: {number_of_servings}\nСумма: {juice_price} руб')
    case '4'|'Вода':
        print(f'Товар: Вода🫗\nЦена за порцию:{WATER} руб\nКоличество: {number_of_servings}\nСумма: {water_price} руб')
    case '5'|'Лимонад':
        print(f'Товар: Лимонад🥤\nЦена за порцию:{LEMONADE} руб\nКоличество: {number_of_servings}\nСумма: {lemonade_price} руб')
    case _:
        print('☢Неизвестная команда')

discounted_price_coffee = coffee_price * STUDENT
discounted_price_tea = tea_price * STUDENT
discounted_price_juice = juice_price * STUDENT
discounted_price_water = water_price * STUDENT
discounted_price_lemonade = lemonade_price * STUDENT

match discount:
    case 'STUDENT':
        print(f'Скидка "STUDENT" (20%): -{discounted_price_coffee:.0f} руб')
    case 'STUDENT':
        print(f'Скидка "STUDENT" (20%): -{discounted_price_tea:.0f} руб')
    case 'STUDENT':
        print(f'Скидка "STUDENT" (20%): -{discounted_price_juice:.0f} руб')
    case 'STUDENT':
        print(f'Скидка "STUDENT" (20%): -{discounted_price_water:.0f} руб')
    case 'STUDENT':
        print(f'Скидка "STUDENT" (20%): -{discounted_price_lemonade:.0f} руб')

print('=' * 40)
print(f'К ОПЛАТЕ: ')
print('=' * 40)

