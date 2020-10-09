#
#   Demonstrate creating classes and inheritance
#   Set attributes with default values

class Class1: 
    def m(self):
        class1att = 'random1'
        class1att2 = 'random2'
        print("In Class1")  
        
class Class2(Class1): 
    def m(self):
        class2att = 'random1'
        class2att2 = 'random2'
        print("In Class2") 
  
class Class3(Class1): 
    def m(self):
        class3att = 'random1'
        class3att2 = 'random2'
        print("In Class3")      
      
class Class4(Class2, Class3): 
    def m(self):
        class4att = 'random1'
        class4att2 = 'random2'
        print("In Class4")    
  
obj = Class4() 
obj.m() 
  
Class2.m(obj) 
Class3.m(obj) 
Class1.m(obj) 
    
    
