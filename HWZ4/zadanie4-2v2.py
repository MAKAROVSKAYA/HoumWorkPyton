# Задание 2 Задача 2 Вариант 2 - файл
# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# n     54
# out   [2, 3, 3, 3]
# in    9990
# out   [2, 3, 3, 3, 5, 37]
# in    650
# out   [2, 5, 5, 13]

def with_multipliers (number):
    with open("f1.txt", "a", encoding="utf-8") as my_f:     
        i = 2                       # первое простое число возможного сомножителя
        multiplier = number
        while i <= number:
            if multiplier % i == 0:
                my_f.write(f" {i}  ")
                multiplier //= i
                i = 2
            else:
                i += 1
    return 
      

number = int(input("Введите целое число: "))
with_multipliers (number)
f = open('f1.txt', 'r')
for line in f:
    print(f"[ {line}]")
f.close()



