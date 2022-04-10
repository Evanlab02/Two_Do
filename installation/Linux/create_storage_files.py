import os, json, platform

from my_logging.install_logging import log_start

home_dir = os.getenv("HOME")

def create_storage_files():
    log_start("Creating Storage Files")
    create_settings_file()
    create_issues_file()
    log_start("Completed Creation of Storage Files")

def create_settings_file():
    log_start("     Started Settings File Install #1")

    if not os.path.exists(f"{home_dir}/.config/kanban/settings.json"):
        os.system(f"touch {home_dir}/.config/kanban/settings.json")

    with open(f"storage_files/json_files/settings.json", "r") as read_file:
        json_data = json.load(read_file)
    
    json_data["my_system"] = platform.system()
    json_data["my_program"] = "kanban_cli"

    with open(f"{home_dir}/.config/kanban/settings.json", "w") as write_file:
        json.dump(json_data, write_file)

    log_start("     Completed Settings File Install #1")


def create_issues_file():
    log_start("     Started Issues File Install #2")

    if not os.path.exists(f"{home_dir}/.secret_kanban/issues.json"):
        os.system(f"{home_dir}/.secret_kanban/issues.json")

    with open(f"storage_files/json_files/issues.json", "r") as read_file:
        json_data = json.load(read_file)

    with open(f"{home_dir}/.secret_kanban/issues.json", "w") as write_file:
        json.dump(json_data, write_file)

    log_start("     Completed Issues File Install #2")
