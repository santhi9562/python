class Animal:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print("hello inheritance")

class dog(Animal):
    def speak (self):
        print("says wooofff!!!",self.name)

class cat(Animal):
    def speak(self):
        print("hey meow!!!!!!",self.name)



C=Animal("hai")
C.speak()

    