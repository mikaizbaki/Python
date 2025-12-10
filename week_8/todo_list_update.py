# Step 1: Load tasks from file
filename = "tasks.txt"
todo_list = []

try:
    with open(filename, "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    pass   # If file doesn't exist, start with an empty list


while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Choose an option: ")

    # Add task
    if choice == "1":
        task = input("Enter a new task: ")
        todo_list.append(task)

        # save to file
        with open(filename, "w") as file:
            for t in todo_list:
                file.write(t + "\n")

        print("Task added!")

    # View tasks
    elif choice == "2":
        print("\nYour tasks:")
        for i, t in enumerate(todo_list, 1):
            print(i, t)

    # Delete task
    elif choice == "3":
        delete = input("Delete by number or name: ")

        if delete.isdigit():  # delete by number
            index = int(delete) - 1
            if 0 <= index < len(todo_list):
                todo_list.pop(index)
        else:                 # delete by name
            if delete in todo_list:
                todo_list.remove(delete)

        # save updated file
        with open(filename, "w") as file:
            for t in todo_list:
                file.write(t + "\n")

        print("Task deleted!")

    # Quit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")