#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Noah Bozkurt 2024 - Todo List App
"""

from todo import TodoList

# Initialize TodoList instance
todolist = TodoList(task_file_name="todos.txt")

actions = ["add", "show", "edit", "complete", "exit"]
formatted_actions = f"['{"', '".join(actions[:-1])}' or '{actions[-1]}']"

print("--- Simple Python CLI ToDo List ---")

while True:
    user_action = input(f"\nWhat do you want to do? {formatted_actions}: ").strip().lower()

    if user_action.startswith("add"):
        task_name = user_action[4:].strip() or input("\nEnter a new task: ").strip()
        task_name = task_name.capitalize()
        if task_name:
            print(f"Added '{todolist.add_task(name=task_name)}' to tasks!")

    elif user_action.startswith("edit"):
        if todolist.tasks:
            try:
                if user_action == "edit":
                    print(f"\nWhich of the following tasks do you want to edit? [1-{len(todolist.tasks)}]")
                    todolist.print_tasks()
                    task_num = int(input("Enter the task number to edit: ")) - 1
                else:
                    task_num = todolist.get_index(name=user_action[5:].strip())
                    if task_num == -1:
                        raise ValueError("Task not found!")

                old_task = todolist.tasks[task_num].name
                print(f"Now editing task {task_num + 1}: '{old_task}'")
                new_task = input(f"Enter the task name to replace '{old_task}': ").strip()

                if new_task and new_task != old_task:
                    todolist.edit_task(index=task_num, value=new_task.capitalize())
                    print(f"Task {task_num + 1} updated: '{old_task}' -> '{new_task}'")
                else:
                    print("Task name cannot be the same or empty!")

            except (ValueError, IndexError):
                print("Invalid task number!")

    elif user_action.startswith("complete"):
        if todolist.tasks:
            try:
                if user_action == "complete":
                    print(f"Which of the following tasks do you want to mark as completed? [1-{len(todolist.tasks)}]")
                    todolist.print_tasks()
                    task_num = int(input("Enter the task number to complete: ")) - 1
                else:
                    task_num = todolist.get_index(name=user_action[9:].strip())
                    if task_num == -1:
                        raise ValueError("Task not found!")

                task_name = todolist.tasks[task_num].name
                todolist.remove_task(task_num)
                print(f"Task '{task_name}' removed successfully!")

            except (ValueError, IndexError):
                print("Invalid task number!")

    elif user_action == "show":
        if todolist.tasks:
            print(f"\nListing tasks [1-{len(todolist.tasks)}]:")
            todolist.print_tasks()
        else:
            print("No tasks yet, add one first.")

    elif user_action == "exit":
        break

    elif user_action == "clear":
        print("\033[H\033[J", end="")

    else:
        print(f"The input '{user_action}' is not recognized.")

print("\n--- Simple Python CLI ToDo List ---")
