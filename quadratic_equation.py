import csv
import json
import math
import random
from pathlib import Path

path = ''


def solution(a, b, c) -> list:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        root1 = -b / (2 * a)
        root2 = None
    else:
        root1 = None
        root2 = None

    return [root1, root2]


def csv_gen(filename: str, count: tuple[int, int] = (100, 1000)):
    global path
    path = filename
    counts = random.randint(count[0], count[1])
    numbers = []
    for _ in range(counts):
        numbers.append([random.randint(1, 21) for _ in range(3)])
    with open(f'{filename}.csv', 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', lineterminator='\n')
        csv_write.writerows(numbers)


def save_results_deco(func):
    def wrapper(*args, **kwargs):
        global path
        input_data = func(*args, **kwargs)
        result_dict = {}
        for i in range(len(input_data[0])):
            result_dict.setdefault(i, (input_data[0][i], input_data[1][i]))
        with open(f'{path}.json', 'w', encoding='utf-8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=2)
        return result_dict

    return wrapper


def read_csv_deco(func):
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        results = []
        for line in numbers:
            results.append(solution(int(line[0]), int(line[1]), int(line[2])))
        return numbers, results

    return wrapper


@save_results_deco
@read_csv_deco
def passing_arguments(filename: str) -> list:
    numbers = []
    with open(f'{filename}.csv', 'r', encoding='utf-8') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line:
                numbers.append(line)
    return numbers
