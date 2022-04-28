from GraphMethods import draw_polygon, draw_histogram, draw_distribution_function
from IOMethods import print_table, print_distribution_func, get_input_data
from MathMethods import get_estimated_math_expectation, get_estimated_standart_deviation
from Selection import create_discrete_selection, create_interval_selection

n, arr = get_input_data()

discrete_selection = create_discrete_selection(n, arr)
interval_selection = create_interval_selection(n, arr)

print("------------------------")
print("Дискретная выборка")
print_table(discrete_selection)
print("Минимальное значение: ", discrete_selection.extreme_min)
print("Максимальное значение: ", discrete_selection.extreme_max)
print("Размах: ", discrete_selection.range)
print("Оценка математического ожидания: ", get_estimated_math_expectation(discrete_selection))
print("Оценка среднеквадратического отклонения: ", get_estimated_standart_deviation(discrete_selection))
draw_polygon(discrete_selection)
print_distribution_func(discrete_selection)
draw_distribution_function(discrete_selection)
print("\n\n------------------------")

print("Интервальная выборка")
print_table(interval_selection)
print("Минимальное значение: ", interval_selection.extreme_min)
print("Максимальное значение: ", interval_selection.extreme_max)
print("Размах: ", interval_selection.range)
print("Оценка математического ожидания: ", get_estimated_math_expectation(interval_selection))
print("Оценка среднеквадратического отклонения: ", get_estimated_standart_deviation(interval_selection))
draw_histogram(interval_selection)
print_distribution_func(interval_selection)
draw_distribution_function(interval_selection)
print("------------------------")


