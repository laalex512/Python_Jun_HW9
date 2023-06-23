# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********


def christmas_tree():
    rows = int(input("How many rows do the tree have?"))

    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars + spaces)

    for i in range(1, rows + 1):
        stars = "*" * (2 * i - 1)
        print(f"{stars:^{rows * 2}}")
