def Load_task():
    tasks=[]
    try:
        with open("text.txt","r") as file:
            tasks=[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks
def save_task(tasks):
    with open ("text.txt","w") as file:
        for task in tasks:
            file.write(task + "\n" )

def Add_task(tasks): #function to add task in your tasks list
    task=input("Enter the task: ")
    tasks.append(task)
    View_tasks(tasks)

def View_tasks(tasks): #function to view the tasks
    print("\n---The List---\n") 
    for i,task in enumerate(tasks):
        print(f"{i+1}. {task}")
    print("\n---The End---\n")
    
def delete_task(tasks): #function to delete the tasks
    View_tasks(tasks) # View the tasks
    if not tasks:
        return
    try:
        index=int(input("Enter the index of task you want to delete: ")) - 1
        if 0<= index < len(tasks):
            remove = tasks.pop(index)
            print(f"{remove} is remove successfully.\n")
        else:
            print("Invalid the task number. \n")
    except ValueError:
        print("Enetr the correct index, please.\n")

def main():

    tasks=[] # empty list to add task
    tasks = Load_task()
    while True:
        print('''1. Add task
2. View tasks
3. Delete a task
4. Exit''')
        choice= input("hii sir/madam, what is your choice: ")
        if choice == '4':
            print("your to-do list is ended, see you soon!")
            break
        if choice == '1':
            Add_task(tasks)
        elif choice == '2':
            View_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        else:
            print("invalid choice. Enter the correct choice.")
    save_task(tasks)
    print("Hello Venii")

if __name__ == "__main__":
    main()
