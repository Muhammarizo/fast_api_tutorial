from .animal import *


class Dog(Animal):
    can_shed: bool
    domestic_name: str

    def eat(self): # bu yerda animal class dagi eat ni override qildik
        print('Dog eating')
