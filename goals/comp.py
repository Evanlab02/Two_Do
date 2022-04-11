import json, inquirer

from setup.helpers import get_home_dir

def complete_goal():
    home_dir = get_home_dir()

    with open(f"{home_dir}/.todo/.goals.json", "r") as read_file:
        json_data = json.load(read_file)

    refined_json_data = {}

    for key, value in json_data.items():
        if value["Completed"] == False:
            refined_json_data[key] = json_data[key]

    choice_list = []

    for key, value in refined_json_data.items():
        term = value["Term"]
        classification = value["Class"]
        choice_list.append(f"{key} - {term} - {classification}")

    goal_menu = [
    inquirer.List('Goal Menu',
                message="Goals",
                choices=choice_list,
            ),
    ]
    selected_goal = inquirer.prompt(goal_menu)["Goal Menu"]

    selected_goal_key = selected_goal.split("-")[0].strip()

    json_data[selected_goal_key]["Completed"] = True

    with open(f"{home_dir}/.todo/.goals.json", "w") as write_file:
        json.dump(json_data, write_file)

    print("Goal Marked As Complete")

    