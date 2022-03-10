import os

from setup.helpers import get_home_dir

def check_directory():
    home_dir = get_home_dir()

    if os.path.exists(f"{home_dir}/.todo/"):
        return True
    else:
        return False