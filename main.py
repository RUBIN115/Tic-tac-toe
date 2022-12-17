def greet():
    print("--------------------")
    print("  Приветствуем вас  ")
    print("       в игре       ")
    print("   крестики-нолики  ")
    print("--------------------")
    print("  формат ввода: x y ")
    print("  x - номер строки  ")
    print("  y - номер столбца ")

greet()


field = [[" "] * 3 for i in range(3)] # создаём список из списков в виде игрового поля 3x3
# в этом списке храним данные


#создадим функции, которые будут запрашивать данные у пользователя и,если пользователь написал что-то неправильно,
#то эти самые функции будут запрашивать ввод от пользователя снова с снова до тех пор,
#пока он не введёт координаты, возможные для ввода

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print(" ---------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ---------------- ")
    print()

#функция show делает список field более удобным к прочтению для пользователя

def ask():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print(' Введите ДВЕ координаты! ')
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Введите ЧИСЛА! ')
            continue

        x = int(x)
        y = int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Координаты вне диапазона! ')
            continue

        if field[x][y] != ' ':
            print(' Клетка занята! ')
            continue

        return x, y

#функция ask запрашивает ввод от пользователя снова с снова до тех пор,
#пока он не введёт координаты, возможные для ввода

def win_checking():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
            if symbols == ["X", "X", "X"]:
                print("Выиграл крестик!")
                return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
            if symbols == ["X", "X", "X"]:
                print("Выиграл крестик!")
                return True

        symbols = []
        for i in range(3):
            symbols.append(field[i][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!")
            return True

        symbols = []
        for i in range(3):
            symbols.append(field[i][2 - i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
            if symbols == ["0", "0", "0"]:
                print("Выиграл нолик!")
                return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
            if symbols == ["0", "0", "0"]:
                print("Выиграл нолик!")
                return True

            symbols = []
            for i in range(3):
                symbols.append(field[i][i])
            if symbols == ["0", "0", "0"]:
                print("Выиграл нолик!")
                return True

            symbols = []
            for i in range(3):
                symbols.append(field[i][2 - i])
            if symbols == ["0", "0", "0"]:
                print("Выиграл нолик!")
                return True

        return False

win_checking()

#функция win_checking проверяет выигрышные комбинации

num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print(' Ходит крестик ')
    else:
        print(' Ходит нолик ')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_checking():
        break

    if num == 9:
        print(' Ничья! ')
        break
