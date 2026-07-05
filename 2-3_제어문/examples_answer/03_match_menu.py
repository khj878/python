menu_code = "B"

# 추가 확인용 테스트 케이스를 확인할 때는 아래 값으로 바꿔 실행하세요.
# menu_code = "X"

match menu_code:
    case "A":
        print("주문 조회 화면으로 이동합니다.")
    case "B":
        print("배송 조회 화면으로 이동합니다.")
    case "C":
        print("상담원 연결 화면으로 이동합니다.")
    case _:
        print("존재하지 않는 메뉴입니다.")
