import os

def check_modules():
    try:
        import PyInstaller, inquirer, tabulate
        return True
    except:
        return False

    