import json


def load_tasks():
    try:
        with open("tasks.json") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    description = input("Enter the description of the task: ").capitalize().strip()
    priority = input("Enter the level of priority of the task(low/medium/high): ").capitalize().strip()
    info = {
        "Description": description,
        "Priority": priority,
        "Status": "Pending"
    }
    tasks.append(info)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks recorded yet!")
    else:
        for idx, info in enumerate(tasks, start=1):
            print(f"{idx}.  Description: {info['Description']}\n"
                  f"        Priority: {info['Priority']}\n"
                  f"        Status: {info['Status']}")


def mark_complete(tasks):
    if not tasks:
        print("No tasks to mark complete!")
        return

    for idx, info in enumerate(tasks, start=1):
        print(f"{idx}. Description: {info['Description']}")

    change = int(input("Enter the index of the task you want to mark complete: "))
    tasks[change - 1]["Status"] = "Complete"

    save_tasks(tasks)
    print("Task marked as complete!")


while True:
    print("\n--- Task Manager ---")
    print("1. Add a Task")
    print("2. View all Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "4":
        print("Have a productive day!")
        break

    elif choice == "1":
        current_tasks = load_tasks()
        add_task(current_tasks)

    elif choice == "2":
        current_tasks = load_tasks()
        view_tasks(current_tasks)

    elif choice == "3":
        current_tasks = load_tasks()
        mark_complete(current_tasks)

    else:
        print("Invalid choice, try again.")