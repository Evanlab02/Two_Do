import json

from setup.helpers import get_home_dir


def add_goal_class():
    home_dir = get_home_dir()

    with open(f"{home_dir}/.todo/.category.json", "r") as read_file:
        json_data = json.load(read_file)

    category_id = input("? Enter Goal Classification: ")

    json_data["categories"].append(category_id)

    with open(f"{home_dir}/.todo/.category.json", "w") as write_file:
        json.dump(json_data, write_file)


    category_name = input("? Enter Goal Classification Name: ")

    with open(f"{home_dir}/.todo/.category_full.json", "r") as read_file:
        json_data = json.load(read_file)

    json_data[category_id] = category_name

    with open(f"{home_dir}/.todo/.category_full.json", "w") as write_file:
        json.dump(json_data, write_file)

    print("Added Goal Classification")
