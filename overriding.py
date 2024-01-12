class Bank:
    def getroi():
        return 10
class SBI(Bank):

    def getroi(self):
        return 7
class ICIC(Bank):
    def getroi(self):
        return 8
b1=Bank()
b2=SBI()
b3=ICIC()
print("bank rate of intrest:",b1.getroi())
print("bank rate of intrest:",b2.getroi())
print("bank rate of intrest:",b3.getroi())