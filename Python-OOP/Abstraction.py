
# Abstraction Assignment

from abc import ABC, abstractmethod

# base/abstract class Building
class Building(ABC):
    def enter(self):
        print("I am entering...")

    @abstractmethod
    def exit(self, throughWhat):
        pass

# child class 
class Narnia(Building):
    def exit(self, throughWhat):
        print("though the wardrobe...",throughWhat)

# child class 
class TrainStation(Building):
    def exit(self, throughWhat):
        print("Through platform 9 and three-quarters...",throughWhat)

# Instantiation of child classes
brockport = Narnia()
brockport.enter()
brockport.exit("Like a normal person...")
viewChurch = TrainStation()
viewChurch.enter()
viewChurch.exit("Like a normal person...")
