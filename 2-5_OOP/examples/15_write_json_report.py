"""
문제
주식 거래 기록을 JSON 파일로 저장하려고 합니다.
주문 정보를 딕셔너리로 만들고 data/order_record.json 파일에 저장하세요.

상황
당신은 투자 연습 앱을 만드는 개발자입니다.
사용자가 삼성전자 주식 3주를 70000원에 매수했습니다.
주문이 완료되면 나중에 다시 확인할 수 있도록 거래 기록을 JSON 파일로 남겨야 합니다.

저장할 거래 정보
- stock_name: 삼성전자
- order_type: buy
- quantity: 3
- price: 70000
- total_price: quantity * price
- status: completed

필수 요구사항
1. pathlib의 Path를 사용해 data 폴더 경로를 만드세요.
2. data 폴더가 없으면 만들 수 있도록 mkdir(exist_ok=True)를 사용하세요.
3. total_price는 quantity * price로 계산하세요.
4. json.dump()를 사용해 data/order_record.json 파일로 저장하세요.
5. ensure_ascii=False를 사용하세요.
6. indent=4를 사용하세요.

저장 결과 예시 :
{
    "stock_name": "삼성전자",
    "order_type": "buy",
    "quantity": 3,
    "price": 70000,
    "total_price": 210000,
    "status": "completed"
}
"""

# 여기에 코드를 작성하세요.
stock_name = "삼성전자"
order_type = "buy"
quantity = 3
price = 70000