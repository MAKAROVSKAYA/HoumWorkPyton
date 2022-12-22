# Задание 2. Задача 5**
# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

def massiv (n): # Метод формирования массива чисел от -n до n
    mas_a = [] 
    for i in range(-n, n+1):
        mas_a.append(i)
    return mas_a

def mixed_massiv (mas_a, n): # Метод перемешивания массива. Примечание: при кол-ве членов массива в 3 элемента (т.е. n=1), может возникнуть ситуация, что массив перемешанный равен исходному
    import random
    for i in range(2*n+1):
        j = random.randint(0, n + 1) 
        buffer = mas_a[i]
        mas_a[i] = mas_a[j]
        mas_a[j] = buffer
    return mas_a

n = int (input('Введите целое число n=  '))
mas_a = massiv (n)
print (*mas_a, sep = ", ")
mixed_a = mixed_massiv (mas_a, n)
print (*mixed_a, sep = ", ")