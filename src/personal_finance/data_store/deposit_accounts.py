class DepositAccountDataStore:
    def __init__(self, account_id, balance, interest_rate):
        self.account_id = account_id
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest