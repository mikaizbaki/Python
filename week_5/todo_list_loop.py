todo = []
while True:
    choice = input("\n1.Add  2.View  3.Delete  4.Quit: ")

    if choice == "1":
        task = input("Task: ")
        todo.append(task)

    elif choice == "2":
        for i, t in enumerate(todo, 1):
            print(i, t)

    elif choice == "3":
        delete = input("Delete by number or name: ")

        if delete.isdigit():
            num = int(delete) - 1
            if 0 <= num < len(todo):
                todo.pop(num)
        else:
            if delete in todo:
                todo.remove(delete)

    elif choice == "4":
        break