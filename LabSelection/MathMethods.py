import math

from Selection import Selection, Type


def get_estimated_math_expectation(selection: Selection):
    if selection.type == Type.DISCRETE:
        m = 0
        for i in range(selection.n):
            m += selection.x_arr[i] * selection.p_arr[i]
        return m
    else:
        m = 0
        for i in range(selection.n):
            m += ((selection.x_arr[i][0] + selection.x_arr[i][1]) / 2) * selection.p_arr[i]
        return m


def get_estimated_dispersion(selection: Selection):
    if selection.type == Type.DISCRETE:
        m = get_estimated_math_expectation(selection)
        q = 0
        for i in range(selection.n):
            q += (selection.x_arr[i] - m)**2 * selection.p_arr[i]
        return q
    else:
        m = get_estimated_math_expectation(selection)
        q = 0
        for i in range(selection.n):
            x_i = (selection.x_arr[i][0] + selection.x_arr[i][1]) / 2
            q += (x_i - m)**2 * selection.p_arr[i]
        return q


def get_estimated_standart_deviation(selection: Selection):
    return math.sqrt(get_estimated_dispersion(selection))