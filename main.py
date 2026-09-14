todo_list=[]

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New task added successfully!")

def view_task():
    print("Your Todo list:")
    if len(todo_list)== 0:
        print("No pending tasks")
    else:
        for index, task in enumerate(todo_list,1):
            print(f"{index}:{task}")

def remove_task():
    if len(todo_list)==0:
        print("List is empty!")
    else:
        search_index= int(input("Enter the task number that you want to remove:"))-1
        if 0<=search_index<len(todo_list):
            removed_task= todo_list.pop(search_index)
            print(f"Task removed:{removed_task}")
        else:
            print("Invalid Task Number")

def mark_done():
    if len(todo_list)==0:
            print("List is empty!")
    else:
        search_index= int(input("Enter the task number that you want to mark as complete:"))-1
        if 0<=search_index<len(todo_list):
            todo_list[search_index]['Status']= 'done'
            print(f"Task {todo_list[search_index]['Task']} has been marked as Done.")
        else:
            print("Invalid Task Number")


def menu():
    while(True):
        print("***Main menu***")
        print("1.Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice= int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! Try again!!!")

if __name__ == "__main__":
    menu()



