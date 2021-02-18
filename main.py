test = [['0', 'x', 'x'],
        ['0', 'x', '0'],
        ['x', '0', 'x']]


def check_horizontal_rows(M, sign):
    pos = 0
    while pos < 3:
        result = True
        for x in M[pos]:
            result = result and x == sign
        yield result
        pos += 1


def check_vertical_rows(M, sign):
    pos = 0
    while pos < 3:
        result = True
        for x in M:
            result = result and x[pos] == sign
        yield result
        pos += 1


def check_diagonal_row(M, sign):
    pos = 0
    while pos < 2:
        result = True
        for i in range(3):
            result = result and M[i][i if pos == 0 else 2 - i] == sign
        yield result
        pos += 1


def won(M, sign):
    return any(check_horizontal_rows(M, sign)) or\
           any(check_vertical_rows(M, sign)) or\
           any(check_diagonal_row(M, sign))

def start():
    return [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]


def show_win_message(sign):
    str = "крестики" if sign == "x" else "нолики"
    print(f"Выиграли {str}")


def show_field(M):
    for i in range(3):
        for j in range(3):
            print(M[i][j], end=' ')
        print()
    print()


def move(moves, pos, sign):
    if 0 <= pos < 9 and moves[-1][pos // 3][pos % 3] == '-':
        moves.append(moves[-1])
        moves[-1][pos // 3][pos % 3] = sign
        show_field(moves[-1])
        return True
    return False


def crosses_move(moves):
    while not move(moves, int(input(f"{len(moves)}-й xод крестиков: ")) - 1, 'x'):
        print("эта позиция занята или не существует")
    if won(moves[-1], 'x'):
        show_win_message('x')
        return True
    return False


def noughts_move(moves):
    while not move(moves, int(input(f"{len(moves)}-й xод ноликов: ")) - 1, '0'):
        print("эта позиция занята или не существует")
    if won(moves[-1], '0'):
        show_win_message('0')
        return True
    return False


def run():
    moves = [start()]
    suspended = False

    while not suspended:
        if len(moves) % 2:
            suspended = crosses_move(moves)
        else:
            suspended = noughts_move(moves)


run()
