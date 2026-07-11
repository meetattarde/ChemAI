from datetime import datetime
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "chemai.log")


def log(message):

    os.makedirs(LOG_FOLDER, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{current_time}] {message}\n")