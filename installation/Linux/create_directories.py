import os

home_dir = os.getenv("HOME")

def create_directories():
    create_setting_directory()
    create_visible_storage_directory()
    create_invisible_storage_directory()
    create_log_directory()


def create_setting_directory():
    if not os.path.exists(f"{home_dir}/.config/kanban/"):
        os.mkdir(f"{home_dir}/.config/kanban/")


def create_visible_storage_directory():
    if not os.path.exists(f"{home_dir}/kanban/"):
        os.mkdir(f"{home_dir}/kanban/")


def create_invisible_storage_directory():
    if not os.path.exists(f"{home_dir}/.secret_kanban/"):
        os.mkdir(f"{home_dir}/.secret_kanban/")


def create_log_directory():
    if not os.path.exists(f"{home_dir}/kanban/logging/"):
        os.mkdir(f"{home_dir}/kanban/logging/")