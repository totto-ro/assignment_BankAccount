class BankAcount:
    bankName = "Costa Rica Bank"
    accounts = []

    def __init__( self, int_rate, balance ):
        self.int_rate = int_rate
        self.balance = balance
        BankAcount.accounts.append( self )


    def deposite( self, amount ):
        self.balance += amount
        return self

    def withdraw( self, amount ):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def yieldInterest ( self ):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    def accountInfo( self ):
        print( f"Account balance: {self.balance}" )
        return self

    @classmethod
    def printAllAccounts( cls ):
        for account in cls.accounts:
            account.accountInfo()
        
