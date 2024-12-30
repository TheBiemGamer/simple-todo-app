#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Noah Bozkurt 2024 - Todo List App
"""

import os

program_path = os.path.dirname(os.path.realpath(__file__))


class TodoList:
    def __init__(self, task_file_name: str = "todos.txt"):
        self.todos_file_name = task_file_name
        self.todos_file = os.path.join(program_path, self.todos_file_name)
        self.tasks = []
        self.__get_tasks()

    def __get_tasks(self) -> None:
        """Load tasks from the file."""
        if os.path.exists(self.todos_file):
            with open(self.todos_file, "r") as file:
                file_tasks = file.readlines()
                for task in file_tasks:
                    self.add_task(name=task.strip())  # Automatically capitalize task names
        else:
            return []

    def __write_tasks(self) -> None:
        """Write tasks to the file."""
        with open(self.todos_file, "w") as file:
            file.writelines("\n".join([task.name.lower() for task in self.tasks]))

    def add_task(self, name: str) -> str:
        """Add a task to the list and save to file."""
        name = name.strip().capitalize()
        self.tasks.append(Task(name=name))
        self.__write_tasks()
        return name

    def get_index(self, name: str) -> int:
        """Get the index of a task by its name."""
        name = name.strip().capitalize()
        for index, task in enumerate(self.tasks):
            if task.name == name:
                return index
        return -1

    def remove_task(self, index: int) -> bool:
        """Remove a task by its index."""
        if isinstance(index, int) and 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.__write_tasks()
            return True
        return False
    
    def edit_task(self, index: int, value: str) -> bool:
        """Edit an existing task."""
        value = value.strip().capitalize()
        if 0 <= index < len(self.tasks):
            self.tasks[index].name = value
            self.__write_tasks()
            return True
        return False
    
    def print_tasks(self) -> None:
        """Print all tasks."""
        for number, task in enumerate(self.tasks):
            print(f"Task {number + 1}: {task.name}")

    def get_tasks(self) -> list:
        task_list = []
        for task in self.tasks:
            task_list.append(task.name)
        return task_list

class Task:
    def __init__(self, name: str, completed: bool = False):
        self.name = name
        self.completed = completed
