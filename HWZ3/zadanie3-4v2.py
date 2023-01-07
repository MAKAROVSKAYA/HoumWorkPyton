# Задание №3 Задача №4 Вариант 2

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

import random, math
n = int(input("Enter the size of the list = "))
real_lst = []
for i in range(n):
    f = random.uniform(0, 9)
    real_lst.append(round(f, 2))
maximum = max(real_lst)
minimum = min(real_lst)
print(f" for the list = {real_lst}")
print(f" maximum = {maximum}, minimum = {minimum}")
delta= abs(float(maximum)%1 - float(minimum)%1)  # разница по абсолютному значению
print(f" the difference between the maximum minimum of the fractional part of the elements by absolute value = {round(delta, 2)}")

