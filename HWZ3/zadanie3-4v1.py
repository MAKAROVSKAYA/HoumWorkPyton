# Задание №3 Задача №4 Вариант 1

# Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# in 5
# out  [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16,   Max: 0.92.     Difference: 0.76
# in 3
# out  [9.26, 8.5, 1.14]
# Min: 0.14,   Max: 0.5.      Difference: 0.36

import random
n = int(input("Enter the size of the list = "))
real_list = []
for i in range(n):
    f = random.uniform(0, 9)
    real_list.append(round(f, 2))

min = real_list[0]
max = 0
for i in range(len(real_list)):
    
    if max < real_list[i]:
        max = real_list[i]
    if min > real_list[i]:
        min = real_list[i]
dif = abs (round((max - int(max)) - (min - int(min)),2)) # разница по абсолютному значению

print(f" for the list = {real_list}")
print(f" maximum = {max}, minimum = {min}")
print(f" the difference between the maximum minimum of the fractional part of the elements by absolute value= {round(dif,2)}")

