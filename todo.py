def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                tasks.pop(num - 1)
                print("Task deleted!")
            except:
                print("Invalid input.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()