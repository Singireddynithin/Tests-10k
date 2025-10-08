class BankAccount:
    def __init__(self, name, balance, pin):
        self._name = name                      
        self.__balance = balance               
        self.__pin = pin                        
        self._is_active = True
        self._atm_requested = False
        self._cheque_requested = False

    def __validate_pin(self, pin):
        return self.__pin == pin

    def _get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    def check_balance(self, pin):
        if not self._is_active:
            print(f"Account for {self._name} is inactive ")
            return
        if self.__validate_pin(pin):
            print(f"Current balance for {self._name}: ₹{self.__balance}")
        else:
            print("Invalid PIN ")

    def deposit(self, amount, pin):
        if not self._is_active:
            print("Account is inactive ")
            return
        if not self.__validate_pin(pin):
            print("Invalid PIN ")
            return
        if amount <= 0:
            print("Deposit amount must be greater than 0 ")
            return
        self.__balance += amount
        print(f"Deposit successful  New balance: ₹{self.__balance}")

    def freeze_account(self):
        if not self._is_active:
            print("Account already frozen ")
        else:
            self._is_active = False
            print("Account has been frozen ")

    def unfreeze_account(self):
        if self._is_active:
            print("Account already active ")
        else:
            self._is_active = True
            print("Account has been unfrozen ")

    def request_atm_card(self):
        if self._atm_requested:
            print("ATM card already requested ")
        else:
            self._atm_requested = True
            print("ATM card request approved ")

    def request_cheque_book(self):
        if self._cheque_requested:
            print("Cheque book already requested ")
        else:
            self._cheque_requested = True
            print("Cheque book request approved ")

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, pin, daily_limit=20000):
        super().__init__(name, balance, pin)
        self._daily_limit = daily_limit

    def withdraw(self, amount, pin):
        if not self._is_active:
            print("Account is inactive ")
            return
        if amount > self._daily_limit:
            print("Amount exceeds daily withdrawal limit ")
            return
        if amount > self._get_balance():
            print("Insufficient balance ")
            return
        if not self._BankAccount__validate_pin(pin):
            print("Invalid PIN ")
            return
        self._set_balance(self._get_balance() - amount)
        print(f"Withdrawal successful  New balance: ₹{self._get_balance()}")

class BusinessAccount(BankAccount):
    def __init__(self, name, balance, pin, overdraft_limit=50000, loan_limit=100000):
        super().__init__(name, balance, pin)
        self._overdraft_limit = overdraft_limit
        self._loan_limit = loan_limit

    def withdraw(self, amount):
        if not self._is_active:
            print("Account is inactive ")
            return
        total_limit = self._get_balance() + self._overdraft_limit
        if amount > total_limit:
            print("Amount exceeds overdraft limit ")
            return
        self._set_balance(self._get_balance() - amount)
        print(f"Withdrawal successful  New balance: ₹{self._get_balance()}")

    def request_loan(self, amount):
        if amount <= self._loan_limit:
            print(f"Loan of ₹{amount} approved ")
        else:
            print("Loan amount exceeds limit ")

if __name__ == "__main__":
    s1 = SavingsAccount("Nithin", 10000, 1234)
    s1.check_balance(1234)
    s1.check_balance(9999)
    s1.withdraw(5000, 1234)
    s1.withdraw(25000, 1234)
    s1.withdraw(1000, 9999)
    s1.deposit(2000, 1234)
    s1.deposit(2000, 9999)
    s1.request_atm_card()
    s1.request_atm_card()
    s1.request_cheque_book()
    s1.request_cheque_book()
    s1.freeze_account()
    s1.withdraw(1000, 1234)
    s1.unfreeze_account()
    b1 = BusinessAccount("ABC Pvt Ltd", 50000, 1111)
    b1.check_balance(1111)
    b1.withdraw(90000)
    b1.withdraw(200000)
    b1.request_loan(50000)
    b1.request_loan(200000)
    b1.request_cheque_book()
