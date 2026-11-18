from task_manager import TaskManager

def show(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
    for t in tasks:
        mark = "x" if t["completed"] else " "
        print(f'[{mark}] {t["id"]}. {t["title"]}')

def main():
    manager = TaskManager()
    while True:
        print("\n1.Add  2.Show  3.Complete  4.Delete  5.Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            manager.add_task(input("Title: "))
        elif choice == "2":
            show(manager)
        elif choice == "3":
            manager.complete_task(int(input("Task ID: ")))
        elif choice == "4":
            try:
                manager.delete_task(int(input("Task ID: ")))
                print("Task deleted.")
            except ValueError:
                print("Invalid task ID.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()