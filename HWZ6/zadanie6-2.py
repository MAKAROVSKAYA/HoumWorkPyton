# Урок №6 Задание №2

# Для чисел в пределах от 20 до n найти числа,
# кратные 20 или 21. Use comprehension.

def multiples_list(num):
    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]
print(multiples_list(int(input('print the number: '))))
