class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f"현재 잔액: {self.balance}원")


class SavingsAccount(Account):
    def add_interest(self):
        self.balance = self.balance + 1000
        print(f"이자 지급 후 잔액: {self.balance}원")


class StockAccount(Account):
    def show_stock(self):
        print("보유 종목: 삼성전자")


savings_account = SavingsAccount(10000)
stock_account = StockAccount(50000)

savings_account.show_balance()
savings_account.add_interest()
stock_account.show_balance()
stock_account.show_stock()
