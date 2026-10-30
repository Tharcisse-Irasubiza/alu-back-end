#!/usr/bin/python3
"""Export all employees' TODO lists to todo_all_employees.json."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    data = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + "todos",
                             params={"userId": user_id}).json()
        data[str(user_id)] = [{"username": user.get("username"),
                               "task": t.get("title"),
                               "completed": t.get("completed")}
                              for t in todos]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
