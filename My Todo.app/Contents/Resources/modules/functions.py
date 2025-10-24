FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items in a text file. """
    todos_arg = [todo if todo.endswith('\n') else todo + '\n' for todo in todos_arg]
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    test_get_todos = get_todos('../todos.txt')
    print(test_get_todos)
