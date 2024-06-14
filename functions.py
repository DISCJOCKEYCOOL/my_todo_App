FILEPATH = "/Users/DJcoding/Desktop/Python_Projects/web_app1/pythonProject/todos.txt"

def get_todos(filepath="/Users/DJcoding/Desktop/Python_Projects/web_app1/pythonProject/todos.txt"):
    """Read a text file
    and return the list of text files"""

    with open(filepath, "r") as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write a todos item list in a text file"""
    with open("/Users/DJcoding/Desktop/Python_Projects/web_app1/pythonProject/todos.txt", "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())
