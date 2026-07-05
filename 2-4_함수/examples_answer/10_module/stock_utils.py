def calculate_return_rate(buy_price, current_price):
    return_rate = (current_price - buy_price) / buy_price * 100
    return round(return_rate, 2)