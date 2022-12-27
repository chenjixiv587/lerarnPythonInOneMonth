class Person(object):
    def __init__(self):
        self.__age = 90

    @property
    def age(self):
        return self.__age
   