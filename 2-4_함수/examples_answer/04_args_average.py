def calculate_average(*scores):
    return sum(scores) / len(scores)

first_average = calculate_average(90, 80, 70)
second_average = calculate_average(100, 95, 85, 80)

print(f"첫 번째 학생 평균: {first_average}")
print(f"두 번째 학생 평균: {second_average}")
