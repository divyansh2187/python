import math
class circle:
    def __init__(self , r):
        self.radius = r 
       
    
    def area(self):
     return  math.pi * self.radius * self.radius

    def peri(self):
        return 2 * math.pi * self.radius
    
    @property
    def print(self):
       print("area of circle is :" , self.area()) 
       print("perimeter of circle is :" , self.peri()) 
          

c1 = circle(5)
c1.area()
c1.peri()
c1.print


