'''
Q.5. Write a Python program for the following:
 Define a class accountHolder consisting of attributes accNo, accName, accEmail.
It consists a method dispDetails to display the details in appropriate format.
 Inherit two classes viz. depositAccount (accountBalance) and loanAccount
(loanAmount, EMI, loanBalance). The depositAccount contains methods
debitAmt(amt)-which debits amt amount from the accountBalance, creditAmt(amt)-
which credits the amt amount to the accountBalance and dispTrans()-which
displays the whole transaction in appropriate format showing initial balance,
debit/credit amount and final amount.
'''

class accountHolder:
    def __init__(self,accNo,accName,accEmail):
        self.accNo = accNo
        self.accName = accName
        self.accEmail = accEmail

    def dispDetails(self):
        print("AccNo : ",self.accNo)
        print("AccName : ",self.accName)
        print("AccEmail : ",self.accEmail)


class depositAccount(accountHolder):
    def __init__(self,accBalance,accNo,accName,accEmail):
        accountHolder.__init__(self,accNo,accName,accEmail)
        #super().__init__(accNo,accName,accEmail)
        self.accBalance = accBalance

    def debitAmt(self,amt):
        self.accBalance = self.accBalance - amt
        self.dispTrans(amt,"debit")

    def creditAmt(self,amt):
        self.accBalance = self.accBalance + amt
        self.dispTrans(amt,"credit")

    def dispTrans(self,amt,transType):
        self.dispDetails()
        if(transType == "debit"):
            print("Initial Balance : ",self.accBalance+amt)
            print("Debit Amount : ",amt)
            print("FInal Balance : ",self.accBalance)
        elif(transType == "credit"):
            print("Initial Balance : ",self.accBalance-amt)
            print("Credit Amount : ",amt)
            print("FInal Balance : ",self.accBalance)

        
class loanAccount(accountHolder):
    def __init__(self,loanAmount,EMI,loanBalance,accNo,accName,accEmail):
        accountHolder.__init__(self,accNo,accName,accEmail)
        self.loanAmount = loanAmount
        self.EMI = EMI
        self.loanBalance = loanBalance

    def depositAmt(self,amt):
        self.loanBalance = self.loanBalance - amt
        self.dispTrans(amt)

    def dispTrans(self,amt):
        self.dispDetails()
        print("Initial Loan Amount : ",self.loanAmount)
        print("Initial EMI : ",self.EMI)
        print("Initial Loan Balance : ",self.loanBalance + amt)
        print("Deposit Amount in Loan : ",amt)
        print("Final Loan Balance : ",self.loanBalance)



accBalance = 10000
accNo = "111111111111"
accName = "Chandani SIngh"
accEMail = "chandani@gmail.com"
da = depositAccount(accBalance,accNo,accName,accEMail)

loanAmount = 10000
EMI = 1000
loanBalance = 10000
la = loanAccount(loanAmount,EMI,loanBalance,accNo,accName,accEMail)

while True:
    print("----Menu for Account-----")
    print("1 Deposit Account")
    print("2 Loan Account")
    print("3. Exit")
    op = int(input("ENter Option : "))
    if(op == 1):
        while True :
            print("----Menu Deposit Account-----")
            print("1 Debit Amt")
            print("2 Credit Amt")
            print("3 Exit")
            opd = int(input("Select Option : "))
            if(opd == 1):
                amt = int(input("Amount : "))
                da.debitAmt(amt)
            elif(opd == 2):
                amt = int(input("Amount : "))
                da.creditAmt(amt)
            elif(opd == 3):
                break
            else:
                print("Please select Valid Choice....")
    elif(op == 2):
        while True :
            print("----Menu Loan Account-----")
            print("1 Deposit Amt")
            print("2 Exit")
            opd = int(input("Select Option : "))
            if(opd == 1):
                amt = int(input("Amount : "))
                la.depositAmt(amt)
            elif(opd == 2):
                break
            else:
                print("Please select Valid Choice....")
    elif(op == 3):
        break
            


