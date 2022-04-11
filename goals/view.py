import json

from tabulate import tabulate
from setup.helpers import get_home_dir

def view_goals():
    home_dir = get_home_dir()

    with open(f"{home_dir}/.todo/.goals.json", "r") as read_file:
        json_data = json.load(read_file)

    data = []
    for key, value in json_data.items():
        if value["Completed"] == False:
            data.append([key,value["Term"], value["Class"]])

    print()
    print(tabulate(data, headers=["Goal", "Term", "Classification"]))
    print()