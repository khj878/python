"""
문제
주식 거래 내역 데이터를 전처리하려고 합니다.
filter(), map(), lambda를 사용해 매수 거래만 골라내고 결제 금액을 계산하세요.

거래 데이터
- type이 "buy"이면 매수 거래입니다.
- 결제 금액은 가격 * 수량 + 수수료로 계산합니다.
- 수수료는 거래 1건당 300원입니다.

필수 요구사항
- filter(), map(), lambda를 사용하세요.

실행 결과 예시 :
매수 종목: ['삼성전자', '네이버', '현대차']
매수 결제 금액: [148000, 183000, 426000]
"""

# 여기에 코드를 작성하세요.
trades = [
    {"name": "삼성전자", "type": "buy", "price": 73500, "quantity": 2},
    {"name": "카카오", "type": "sell", "price": 51000, "quantity": 3},
    {"name": "네이버", "type": "buy", "price": 182000, "quantity": 1},
    {"name": "LG에너지솔루션", "type": "sell", "price": 342000, "quantity": 1},
    {"name": "현대차", "type": "buy", "price": 85000, "quantity": 5},
]

fee = 300
