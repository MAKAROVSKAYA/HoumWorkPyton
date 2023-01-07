# Задание №3 Задача №1

# Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in   5
# out  [10, 2, 3, 8, 9]     
#      22
# in   4
# out  [4, 2, 4, 9]
#      8

def sum_odd_positions(l):
    s = 0
    for i in range(len(l)):
        if i % 2 == 0:  # Для нечетной позиции значение i будет всегда четное
            s += l[i]
    return s

n = int(input("enter the number of numbers in the list:  "))
L = [ int(input("number=:  ")) for i in range(n) ] 
s=sum_odd_positions(L)
print (f"The sum =:   {s}")

