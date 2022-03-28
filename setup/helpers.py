#Import Statements
import os

#Global home_dir - Does this whenever the module is imported
home_dir = os.getenv("HOME")


def get_home_dir():
    """get_home_dir
    ------------
    
    Returns the path of the home_dir, does not work for Windows OS
    
    Returns
    -------
    
    string - home directory path is returned, used to store data files in same location"""
    return home_dir