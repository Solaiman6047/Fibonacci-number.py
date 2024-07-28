Todo_list={
    "1":"study maths",
    "2":"head the gym"
}
completed_tasks={
    
}
def add_task():
    print("Enter the task:")
    x=input()
    Todo_list.update({"3":x})
    print(f"Your to-do list:{Todo_list}")
    print(f"Your completed tasks:{completed_tasks}")

def view_tasks():
    print(f"Your to-do list:{Todo_list}")
    print(f"Your completed tasks:{completed_tasks}")
    
def mark_task():
    print("Enter the completed task:")
    x=input()
    if x in Todo_list:
        completed_tasks.update({"1":x})
        del Todo_list[x]
        print(f"YOU HAVE COMPLETED THIS TASK:{x}")
        print(f"Your to-do list:{Todo_list}")
        print(f"Your completed tasks:{completed_tasks}")
    else:
        print("Can't find this task")
        
def delete_task():
    x=input("Enter task number")
    if x in Todo_list:
        del Todo_list[x]
        print(f"Your to-do list:{Todo_list}")
        print(f"Your completed tasks:{completed_tasks}")
    else:
        print("Task not found")
        
print("Enter action (add/delete/mark/view)")
x=input()
if x == "add":
    add_task()
elif x == "delete":
    delete_task()
elif x == "mark":
    mark_task()
elif x == "view":
    view_tasks()
else:
    print("Invalid action. Please try again")