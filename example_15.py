class SampleCls:
    @classmethod
    def some_func(self):
        print('Вызов {}'.format(self.__name__))


print(type(SampleCls.some_func))
