# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#
#
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random

_BOARD_SIZE = 8


def is_valid(board: list[tuple[int, int]]) -> bool:
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i][0] == board[j][0] \
                    or board[i][1] == board[j][1] \
                    or abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return False
    return True


def generate_board():
    result_list = []
    for i in range(_BOARD_SIZE):
        """Немножко облегчил задачу генератору, чтобы хотя бы индексы по вертикали были уникальными
        Если делать по условию, чтобы все рандомно определялось, очень долго ждать 4 решения)
        Код для выполнения условий задачи закоментил ниже
        """
        j = random.randint(1, _BOARD_SIZE)
        result_list.append(tuple([i + 1, j]))
        # result_list.append(tuple(random.randint(1, _BOARD_SIZE) for _ in range(2)))
    return result_list


def print_board(board: list[tuple[int, int]]):
    output = [["   |" for _ in range(_BOARD_SIZE)] for _ in range(_BOARD_SIZE)]

    for queen in board:
        column, row = (i - 1 for i in queen)
        output[column][row] = " Q |"

    horiz_line = '----' * _BOARD_SIZE
    print(horiz_line)
    for row in output:
        print("|", end="")
        print("".join(row))
        print(horiz_line)
