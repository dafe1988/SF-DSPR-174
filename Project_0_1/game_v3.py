"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

random_seed = 42 # задаем RANDOM SEED, чтобы эксперимент был воспроизводим!


def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_func ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(random_seed)  # фиксируем RANDOM SEED 
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


def midpoint(p1,p2):
    """Назначаем функцию, находящую середину интервала

    Args:
        p1 (int): начало интервала
        p2 (int): конец интервала

    Returns:
        int: число середины интервала
    """
    return int(p1 + (p2-p1)/2)

def game_core_v3(number: int = 1) -> int:
    """Все время берем среднее из уменьшающегося интервала

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1
    end = 101
    predict_number = midpoint(start,end) # предполагаемое число
    
    while number != predict_number:
        
        count+=1
        
        if predict_number < number:
            start = predict_number # назначаем угаданное число началом исследуемого интервала
            predict_number = midpoint(start,end)
        elif number < predict_number:
            end = predict_number # назначаем угаданное число концом исследуемого интервала
            predict_number = midpoint(start,end)

    return count

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
