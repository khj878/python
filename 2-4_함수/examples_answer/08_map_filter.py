students = [
    {"name": "민수", "python": 85, "data": 70},
    {"name": "서연", "python": 55, "data": 90},
    {"name": "지훈", "python": 75, "data": 80},
    {"name": "하린", "python": 40, "data": 95},
    {"name": "도윤", "python": 90, "data": 90},
]


def is_python_pass(student):
    return student["python"] >= 60


def get_data_score(student):
    return student["data"]


python_pass_students = list(filter(is_python_pass, students))
data_scores = list(map(get_data_score, python_pass_students))

data_total = sum(data_scores)
data_average = data_total / len(data_scores)

print(f"Python 합격 학생 수: {len(python_pass_students)}명")
print(f"Data 점수 목록: {data_scores}")
print(f"Data 점수 합계: {data_total}")
print(f"Data 점수 평균: {data_average}")
