import argparse
import json
from datetime import date


def add(args):
    last_id = 0

    with open("expense.json", "r") as file:
        existing_data = json.load(file)
    
    if existing_data:
        last_id = existing_data[-1]["ID"]
    
    new_data = {
        "ID": last_id + 1,
        "Description": args.description,
        "Amount": args.amount,
        "Date": date.today().isoformat()
    }

    existing_data.append(new_data)
    
    with open("expense.json", "w") as file:
        json.dump(existing_data, file, indent=4)
        print(f"The expense {new_data["Description"]} was added with ID {new_data["ID"]}")
    

def delete(args):

    new_data = []
    deleted = False

    with open("expense.json", "r") as file:
        existing_data = json.load(file)
     
    for data in existing_data:        
        if data["ID"] != int(args.id):
            new_data.append(data)
        else:
            deleted = True
    
    if deleted:
        with open("expense.json", "w") as file:
            json.dump(new_data, file, indent=4)
            print(f"The file with id {args.id} was deleted correctly")
    else:
        print(f"The file with id {args.id} not exists")


def list():

    with open("expense.json", "r") as file:
        existing_data = json.load(file)

    column_widths = {
        'ID': 5,
        'Description': 20,
        'Amount': 10,
        'Date': 15
    }

    for key in existing_data[0].keys():
        print(f"{key:<{column_widths[key]}}", end=' ')
    print()

    for value in existing_data:
        for key, to_print in value.items():
            print(f"{str(to_print):<{column_widths[key]}}", end=' ')
        print()

    #with open("expense.json", "r") as file:
    #    existing_data = json.load(file)
    #
    #for key in existing_data[0].keys():
    #    print(key, end='    ')
    #print()
    #for value in existing_data:
    #    
    #    for to_print in value.values():
    #        print(to_print, end='    ')
    #    print()


def summary(args):

    total = 0
    with open("expense.json", "r") as file:
        existing_data = json.load(file)
    
    if args.month:
        for data in existing_data:
            if data["Date"][5:7] == str(args.month).zfill(2):
                total += data["Amount"]
    else:
        for data in existing_data:
            total += data["Amount"]

    if total:
        print(f"Total expenses: ${total}")
        return
    print(f"No data for month {args.month}")
         

def main(args):
    
    if args.command == 'add':
        if args.description is None or args.amount is None:
            parser.error("The 'add' command requires --description and --amount arguments.")
        add(args)
    
    elif args.command == 'delete':
        if args.id is None:
            parser.error("The 'delete' command requires --id argument.")
        delete(args)

    elif args.command == 'list':
        if args.description is not None or args.amount is not None or args.id is not None or args.month is not None:
            parser.error("The 'list' command does not accept any additional arguments.")
        list()

    elif args.command == 'summary':
        if args.month is not None or args.month is None:
            summary(args)
        else:
            parser.error("The 'summary' command just requires --month or None arguments.")


if __name__ == "__main__":
    '''Alternative parser code.
    # Configuración del parser principal
    parser = argparse.ArgumentParser(description='Simple expense tracker application to manage your finances')
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

    # Subcomando "add"
    parser_add = subparsers.add_parser('add', help='Add a new expense')
    parser_add.add_argument('--description', type=str, required=True, help='Description of the expense')
    parser_add.add_argument('--amount', type=int, required=True, help='Amount of the expense')

    # Subcomando "delete"
    parser_delete = subparsers.add_parser('delete', help='Delete an expense by ID')
    parser_delete.add_argument('--id', type=int, required=True, help='ID of the expense')

    # Subcomando "list"
    parser_list = subparsers.add_parser('list', help='List all expenses')
    # No se necesitan argumentos adicionales para "list"

    # Subcomando "summary"
    parser_summary = subparsers.add_parser('summary', help='Show summary of expenses for a specific month')
    parser_summary.add_argument('--month', type=int, required=True, help='Month to see total expense')

    # Parsear argumentos
    args = parser.parse_args()
    '''
    parser = argparse.ArgumentParser(description='Simple expense tracker application to manage your finances')
    parser.add_argument('command', choices=['add', 'delete', 'list', 'summary'], help='Command to execute')
    parser.add_argument('--description', type=str, help='Description of the expense')
    parser.add_argument('--amount', type=int, help='Amount of the expense')
    parser.add_argument('--id', type=int, help='ID of the expense')
    parser.add_argument('--month', type=int, help='Month to see total expense')
    args = parser.parse_args()

    try:
        with open("expense.json","r") as file:
            pass
    except FileNotFoundError:
        with open("expense.json", "x+") as file:
            json.dump([],file,indent=4)

    main(args)