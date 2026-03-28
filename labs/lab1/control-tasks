all_task = []
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        all_task = [line.strip() for line in f.readlines()]

while True:
    task_type = input('Enter task type "add", "remove", "show", or "exit": ').lower()

    if task_type == "add":
        task = input("Enter a task: ")
        all_task.append(task)
        with open(file_name, "a") as f:
            f.write(task + "\n")
    elif task_type == "remove":
        task = input("Enter a task to remove: ")
        if task in all_task:
            all_task.remove(task)
           
            with open(file_name, "w") as f:
                for t in all_task:
                    f.write(t + "\n")
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")
    elif task_type == "show":
        print("Your tasks:")
        for t in all_task:
            print("-", t)
    elif task_type == "exit":
        break
    else:
        print("Invalid option!")
