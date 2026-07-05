has_user_id = True
is_password_correct = True
is_admin = False
is_manager = True
user_age = 19
is_blocked = False

can_login = has_user_id and is_password_correct
can_access_dashboard = can_login and (is_admin or is_manager)
can_use_paid_service = can_login and user_age >= 20 and not is_blocked

print(f"로그인 가능: {can_login}")
print(f"관리 화면 접근 가능: {can_access_dashboard}")
print(f"유료 서비스 사용 가능: {can_use_paid_service}")
