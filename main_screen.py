import inquirer, sys

from setup.installation import install_todo
from classifications.add import add_goal_class
from classifications.view import view_goal_class
from goals.add import add_goal
from goals.view import view_goals
from goals.comp import complete_goal

def main_options():
    main_menu = [
    inquirer.List('Main Menu',
                message="Main Menu",
                choices=["Complete Goal", "View Goals","Add Goal","View Goal Classifications","Add Goal Classification","Reset", "Exit"],
            ),
    ]
    selected_menu = inquirer.prompt(main_menu)["Main Menu"]
    return selected_menu


def main():
    selected = main_options()

    if selected == "Reset":
        install_todo()
    elif selected == "Exit":
        sys.exit("Goodbye!")
    elif selected == "Add Goal Classification":
        add_goal_class()
    elif selected == "View Goal Classifications":
        view_goal_class()
    elif selected == "Add Goal":
        add_goal()
    elif selected == "View Goals":
        view_goals()
    elif selected == "Complete Goal":
        complete_goal()

