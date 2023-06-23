"""Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

from random import randint


def choice_num(min_num=1, max_num=100, count_tries=7):
    number = randint(min_num, max_num + 1)
    for _ in range(count_tries):
        input_num = int(input("Enter num: "))
        if input_num == number:
            return True
        elif input_num > number:
            print("Lower")
        else:
            print("Higher")
    return False


if __name__ == "__main__":
    print(choice_num(1, 100, 5))
