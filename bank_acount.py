"""
make a random genrator generats a code for your acounts number import random as id
make a password sysytem
use encapsulation
make a history regestry for every transaction 
make the abality to transfer mony to other peopel and demand thier name and id 
integrate it with html css and make a web for this idea
the ability to make multuple acounts 
admin ability see whats happining
"""
def main():
    print("welcom. may you give me your name nickname and age to creat an acount")

main()
shouldcontinue = True
stop = False

while True:
    try:
        
        namee = str(input("your name: "))
          
        nicknamee = str(input("your nickname: "))
   
        agee = int(input("your age: "))
        
        if agee < 18 :
            print("you are under age begone kid!!")
            stop = True
            shouldcontinue = False
            break
            
        if not stop:
                print("your acount is now created!")
                account = 1
            
                print("unvalid operation")
    except ValueError:
        print("enter a valid number or text")
    else :
        break 


#1  this shooldnt be here
def check():
    if balance:
        return "your balance is {balance}"
#2
class make_acount:
    def __init__(self):
        self.name = namee
        self.nickname = nicknamee
        self.age = agee
        
    def __str__(self):
        return "the banks name is \"abu wassim\""
        
class managing:
    balance = 0
    def __init__(self):
        pass
        
    @classmethod
    def see_balance(cls,balance):
        return "your balance is {balance} $"
    @staticmethod
    def check():
        if account is None:
            return"you dont an acount yet sign up!!"
        return "loading..."
        check()
    def deposit(self):
        check()
        while True:
            try:
                deposit = int(input("how much do you want to deposit: "))
                break
            except ValueError:
                print("pls provide only numbers")
        balance += deposit 
        return balance
    
    def withdraw(self):
        pass
if shouldcontinue:
    while True:
        choice = input("what do you wish to do: deposit , withdraw or see your balance: ")
        choice = choice.lower()
        if choice == "deposit":
            try:
                amount = input(int("how much do you wana deposit: "))
       
            except ValueError:
                print("invalid operation")
            # continue from here
                    
                    
