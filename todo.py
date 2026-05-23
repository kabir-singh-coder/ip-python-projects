todo = []

while True:

    print("\n1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Exit")

    ch = input("Enter Choice: ")

    if ch == "1":

        task = input("Enter Task: ")

        todo.append(task)

        print("Task Added")

    elif ch == "2":

        print(todo)

    elif ch == "3":

        task = input("Enter Task To Remove: ")

        todo.remove(task)

        print("Task Removed")

    elif ch == "4":

        break

    else:

        print("Wrong Choice")
