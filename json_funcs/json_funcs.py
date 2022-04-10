import json, inquirer

def get_user_input(prompt):
    return inquirer.text(prompt)


def get_json_data(path):
    with open(f"{path}", "r") as read_file:
        return json.load(read_file)


def set_json_data(object, path):
    with open(f"{path}", "w") as write_file:
        json.dump(object, write_file)
