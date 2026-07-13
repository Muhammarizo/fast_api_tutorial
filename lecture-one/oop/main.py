from enemy import *
from inheritance.dog import *


zombie = Enemy('Zombie', 10, 1)


print(zombie.get_type_of_enemy())

dog = Dog()
dog.eat()
