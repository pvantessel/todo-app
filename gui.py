from modules import functions
import FreeSimpleGUI as fsg
import time

fsg.theme("LightGreen7")

label_clock = fsg.Text("", key="clock")
label_input = fsg.Text("Type in a To-Do")
input_field = fsg.InputText(tooltip="Enter a To-Do", key="todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window("My To-Do App",
                    layout=[[label_clock],
                            [label_input, input_field, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Times New Roman", 20))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%d %B %Y, %X"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                fsg.popup("Please select a todo to edit", font=("Times New Roman", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0].strip()
                todos = [t.strip() for t in functions.get_todos()]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                fsg.popup("Please select a todo to complete", font=("Times New Roman", 20))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0].strip())

        case fsg.WIN_CLOSED:
            break

window.close()