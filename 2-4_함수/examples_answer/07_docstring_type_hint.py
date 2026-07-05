def make_score_dict(python_score: int, data_score: int, web_score: int) -> dict[str, int]:
    """
    Python, Data, Web 점수를 받아 과목별 점수 딕셔너리를 반환한다.
    """
    return {
        "Python": python_score,
        "Data": data_score,
        "Web": web_score,
    }


scores = make_score_dict(90, 85, 80)
print(scores)
