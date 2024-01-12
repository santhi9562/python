from abc import ABC,abstractmethod


class Shape(ABC):
    def area(self):
        print("area of the shape")

    def perimeter(self):
        print("perimeter of the shape")


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
    def parameter(self):
        return 2*3.14*self.radius
    
class Square(Shape):
    def __init__(self,length):
        self.length=length

    
    def area(self):
        return self.length**2
    
    def perimeter(self):
        return 4*self.length
    


c=Circle(4)
s=Square(3)


print("area is:",c.area())
print("area is:",s.area())
    
