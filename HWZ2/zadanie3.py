# Задание 2. Задача №3
# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

def composition (n):
   p = 0
   i = 1
   while i <= n: 
    m = i
    number = round ((1 + 1/m) ** m, 3)
    print (number, end="   ")
    p+= number
    i = i + 1 
   return p
     
n = int(input('Введите целое число '))
p = round (composition (n), 3)
print (f'\n проиведение чисeл в последовательности = {p}')
 
