"""
문제
당신은 Gangnam 금융 서비스의 Python 개발자입니다.
고객이 보유한 여러 종류의 계좌를 관리하는 프로그램을 만들고 있습니다.

예금 계좌와 주식 계좌는 모두 잔액을 조회할 수 있어야 합니다.
하지만 예금 계좌는 이자를 지급하는 기능이 필요하고,
주식 계좌는 보유 종목을 확인하는 기능이 필요합니다.

공통 기능은 부모 클래스에 두고, 각 계좌만의 기능은 자식 클래스에 작성하세요.

처리 규칙
- Account 클래스에는 show_balance 메서드가 있고 "현재 잔액: 현재 잔액"을 출력합니다.
- SavingsAccount 클래스는 Account를 상속받고 add_interest 메서드가 있습니다.
- add_interest 메서드는 잔액에 이자 1000원을 더한 뒤 "이자 지급 후 잔액: 현재 잔액"을 출력합니다.
- StockAccount 클래스는 Account를 상속받고 show_stock 메서드가 있습니다.
- show_stock 메서드는 "보유 종목: 삼성전자"를 출력합니다.
- SavingsAccount 객체와 StockAccount 객체를 각각 생성해 공통 기능과 고유 기능을 호출합니다.

실행 결과 예시 :
현재 잔액: 10000원
이자 지급 후 잔액: 11000원
현재 잔액: 50000원
보유 종목: 삼성전자
"""

# 여기에 코드를 작성하세요.
class Account:
    pass

class SavingsAccount():
    pass

class StockAccount():
    pass