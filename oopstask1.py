class Animal:
    def __init__(self,name):
    

       self.name=name
    def makesound(self):
        print("wowww")

class Dog(Animal):
    def makesound(self):
        print("bowww boww",self.name)

class Cat(Animal):
    def makesound(self):
        print("meowwwwww",self.name)



s=Dog("labarodor")
s.makesound()



