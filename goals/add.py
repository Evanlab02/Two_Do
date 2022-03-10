import inquirer, json

from setup.helpers import get_home_dir


def goal_term_options():
    main_menu = [
    inquirer.List('Term Menu',
                message="Goal Term",
                choices=["Short Term", "Medium Term", "Long Term"],
            ),
    ]
    selected_term = inquirer.prompt(main_menu)["Term Menu"]
    return selected_term


def goal_class_options():
    home_dir = get_home_dir()

    with open(f"{home_dir}/.todo/.category_full.json", "r") as read_file:
        json_data = json.load(read_file)
    
    data = []
    for key,value in json_data.items():
        data.append(f"{key}-{value}")

    class_menu = [
    inquirer.List('Class Menu',
                message="Goal Classification",
                choices=data,
            ),
    ]
    selected_class = inquirer.prompt(class_menu)["Class Menu"]
    return selected_class



def add_goal():
    home_dir = get_home_dir()

    selected_term = goal_term_options()
    
    user_goal = input("? What is the goal?: ")

    selected_class = goal_class_options()

    with open(f"{home_dir}/.todo/.goals.json", "r") as read_file:
        json_data = json.load(read_file)

    json_data[user_goal] = {"Term": selected_term, "Class": selected_class, "Completed": False}

    with open(f"{home_dir}/.todo/.goals.json", "w") as write_file:
        json.dump(json_data, write_file)

    
