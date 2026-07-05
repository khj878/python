from pathlib import Path

data_dir = Path(__file__).parent / "dataset"
data_dir.mkdir(exist_ok=True)
file_path = data_dir / "daily_note.txt"

lines = [
    "파일 쓰기 연습\n",
    "writelines 사용\n",
    "UTF-8 인코딩 확인\n",
]

with open(file_path, "w", encoding="utf-8") as file:
    file.writelines(lines)

print("daily_note.txt 작성 완료")
