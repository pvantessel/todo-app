import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This App is used to keep track on your todo's.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo....")

