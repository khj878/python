"""
문제
오늘 배운 자료구조를 사용해 우리 팀 데이터를 표현하세요.

팀 데이터에는 리스트, 딕셔너리, 세트, 튜플을 모두 사용해야 합니다.
팀원들과 이야기해서 팀 이름, 역할, 관심사, 팀원 정보 등을 자유롭게 정하고 코드로 작성하세요.

필수 요구사항
1. 전체 팀 데이터는 딕셔너리로 표현하세요.
2. 리스트, 딕셔너리, 세트, 튜플은 각각 적어도 하나씩 있어야 하며, 해당 데이터 타입을 사용한 근거를 주석으로 다세요.

결과 예시 :
team = {
    "team_name": "Bug Hunters",
    "slogan": "에러는 성장 로그다",

    # 리스트: 팀원이 여러 명이고 순서대로 모아두기 위해 사용
    "members": [
        {
            # 딕셔너리: 한 팀원의 여러 정보를 key와 value로 저장하기 위해 사용
            "name": "김민수",

            # 튜플: MBTI 네 글자는 순서가 있고 쉽게 바뀌지 않는 값이라 사용
            "mbti": ("I", "N", "T", "J"),

            "role": "팀장",

            # 리스트: 좋아하는 언어를 여러 개 순서대로 저장하기 위해 사용
            "favorite_languages": ["Python", "JavaScript"],

            # 세트: 보유 기술은 중복 없이 모아두기 위해 사용
            "skills": {"Python", "Git"},

            "is_leader": True,
        },
        {
            "name": "이서연",
            "mbti": ("E", "N", "F", "P"),
            "role": "발표 담당",
            "favorite_languages": ["Python"],
            "skills": {"Python", "발표"},
            "is_leader": False,
        },
        {
            "name": "박지훈",
            "mbti": ("I", "S", "T", "P"),
            "role": "기록 담당",
            "favorite_languages": ["JavaScript", "Python"],
            "skills": {"HTML", "CSS", "JavaScript"},
            "is_leader": False,
        },
        {
            "name": "최하늘",
            "mbti": ("I", "S", "F", "J"),
            "role": "자료 조사 담당",
            "favorite_languages": ["Python"],
            "skills": {"Python", "Excel", "데이터분석"},
            "is_leader": False,
        },
    ],
}
"""

# 여기에 코드를 작성하세요.
