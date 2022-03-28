#Import Statement
import os

#From Import Statement
from setup.helpers import get_home_dir

def check_files():
    """
    check_files
    ---------------
    This functions returns True if all the files exist where the data will be
    stored, if it does not exist the program will return False indicating it needs
    to create the files. All data files are .json files

    Returns
    -------
    bool - True/False to indicate if this check passed or not. 
    """
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