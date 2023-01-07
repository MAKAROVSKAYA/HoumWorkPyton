# Задание № Задача №2 Вариант 1 - список

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 
# n     54
# out   [2, 3, 3, 3]
# in    9990
# out   [2, 3, 3, 3, 5, 37]
# in    650
# out   [2, 5, 5, 13]

def with_multipliers (number):
    lst = []
    i = 2                       # первое простое число возможного сомножителя
    multiplier = number
    while i <= number:
        if multiplier % i == 0:
            lst.append(i)
            multiplier //= i
            i = 2
        else:
            i += 1
    return lst

number = int(input("Введите целое число: "))
lst = []
lst = with_multipliers (number)
print(f"Простые множители числа {number} представлены: {lst}")

