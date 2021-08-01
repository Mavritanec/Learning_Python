import time
from typing import Callable, Any
from example_09 import sum_of_squares, sum_of_cubes


def timer(func: Callable, *args, **kwargs) -> Any:
    """ Функция-таймер. Выводит время работы функции и возвращает ее результат """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    run_time = round(end_time - start_time, 3)
    print('Программа работала {} сек'.format(run_time))
    return result


def new_timer(func: Callable, *args, **kwargs) -> Any:
    """ Функция-таймер. Выводит время работы функции и возвращает ее результат """
    def wrapped_func():
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = round(end_time - start_time, 3)
        print('Программа работала {} сек'.format(run_time))
        return result
    return wrapped_func


def new_timer_2(func: Callable) -> Callable:
    """ Декоратор. Выводит время работы декорируемой функции """
    def wrapped_func(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = round(end_time - start_time, 3)
        print('Программа работала {} сек'.format(run_time))
        return result
    return wrapped_func


# декорируем функцию
@new_timer_2
def sum_of_cubes_1(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


if __name__ == '__main__':
    # если мы хотим дополнить возможности функции не изменяя ее
    # допустим это функция из другого модуля,
    new_sum_of_squares_1 = timer(sum_of_squares)
    # получили результат работы ф-ции timer, у которой ф-ция sum_of_squares передана как аргумент

    # а, если мы хотим, чтобы результатом работы (возвратом) функции timer была другая функция?
    # и мы могли с ней обращаться как и с начальной функцией?
    # переделаем ее по новому, см. new_timer
    new_sum_of_squares_2 = new_timer(sum_of_squares)
    # и теперь функция возвращает функцию, а не результат работы
    new_sum_of_squares_2()

    # а если у нас есть аргумент в изменяемой функции
    new_sum_of_cubes_1 = new_timer(sum_of_cubes)
    # новую функцию сделали, а дальше:
    # new_sum_of_cubes_1() TypeError: sum_of_cubes() missing 1 required positional argument: 'number'
    # new_sum_of_cubes_1(100) TypeError: wrapped_func() takes 0 positional arguments but 1 was given

    # переделаем new_timer
    new_sum_of_cubes_2 = new_timer_2(sum_of_cubes)
    new_sum_of_cubes_2(100)
    # ф-ция new_timer_2 называется декоратором,
    # она как-бы оборачивает переданную ей функцию,
    # таким образом, модифицируя ее работу

    # т.к. это очень часто встречающийся прием,
    # в Python есть соответствующий синтаксис, см. конструкцию
    # теперь при обращении к функции sum_of_cubes_1 мы будем получать ее измененный декоратором результат
    print()
    sum_of_cubes_1(100)

    # декораторы являются одним из паттернов проектирования
    # один из минусов это усложнение отладки,
    # т.к. при вызове обернутой функции мы сначала оказываемся во wrapped_func
    # при сложных декораторах это сильно усложняет определение логики работы приложения
    # также достаточно проблематично раздекорировать функцию,
    # а иногда (из стороннего модуля) это и вовсе невозможно
