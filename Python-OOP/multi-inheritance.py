#
#   Demonstrate creating classes and inheritance
#   Set attributes with default values


class Animals: 
      
    # Initializing constructor 
    def __init__(self): 
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
      
    def isMammal(self): 
        if self.isMammal: 
            print("It is a mammal.") 
      
    def isDomestic(self): 
        if self.mammals: 
            print("It is a domestic animal.") 
      
class Dogs(Animals): 
    def __init__(self): 
        super().__init__() 
  
    def isMammal(self): 
        super().isMammal() 
  
class Cat(Animals): 
    def __init__(self): 
        super().__init__() 
  
    def hasTailandLegs(self): 
        if self.tail and self.legs == 4: 
            print("Has legs and tail") 
  
# Dirver code 
Hebe = Dogs() 
Hebe.isMammal() 
Baxter = Cat() 
Baxter.hasTailandLegs() 
    
    
