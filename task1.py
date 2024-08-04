class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"{self.title} - {status}\nDescription: {self.description}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def update_task(self, index, title=None, description=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            print("Task added successfully.")
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title (leave blank to keep unchanged): ")
            description = input("Enter new description (leave blank to keep unchanged): ")
            todo_list.update_task(index, title if title else None, description if description else None)
            print("Task updated successfully.")
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
            print("Task marked as completed.")
        elif choice == '4':
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
            print("Task removed successfully.")
        elif choice == '5':
            print("\nTo-Do List:")
            todo_list.list_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
