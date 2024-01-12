class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    

class Car(Vehicle):
    def display(self):
        print("hurry up!!",self.brand,"model is",self.model)
class Motorcycle(Vehicle):
    def display(self):
        print("hurry",self.brand,"model is ",self.model)

s=Car("volks","polo")
s.display()
c=Motorcycle("bmw","5 series")
c.display()
