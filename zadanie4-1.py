# Задание 4 Задача 1
# Вычислить число c заданной точностью d
# in Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out 9.000000

# in Enter a real number: 8.98785
# Enter the required accuracy '0.001': 0.001
# out 8.988

def order_accuracy (accuracy): # Определение порядка округления
    order=0
    z1=(accuracy)
    while  z1 < 1:
        z1=z1*10
        order= order+1
    return order
    

number = float(input("Введите действительное число : "))
accuracy = float(input("Введите требуемую точность для введенного вами числа : "))
print(f'число {number} c заданной точностью {accuracy} будет равно {round(number, order_accuracy (accuracy))}')

