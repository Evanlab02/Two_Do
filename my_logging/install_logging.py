import os

from datetime import datetime

home_dir = os.getenv("HOME")

def log_start(message):
    with open(f"{home_dir}/kanban/logging/installation_log.txt", "a") as write_file:
        write_file.writelines(f"{message} @ {datetime.now()}\n")
