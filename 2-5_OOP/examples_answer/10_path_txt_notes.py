from pathlib import Path


data_dir = Path(__file__).parent / "data"
file_path = data_dir / "path_notes.txt"

content = file_path.read_text(encoding="utf-8")
print(content, end="")
