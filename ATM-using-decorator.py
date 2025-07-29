
#-----------ATM------------
def authentification(original_function):
    def wrapper(self,*args,**kwargs):
        if not self.loggedin:
            print("please log in first")
            return
        return original_function(self,*args,**kwargs)
    return wrapper
#class block starts here
#ATM class with decorator for authentication
class ATM:
    def __init__(self,name,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=balance
        self.loggedin=False
    
    def log_in(self,input_name,input_pin):
        if ((self.name==input_name) and (self.pin==input_pin)):
            self.loggedin=True
            print("login successful")
        else:
            print("invalid username or pin")
    @authentification
    def check_balance(self):
        print("Balance amount is:",self.balance)
    @authentification
    def deposit(self,num):
        var=num
        a=self.balance+num
        print("Deposited amount is:",var)
        print("After deposition:",a)
    @authentification
    def withdraw(self,number):
        if number>0 and number<8000:
            c=number
            print("ruppess:",c,"withdrawn")
        else:
            print("withdraw not possible because of insufficient balance")
        
        
obj=ATM("megus","1234",5000)
obj.log_in("megus","1234")
obj.check_balance()
obj.deposit(3000)
obj.withdraw(4000)





