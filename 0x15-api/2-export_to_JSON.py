#!/usr/bin/python3
"""Exports data in the JSON format"""


if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser = {userId: taskList}
    filename = f'{userId}.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
