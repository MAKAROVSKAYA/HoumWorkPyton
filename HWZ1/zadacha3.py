# Задание 1 задача 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты точки по оси х (причем, координата x≠0):'))
y = int(input('Введите координаты точки по оси y (причем, координата y≠0):'))
if x == 0 and y == 0:
    print('Вы осуществили неверный ввод данных, координаты  х и y ≠0')
elif x > 0 and y > 0:
    print(
        f'точка ({x},{y}) находится в I-ой четверти')
elif x < 0 and y > 0:
    print(
        f'точка ({x},{y}) находится в II-ой четверти')
elif x < 0 and y < 0:
    print(
        f'точка ({x},{y}) находится в III-ей четверти')
elif x > 0 and y < 0:
    print(
        f'точка ({x},{y}) находится в IV-ой четверти')