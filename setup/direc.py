#Import Statements
import os

#From Import Statements
from setup.helpers import get_home_dir

def check_directory():
    """
    check_directory
    ---------------
    This functions returns True if the directory exists where the data will be
    stored, if it does not exist the program will return False indicating it needs
    to create the directory

    Returns
    -------
    bool - True/False to indicate if this check passed or not. 
    """
    home_dir = get_home_dir()

    if os.path.exists(f"{home_dir}/.todo/"):
        return True
    else:
        return False