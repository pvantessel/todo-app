from modules import functions
import FreeSimpleGUI as fsg

label_input = fsg.Text("Type in a To-Do")
input_field = fsg.InputText(tooltip="Enter a To-Do", key="todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = fsg.Button("Edit")

window = fsg.Window("My To-Do App",
                    layout=[[label_input, input_field, add_button],
                            [list_box, edit_button]],
                    font=("Times New Roman", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todo"])
    print(4, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case fsg.WIN_CLOSED:
            break

window.close()