import os

def install_modules():
    try:
        import PyInstaller, inquirer, tabulate
    except:
        os.system("sudo pip install PyInstaller")
        os.system("sudo pip install inquirer")
        os.system("sudo pip install tabulate")