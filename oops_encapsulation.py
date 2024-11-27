
class Bankaccount :
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
            self.__balance+=amount
            print(f"Deposited{amount}.New balance is{self.__balance}.")
    def withdraw(self,amount):
            if amount<=self.__balance:
                self.__balance-=amount
                print(f"withdraw{amount} New balance is{self.__balance}.")
            else:
                print("insufficient balance.")
account=Bankaccount("123456789",1000)
account.deposit(500)
account.withdraw(200)
