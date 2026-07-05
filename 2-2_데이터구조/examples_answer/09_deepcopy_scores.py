import copy

original_score_sheet = {
    "class_name": "A반",
    "scores": [90, 80, 70],
}

edited_score_sheet = copy.deepcopy(original_score_sheet)
edited_score_sheet["scores"].append(100)

print(f"원본 성적표: {original_score_sheet}")
print(f"수정용 성적표: {edited_score_sheet}")
