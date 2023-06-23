# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#  Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:

def guess_number():
    from random import randint

    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    COUNT_ATTEMPTS = 10

    hidden_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    for i in range(1, COUNT_ATTEMPTS + 1):
        user_number = int(input(f"Attempt {i}. Enter your number: "))
        if (user_number < hidden_number):
            print("Upper")
        elif (user_number > hidden_number):
            print("Lower")
        else:
            print("You win!")
            return
    print("The number of attempts is over")
