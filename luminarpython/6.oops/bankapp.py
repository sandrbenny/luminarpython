# self is a keyword used to point current class instance variable
# constructor to initializeinstance variable.automatically invoked during object creation.
# name ofobject is always __init__()
class bank:
    def __init__(self,acntno,name,balance,bankname):#constructoris always__init__
        self.acntno = acntno
        self.name = name
        self.balance = balance
        self.bankname=bankname
    def printValues(self):
        print(self.acntno)
        print(self.name)
        print(self.balance)
        print(self.bankname)
    def withdraw(self):
        print("your current balance:",self.balance)

        amount=int(input("enter the amount you want to withdraw"))
        if(amount>self.balance):
            print("transaction not possible.......")
        else:
            self.balance=self.balance-amount
            print("your current balance:",self.balance)
    def deposit(self):
        damount=int(input("enter the amount you want to deposit:"))
        self.balance=self.balance+damount
        print("your current balance:", self.balance)



acntno=int(input("enter your account number:"))
name=input("enter account holders name:")
balance=50000
bankname=input("enter your bankname:")
ob=bank(acntno,name,balance,bankname)
ob.printValues()
print("1.WITHDRAWAL.")
print("2.DEPOSIT.")
ch=int(input("enter your choice..."))
while(ch>0):
    if(ch==1):
        ob.withdraw()
        break
    elif(ch==2):
        ob.deposit()
        break
    else:
       break









1