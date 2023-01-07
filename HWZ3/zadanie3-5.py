# Задание №3 Задача №5 

# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Негафибоначчи
# in         8
# out       -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in        5
# out       5 -3 2 -1 1 0 1 1 2 3 5

def fibonacci_n(n): # Метод определения отрицательной части списка Фибоначчи
    fibo_negative = []
    a = 0
    b = 1
    fibo_negative.append(a)
    fibo_negative.append(b)
    n=n-2
    while n+1>0:
        f=a-(b)   
        fibo_negative.append(f)
        a=b
        b=f
        n=n-1
    fibo_negative.reverse() # Переворачивание списка Фибоначчи отрицательной части
    return (fibo_negative)

def fibonacci_p(n): # Метод определения положительной части списка Фибоначчи
    fibo_positive = []
    a=0
    b=1
    fibo_positive.append(b)
    n=n-2
    while n+1>0:
        f=a+(b)   
        fibo_positive.append(f)
        a=b
        b=f
        n=n-1
    return(fibo_positive)

n = int(input("enter an integer nunber: "))
lst1 = []
lst2 = []
lst = []
lst1 = fibonacci_n (n)
lst2 = fibonacci_p (n)
lst = lst1 + lst2 # Слияние отрицательной и положительной частей списка Фибоначчи
print(f" fibo_negative {lst1}")
print(f" fibo_positiv {lst2}")
print(f" fibonacci_negative_positiv {lst}")

