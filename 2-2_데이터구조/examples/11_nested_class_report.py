"""
문제
강사가 수강생 학습 리포트를 만들려고 합니다.
원본 수강생 데이터는 그대로 두고, 리포트용 데이터에만 보너스 점수를 반영한 뒤 요약 정보를 출력하세요.

수강생 중 Julie의 Python 점수에만 보너스 5점을 더합니다.

처리 규칙
- 전체 데이터는 중첩 딕셔너리와 리스트로 표현합니다.
- 리포트용 데이터는 원본 데이터를 복사해서 만듭니다.
- 보너스 점수는 리포트용 데이터에만 반영합니다.
- 각 수강생의 평균은 Python 점수와 Data 점수의 합계를 점수 개수로 나누어 계산합니다.
- 전체 복습 키워드는 두 수강생의 키워드 목록을 합친 뒤 set()으로 중복을 제거하고 sorted()로 정렬합니다.

실행 결과 예시 :
원본 Julie Python 점수: 95
리포트 Julie Python 점수: 100
Julie 평균: 94.0
Min 평균: 86.5
전체 키워드: ['copy', 'dict', 'list', 'set']
"""

# 여기에 코드를 작성하세요.
classroom = {
    "class_name": "AI Agent 기초반",
    "students": [
        {
            "name": "Julie",
            "profile": {
                "city": "Seoul",
            },
            "scores": {
                "python": 95,
                "data": 88,
            },
            "keywords": ["list", "dict", "list"],
        },
        {
            "name": "Min",
            "profile": {
                "city": "Busan",
            },
            "scores": {
                "python": 82,
                "data": 91,
            },
            "keywords": ["dict", "set", "copy"],
        },
    ],
    "bonus": {
        "target": "Julie",
        "subject": "python",
        "point": 5,
    },
}
