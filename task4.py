"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_with_sort(var_1, var_2, var_3):
    try:
        array = [var_1, var_2, var_3]
        array.sort()
        return array[1] + array[2]
    except TypeError:
        return


def my_func_without_sort(var_1, var_2, var_3):
    try:
        array = [var_1, var_2, var_3]
        array.pop(array.index(min(array)))
        sum_of_el = 0
        for el in array:
            sum_of_el += el
        return sum_of_el
    except TypeError:
        return


print(my_func_with_sort(2, 1, 8))
print(my_func_without_sort(10, 1, 8))
