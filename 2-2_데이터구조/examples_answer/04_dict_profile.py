user_profile = {
    "name": "Julie",
    "age": 30,
    "job": "Student",
    "languages": ["Python", "JavaScript"],
}

email = user_profile.get("email", "등록되지 않음")

print(f"이름: {user_profile['name']}")
print(f"직업: {user_profile['job']}")
print(f"첫 번째 학습 언어: {user_profile['languages'][0]}")
print(f"이메일: {email}")
