#
#   Demonstrate creating classes and inheritance
#   Set attributes with default values


class Animal:
    has_fur = 'true'
    number_of_legs = 4

class Cat(Animal):
    claw_sharpness = 86 # on a 0-100 scale
    number_of_lives = 9 # normal value is 1

class Turtle(Animal):
    breath_underwater = 'true'
    animal_type = 'Reptile'
    
    
    
