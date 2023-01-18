# Задание 5 Задача 3
# Создайте программу для игры в "Крестики-нолики".
# Поле 3x3. Игрок - игрок, без бота.

field = [1,2,3,         # игровое поле
         4,5,6,
         7,8,9]
 
wins = [[0,1,2],        # перечень победных комбинаций
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]
 
def print_field():              # вывод игрового поля
    print(field[0], end=' ')
    print(field[1], end=' ')
    print(field[2])
    print(field[3], end=' ')
    print(field[4], end=' ')
    print(field[5])
    print(field[6], end=' ')
    print(field[7], end=' ')
    print(field[8])

def step_field(step, symbol):   # ход в ячейку поля
    ind = field.index(step)
    field[ind] = symbol
 
def checkwin():                 # текущий результат игры
    win = ''
    for i in wins:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            win = 'X'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            win = 'O'   
    return win
 
def check_line(sum_O, sum_X):   # поиск линии "!!!" с нужным количеством X и O на победных линиях
 
    step = ''
    for line in wins:
        o = 0
        x = 0
 
        for j in range(0,3):
            if field[line[j]] == 'O':
                o = o + 1
            if field[line[j]] == 'X':
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if field[line[j]] != 'O' and field[line[j]] != 'X':
                    step = field[line[j]]
    return step
 
def bot_move():     # выбор хода "!!!"   
 
    step = ''

 
    step = check_line(2, 0) # ход, если на какой-либо из победных линий, 2-е свои фигуры и 0-ль чужих
 
    # ходит, если на какой либо из победных линий, 2-е чужие фигуры и 0 своих
    if step == '':
        step = check_line(0, 2)        
 
    # ходит, если 1-а фигура своя, 0 чужих
    if step == '':
        step = check_line(1, 0)           
 
    # центр пуст, занимаем центр
    if step == '':
        if field[4] != 'X' and field[4] != 'O':
            step = 5           
 
    # если центр занят, то занимает первую ячейку
    if step == '':
        if field[0] != 'X' and field[0] != 'O':
            step = 1           
    return step
 
def main():
    game_over = False
    player = True
    
    while game_over == False:
    
        # показываем поле
        print_field()
    
        # ход ЧЕЛОВЕКА
        if player == True:
            symbol = 'X'
            step = int(input('Ваш ход: '))
        else:
            # ход МАШИНЫ
            print('Компьютер делает ход: ')
            symbol = 'O'
            step = bot_move()
    
        # если МАШИНА нашла куда сделать ход, то играем, если нет, то конец игры
        if step != '':
            step_field(step, symbol)
            # определим, есть ли победитель
            win = checkwin()
            if win != '':
                game_over = True
            else:
                game_over = False
        else:
            game_over = True
            win = 'Ничья'
    
        player = not(player)        
    
    # игра окончена, вывод результатов
    print_field()
    if win == 'Ничья':
        print('Ничья!')
    else:
        print('Победил', 'МАШИНА' if win=='O' else 'ЧЕЛОВЕК')
if __name__ == '__main__':
    main()