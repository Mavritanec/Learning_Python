from typing import Callable
import functools
from datetime import datetime
import time


# декоратор для класса
# cls, т.к. передаем класс, а не функцию
# аннотацию обычно не ставят, т.к. есть cls
def create_time(cls):
    """ Декоратор класса. Выводит время создания инстанса класса. """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        inst = cls(*args, **kwargs)
        print('Класс создан в', datetime.utcnow())
        return inst
    return wrapper


def timer(func: Callable) -> Callable:
    """ Декоратор. Выводит время работы функции """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = round(end_time - start_time, 3)
        print('Функция работала {} сек'.format(run_time))
        return result
    return wrapped


def for_all_methods(dec: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса.
    """

    @functools.wraps(dec)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.endswith('__') is False:
                # сюда попадают статические атрибуты класса, хотя работает и с ними
                # timer будет мерить время объявления переменной,
                # но это только в случае с timer
                cur_method = getattr(cls, i_method)
                if callable(cur_method):
                    dec_method = dec(cur_method)
                    setattr(cls, i_method, dec_method)
        return cls
    return decorate


# если здесь поставить декоратор timer, то он будет мерить только время инициализации класса
# можно задекорировать все методы, но это не вариант,
# т.е. нужен декоратор для класса, который задекорирует все методы с помощью другого декоратора
@create_time
@for_all_methods(timer)
class Sums:
    count = 0
    psw = True

    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        num = 100
        res = 0
        for _ in range(num + 1):
            res += sum([i ** 2 for i in range(self.max_num)])
        return res

    def cubes_sum(self, num: int) -> int:
        res = 0
        for _ in range(num + 1):
            res += sum([i ** 2 for i in range(self.max_num)])
        return res


if __name__ == '__main__':
    #  для декоратора класса
    sum_1 = Sums(max_num=1000)
    time.sleep(1)
    sum_2 = Sums(max_num=2000)
    time.sleep(1)
    sum_3 = Sums(max_num=3000)

    sum_1.squares_sum()
    sum_1.cubes_sum(num=2000)
