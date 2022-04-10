import os

def create_bin():
    os.system("python3 -m PyInstaller --onefile two_do.py")
    if os.path.exists("/usr/local/bin/"):
        os.system("sudo cp dist/two_do /usr/local/bin/")
    else:
        user_input = input("Please enter a bin storage location[/usr/local/bin/]: ")
        os.system(f"sudo cp dist/two_do {user_input}")
