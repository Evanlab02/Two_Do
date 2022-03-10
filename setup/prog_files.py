import os

from setup.helpers import get_home_dir

def check_files():
    home_dir = get_home_dir()

    if not os.path.exists(f"{home_dir}/.todo/.settings.json"):
        return False
    elif not os.path.exists(f"{home_dir}/.todo/.category.json"):
        return False
    elif not os.path.exists(f"{home_dir}/.todo/.category_full.json"):
        return False
    elif not os.path.exists(f"{home_dir}/.todo/.goals.json"):
        return False
    else:
        return True