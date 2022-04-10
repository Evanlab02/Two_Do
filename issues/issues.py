import os

from json_funcs.json_funcs import *

home_dir = os.getenv("HOME")

def open_issue():
    json_data = get_json_data(f"{home_dir}/.secret_kanban/issues.json")
    all_keys = [int(key) for key in json_data.keys()]
    new_key_value = max(all_keys)+1
    new_issue = get_user_input("What is the issue? ")
    json_data[new_key_value] = {"my_issue": new_issue, "completed": False, "progress_of_issue": "To-Do"}
    set_json_data(json_data, f"{home_dir}/.secret_kanban/issues.json")

    #for key, value in json_data.items():
    #    my_json_data[key] = [value["my_issue"], value["progress_of_issue"], value["closed"]]
    

    