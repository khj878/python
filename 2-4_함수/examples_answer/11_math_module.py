import math

def calculate_presenter_cases(total_applicants, presenter_count):
    combination_count = math.comb(total_applicants, presenter_count)
    permutation_count = math.perm(total_applicants, presenter_count)
    return combination_count, permutation_count


total_applicants = 12
presenter_count = 3
combination_count, permutation_count = calculate_presenter_cases(
    total_applicants,
    presenter_count,
)

print(f"발표자 조합 수: {combination_count}")
print(f"발표 순서 포함 경우의 수: {permutation_count}")
