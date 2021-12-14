from random import randint
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


def random_coords() -> (int, int):
    return randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
