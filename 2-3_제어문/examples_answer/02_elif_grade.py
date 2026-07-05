age = 17
has_parent_agreement = True
is_early_bird = False

if age < 14:
    result = "수강 불가"
elif age < 19:
    if has_parent_agreement:
        result = "청소년 수강 가능"
    else:
        result = "보호자 동의 필요"
elif age < 65:
    if is_early_bird:
        result = "성인 얼리버드 할인"
    else:
        result = "성인 일반 수강"
else:
    result = "시니어 할인 수강"

print(f"나이: {age}세")
print(f"판정: {result}")
