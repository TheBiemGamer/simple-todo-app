#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Noah Bozkurt 2024 - Todo List App
"""

import FreeSimpleGUI as sg
from todo import TodoList

todolist = TodoList()
sg.theme("Black")

label = sg.Text("Enter a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="task")
add_buton = sg.Button("Add")
list_box = sg.Listbox(values=todolist.get_tasks(), key="tasks", enable_events= True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

layout = [[label],
          [input_box, add_buton],
          [list_box, sg.Column([
              [edit_button],
              [complete_button]
          ])]]

window = sg.Window("Simple Python ToDo List", 
                   layout=layout, 
                   font=("Helvetica", 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED:
            break
        case "Add":
            task = values.get("task")
            if task:
                todolist.add_task(name=task)
                window["tasks"].update(values=todolist.get_tasks())
                
        case "Edit":
            task_to_edit = values.get("tasks")
            new_task = values.get("task")
            if task_to_edit and new_task:
                index = todolist.get_index(name=task_to_edit[0].strip())
                todolist.edit_task(index=index, value=new_task)
                window["tasks"].update(values=todolist.get_tasks())

        case "Complete":
            task_to_complete = values.get("tasks")
            if task_to_complete:
                index = todolist.get_index(name=task_to_complete[0].strip())
                todolist.remove_task(index=index)
                window["tasks"].update(values=todolist.get_tasks())
                window["task"].update(value="")

        case "tasks":
            tasks = values.get("tasks")
            if tasks:
                window["task"].update(value=tasks[0])

window.close()