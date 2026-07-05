from pathlib import Path
import json


data_dir = Path(__file__).parent / "data"
file_path = data_dir / "settings.json"

with open(file_path, "r", encoding="utf-8") as file:
    settings = json.load(file)

notifications = "사용" if settings["notifications"] else "미사용"

print(f"테마: {settings['theme']}")
print(f"알림: {notifications}")
print(f"백업 개수: {settings['backup_count']}")
