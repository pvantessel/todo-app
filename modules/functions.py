import os

# Dynamic folder in home directory user.
APP_DIR = os.path.join(os.path.expanduser("~"), "My Todo App")

# Complete file path to todos.txt in that folder.
FILEPATH = os.path.join(APP_DIR, "todos.txt")

def ensure_app_directory_and_file():
    """Zorgt dat de appmap en todos.txt bestaan."""
    # Maak de map aan als die nog niet bestaat
    os.makedirs(APP_DIR, exist_ok=True)

    # Maak een leeg todos.txt-bestand aan als het nog niet bestaat
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w') as file:
            pass

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    ensure_app_directory_and_file()

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items in a text file. """
    ensure_app_directory_and_file()

    todos_arg = [todo if todo.endswith('\n') else todo + '\n' for todo in todos_arg]
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    ensure_app_directory_and_file()
    test_get_todos = get_todos('../todos.txt')
    print(test_get_todos)
