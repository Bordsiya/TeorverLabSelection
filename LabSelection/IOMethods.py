from tabulate import tabulate
from Selection import Selection, Type


def get_input_data():
    print("Введите количество чисел в выборке:")
    n = input()
    try:
        n = int(n.strip().replace(',', '.'))
    except ValueError:
        print("Ошибка: небходимо ввести целое число")
        exit(1)

    arr = []
    try:
        print("Введите построчно числа в выборке: ")
        for i in range(n):
            a = float(input().strip().replace(',', '.'))
            arr.append(a)
    except ValueError:
        print("Ошибка: необходимо ввести число")
        exit(1)
    return n, arr


def print_table(selection: Selection):
    if selection.type == Type.DISCRETE:
        headers = ["x", "p"]
        table = []
        for i in range(selection.n):
            table.append([selection.x_arr[i], selection.p_arr[i]])
        print(tabulate(table, headers, tablefmt="github"))
    else:
        headers = ["x_left", "x_right", "p"]
        table = []
        for i in range(selection.n):
            table.append([selection.x_arr[i][0], selection.x_arr[i][1], selection.p_arr[i]])
        print(tabulate(table, headers, tablefmt="github"))


def print_distribution_func(selection: Selection):
    print("F = ")
    if selection.type == Type.DISCRETE:
        headers = ["x", "p_н"]
        table = []
        sum_p = 0
        for i in range(selection.n):
            sum_p += selection.p_arr[i]
            table.append([selection.x_arr[i], sum_p])
        print(tabulate(table, headers, tablefmt="github"))
    else:
        headers = ["x_left", "x_right", "p_н"]
        table = []
        sum_p = 0
        for i in range(selection.n):
            sum_p += selection.p_arr[i]
            table.append([selection.x_arr[i][0], selection.x_arr[i][1], sum_p])
        print(tabulate(table, headers, tablefmt="github"))
