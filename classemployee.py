class Employee:
    def __init__(self,name,email,mob):
        self.name=name
        self.email=email
        self.mob=mob
    def display(self):
        print("name is:",self.name, "email is:",self.email ,"mob is:",self.mob)

e1=Employee("santhi","santhi@gmail.com",9562099701)
e1.display()
    