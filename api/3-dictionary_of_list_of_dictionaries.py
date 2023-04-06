#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests


if __name__ == "__main__":

    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    dict_todos = r_todos.json()

    r_users = requests.get("https://jsonplaceholder.typicode.com/users/")
    dict_users = r_users.json()

    new_dict2 = {}

    for employee in dict_users:
        USER_ID = str(employee["id"])
        USERNAME = employee["username"]
        new_list = []
        for task in dict_todos:
            if task.get("userId") == int(USER_ID):
                new_dict = {}
                new_dict["username"] = USERNAME
                new_dict["task"] = task["title"]
                new_dict["completed"] = task["completed"]
                new_list.append(new_dict)

        new_dict2[USER_ID] = new_list

    all_tasks = new_dict2

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
