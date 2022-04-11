import json

from tabulate import tabulate
from setup.helpers import get_home_dir


def view_goal_class():
    home_dir = get_home_dir()

    with open(f"{home_dir}/.todo/.category_full.json", "r") as read_file:
        json_data = json.load(read_file)

    data = []
    for key, value in json_data.items():
        data.append([key, value])

    print()
    print(tabulate(data, headers=["Goal Classification", "Goal Classification Name"]))
    print()