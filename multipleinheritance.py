class Calculation1:
    def summation(self,a,b):
        return a+b;
class Calculation1:
    def multiplication(self,a,b):
        return a*b;

class Calculation3(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b;
d=Calculation3
    
