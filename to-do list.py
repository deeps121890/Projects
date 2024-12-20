'''
#define a list to store tasks
tasks=[]
def display_menu():   #display menu and get user input
    print("\n------To do list menu------")
    print("1.Add a task")
    print("2.View all the tasks")
    print("3.Mark a task as completed")
    print("4.Delete a task")
    print("5.Exit")
    return input("choose an option(1-5):")
def add_task():
    task=input('Enter a task:')
    tasks.append({"task":task,"completed":False})
    print(f"Task'{task}'added successfully")
def view_task():
    if not tasks:
        print("no tasks to display")
    else:
        print("\n----To do list----")
        task_number=1
        for task in tasks:
            status ="completed" if task["completed"]else"not completed"
            print(f"{task_number}.{task['task']}[{status}]")
            task_number+=1
def mark_task_completed():
    view_task()
    if tasks:
        try:
            task_num=int(input("\nenter the task to mark as completed"))
            if 1 <= task_num <=len(tasks):
                tasks[task_num -1]["completed"]=True
                print(f"Task'{tasks[task_num-1]['task']}' marksed as completed")
            else:
                print('invalid task number!')
        except ValueError:
            print("please enter a valid number!")
def delete_task():
    view_task()
    if tasks:
        try:
            task_num=int(input("\n enter the task number to delete:"))
            if 1 <= task_num <=len(tasks):
                removed_task=tasks.pop(task_num-1)
                print(f"Task'{removed_task['task']}'deleted succesfully!")
            else:
                print("invaild task number!")
        except ValueError:
            print("please enter a vaild number!")
while True:
    choice =display_menu()
    if choice =="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        mark_task_completed()
    elif choice=="4":
        delete_task()
    elif choice=="5":
        print("Exiting To-do list.Goodbye!")
        break
    else:
        print("invaild choice!please choose a valid option")

'''
o/p:
------To do list menu------
1.Add a task
2.View all the tasks
3.Mark a task as completed
4.Delete a task
5.Exit
choose an option(1-5):1
Enter a task:wake up at 4am
Task'wake up at 4am'added successfully

------To do list menu------
1.Add a task
2.View all the tasks
3.Mark a task as completed
4.Delete a task
5.Exit
choose an option(1-5):2
wake up at 4am

----To do list----
1.wake up at 4am[not completed]

------To do list menu------
1.Add a task
2.View all the tasks
3.Mark a task as completed
4.Delete a task
5.Exit
choose an option(1-5):invaild choice!please choose a valid option

------To do list menu------
1.Add a task
2.View all the tasks
3.Mark a task as completed
4.Delete a task
5.Exit
choose an option(1-5):3

----To do list----
1.wake up at 4am[not completed]

enter the task to mark as completed done my breakfast
please enter a valid number!

------To do list menu------
1.Add a task
2.View all the tasks
3.Mark a task as completed
4.Delete a task
5.Exit
choose an option(1-5):4

----To do list----
1.wake up at 4am[not completed]

 enter the task number to delete:wake up at 4am
please enter a vaild number!

------To do list menu------
1.Add a task
2.View all the tasks
3.Mark a task as completed
4.Delete a task
5.Exit
choose an option(1-5):5
Exiting To-do list.Goodbye!
