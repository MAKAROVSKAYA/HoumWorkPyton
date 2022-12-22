# Задание 2. Задача №4

# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами 
# в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!
##

def massiv (n): # Метод формирования массива чисел от -n до n
    mas_a = [] 
    for i in range(-n, n+1):
        mas_a.append(i)
    return mas_a

# Перевод строк в числа, в указатели на индексы
# a, b = int(a)-1, int(b)-1
x1 = int(input('Введите первое число диапазона (натуральное, т.е. целое положительное)  '))
x2 = int(input('Введите второе число диапазона (натуральное, т.е. целое положительное)  '))
n = int (input('Введите целое число n=  '))
kol= 2*abs(n)+1
if n==0:
    print (f'пустой список, n={n}')    
elif x1 > kol or x2 > kol:
    print (f'There are no values for these indexes!')
else:
    mas_a = massiv (n)
    composition = mas_a[x1-1]*mas_a[x2-1]
    print (*mas_a, sep = ", ")
    print (f'Произведение элементов на позициях {x1} и {x2} равно {composition}')  
    
