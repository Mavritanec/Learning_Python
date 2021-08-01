class SomeClass3:
    # атрибут стал приватным, и обратиться к нему за пределами класса становиться невозможным
    # (хотя Python допускает одну конструкцию: SomeClass3._SomeClass3__count,
    # т.е. если нельзя, но очень хочется, то можно)
    # это называется сокрытием данных и входит в один из принципов ООП (инкапсуляция),
    # но инкапсуляция это не только сокрытие (это еще и объединение данных и методов)
    __count = 0
    __name = __qualname__

    # хорошей практикой считается сокрытие всех полей объектов от прямого присвоения им значений
    def __init__(self, var_1, var_2):
        self.__variable_1 = self.set_var_1(var_1)
        self.__variable_2 = var_2
        SomeClass3.__count += 1

    def __repr__(self):
        return 'Это объект {} класса {}'.format(self.__count, self.__name)

    # чтобы получить приватный атрибут можно создать соответствующий метод
    # такой метод называется геттером
    def get_count(self):
        return self.__count

    # такой метод называется сеттером
    # про статические методы см. дальше
    def set_var_1(self, var):
        if isinstance(var, str):
            return var
        else:
            if var < 0:
                raise ValueError('Для первой переменной недопустимо отрицательное значение')
            else:
                return var


if __name__ == '__main__':
    object_1 = SomeClass3('one', 'two')
    object_2 = SomeClass3(1, 2)
    object_3 = SomeClass3(False, True)
    massive_1 = [object_1, object_2, object_3]
    print(massive_1)
    object_4 = SomeClass3(-1, 2)
