python_students = {1, 2, 3, 4, 5}
ai_students = {3, 4, 5, 6, 7}

all_students = python_students | ai_students
both_students = python_students & ai_students
python_only_students = python_students - ai_students
ai_only_students = ai_students - python_students

print(f"전체 신청자: {sorted(all_students)}")
print(f"동시 신청자: {sorted(both_students)}")
print(f"파이썬만 신청: {sorted(python_only_students)}")
print(f"AI만 신청: {sorted(ai_only_students)}")
