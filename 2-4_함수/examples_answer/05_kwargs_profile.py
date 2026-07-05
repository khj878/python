def print_stock_info(**kwargs):
    name = kwargs.get("name")
    code = kwargs.get("code")
    current_price = kwargs.get("current_price")
    market = kwargs.get("market")
    target_price = kwargs.get("target_price", "미등록")

    print(f"종목명: {name}")
    print(f"종목 코드: {code}")
    print(f"현재가: {current_price}원")
    print(f"시장: {market}")
    if target_price == "미등록":
        print(f"목표가: {target_price}")
    else:
        print(f"목표가: {target_price}원")


samsung = {
    "name": "삼성전자",
    "code": "005930",
    "current_price": 73500,
    "market": "KOSPI",
}

naver = {
    "name": "NAVER",
    "code": "035420",
    "current_price": 182000,
    "market": "KOSPI",
    "target_price": 210000,
}

print_stock_info(**samsung)
print()
print_stock_info(**naver)
