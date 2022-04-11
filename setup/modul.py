#Import Statements
import os

def check_modules():
    """check_modules
    -------------
    This function tries to import the modules/packages that are 
    required to run this program. If an error is thrown, it returns a false 
    which indicates the modules/packages need to be installed, otherwise
    it returns a true to indicate the packages work as expected.
    
    Returns
    -------
    bool - True/False to indicate if this check passed or not. 

    """
    try:
        import PyInstaller, inquirer, tabulate
        return True
    except:
        return False

    