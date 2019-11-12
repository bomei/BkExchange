import pickle
import pandas as pd
import chardet
import codecs


class Test:
    def __init__(self):
        pass

    def test_set_attr(self, name, value):
        self.__setattr__(name, value)

    def __str__(self):
        res = ''
        for each in self.__dict__:
            res += f'{each}:{self.__getattribute__(each)}'
        return res


if __name__ == '__main__':
    test = Test()
    print(test)
    test.test_set_attr('hello', 1)
    print(test)
