import inquirer, sys

from issues.issues import open_issue

def main():
    main_screen_menu = [
    inquirer.List('task',
        message="What would you like to do?",
        choices=['Open Issue','Exit'],
    ),]
    main_screen_choice = inquirer.prompt(main_screen_menu)["task"]

    if main_screen_choice == "Exit":
        sys.exit("Goodbye!")
    elif main_screen_choice == "Open Issue":
        open_issue()