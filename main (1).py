class BankAcount:
  def _init_(self,account_number,initial_balance=0):
   self._account_number=account_number
   self._account_holder_name=account_holder_name
   self._account_balance=initial_balance
  def deposite(self,account):
   if amount>0:
    self._account_balance+=amount
  return f"Deposited${amount}.New balance:${self._account_balance}"
 else:
return"Invalid deposit amount.Please enter a positive number."
def withdraw(self,amount):
  if amount>0 and amount<=self._account_balance:
    self._account_balance-=amount
    return f"Withdrew${amount}.New balance:${self._account balance}"elif amount<=0:
    return"Invalid withdrawal amount.Please enter a positive number."
  else:
    return"Insufficient funds for withdrawal."
    def display_balance(self):
      return f"Account Balance for {self._account_holder_name}:${self._account_balance"
      #Creating an instance of tje BankAcoount class
      my_account=BankAccount("12345","johnDeo",1000)
      #Testing deposit and withdrawal funcionality
      print(my_account.display_balance())
      #Display initial balance
      print(my_account.deposit(500))
      #Deposit$500
      print(my_account.withdaw(200))
#Withdraw$200
print(my_account.display_balance())
#Display updated balance