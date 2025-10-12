from modules import functions
import time

timestamp = time.strftime("%d %B %Y, %X")
print(f"The time is: ", timestamp)

while True:
    # Get user input and strip space chars.
    user_action = input("Type add <todo>, show, edit <nr>, complete <nr> or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # Add an item to todo list
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # Show items from todo list

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            # Edit items in todo list
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            if index < 0 or index >= len(todos):
                raise IndexError

            new_todo = input("Enter your new todo: ")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            # The command is not ok. Program expects a number.
            print("The command you entered is not valid. Enter a valid number.")
            continue

        except IndexError:
            # The command is not ok. Program expects a existing index number.
            print("The command you entered is not valid. The number you entered doesn't exist!")
            continue

    elif user_action.startswith('complete'):
        try:
            # Remove items from todo list
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            if index < 0 or index >= len(todos):
                raise IndexError

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' has been successfully removed"
            print(message)

        except ValueError:
            # The command is not ok. Program expects a number.
            print("The command you entered is not valid. Enter a valid number.")
            continue

        except IndexError:
            # The command is not ok. Program expects a existing index number.
            print("The command you entered is not valid. The number you entered doesn't exist!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("You didn't enter a valid command")

print("Bye bye")

