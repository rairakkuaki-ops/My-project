#Задание 1

a = 42
b = 3.14159
c = "Hello, Python!"
d = True
e = [1, 2, 3]
f = (4, 5, 6)
g = {"name": "Alice", "age": 30}
h = {7, 8, 9}
i = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

#Задание 2
my_list = [1, 2, 3]
my_list.insert(0, 100)
print(my_list)

#Задание 2.1
my_tuple = (1, 2, 3)
my_tuple.insert(0, 100) #из-за того что это кортеж, то insert нельзя сделать
print(my_tuple)

#Задание 2.2
my_string = 'cat'
print(my_string[0], 'b')

#Задание 3
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
sum = num1 + num2
print(sum)

#Задание 5
shopping_list = ['молоко', 'хлеб', 'яйца']
shopping_list.append('сахар')
sum_shopping_list = len(shopping_list)
print(shopping_list)
print('Сколько всего продуктов в списке:', sum_shopping_list)

unique_items = {'молоко', 'хлеб', 'яйца'}
unique_items.add('сахар')
print(unique_items)

#Задание 6
name = input('Ваше имя: ') #ввод данных от пользователя
age_str = input('Ваш возраст: ')
subjects_str = input('Любые предметы(через запятую): ')

student = {
    'Имя': name,
    'Возраст': age_str,
    'Предметы': subjects_str
} #создание словаря в котором хранятся данные
print('=' * 30)
print('АНКЕТА СТУДЕНТА')
print('=' * 30) #вывод оформления анкеты

print(f'Имя: {name}\nВозраст: {age_str}\nПредметы: [{subjects_str}]')
#использование форматированной строчки. Вывод данных

print('=' * 30)

