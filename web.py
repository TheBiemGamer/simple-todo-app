#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Noah Bozkurt 2024 - Todo List App
"""

import streamlit as st
from todo import TodoList
import time

todolist = TodoList()

def add_task():
    new_task = st.session_state.get("new_task")
    if new_task and new_task not in todolist.get_tasks():
        todolist.add_task(name=new_task)

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app increases your productivity")

for index, task in enumerate(todolist.get_tasks()):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todolist.remove_task(index=index)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(
    label="Task", 
    placeholder="Enter a task...", 
    on_change=add_task, 
    key="new_task", 
    label_visibility="collapsed"
)

time.sleep(1)