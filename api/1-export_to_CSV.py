#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
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

    with open(str(USER_ID) + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for key in dict_todos:
            row = []
            if key.get("userId") == USER_ID:
                row.append(USER_ID)
                row.append(USERNAME)
                row.append(key.get("completed"))
                row.append(key.get("title"))
                print(row)
                writer.writerow(row)
