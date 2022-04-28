import matplotlib.pyplot as plt
import numpy as np

from Selection import Selection, Type


def draw_polygon(selection: Selection):
    if selection.type == Type.INTERVAL:
        return
    plt.clf()
    plt.gcf().canvas.set_window_title("Полигон частностей")
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    X = selection.x_arr
    Y = selection.p_arr
    plt.xticks(np.arange(min(X), max(X) + 1, 1.0))
    axes.plot(X, Y)

    axes.scatter(selection.x_arr, selection.p_arr)

    plt.savefig('polygon')


def draw_histogram(selection: Selection):
    if selection.type == Type.DISCRETE:
        return
    plt.clf()
    plt.gcf().canvas.set_window_title("Гистограмма частностей")
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    x_middle_arr = []
    [x_middle_arr.append((i[0] + i[1]) / 2) for i in selection.x_arr]

    p_weights = []
    [p_weights.append(i / selection.h) for i in selection.p_arr]

    plt.bar(x_middle_arr, p_weights, [selection.h]*selection.n, edgecolor='k', linewidth=1)

    x = [selection.x_arr[0][0]]
    for i in range(1, selection.n):
        x.append(selection.x_arr[i-1][1])
        x.append(selection.x_arr[i][0])
    x.append(selection.x_arr[selection.n - 1][1])
    #plt.xticks(x)
    plt.yticks(p_weights)

    plt.savefig('histogram')


def draw_distribution_function(selection: Selection):
    plt.clf()
    plt.gcf().canvas.set_window_title("Функция распределения")
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    if selection.type == Type.DISCRETE:
        p_accumulated = []
        sum_p = 0
        for i in range(selection.n):
            p_accumulated.append(sum_p)
            sum_p += selection.p_arr[i]
        p_accumulated.append(sum_p)

        x = []
        for i in range(selection.n):
            x.append(selection.x_arr[i])
        x.append(selection.extreme_max + selection.h + 1)

        plt.step(x, p_accumulated)
        plt.hlines(y=0, xmin=selection.extreme_min - selection.h - 1, xmax=x[0])
        #plt.xticks(x)
        plt.yticks(p_accumulated)
        plt.savefig('distribution_func_discrete')
    else:
        p_accumulated = [0, 0]
        p_sum = 0
        for i in range(selection.n):
            p_sum += selection.p_arr[i]
            p_accumulated.append(p_sum)
        p_accumulated.append(p_sum)

        x = [selection.extreme_min - selection.h - 1, selection.x_arr[0][0]]
        for i in range(selection.n):
            x.append(selection.x_arr[i][1])
        x.append(selection.extreme_max + selection.h + 1)

        plt.plot(x, p_accumulated)
        plt.scatter(x[1:len(x)-1], p_accumulated[1:len(p_accumulated)-1])
        #plt.xticks(x[1:len(x)-1])
        plt.yticks(p_accumulated)
        plt.savefig('distribution_func_interval')


