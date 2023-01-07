# Задание №4 Задача №3

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in 7
# out 
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in -1
# out
# Negative value of the number of numbers!

import random
def int_lst (n,d1,d2,old_lst)-> list:
    old_lst=[]
    for i in range(n):
        old_lst.append(random.randint(d1, d2))
    return old_lst

def translet_list(old_lst) -> list:
    for k in old_lst: 
        if old_lst.count(k) == 1: 
            new_lst.append(k)
    return new_lst

old_lst=[]
new_lst=[]
n = int(input("Введите количество элементов исходного списка: "))
d1 = int(input("Введите начальное значение диапазона исходного списка: "))
d2 = int(input("Введите конечное значение диапазона исходного списка : "))
old_lst= int_lst (n,d1,d2,old_lst)
print(f"Список исходных элементов:")
print(old_lst)
new_lst = translet_list(old_lst)
print("Список преобразованных элементов: ")
print(new_lst)
