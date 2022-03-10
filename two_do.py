import sys

from setup import modul, direc, prog_files, installation


def main():
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