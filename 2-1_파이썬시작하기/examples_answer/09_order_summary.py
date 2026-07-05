reservation_name = "Julie"
room_name = "Gangnam Study Room"
hourly_price = 12000
reservation_hours = 3
snack_price = 8000
point_discount = 5000
extension_minimum = 30000

room_total = hourly_price * reservation_hours
final_price = room_total + snack_price - point_discount
can_extend = final_price >= extension_minimum

print(f"예약자: {reservation_name}")
print(f"공간: {room_name}")
print(f"예약 시간: {reservation_hours}시간")
print(f"최종 결제 금액: {final_price}원")
print(f"연장 가능: {can_extend}")
