"""
This file contains functions to handle completions as either files or commands.
"""

import subprocess
from llm_interface import complete
from prompts import debugging_prompt

def handle_completion_as_file(completion):
    # Get the file name
    filename = completion.split('\n')[0]
    filename = filename[2:]

    # Get the contents
    contents = completion[completion.find('\n')+1:]

    # Write the file
    with open(filename, 'w') as f:
        f.write(contents)

    print(f"""================
{filename}
================
{contents}""")

def handle_completion_as_command(completion):
    # Get the file name
    first_line = completion.split('\n')[0]

    commands_to_run = completion.splitlines()[1:-1]
    commands_to_run_as_string = "\n".join(commands_to_run)
    input(f"autocoder would like to run the following commands. Press enter to continue. (to cancel, press control-c)\n\n\033[0;33m{commands_to_run_as_string}\033[0m")
    for command in commands_to_run:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        stdout, stderr = process.communicate()

        print('STDOUT:')
        print(stdout.decode())

        print('STDERR:')
        errs = stderr.decode()

        if errs:
            print(f"I got the following error:\n\n{errs} \nLet me see if I can debug it...")

            # Make one attempt to debug the error
            completion = complete(debugging_prompt(command, errs)).strip()

            handle_completion_as_file(completion)

            # Try running the command again
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            stdout, stderr = process.communicate()

            print('STDOUT:')
            print(stdout.decode())

            print('STDERR:')
            errs = stderr.decode()

            if errs:
                print(f"I still got an error:\n\n{errs}\n")

def handle_completion_as_file_or_command(completion):
    if completion.split('\n')[0] == "```console":
        handle_completion_as_command(completion)
    else:
        handle_completion_as_file(completion)

