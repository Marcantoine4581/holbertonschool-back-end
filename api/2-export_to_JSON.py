#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = int(argv[1])

    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    dict_todos = r_todos.json()

    r_users = requests.get("https://jsonplaceholder.typicode.com/users/")
    dict_users = r_users.json()

    for key in dict_users:
        if key.get("id") == USER_ID:
            USERNAME = key.get("username")

    new_list = []

    for key in dict_todos:
        new_dict = {}
        if key.get("userId") == USER_ID:
            new_dict["task"] = key.get("title")
            new_dict["completed"] = key.get("completed")
            new_dict["username"] = USERNAME
            new_list.append(new_dict)

    new_dict2 = {}
    new_dict2[USER_ID] = new_list
    json_object = json.dumps(new_dict2)

    with open(str(USER_ID) + ".json", "w") as f:
        f.write(json_object)
