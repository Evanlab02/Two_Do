import sys, os, json

from setup.helpers import get_home_dir

def setup_files(home_dir):
    try:
        with open(f"{home_dir}/.todo/.settings.json", "r") as read_file:
            json_data = json.load(read_file)
            print("SETTINGS INSTALLED")
    except:
        with open(f"{home_dir}/.todo/.settings.json", "w") as write_file:
            json.dump({}, write_file)
            print("INSTALLING SETTINGS")

    try:
        with open(f"{home_dir}/.todo/.category.json", "r") as read_file:
            json_data = json.load(read_file)
            print("CATEGORIES INSTALLED")
    except:
        with open(f"{home_dir}/.todo/.category.json", "w") as write_file:
            json.dump({"categories": []}, write_file)
            print("INSTALLING CATEGORIES")

    try:
        with open(f"{home_dir}/.todo/.category_full.json", "r") as read_file:
            json_data = json.load(read_file)
            print("CATEGORIES#2 INSTALLED")
    except:
        with open(f"{home_dir}/.todo/.category_full.json", "w") as write_file:
            json.dump({}, write_file)
            print("INSTALLING CATEGORIES#2")

    try:
        with open(f"{home_dir}/.todo/.goals.json", "r") as read_file:
            json_data = json.load(read_file)
            print("SHORT_TERM INSTALLED")
    except:
        with open(f"{home_dir}/.todo/.goals.json", "w") as write_file:
            json.dump({}, write_file)
            print("INSTALLING SHORT_TERM")
            

def install_todo():
    if input("Install/Reset todo program?[Installation will only work on some Linux devides)(y\\n): ").lower() == "n":
        sys.exit("Installation/Reset cancelled.")

    #os.system("python3 -m pip install --upgrade pip")
    os.system("pip install PyInstaller")
    os.system("pip install inquirer")
    os.system("pip install tabulate")

    home_dir = get_home_dir()

    os.system(f"mkdir {home_dir}/.todo/")

    os.system(f"touch {home_dir}/.todo/.settings.json")

    setup_files(home_dir)

    if (len(sys.argv) == 1) and sys.argv[0] == "two_do.py":
        os.system("python3 -m PyInstaller --onefile two_do.py")
        os.system("IFS=$'\n' read -rd ':' -a array <<< '$PATH'")
        os.system("chmod +x dist/two_do")
        os.system("sudo cp dist/two_do $array")
