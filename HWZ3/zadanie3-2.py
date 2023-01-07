# Задание №3 Задача №2

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in   4
#  out  [2, 5, 8, 10]
#       [20, 40]
# in   5
#  out  [2, 2, 4, 8, 8]
#  [16, 16, 4]

def composition_positions(l,k,dl): # Метод создания списка содержащего произведение парных (противостоящих) чисел другого списка
    number = len(l)
    for i in range(len(l)):
        while i < len(l)/2 and number > len(l)/2:
            number = number - 1
            p = l[i] * l[number]
            k.append(p)
            i += 1            
    if (len(l)) % 2 != 0:
      k.pop(dl-1)                # Удаление последнего элемента списка
      k.insert(dl-1, l[dl-1])    # Добавление последнего элемента списка
    return k    
    
import math
n = int(input("enter the number of numbers in the list:  "))
l = [ int(input("number=:  ")) for i in range(n) ] 
dl= math.ceil(n/2)
print (f"dl =:   {dl}")
k=[]
composition_positions(l,k,dl)

print (f"The source list =:   {l}")
print (f"The the resulting list =:   {k}")

