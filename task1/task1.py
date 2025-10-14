def to_do_list():
    tasks = []

    while True:
        print("\nTO DO LIST")
        print("1 : Add Task")
        print("2 : Remove Task")
        print("3 : View Tasks")
        print("4 : Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter to added task: ").strip()
            tasks.append(task)
            
        elif choice == "2":
            task = input("Enter to removed task: ").strip()
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found")

        elif choice == "3":
            print("\nTasks: ")
            if not tasks:
                print("No tasks available")
            else:
                for task in tasks:
                    print("-" + task)

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

to_do_list()

