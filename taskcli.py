#Author: Adam Alberski
#Date: 6/1/20225

import argparse
import datetime
import json
import os


def main() -> None:
    # Verify JSON file, create if it doesn't exist
    file_name = "data.json"
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name) as json_file:
            data = json.load(json_file)
    else:
        data = {
            "Counter": 0,
        }

    # Construct CLI
    parser = argparse.ArgumentParser(description='CLI for task tracker')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add Command
    add_parser = subparsers.add_parser('add', help='add task')
    add_parser.add_argument('description', help='task description')

    # Update Command
    update_parser = subparsers.add_parser('update', help='update task')
    update_parser.add_argument('task_id', help='task id')
    update_parser.add_argument('description', help='task description')

    # Delete Command
    delete_parser = subparsers.add_parser('delete', help='delete task')
    delete_parser.add_argument('task_id', help='task id')

    # Mark Command
    mark_parser = subparsers.add_parser('mark', help='mark task')
    mark_parser.add_argument('task_id', help='task id')
    mark_parser.add_argument('status', help='task status')

    # List Command
    list_parser = subparsers.add_parser('list', help='list tasks')
    list_parser.add_argument('list_status', nargs='?', help ='status to look for')

    args = parser.parse_args()

    match args.command:
        case 'add':
            add_task(args.description, data)
        case 'update':
            update_task(args.task_id, args.description, data)
        case 'delete':
            delete_task(args.task_id, data)
        case 'mark':
            mark_task(args.task_id, args.status, data)
        case 'list':
            list_tasks(args.list_status, data)

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def add_task(description, data) -> None:
    data["Counter"] += 1
    task_id = data["Counter"]
    task = {
        'id': task_id,
        'description': description,
        'status': "todo",
        'createdAt': datetime.date.today().isoformat(),
        'updatedAt': datetime.date.today().isoformat(),
    }
    data[task_id] = task
    print("Task added successfully (ID: " + str(task_id) + ")")


def update_task(task_id, description, data) -> None:
    data[task_id]['description'] = description
    data[task_id]['updatedAt'] = datetime.date.today().isoformat()

def delete_task(task_id, data) -> None:
    del data[task_id]
    print("Task deleted successfully (ID: " + str(task_id) + ")")

def mark_task(task_id, status, data) -> None:
    if status == "todo" or status == "done" or status == "in-progress":
        data[task_id]['status'] = status
        print("Task marked as " + status + " successfully (ID: " + str(task_id) + ")")
    else:
        print("Unknown status: " + status)

def list_tasks(status, data) -> None:
    match status:
        case None:
            for task in data:
                if task != "Counter":
                    print_task(task, data)
        case "todo":
            for task in data:
                if task != "Counter" and data[task]['status'] == "todo":
                    print_task(task, data)
        case "in-progress":
            for task in data:
                if task != "Counter" and data[task]['status'] == "in-progress":
                    print_task(task, data)
        case "done":
            for task in data:
                if task != "Counter" and data[task]['status'] == "done":
                    print_task(task, data)
        case _:
            print(status + " is an unknown command.")

def print_task(task_id, data) -> None:
    print("ID: " + str(task_id))
    print("Description: " + data[task_id]['description'])
    print("Status: " + data[task_id]['status'])
    print("Created at: " + data[task_id]['createdAt'])
    print("Updated at: " + data[task_id]['updatedAt'])
    print("")

if __name__ == '__main__':
    main()