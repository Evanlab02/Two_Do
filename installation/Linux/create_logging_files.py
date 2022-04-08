import os
from datetime import datetime

home_dir = os.getenv("HOME")

def create_logging_files():
    create_install_log_file()
    log_first_install_messages()


def create_install_log_file():
    if not os.path.exists(f"{home_dir}/kanban/logging/installation_log.txt"):
        os.system(f"cp storage_files/txt_log_files/installation_log.txt {home_dir}/kanban/logging/")


def log_first_install_messages():
    with open(f"{home_dir}/kanban/logging/installation_log.txt", "a") as write_file:
        write_file.writelines(f"INSTALL STARTED @{datetime.now()}\n")
        write_file.writelines(f"CREATED INITIAL FILES AND DIRECTORIES @{datetime.now()}\n")
        write_file.writelines(f"STARTED INSTALLATION_LOG INSTALL 0% @{datetime.now()}\n")
        write_file.writelines(f"COMPLETED INSTALLATION_LOG INSTALL 100% @{datetime.now()}\n") 