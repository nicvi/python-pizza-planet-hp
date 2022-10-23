import random
import string
from typing import Any, Union
from datetime import datetime


def get_random_string() -> str:
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters[:10])


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def get_random_price(lower_bound: float, upper_bound: float) -> float:
    return round(random.uniform(lower_bound, upper_bound), 2)


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy


def get_random_email() -> str:
    return f"{get_random_string()}@{get_random_choice(['hotmail.com', 'gmail.com', 'test.com'])}"


def get_random_sequence(length: int = 10) -> str:
    digits = list(map(str, range(10)))
    sequence = [digits[random.randint(0, 9)] for _ in range(length)]
    return ''.join(sequence)


def get_random_phone() -> str:
    return get_random_sequence(10)


def get_random_month():
    return random.randint(2, 12)


def random_date() -> str:
    random_date = datetime(
        2022, random.randint(1, 12), random.randint(1, 28),
        random.randint(9, 22), random.randint(1, 59), 5)
    return str(random_date)


def random_id_list() -> list:
    id_list = []
    id_list_size_options = [1, 2, 3, 4, 5]
    id_list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    id_number = 0
    while id_number < random.choice(id_list_size_options):
        random_id = str(random.choice(id_list_elements))
        while random_id in id_list:
            random_id = str(random.choice(id_list_elements))
        id_list.append(random_id)
        id_number += 1
    return id_list


def random_size_id() -> str:
    size_id_options = [1, 2, 3, 4, 5]
    size_id = str(random.choice(size_id_options))
    return size_id
