correct_password = "python2026"
fail_count = 0

while True:
    password = input("비밀번호를 입력하세요: ")

    if password == correct_password:
        print("로그인 성공")
        break

    print("올바르지 않은 비밀번호입니다.")
    fail_count = fail_count + 1

    if fail_count == 5:
        print("계정이 잠겼습니다.")
        break
