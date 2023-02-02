import os

def get_all_files():
    # Get list of all files in the current directory
    files = os.listdir('.')
    all_files_appended = ""

    # Iterate through each file
    for file in files:
        # Open and read the file
        if os.path.isfile(file):
            with open(file) as fp:
                # Print the contents of the file

                all_files_appended += "\n================\n"
                all_files_appended += file
                all_files_appended += "\n================\n"
                all_files_appended += fp.read()
                all_files_appended += "\n"

    return all_files_appended

all_files_appended = get_all_files()

def prompt(input_from_user):
    return f"""You are an experienced programmer that can write safe, readable, and commented code in a variety of languages.

You are working in a directory with the following contents:

{all_files_appended}

Your goal now is to {input_from_user}.
Make sure to write safe, readable, and commented code in an appropriate language based on the goal.


================
EXAMPLES
================

Code to write me a python file called example.py that prints out Hello World!:

# example.py
if __name__ == "__main__":
    print("Hello World!")

Code to Modify example.py to print it out 10 times:

# example.py
if __name__ == "__main__":
    for i in range(10):
        print("Hello World!")

Code to please comment example.py:

# example.py
# This file prints out "Hello World!" 10 times

if __name__ == "__main__": # Checks to see if the program is being run directly
    for i in range(10):
        print("Hello World!") # Prints "Hello World!" each time the loop is executed

Code to please write me a command line tool called autocoder:

# autocoder
#!/usr/bin/env python3

print("Welcome to autocoder!")

Code to go ahead and run the webserver:

```console
python3 webserver.py
```

Code to remove the webserver file:

```console
rm webserver.py
```

Code to make me an example webpage:

# index.html
<!DOCTYPE html>
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <p>This is an example of a simple HTML page with one paragraph.</p>
    </body>
</html>


================
Actual Prompt
================

Code to {input_from_user}:"""

def debugging_prompt(command, error_message):
    return f"""You are an experienced programmer that can write safe, readable, and commented code in a variety of languages.

You are working in a directory with the following contents:

{all_files_appended}

You recently ran {command} and got the following error message:

{error_message}

Your goal is now to debug this error by modifying one of the files in the directory.

================
EXAMPLES
================

Code to write me a python file called example.py that prints out Hello World!:

# example.py
if __name__ == "__main__":
    print("Hello World!")

Code to Modify example.py to print it out 10 times:

# example.py
if __name__ == "__main__":
    for i in range(10):
        print("Hello World!")

Code to please comment example.py:

# example.py
# This file prints out "Hello World!" 10 times

if __name__ == "__main__": # Checks to see if the program is being run directly
    for i in range(10):
        print("Hello World!") # Prints "Hello World!" each time the loop is executed

Code to please write me a command line tool called autocoder:
# autocoder
#!/usr/bin/env python3

print("Welcome to autocoder!")


================
Actual Prompt
================

Code to debug the error message:
    """