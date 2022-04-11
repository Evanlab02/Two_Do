#Import Statements
import sys

#From Import Statements
from setup import modul, direc, prog_files, installation


def main():
    """two_do main function
    This is the entry function for the whole program and starts the program up.
    It checks that everything is installed.
    If two_do is installed, it will run the program
    otherwise it will do the installation process."""

    modules_check = modul.check_modules()
    direc_check = direc.check_directory()
    file_check = prog_files.check_files()

    check_list = [modules_check, direc_check, file_check]

    if False in check_list:
        installation.install_todo()

    if (len(sys.argv) == 2) and (sys.argv[1] == "view"):
        import goals.view as view
        view.view_goals()
        sys.exit()


    import main_screen
    main_screen.main()


if __name__ == "__main__":
    main()