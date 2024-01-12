class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
            print("hoorey",self.make)




class Car(Vehicle):
    def display(self,brand):
        self.brand=brand
        print("make is :",self.make,"brand is:",self.brand)


c=Vehicle('car',200)
c.start()
        