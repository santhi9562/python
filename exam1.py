class Person:
    def __init__(self,name,age):

        self.name=name
        self.age=age
    def dispaly(self):
          
          print("hello")

class Employee(Person):
        def display(self):
             print("hello!!",self.name)
class Employeeage(Person):
         def display(self):
               print("hello!!",self.age)


a=Employee("davis",22)
a.display()
s=Employeeage("dennis",23)
s.display()


    
    
               


