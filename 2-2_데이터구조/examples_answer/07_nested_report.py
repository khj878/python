student_report = {
    "name": "Julie",
    "profile": {
        "age": 30,
        "job": "Student",
    },
    "languages": ["Python", "JavaScript"],
    "scores": [90, 80, 70],
}

representative_language = student_report["languages"][0]
average_score = sum(student_report["scores"]) / len(student_report["scores"])

print(f"학생: {student_report['name']}")
print(f"직업: {student_report['profile']['job']}")
print(f"대표 학습 언어: {representative_language}")
print(f"평균 점수: {average_score}")
