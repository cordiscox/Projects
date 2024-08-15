# Task Management CLI Application

This CLI application allows users to manage tasks from the command line. It supports adding, updating, deleting tasks, and marking tasks as in-progress or done. Tasks are stored in a JSON file.

## Features

- **Add, Update, and Delete tasks**
- **Mark a task as in-progress or done**
- **List all tasks**
- **List tasks by status: done, not done, in-progress**

## Constraints

- Any programming language can be used.
- Use positional arguments in the command line to accept user inputs.
- Store tasks in a JSON file in the current directory.
- The JSON file is created if it does not exist.
- Use the native file system module to interact with the JSON file.
- Do not use external libraries or frameworks.
- Handle errors and edge cases gracefully.

## Task Properties

Each task has the following properties:

- **id:** A unique identifier
- **description:** A short description of the task
- **status:** The status (todo, in-progress, done)
- **createdAt:** The date and time when the task was created
- **updatedAt:** The date and time when the task was last updated

## Command Examples

- **Adding a new task**

  ```bash
    task-cli.py add "Buy groceries"
    task-cli.py update 1 "Buy groceries and cook dinner"
    task-cli.py delete 1
    task-cli.py mark-in-progress 1

    task-cli.py mark-done 1

    task-cli.py list

    task-cli.py list done
    task-cli.py list todo
    task-cli.py list in-progress
    ```

