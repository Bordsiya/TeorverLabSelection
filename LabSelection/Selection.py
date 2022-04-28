import math
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum, auto


class Type(Enum):
    DISCRETE = auto(),
    INTERVAL = auto()


@dataclass
class Selection:
    n: int
    x_arr: []
    n_arr: list[int]
    p_arr: list[float]
    h: float
    range: float
    extreme_min: float
    extreme_max: float
    type: Type


def create_discrete_selection(n: int, arr: list[float]) -> Selection:
    max_x = max(arr)
    min_x = min(arr)
    m = defaultdict(int)
    for i in range(n):
        m[arr[i]] += 1
    m = sorted(m.items())
    x_arr = []
    [x_arr.append(i[0]) for i in m]
    n_arr = []
    [n_arr.append(i[1]) for i in m]
    p_arr = []
    [p_arr.append(i[1] / len(arr)) for i in m]
    rng = max_x - min_x
    return Selection(len(x_arr), x_arr, n_arr, p_arr, 0, rng, min_x, max_x, Type.DISCRETE)


def create_interval_selection(n: int, arr: list[float]) -> Selection:
    max_x = max(arr)
    min_x = min(arr)
    h = round((max_x - min_x) / (1 + math.log(n, 2)), 3)
    x_arr = []
    curr = round(min_x - h / 2, 3)
    while curr < max_x:
        x_arr.append((curr, round(curr + h, 3)))
        curr += h
        curr = round(curr, 3)
    n_arr = [0] * len(x_arr)
    for i in range(n):
        for j in range(len(x_arr)):
            if (arr[i] >= x_arr[j][0]) and (arr[i] < x_arr[j][1]):
                n_arr[j] += 1
    p_arr = []
    [p_arr.append(i / len(arr)) for i in n_arr]
    rng = max_x - min_x
    return Selection(len(x_arr), x_arr, n_arr, p_arr, h, rng, min_x, max_x, Type.INTERVAL)


