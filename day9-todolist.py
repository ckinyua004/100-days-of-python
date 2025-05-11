# A mini project to learn error handling from 

def show_menu():
    print("\nTo-Do List:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def load_tasks():
    try:
        with open("todo.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
        
tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

    elif choice == "2":
        task = input("Enter a new task: ")
        if task:
            tasks.append(task)
            save_tasks(tasks)
            print(f"Task '{task}' added.")
        else:
            print("Invalid task. Please try again.")

    elif choice == "3":
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                save_tasks(tasks)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        except IndexError:
            print("Task not found.")

    elif choice == "4":
        print("Exiting the To-Do List app. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")


'''
Mini Project: Simple To-Do List (CLI App with Error Handling)
Create a command-line To-Do List app that:
    Adds tasks
    Views tasks
    Deletes tasks
    Saves them to a file (todo.txt)

Handles common errors like invalid input, file not found, etc.

🛠️ Features & What You’ll Learn
Feature	Concepts Learned
Save/load from file	File handling, FileNotFoundError
Input validation	ValueError, string parsing
Menu loop	Control flow, user input
Delete by index	List handling, IndexError
'''