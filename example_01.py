# объектно-ориентированное программирование - это одна из парадигм программирования
# формальное описание объекта называется классом
class SomeClass:
    # статические атрибуты класса (иногда их еще называют переменными класса, а то и константами)
    variable_1 = 'text'
    variable_2 = 12345
    variable_n = False
    massive_1 = []

    # метод класса
    # атрибут self - ссылка на текущий объект
    # по умолчанию (соглашение Python) это первый атрибут в любом методе класса
    # и может быть любым словом (к примеру this)
    def some_func(self):
        print('Какие-то переменные: {}, {}, ..., {}.'
              .format(self.variable_1, self.variable_2, self.variable_n))
        # без self Python просто не видит данные переменные

    # метод с аргументом
    def add_some_element(self, elem):
        self.massive_1.append(elem)


# этот блок кода будет выполнен только при прямом запуске файла .py (запуск как основная программа)
# если код (классы, функции и пр.) этого файла были импортированы,
# то выполнения ниже представленного кода не произойдет
if __name__ == '__main__':
    # создание объекта класса SomeClass (инстанс / экземпляр класса)
    object_1 = SomeClass()
    # доступ к атрибутам
    print(object_1.variable_1)

    # изменение (переприсваивание) атрибута
    object_1.variable_1 = 'not text'
    object_2 = SomeClass()
    # значение атрибута в самом классе не поменялось
    print(object_1.variable_1, object_2.variable_1)

    # обращение к атрибуту самого класса, а не экземпляра
    print(SomeClass.variable_2)
    SomeClass.variable_2 = 54321
    print(object_1.variable_2, object_2.variable_2)
    # НО:
    object_2.variable_n = None
    SomeClass.variable_n = True
    print(object_1.variable_n, object_2.variable_n)

    # обращение к методу
    object_1.some_func()

    # добавим элемент в massive_1 объекта object_1
    object_1.add_some_element('первый элемент')
    print(object_1.massive_1)
    # а можно добавить и другой объект
    object_1.add_some_element(object_2)
    print(object_1.massive_1)
    print(object_1.massive_1[1] == object_2)
