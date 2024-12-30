tasks = []

def display_menu():
    """Display the main menu."""
    print("\nTo-Do List Manager")
    print("-------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Exit")

def view_tasks():
    """View all tasks."""
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    """Add a new task to the list."""
    title = input("\nEnter the task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added!")
    else:
        print("Task description cannot be empty.")

def mark_task_completed():
    """Mark a task as completed."""
    if not tasks:
        print("\nNo tasks to mark as completed!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
