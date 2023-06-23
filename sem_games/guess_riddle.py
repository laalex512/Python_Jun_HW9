# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны

def guess_riddle(riddle: str, guesses: list[str], count_tryes: int = 3):
    print(riddle)
    for i in range(count_tryes):
        current_guess = input("Введите отгадку:")
        if current_guess in guesses:
            print(f"Вы угадали с попытки №{i + 1}")
            return i + 1
        else:
            print("Неправильно")
    print("Попытки кончились")
    return 0
