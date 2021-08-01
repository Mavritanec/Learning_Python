import time
from typing import Callable, Any


# тяжеловесная функция
def sum_of_squares() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


# тяжеловесная функция
def sum_of_cubes(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


# т.к., в аргумент передаем функцию, эта функция называется функцией высшего порядка
# также такие функции могут возвращать функцию как результат работы или делать все вышеперечисленное одновременно
# обычные функции наз-ся функциями / объектами первого класса
# и могут передаваться и использоваться в качестве аргумента для других функций
# Callable - переводится как вызываемая
def timer(func: Callable) -> Any:
    """ Функция-таймер. Выводит время работы функции и возвращает ее результат """
    # приставка f_ чтобы не было совпадения имен
    f_start_time = time.time()
    result = func()
    f_end_time = time.time()
    f_run_time = round(f_end_time - f_start_time, 3)
    print('Программа работала {} сек'.format(f_run_time))
    return result


# когда принимаемая функция требует один аргумент
def timer_with_arg(func: Callable, number: int) -> Any:
    """ Функция-таймер. Выводит время работы функции и возвращает ее результат """
    # приставка f_ чтобы не было совпадения имен
    f_start_time = time.time()
    result = func(number)
    f_end_time = time.time()
    f_run_time = round(f_end_time - f_start_time, 3)
    print('Программа работала {} сек'.format(f_run_time))
    return result


# для произвольного количества и типа аргументов
def timer_with_args(func: Callable, *args, **kwargs) -> Any:
    """ Функция-таймер. Выводит время работы функции и возвращает ее результат """
    # приставка f_ чтобы не было совпадения имен
    f_start_time = time.time()
    result = func(*args, **kwargs)
    f_end_time = time.time()
    f_run_time = round(f_end_time - f_start_time, 3)
    print('Программа работала {} сек'.format(f_run_time))
    return result


if __name__ == '__main__':
    # 1-й способ замера времени работы программы
    # но, писать так каждый раз не лучший вариант
    start_time = time.time()
    run = sum_of_squares()
    end_time = time.time()
    run_time = round(end_time - start_time, 3)
    print('Программа работала {} сек'.format(run_time))

    # 2-й способ
    time_run_1 = timer(sum_of_squares)
    # заметьте, что при присвоении timer отрабатывает
    # и в переменную time_run_1 записывается результат (return функции timer)
    print(type(time_run_1))

    # если передаваемая функция имеет аргумент
    time_run_2 = timer_with_arg(sum_of_cubes, 100)

    # а, если аргументов произвольное количество?
    # необходимо использовать операторы распаковки (вспоминаем про звездочки)
    time_run_3 = timer_with_args(sum_of_cubes, 100)
