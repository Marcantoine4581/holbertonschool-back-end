#!/usr/bin/python3
"""Using a rest API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    dict_todos = r_todos.json()

    r_users = requests.get("https://jsonplaceholder.typicode.com/users/")
    dict_users = r_users.json()

    for key in dict_users:
        if key.get("id") == int(argv[1]):
            EMPLOYEE_NAME = key.get("name")

    for key in dict_todos:
        if key.get("userId") == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if key.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(key.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print("\t {}".format(title))
