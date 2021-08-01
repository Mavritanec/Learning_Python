import time
from typing import Callable, Any
from example_09 import sum_of_squares, sum_of_cubes


def timer(func: Callable) -> Callable:
    """ Декоратор. Выводит время работы декорируемой функции """
    def wrapped_func(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = round(end_time - start_time, 3)
        print('Программа работала {} сек'.format(run_time))
        return result
    return wrapped_func


if __name__ == '__main__':
    # @timer
    # sum_of_cubes()

    sum_of_squares()
