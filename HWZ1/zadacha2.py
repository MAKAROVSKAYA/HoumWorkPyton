# Задание 1 задача №2
# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for w in [True, False]:
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                if (w and z) or (not y) or ((not x) == (not w)):
                    result_logical = 'the statement is FALSE'
                else:
                    result_logical = 'the statement is TRUE'
print ( result_logical)
     
