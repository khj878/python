"""
문제
온라인 학습 플랫폼의 권한 확인 프로그램을 만드려고 합니다.
사용자의 정보를 바탕으로 로그인 가능 여부, 관리자 화면 접근 가능 여부, 유료 서비스 사용 가능 여부를 판단하세요.

사용자 정보
- 아이디가 있음
- 비밀번호가 맞음
- 관리자는 아님
- 매니저는 맞음
- 나이: 19세
- 차단된 사용자가 아님

판단 규칙
- 로그인은 아이디가 있고 비밀번호가 맞을 때만 가능합니다.
- 관리자 화면은 로그인 가능하면서, 관리자 또는 매니저일 때 접근할 수 있습니다.
- 유료 서비스는 로그인 가능하면서, 나이가 20세 이상이고, 차단된 사용자가 아닐 때 사용할 수 있습니다.

필수 요구사항
1. 비교 연산자와 논리 연산자를 사용하세요.
2. 판단 규칙을 코드로 옮겨 아래 결과와 같게 출력하세요.

실행 결과 예시 :
로그인 가능: True
관리 화면 접근 가능: True
유료 서비스 사용 가능: False
"""

# 여기에 코드를 작성하세요.
has_user_id = True
is_password_correct = True
is_admin = False
is_manager = True
user_age = 19
is_blocked = False

can_login = # 작성하시오
can_access_dashboard =  # 작성하시오
can_use_paid_service =  # 작성하시오

print(f"로그인 가능: {can_login}")
print(f"관리 화면 접근 가능: {can_access_dashboard}")
print(f"유료 서비스 사용 가능: {can_use_paid_service}")
