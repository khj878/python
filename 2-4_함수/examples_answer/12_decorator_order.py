def check_order_time(func):
    def wrapper(stock_name, quantity, price, order_hour):
        if 9 <= order_hour <= 15:
            print("주문 가능 시간입니다.")
            func(stock_name, quantity, price, order_hour)
        else:
            print("주문 가능 시간이 아닙니다.")

    return wrapper


@check_order_time
def buy_stock(stock_name, quantity, price, order_hour):
    total_price = quantity * price
    print(f"{stock_name} {quantity}주 주문을 접수했습니다.")
    print(f"총 주문 금액: {total_price}원")


buy_stock("삼성전자", 3, 70000, 10)
