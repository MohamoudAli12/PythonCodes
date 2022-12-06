class BankAccount:

    def __init__(self, AccountNumber, Name, Balance):
        self.AccountNumber = AccountNumber
        self.Name = Name
        self.Balance = Balance

    def Deposit(self, DepositAmount):
        self.Balance = self.Balance + DepositAmount

    def Withdrawal(self, WithdrawalAmount):

        if  self.Balance < WithdrawalAmount or self.Balance == 0:
            print ("Incorrect operation. Please check your Balance")
        else:
           self.Balance = self.Balance - WithdrawalAmount
           print ("you have successfully withdrawn:$", WithdrawalAmount)
        

    def BankFees(self):
        self.Balance = self.Balance * 0.05
        print ("Bank fees is :", self.Balance)

    
    def Display(self):
        print("Account number is:", self.AccountNumber)
        print("Account Name is :", self.Name)
        print("Balance is :",self.Balance)

myAccount = BankAccount(1452542, "Mohamoud", 50000)
myAccount.Display()
#myAccount.Deposit(500)
myAccount.Withdrawal(200)

myAccount.BankFees()
