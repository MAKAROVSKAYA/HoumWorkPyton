# Урок 6 Задание 1
# 1. Представлен список чисел. Необходимо вывести элементы
#    исходного списка, значения которых больше предыдущего элемента.
#    Use comprehension.

from random import sample

def more_than(number):
    my_list = sample(range(number * 3), number)
    print(my_list)
    return [my_list[number] for number in range(1, len(my_list)) if my_list[number] > my_list[number - 1]]

print(more_than(int(input('print the number: '))))