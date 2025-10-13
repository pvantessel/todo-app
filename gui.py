from modules import functions
import FreeSimpleGUI as fsg

label_input = fsg.Text("Type in a To-Do")
input_field = fsg.InputText(tooltip="Enter a To-Do")
add_button = fsg.Button("Add")

window = fsg.Window('My To-Do App', layout=[[label_input], [input_field, add_button]])
window.read()
window.close()


