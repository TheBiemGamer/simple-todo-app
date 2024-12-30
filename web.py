import streamlit as st
from todo import TodoList

todolist = TodoList()

def add_task():
    new_task = st.session_state.get("new_task")
    if not new_task in todolist.get_tasks():
        todolist.add_task(name=new_task)

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app increases your productivity")

for index, tasks in enumerate(todolist.get_tasks()):
    checkbox = st.checkbox(tasks, key=tasks)
    if checkbox:
        todolist.remove_task(index=index)
        del st.session_state[tasks]
        st.rerun()

st.text_input(label="Task", placeholder="Enter a task...", on_change=add_task, key="new_task", label_visibility="collapsed")
