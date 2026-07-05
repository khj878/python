import copy

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

report_classroom = copy.deepcopy(classroom)
report_classroom["students"][0]["scores"]["python"] += report_classroom["bonus"]["point"]

julie_scores = report_classroom["students"][0]["scores"]
min_scores = report_classroom["students"][1]["scores"]

julie_average = (julie_scores["python"] + julie_scores["data"]) / len(julie_scores)
min_average = (min_scores["python"] + min_scores["data"]) / len(min_scores)

all_keywords = (
    report_classroom["students"][0]["keywords"]
    + report_classroom["students"][1]["keywords"]
)
unique_keywords = sorted(set(all_keywords))

print(f"원본 Julie Python 점수: {classroom['students'][0]['scores']['python']}")
print(f"리포트 Julie Python 점수: {report_classroom['students'][0]['scores']['python']}")
print(f"Julie 평균: {julie_average}")
print(f"Min 평균: {min_average}")
print(f"전체 키워드: {unique_keywords}")
