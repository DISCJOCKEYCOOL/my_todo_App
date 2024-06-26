FILEPATH = "todos.txt"

def get_todos(filepath="todos.txt"):
    """Read a text file
    and return the list of text files"""

    with open(filepath, "r") as file_global:
        todo_global = file_global.readlines()
    return todo_global


def write_todos(todos_arg, filepath="todos.txt"):
    """Write a todos item list in a text file"""
    with open("todos.txt", "w") as file_global:
        file_global.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())
