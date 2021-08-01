import random


# создадим итератор или из класса сделаем итератор
class RandomNumbers:
    def __init__(self, length):
        self.__length = length
        self.__counter = 0

    # этот метод должен возвращать итератор,
    # а, т.к. наш класс это и есть итератор, то метод будет возвращать сам себя
    # а, вообще, здесь можно сбрасывать значений (перезапускать итератор)
    # или возвращать итератор от другого класса
    def __iter__(self):
        return self

    # чтобы перебирать значения в цикле
    def __next__(self):
        if self.__counter < self.__length:
            self.__counter += 1
            return random.randint(0, 10)
        else:
            raise StopIteration


# итератор по числам Fibonacci
class Fibonacci:
    def __init__(self, number):
        self.count = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number

    # тут как раз перезапускаем итератор,
    # чтобы по нему можно было итерироваться произвольное количество раз
    def __iter__(self):
        self.count = 0
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        self.count += 1
        if self.count > 1:
            if self.count > self.number:
                raise StopIteration
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
        return self.next_val


if __name__ == '__main__':
    custom_iter = RandomNumbers(length=3)

    for num in custom_iter:
        print(num)

    print('\n\n')
    fib_iterator = Fibonacci(10)

    for i_val in fib_iterator:
        print(i_val)

    # чтобы итератор не оказался пустым и по нему можно было итерироваться повторно
    # в методе __iter__ класса был предусмотрен сброс параметров итератора
    print(8 in fib_iterator)
    # такие вычисления называют ленивыми
    # (мы не храним все значения в памяти, а храним только необходимые
    # и вычисляем следующие по мере их необходимости
    # (как бы, лениво (если надо, так надо, а если нет, то и не надо)))
    # или lazy evaluation
