import tkinter as tk
from tkinter import messagebox

#name of the file you want to save tasks
Tasks_file="Task.txt"

#function to load tasks from file
def Load_task():
    try:
        with open("Task_file","r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

#function to save tasks to file
def Save_task():
        with open("Tasks_file","w") as file:
            for task in tasks:
                 file.write(task + '\n')
            
# Add a new task
def Add_task():
    task = task_entry.get() #Global varibale
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0,tk.END)
        Save_task()
    else:
         messagebox.showwarning("Input Error","Please enter the task.")

#Delete a task
def Delete_task():
    selected= listbox.curselection()
    if selected:
        index=selected[0]
        tasks.pop(index)
        listbox.delete(index)
        Save_task()
    else:
         messagebox.showwarning("Select Task","Please select a task to delete")

# ------------------------ GUI Setup ------------------------

#create window
root=tk.Tk()
root.title("To-Do List")

#Task input field

task_entry=tk.Entry(root,width=40)
task_entry.pack(pady=10)

#Add Task button

add_button=tk.Button(root,text="Add Task",width=20,command=Add_task)
add_button.pack()

#ListBox to show the task

listbox=tk.Listbox(root,width=40,height=10)
listbox.pack(pady=10)

#delete task button

delete_Button=tk.Button(root,text="Delete Selected Task",width=20,command=Delete_task)
delete_Button.pack()

#load task into listbox at start
tasks= Load_task()
for task in tasks:
    listbox.insert(tk.END, task)


#start the GUI event loop
root.mainloop()