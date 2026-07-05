unit_price_text = "15000"
quantity_text = "3"
delivery_fee_text = "3000"
coupon_code = ""

unit_price = int(unit_price_text)
quantity = int(quantity_text)
delivery_fee = int(delivery_fee_text)

product_total = unit_price * quantity
total_price = product_total + delivery_fee
has_coupon_code = bool(coupon_code)

print(f"상품 금액: {product_total}원")
print(f"총 결제 금액: {total_price}원")
print(f"쿠폰 코드 있음: {has_coupon_code}")
