# это базовый класс
# еще его могут называть родительским или супер-классом
class Pet:
    __legs = 4
    has_tail = True

    def __str__(self):
        tail = 'присутствует' if self.has_tail else 'отсутствует'
        return 'Оно с {} ногами\nХвост {}'.format(self.__legs, tail)

    def walk(self):
        print('Гуляет')


# так реализовывается наследование
# это подклассы или дочерние классы
# при наследовании классы получают все атрибуты и методы родительского класса
class Cat(Pet):
    def sound(self):
        print('Мяу')


class Dog(Pet):
    def sound(self):
        print('Гав')


class Frog(Pet):
    # переопределение атрибута
    # приватные атрибуты так не переопределяться (точнее, не попадут в __str__ родительского класса)
    has_tail = False
    __legs = 3

    def sound(self):
        print('Ква')

    def get_legs(self):
        return self.__legs

    # переопределили метод базового класса
    # данная возможность называется полиморфизмом
    # есть еще функция super()
    def walk(self):
        print('Плавает')


if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    frog = Frog()

    print(cat)
    print(dog)
    print(frog)

    # так делать не надо!
    print(Frog._Frog__legs, id(Frog._Frog__legs))

    print(frog.get_legs(), id(frog.get_legs()))
