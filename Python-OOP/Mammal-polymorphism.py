#                   Practice creating classes, utilizing polymorphism
#                   Remember: a child class can override the behavior
#                   of the parent class.

msg = ("Welcome to the Mammal game, where you decide \nwhat each Mammal does or doesn't do. \n\nFirst up...")
print(msg)

# parent class Mammal
class Mammal:
    family = "cougar"
    name = "Baxter"
    legs = 4
    arms = 0
    carnivore = "y"

    def information(self):
        msg = "\nFamily: {}\nName: {}\nLegs: {}\nArms: {}\nCarnivore: {}".format(self.family,self.name,self.legs,self.arms,self.carnivore)
        print(msg)

    def question(self):
        carnivore = input("\nDoes this mammal eat meat? (Y/N): \n>>> ").lower()
        if (carnivore == self.carnivore):
            print("Cheers!")
        else:
            print("Want some dressing with your salad!?")


# child class Human
class Human(Mammal):
    family = "Homosapien"
    name = "Greg"
    legs = 2
    arms = 2
    stands_upright = "y"
    makes_sense = "n"

    def information(self):
        msg = "\nFamily: {}\nName: {}\nLegs: {}\nArms: {}\nCarnivore: {}\nStands Upright: {}\nmakes_sense: {}".format(self.family,self.name,self.legs,self.arms,self.carnivore,self.stands_upright,self.makes_sense)
        print(msg)
    # polymorphism: child class 'Human' keeps the same function name of their parent class 'Mammal',
    # but we modify the functionality within this method.
    def question(self):
        carnivore = input("\nDoes this mammal eat meat? (Y/N): \n>>> ").lower()
        understandable = input("\nDoes this mammal make sense? (Y/N): \n>>> ").lower()
        if (carnivore == self.carnivore and understandable == self.makes_sense):
            print("You seem pleasant!")
        else:
            print("Got to go!")


# child class Bird
class Eagle(Mammal):
    family = "Bird"
    name = "Bald Eagle"
    legs = 2
    arms = 0
    can_fly = "y"
    feathers = "y"
    
    def information(self):
        msg = "\nFamily: {}\nName: {}\nLegs: {}\nArms: {}\nCarnivore: {}\nCan Fly: {}\nHas Feathers: {}".format(self.family,self.name,self.legs,self.arms,self.carnivore,self.can_fly,self.feathers)
        print(msg)
    # polymorphism: child class 'Eagle' keeps the same function name of their parent class 'Mammal',
    # but we modify the functionality within this method.
    def question(self):
        carnivore = input("\nDoes this mammal eat meat? (Y/N): \n>>> ").lower()
        fly = input("\nDoes this mammal fly? (Y/N): \n>>> ").lower()
        if (carnivore == self.carnivore and fly == self.can_fly):
            print("Spread your wings and fly!")
        else:
            print("Sorry, no bird's eye view here...")
    

# the following code invokes the methods inside each class
cougar = Mammal()
cougar.information()
cougar.question()

human1 = Human()
human1.information()
human1.question()

eagle1 = Eagle()
eagle1.information()
eagle1.question()

thanks = "\n\nThanks for playing!"
print(thanks)




    
