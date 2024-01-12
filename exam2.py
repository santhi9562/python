class Shape:
    def __init__(self,area):
        self.area=area
        def display(self):
            print("hai")
    

class Circle(Shape):
    def dispaly(self):
        print("area is ",self.area)

class Rectangle(Shape):
    def display(self):
        print("area is ",self.area)




s=Circle(176)
s.dispaly()
c=Rectangle(13)
c.display()        