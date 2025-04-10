# Function to display tasks based on status
def view_tasks(tasks):
    print("\nPending Tasks:")
    for task in tasks:
        if task['status'] == 'Pending':
            print(f"{task['id']}. {task['desc']} - Deadline: {task['deadline']} - Priority: {task['priority']} - Category: {task['category']}")
    
    print("\nCompleted Tasks:")
    for task in tasks:
        if task['status'] == 'Completed':
            print(f"{task['id']}. {task['desc']} - Deadline: {task['deadline']} - Priority: {task['priority']} - Category: {task['category']}")
    
    print()

# Function to add a new task
def add_task(tasks):
    task_id = len(tasks) + 1  # New Task ID
    desc = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    category = input("Enter category (call/mail/meeting/other): ")
    priority = input("Enter priority (1 to 5 stars): ")
    
    tasks.append({
        'id': task_id,
        'desc': desc,
        'deadline': deadline,
        'status': 'Pending',
        'priority': '⭐' * int(priority),
        'category': category
    })
    
    print("Task added successfully!\n")

# Function to mark task as completed
def mark_task_completed(tasks):
    task_id = int(input("Enter task number to mark as completed: "))
    
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            print("Task marked as completed!\n")
            return
    
    print("Task not found!\n")

# Function to delete a task
def delete_task(tasks):
    task_id = int(input("Enter task number to delete: "))
    
    tasks = [task for task in tasks if task['id'] != task_id]
    print("Task deleted successfully!\n")
    return tasks

# Main function to drive the program
def main():
    tasks = []  # Store tasks in memory
    
    while True:
        print("Welcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            tasks = delete_task(tasks)  # Delete task and update the task list
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
