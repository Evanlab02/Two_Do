import sys

from installation.start_install import main as do_installation
from to_do.main_screen import main as main_screen

def main():
    if (sys.argv[0] == "two_do.py" and (sys.argv[1] == "--i" or sys.argv[1] == "--update")):
        do_installation()
    else:
        main_screen()

if __name__ == "__main__":
    main()