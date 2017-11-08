import itertools
from random import randint

""""Three tellers for each bank have been created and the login details are
NAME        ID
jane         0
angela       1
christine    2
"""

class Bank():
    generator = itertools.count(1)
    def __init__(self, name, location):
        self.Name = str(name)
        self.Location = str(location)
        self.BankId = next(self.generator)
        self.customerSide = Customer()
        self.tellerSide = Teller()




class Customer():
    generator = itertools.count(1)
    def __init__(self):
        self.Database =  {}
        self.AcctNo = int(10000)

    def OpenAccount(self, name, initialDeposit, Address, PhoneNo,alc):
        self.CustomerId = int(next(self.generator))
        self.AcctNo +=1
        loan_balance = 0
        self.Name = str(name)
        self.Address = str(Address)
        self.Database[self.AcctNo] = [self.Name, initialDeposit, self.Address, PhoneNo, self.CustomerId, loan_balance]
        print('='*70)
        print("Account creation has been successful. Your account number is ", self.AcctNo)
        print('='*70)
        print()
        Account(self.CustomerId,alc)


    def authenticate(self, name, AcctNo):
        print()
        if AcctNo in self.Database.keys():
            if self.Database[AcctNo][0] == name:
                print("Authentication Successful")
                self.AcctNo = AcctNo
                print()
                return True
            else:
                print("Authentication Failed")
                print()
                return False
        else:
            print("Authentication Failed")
            print()
            return False


    def WithdrawMoney(self, withdrawalAmount):
        print()
        if withdrawalAmount > self.Database[self.AcctNo][1]:
            print("Insufficient balance")
        else:
            self.Database[self.AcctNo][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            self.displayBalance()
        print()

    def DepositMoney(self, depositAmount):
        print()
        if self.Database[self.AcctNo][5] != 0:
            if (0.4*depositAmount) > self.Database[self.AcctNo][5]:
                self.Database[self.AcctNo][1] += (depositAmount-self.Database[self.AcctNo][5])
            else:
                self.Database[self.AcctNo][1] += (0.6*depositAmount)
        else:
            self.Database[self.AcctNo][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()
        print()


    def displayBalance(self):
        print("Available balance: UGX ",self.Database[self.AcctNo][1])


    def GeneralInquiry(self):
        input("Please Enter your inquiry: \n")
        print()
        print("Thank you for contacting us, we will reply you in a short while on your phone Number")
        print()

    def CloseAccount(self):
        print("Are you sure you want to close your account? (yes or no)\n")
        self.close = input()
        if self.close == 'yes':
            print("The account ",self.Database.pop(self.AcctNo),"has been deleted")

    def RequestCard(self):
         CardProbability = randint(1,2)
         if CardProbability ==1:
             print("Your Card is ready. You can pick it at the Counter.")
         else:
             print("Your Card is not ready. Please try after one week.")

    def ApplyForLoan(self):
        self.loan_value= int(input("How much would you like to borrow?\n UGX: "))    
        if self.Database[self.AcctNo][1] >=(0.3*self.loan_value):
            print("You are eligible to obtain the loan")
            self.Database[self.AcctNo][1] += self.loan_value
            self.Database[self.AcctNo][5] += self.loan_value
           
            print("Loan credited to your account successfully.")
        else:
            print("You are not eligible for this loan. Please apply for a smaller loan.")
        Loan(self.CustomerId, self.AcctNo)



class Teller():
    tellers = 'jane','angela','christine'
    def __init__(self):
        self.name = Teller.tellers
        self.TellerId = 0
        self.Database = Customer().Database

    def CollectMoney(self,amount):
        Customer().DepositMoney(amount)
        

    def OpenAccount(self, name, initialDeposit, Address, PhoneNo,alc):
        Customer().OpenAccount(name, initialDeposit, Address, PhoneNo,alc)

    def authenticate(self, name, TellerId):
        print()
        if name in self.tellers:
            if TellerId == Teller.tellers.index(name):
                print("Authentication Successful")
                print()
                return True
            
            else:
                print("Authentication Failed")
                print()
                return False
        else:
            print("Authentication Failed")
            print()
            return False
        

    def CloseAccount(self): 
        Customer().CloseAccount()

    def LoanRequest(self):
        Customer().ApplyForLoan()

    def ProvideInfo(self):
        print('What is the customers query')
        input()
        print('We shall process his query in a minute!')

    def IssueCard(self):
        Customer().RequestCard()


class Account():
    Acc_generator = itertools.count(1)
    Ac_base = {}
    def __init__(self, CustomerId,account):
        self.CustomerId = CustomerId 
        self.AccId = int(next(self.Acc_generator))
        self.Ac_base[self.AccId] = [self.CustomerId]
        if account is 1:
            Checking()
        else:
            Savings()
      

class Checking(Account):
    Check_generator = itertools.count(1)
    def __init__(self):
        self.CheckId = int(next(self.Check_generator))


class Savings(Account):
    Savi_generator = itertools.count(1)
    def __init__(self):
        self.SaviId = int(next(self.Savi_generator))

class Loan():
    loan_generator = itertools.count(1)
    def __init__(self, custId, acctno):
        self.loanId = int(next(self.loan_generator))
        self.AccID =int(acctno)
        self.CustomerId = int(custId)
        




stanbic = Bank('Stanbic', 'Kampala')
dfcu = Bank('Dfcu','Jinja')

while True:
        print()
        print('Enter 1 to use Stanbic  bank or 2 to use Dfcu bank')
        print('1.Stanbic')
        print('2.Dfcu')
        userChoice = int(input())
        print()
    
        if userChoice is 1:
            while True:
                print()
                print('Enter 1 for teller or 2 for customer (You are in STANBIC BANK)')
                print('1.Teller')
                print('2.Customer')
                choice = int(input())
                if choice is 2:
                    print()
                    print("Enter 1 to create a new account")
                    print("Enter 2 to access an existing account")
                    print("Enter 3 to exit")
                    user_Choice = int(input())
                    print()
                    if user_Choice is 1:
                        print('Enter 1 for a checking account or enter 2 for a Savings account?')
                        print('1.Checking Account')
                        print('2.Savings Account')
                        acc_type = int(input())
                        print()
                        if acc_type is 1:
                            print("Enter your name: ")
                            name = str(input())
                            print ()
                            print("Enter your Address: ")
                            Address = str(input())
                            print ()
                            print("Enter your PhoneNo: ")
                            PhoneNo = int(input())
                            print ()
                            print("Enter the initial deposit: ")
                            deposit = int(input("UGX: "))
                            stanbic.customerSide.OpenAccount(name, deposit, Address, PhoneNo,acc_type)
                            print()

                        else:
                            print("Enter your name: ")
                            name = str(input())
                            print ()
                            print("Enter your Address: ")
                            Address = str(input())
                            print ()
                            print("Enter your PhoneNo: ")
                            PhoneNo = int(input())
                            print ()
                            print("Enter the initial deposit: ")
                            deposit = int(input("UGX: "))
                            stanbic.customerSide.OpenAccount(name, deposit, Address, PhoneNo,2)
                            print()

                            
                    elif user_Choice is 2:
                        print()
                        print("Enter your name: ")
                        name = input()
                        print("Enter your account number: ")
                        AcctNo = int(input())
                        authenticationStatus = stanbic.customerSide.authenticate(name, AcctNo)
                        if authenticationStatus is True:
                            while True:
                                print()
                                print("Enter 1 to withdraw")
                                print("Enter 2 to deposit")
                                print("Enter 3 to display avialable balance")
                                print("Enter 4 to make a General Inquiry")
                                print("Enter 5 to close your Account")
                                print("Enter 6 to request for your ATM Card")
                                print("Enter 7 to Apply for a Loan")
                                print("Enter 8 to go back to the previous menu")
                                userChoice = int(input())
                                print()
                                
                                if userChoice is 1:
                                    print()
                                    print("Enter a withdrawal amount")
                                    withdrawalAmount = int(input("UGX: "))
                                    stanbic.customerSide.WithdrawMoney(withdrawalAmount)
                                    print()

                                elif userChoice is 2:
                                    print()
                                    print("Enter an amount to be deposited")
                                    depositAmount = int(input("UGX: "))
                                    stanbic.customerSide.DepositMoney(depositAmount)
                                    print()
                                elif userChoice is 3:
                                    print()
                                    stanbic.customerSide.displayBalance()
                                    print()
                                elif userChoice is 4:
                                    print()
                                    stanbic.customerSide.GeneralInquiry()
                                    print()
                                elif userChoice is 5:
                                    print()
                                    stanbic.customerSide.CloseAccount()
                                    print()
                                    break
                                elif userChoice is 6:
                                    print()
                                    stanbic.customerSide.RequestCard()
                                    print()
                                elif userChoice is 7:
                                    print()
                                    stanbic.customerSide.ApplyForLoan()
                                    print()
                                elif userChoice is 8:
                                    break

                    elif user_Choice is 3:
                        quit()


                else:
                    print()
                    print("Enter your name: ")
                    name = input()
                    print("Enter your Tellers' ID number: ")
                    TellerId = int(input())
                    authenticationStatus = stanbic.tellerSide.authenticate(name, TellerId)
                    if authenticationStatus is True:
                        while True:
                                print()
                                print("Enter 1 to Collect Money")
                                print("Enter 2 to Open an Account")
                                print("Enter 3 to Close an account")
                                print("Enter 4 to make a Loan request")
                                print("Enter 5 to provide Information")
                                print("Enter 6 to Issue a Card")
                                print("Enter 7 to go back to the previous menu")
                                userChoice = int(input())
                                print()

                                if userChoice is 1:
                                    print()
                                    print("Provide the client's Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = stanbic.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        print("Enter an amount to be deposited")
                                        depositAmount = int(input("UGX: "))
                                        stanbic.customerSide.DepositMoney(depositAmount)
                                        print()

                                elif userChoice is 2:
                                    print('Enter 1 for a checking account or enter 2 for a Savings account?')
                                    print('1.Checking Account')
                                    print('2.Savings Account')
                                    acc_type = int(input())
                                    print()
                                    
                                    if acc_type is 1:
                                        print("Enter name of client: ")
                                        name = str(input())
                                        print ()
                                        print("Enter Address of client: ")
                                        Address = str(input())
                                        print ()
                                        print("Enter PhoneNo of client: ")
                                        PhoneNo = int(input())
                                        print ()
                                        print("Enter the initial deposit of client: ")
                                        deposit = int(input("UGX: "))
                                        stanbic.customerSide.OpenAccount(name, deposit, Address, PhoneNo,acc_type)
                                        print()

                                    else:
                                        print("Enter name of client: ")
                                        name = str(input())
                                        print ()
                                        print("Enter Address of client: ")
                                        Address = str(input())
                                        print ()
                                        print("Enter PhoneNo of client: ")
                                        PhoneNo = int(input())
                                        print ()
                                        print("Enter the initial deposit of client: ")
                                        deposit = int(input("UGX: "))
                                        stanbic.customerSide.OpenAccount(name, deposit, Address, PhoneNo,2)
                                        print()

                                elif userChoice is 3:
                                    print()
                                    print("Provide the Client's  Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = stanbic.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        stanbic.customerSide.CloseAccount()
                                        print()
                                        break

                                elif userChoice is 4:
                                    print()
                                    print("Provide the Client's  Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = stanbic.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        stanbic.customerSide.LoanRequest()
                                        print()

                                elif userChoice is 5:
                                    print()
                                    stanbic.tellerSide.ProvideInfo()
                                    print()

                                elif userChoice is 6:
                                    print()
                                    print("Provide the Client's  Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = stanbic.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        stanbic.tellerSide.IssueCard()
                                        print()

                                elif userChoice is 7:
                                    break



# dfcu (second bank) implementation 

        if userChoice is 2:
            while True:
                print()
                print('Enter 1 for teller or 2 for customer (YOU ARE IN DFCU)')
                print('1.Teller')
                print('2.Customer')
                choice = int(input())
                if choice is 2:
                    print()
                    print("Enter 1 to create a new account")
                    print("Enter 2 to access an existing account")
                    print("Enter 3 to exit")
                    user_Choice = int(input())
                    print()
                    if user_Choice is 1:
                        print('Enter 1 for a checking account or enter 2 for a Savings account?')
                        print('1.Checking Account')
                        print('2.Savings Account')
                        acc_type = int(input())
                        print()
                        if acc_type is 1:
                            print("Enter your name: ")
                            name = str(input())
                            print ()
                            print("Enter your Address: ")
                            Address = str(input())
                            print ()
                            print("Enter your PhoneNo: ")
                            PhoneNo = int(input())
                            print ()
                            print("Enter the initial deposit: ")
                            deposit = int(input("UGX: "))
                            dfcu.customerSide.OpenAccount(name, deposit, Address, PhoneNo,acc_type)
                            print()

                        else:
                            print("Enter your name: ")
                            name = str(input())
                            print ()
                            print("Enter your Address: ")
                            Address = str(input())
                            print ()
                            print("Enter your PhoneNo: ")
                            PhoneNo = int(input())
                            print ()
                            print("Enter the initial deposit: ")
                            deposit = int(input("UGX: "))
                            dfcu.customerSide.OpenAccount(name, deposit, Address, PhoneNo,2)
                            print()

                            
                    elif user_Choice is 2:
                        print()
                        print("Enter your name: ")
                        name = input()
                        print("Enter your account number: ")
                        AcctNo = int(input())
                        authenticationStatus = dfcu.customerSide.authenticate(name, AcctNo)
                        if authenticationStatus is True:
                            while True:
                                print()
                                print("Enter 1 to withdraw")
                                print("Enter 2 to deposit")
                                print("Enter 3 to display avialable balance")
                                print("Enter 4 to make a General Inquiry")
                                print("Enter 5 to close your Account")
                                print("Enter 6 to request for your ATM Card")
                                print("Enter 7 to Apply for a Loan")
                                print("Enter 8 to go back to the previous menu")
                                userChoice = int(input())
                                print()
                                
                                if userChoice is 1:
                                    print()
                                    print("Enter a withdrawal amount")
                                    withdrawalAmount = int(input("UGX: "))
                                    dfcu.customerSide.WithdrawMoney(withdrawalAmount)
                                    print()

                                elif userChoice is 2:
                                    print()
                                    print("Enter an amount to be deposited")
                                    depositAmount = int(input("UGX: "))
                                    dfcu.customerSide.DepositMoney(depositAmount)
                                    print()
                                elif userChoice is 3:
                                    print()
                                    stanbic.customerSide.displayBalance()
                                    print()
                                elif userChoice is 4:
                                    print()
                                    dfcu.customerSide.GeneralInquiry()
                                    print()
                                elif userChoice is 5:
                                    print()
                                    dfcu.customerSide.CloseAccount()
                                    print()
                                    break
                                elif userChoice is 6:
                                    print()
                                    dfcu.customerSide.RequestCard()
                                    print()
                                elif userChoice is 7:
                                    print()
                                    dfcu.customerSide.ApplyForLoan()
                                    print()
                                elif userChoice is 8:
                                    break

                    elif user_Choice is 3:
                        quit()


                else:
                    print()
                    print("Enter your name: ")
                    name = input()
                    print("Enter your Tellers' ID number: ")
                    TellerId = int(input())
                    authenticationStatus = dfcu.tellerSide.authenticate(name, TellerId)
                    if authenticationStatus is True:
                        while True:
                                print()
                                print("Enter 1 to Collect Money")
                                print("Enter 2 to Open an Account")
                                print("Enter 3 to Close an account")
                                print("Enter 4 to make a Loan request")
                                print("Enter 5 to provide Information")
                                print("Enter 6 to Issue a Card")
                                print("Enter 7 to go back to the previous menu")
                                userChoice = int(input())
                                print()

                                if userChoice is 1:
                                    print()
                                    print("Provide the client's Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = dfcu.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        print("Enter an amount to be deposited")
                                        depositAmount = int(input("UGX: "))
                                        dfcu.customerSide.DepositMoney(depositAmount)
                                        print()

                                elif userChoice is 2:
                                    print('Enter 1 for a checking account or enter 2 for a Savings account?')
                                    print('1.Checking Account')
                                    print('2.Savings Account')
                                    acc_type = int(input())
                                    print()
                                    
                                    if acc_type is 1:
                                        print("Enter name of client: ")
                                        name = str(input())
                                        print ()
                                        print("Enter Address of client: ")
                                        Address = str(input())
                                        print ()
                                        print("Enter PhoneNo of client: ")
                                        PhoneNo = int(input())
                                        print ()
                                        print("Enter the initial deposit of client: ")
                                        deposit = int(input("UGX: "))
                                        dfcu.customerSide.OpenAccount(name, deposit, Address, PhoneNo,acc_type)
                                        print()

                                    else:
                                        print("Enter name of client: ")
                                        name = str(input())
                                        print ()
                                        print("Enter Address of client: ")
                                        Address = str(input())
                                        print ()
                                        print("Enter PhoneNo of client: ")
                                        PhoneNo = int(input())
                                        print ()
                                        print("Enter the initial deposit of client: ")
                                        deposit = int(input("UGX: "))
                                        dfcu.customerSide.OpenAccount(name, deposit, Address, PhoneNo,2)
                                        print()

                                elif userChoice is 3:
                                    print()
                                    print("Provide the Client's  Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = dfcu.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        dfcu.customerSide.CloseAccount()
                                        print()
                                        break

                                elif userChoice is 4:
                                    print()
                                    print("Provide the Client's  Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = dfcu.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        dfcu.customerSide.LoanRequest()
                                        print()

                                elif userChoice is 5:
                                    print()
                                    dfcu.tellerSide.ProvideInfo()
                                    print()

                                elif userChoice is 6:
                                    print()
                                    print("Provide the Client's  Account Number")
                                    Account_no = int(input())
                                    print("Enter the clients' name")
                                    name = input()
                                    authenticationStatus = dfcu.customerSide.authenticate(name, Account_no)
                                    if authenticationStatus is True:
                                        dfcu.tellerSide.IssueCard()
                                        print()

                                elif userChoice is 7:
                                    break




        

                        
                    
                
                    







