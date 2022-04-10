import inquirer, sys

def main():
    main_screen_menu = [
    inquirer.List('task',
        message="What would you like to do?",
        choices=['Exit'],
    ),]
    main_screen_choice = inquirer.prompt(main_screen_menu)["task"]

    if main_screen_choice == "Exit":
        sys.exit("Goodbye!")