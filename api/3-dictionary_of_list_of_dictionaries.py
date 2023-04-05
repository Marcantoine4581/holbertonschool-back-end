#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests


if __name__ == "__main__":

    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    dict_todos = r_todos.json()

    r_users = requests.get("https://jsonplaceholder.typicode.com/users/")
    dict_users = r_users.json()

    new_list = []
    new_dict2 = {}

    for key in dict_users:
        USER_ID = key.get("id")
        USERNAME = key.get("username")
        for k in dict_todos:
            new_dict = {}
            if k.get("userId") == USER_ID:
                new_dict["username"] = USERNAME
                new_dict["task"] = k.get("title")
                new_dict["completed"] = k.get("completed")
                new_list.append(new_dict)
        new_dict2[USER_ID] = new_list

    json_object = json.dumps(new_dict2)

    with open("todo_all_employees.json", "w") as f:
        f.write(json_object)
