from modules import functions
import FreeSimpleGUI as fsg

label_input = fsg.Text("Type in a To-Do")
input_field = fsg.InputText(tooltip="Enter a To-Do", key='todo')
add_button = fsg.Button("Add")

window = fsg.Window('My To-Do App',
                    layout=[[label_input], [input_field, add_button]],
                    font=('Times New Roman', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case fsg.WIN_CLOSED:
            break

window.close()


