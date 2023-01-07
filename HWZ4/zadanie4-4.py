# Задание №4. Задача №4. 

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) 
# многочлена, записать в файл полученный многочлен не менее 3-х раз.
#   in 
#   9
#   5
#   3
#   out in the file
#   3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
#   4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
#   4*x^2 - 4 = 0
# _________________
#   

from itertools import *
from random import randint
import os
os.system('cls||clear')

def array_coefficients(k):  # функция формирования чисел -коэффициентов полинома и свободного члена на отрезке от [0, 10] при условии, что первый коэффициент не был равен "0"
    coeff = [randint(0, 10) for i in range(k + 1)]
    while coeff[0] == 0:
        coeff[0] = randint(0, 10)
    print (f'Массив коэффициентов {coeff}') 
    print ()
    return coeff

def get_polynom (k, coeff):  # функция "составления" (сбора) полинома
    
    var = ['*x^']*(k-1) + ['*x']
    poly = [[a, b, c] for a, b, c in zip_longest(
        coeff, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in poly:
        x.append(' + ')
    poly = list(chain(*poly))
    poly [-1] = ' = 0'
    return "".join(map(str, poly)).replace(' 1*x', ' x')

def cls(): 
    print("/n" * 100) 

for i in range(3):
    k=randint(0,10)
    print (f'коэффициент k= {k}')
    print ()
    
    coeff = array_coefficients(k)
    poly_1 = get_polynom (k, coeff)
    print(poly_1)  # перезаписываем результат в файл 
    with open("f4.txt", "a", encoding="utf-8") as data:
        data.writelines (f" {poly_1}\n  ")
       


