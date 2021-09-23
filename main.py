from BankAccount import BankAcount

oneBankAccount = BankAcount( .05, 1000 )
secondBankAccount = BankAcount( .06, 10 )

oneBankAccount.deposite( 10 ).deposite( 20 ).deposite( 40 ).withdraw( 600 ).yieldInterest().accountInfo()
secondBankAccount.deposite( 10000 ).deposite( 20500 ).withdraw( 500 ).withdraw( 200 ).withdraw( 1000 ).withdraw( 300 ).yieldInterest().accountInfo()

BankAcount.printAllAccounts( )