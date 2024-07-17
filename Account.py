class Account:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance = self._balance + amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        self._balance = self._balance - amount
        return self._balance

    def get_balance(self):
        print(f'Account balance is: {self._balance}')


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._interest_rate = 0.005
        self._withdrawal_limit = 700000

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self._interest_rate
        self._balance = self._balance + interest
        return self._balance

    def withdraw(self, amount):
        if amount > self._withdrawal_limit:
            print("Withdrawal limit exceeded")
        else:
            return super().withdraw(amount)


class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    # No additional restrictions for CurrentAccount


class ChildrenAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._interest_rate = 0.007

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self._interest_rate
        self._balance = self._balance + interest
        return self._balance

    def withdraw(self, amount):
        print("Withdrawals not allowed for Children's Account")


class StudentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._withdrawal_limit = 2000
        self._deposit_limit = 50000

    def deposit(self, amount):
        if amount > self._deposit_limit:
            print("Deposit limit exceeded")
        return super().deposit(amount)

    def withdraw(self, amount):
        if amount > self._withdrawal_limit:
            print("Withdrawal limit exceeded")
        return super().withdraw(amount)


def main():
    savings = SavingsAccount(1000)
    current = CurrentAccount(2000)
    children = ChildrenAccount(500)
    student = StudentAccount(100)


    # Savings account

    print(f"Savings Account Balance after deposit: {savings.deposit(1000)}")
    print(f"Savings Account Balance after withdrawal: {savings.withdraw(500)}")

    # Current account
    print(f"Current Account Balance after deposit: {current.deposit(1000)}")
    print(f"Current Account Balance after withdrawal: {current.withdraw(2500)}")

    # Children's account
    print(f"Children's Account Balance after deposit: {children.deposit(500)}")
    print(f"Children's Account Balance after withdrawal attempt: {children.withdraw(100)}")

    # Student account
    print(f"Student Account Balance after deposit: {student.deposit(2000)}")
    print(f"Student Account Balance after exceeding deposit limit: {student.deposit(60000)}")
    print(f"Student Account Balance after withdrawal attempt: {student.withdraw(3000)}")


if __name__ == "__main__":
    main()



