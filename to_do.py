import os
import json

TODO_FILE = "todo_data.json"

# Load existing tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks found. You're all caught up!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. [{status}] {task['task']}")

# Add a new task
def add_task(tasks):
    task = input("📝 Enter your new task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added.")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("🔢 Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("🗑️ Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"🗑️ Deleted task: {deleted['task']}")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# Main application loop
def main():
    tasks = load_tasks()

    while True:
        print("\n📌 MENU:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❗ Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
