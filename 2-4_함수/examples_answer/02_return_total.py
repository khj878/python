def get_total_minutes(hours, minutes):
    return hours * 60 + minutes


study_hours = 2
study_minutes = 35
total_minutes = get_total_minutes(study_hours, study_minutes)

print(f"총 학습 시간: {total_minutes}분")
