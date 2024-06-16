import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("MY to-do app")
st.subheader("This is my to-do app")
st.write("This app is to increase <b>your</b> productivity",
        unsafe_allow_html=True)
if st.button('DJ'):

    st.write('HI DJ') #displayed when the button is clicked

else:

    print(" ")
if st.button('Venkat'):

    st.write('HI Venkat') #displayed when the button is clicked

else:

   print(" ")
if st.button('Dhiraj'):

    st.write('Hi Dhiraj') #displayed when the button is clicked

else:

    print(" ")
if st.button('Alka'):

    st.write('HI Alka') #displayed when the button is clicked

else:

    print(" ")


for index, todo in enumerate(todos):
checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_todo, key="new_todo")



