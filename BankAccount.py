class BankAccount:

    def __init__(self, AccountNumber, Name, Balance):
        self.AccountNumber = AccountNumber
        self.Name = Name
        self.Balance = Balance

    def Deposit(self, DepositAmount):
        self.Balance = self.Balance + DepositAmount

    def Withdrawal(self, WithdrawalAmount):
    # Check if the balance is less than the withdrawal amount
        if self.Balance < WithdrawalAmount:
            print("Incorrect operation. Please check your balance")
        else:
        # Subtract the withdrawal amount from the balance
            self.Balance -= WithdrawalAmount
        print("You have successfully withdrawn: $", WithdrawalAmount)
        

    def BankFees(self):
        self.Balance = self.Balance * 0.05
        print ("Bank fees is :", self.Balance)

    
    def Display(self):
        print("Account number is:", self.AccountNumber)
        print("Account Name is :", self.Name)
        print("Balance is :",self.Balance)

#myAccount = BankAccount(1452542, "Mohamoud", 50000)
#myAccount.Display()
#myAccount.Deposit(500)
#myAccount.Withdrawal(200)

def test_bank_account():
    # Create a BankAccount object
    myAccount = BankAccount(1452542, "Mohamoud", 50000)

    # Test the Display method
    myAccount.Display()  # Expected output: "Account number is: 1452542, Account Name is: Mohamoud, Balance is: 50000"

    # Test the Withdrawal method
    myAccount.Withdrawal(200)  # Expected output: "You have successfully withdrawn: $200"
    myAccount.Withdrawal(500000)  # Expected output: "Incorrect operation. Please check your balance"

    # Test the BankFees method
    myAccount.BankFees()  # Expected output: "Bank fees is: 2500"

# Run the test
test_bank_account()