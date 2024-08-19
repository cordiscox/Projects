import sys
import json
from error import CommandError, ArgsError
from enum import Enum
from datetime import datetime


class Command(Enum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"  
    INPROGRESS = "mark-in-progress"
    DONE = "mark-done" 
    LIST = "list"

class Status(Enum):
    TODO = "todo"
    INPROGRESS = "in-progress"
    DONE = "done" 

def add(args):

    last_id = 0

    with open("todo.json", "r") as file:
        existing_data = json.load(file)

    if existing_data:
        last_id = existing_data[-1]["id"]
    
    new_data = {
        "id": last_id + 1, # we can use UUID to change this logic.
        "description": args[0],
        "status": Status.TODO.value,
        "createdAT": datetime.now().isoformat(),
        "updateAT": datetime.now().isoformat(),
    }
    
    existing_data.append(new_data)

    with open("todo.json", "w") as file:
        json.dump(existing_data, file, indent=4)
        print(f"task {new_data["description"]} was added with ID {new_data["id"]}.")

        
def update(args):

    with open("todo.json", "r+") as file:
        existing_data = json.load(file)
        updated = False
        
        for item in existing_data:
            if item["id"] == int(args[0]):
                item["description"] = args[1]
                item["updateAT"] = datetime.now().isoformat()
                updated = True
                break   
        
        if updated:
            #move to begin of the file, truncate and save new data.
            file.seek(0)
            file.truncate()
            json.dump(existing_data, file, indent=4)
            print(f"task with ID {args[0]} was updated.")
        else:
            print(f"task with ID {args[0]} was not found.")
            

def delete(args):

    with open("todo.json", "r+") as file:
        new_data = []        
        existing_data = json.load(file)

        new_data = [data for data in existing_data if data["id"] != int(args[0])]

        if existing_data != new_data:
            file.seek(0)
            file.truncate()
            json.dump(new_data, file, indent=4)
            print(f"the data with id {args[0]} was deleted") 
        else:
            print(f"the data with id {args[0]} not exists") 


def mark_in_progress(args):

    with open("todo.json", "r+") as file:
        existing_data = json.load(file)
        updated = False
        
        for item in existing_data:
            if item["id"] == int(args[0]):
                item["status"] = Status.INPROGRESS.value
                item["updateAT"] = datetime.now().isoformat()
                updated = True
                break   
        
        if updated:
            #move to begin of the file, truncate and save new data.
            file.seek(0)
            file.truncate()
            json.dump(existing_data, file, indent=4)
            print(f"task with ID {args[0]} was updated to {Status.INPROGRESS.value}.")
        else:
            print(f"task with ID {args[0]} was not found.")


def mark_done(args):

    with open("todo.json", "r+") as file:
        existing_data = json.load(file)
        updated = False
        
        for item in existing_data:
            if item["id"] == int(args[0]):
                item["status"] = Status.DONE.value
                item["updateAT"] = datetime.now().isoformat()
                updated = True
                break   
        
        if updated:
            #move to begin of the file, truncate and save new data.
            file.seek(0)
            file.truncate()
            json.dump(existing_data, file, indent=4)
            print(f"task with ID {args[0]} was updated to {Status.DONE.value}.")
        else:
            print(f"task with ID {args[0]} was not found.")


def list():
    
    with open("todo.json", "r") as file:
        existing_data = json.load(file)
        [print(item) for item in existing_data]


def list_status(args):

    with open("todo.json", "r") as file:
        existing_data = json.load(file)
        [print(item) for item in existing_data if item["status"] == args[0]] 
    

def main(command, arguments):
    
    if command == Command.ADD.value:
        if len(arguments) != 1:
            raise ArgsError("To ADD a task you need to put only the description")
        add(arguments)
        

    if command == Command.UPDATE.value:
        if len(arguments) != 2:
            raise ArgsError("To UPDATE a task you need to put the id and new description")
        update(arguments)
    

    if command == Command.DELETE.value: 
        if len(arguments) != 1:
            raise ArgsError("To DELETE a task you need to put only the task ID")
        delete(arguments)


    if command == Command.INPROGRESS.value: 
        if len(arguments) != 1:
            raise ArgsError(f"To change the task to {Status.INPROGRESS.value} you need to put only the task ID")
        mark_in_progress(arguments)
    

    if command == Command.DONE.value: 
        if len(arguments) != 1:
            raise ArgsError(f"To change the task to {Status.DONE.value}  you need to put only the task ID")
        mark_done(arguments)


    if command == Command.LIST.value:
        if len(arguments) > 0:
            list_status(arguments)
        else:
            list()

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        raise ArgsError("No args given.")
    
    command = sys.argv[1]
    
    if command not in Command:
        raise CommandError(f"command {command} doesn't exist")
    
    try:
        with open("todo.json","r") as file:
            pass
    except FileNotFoundError:
        with open("todo.json", "x+") as file:
            json.dump([],file,indent=4)
        
    main(command, sys.argv[2::])
    
