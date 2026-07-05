class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("출금액은 0보다 커야 합니다.")
            return

        if amount > self.__balance:
            print("잔액이 부족합니다.")
            return

        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount(10000)

account.deposit(5000)
print(account.get_balance())  # 15000

account.withdraw(3000)
print(account.get_balance())  # 12000

account.withdraw(20000)       # 잔액이 부족합니다.
print(account.get_balance())  # 12000