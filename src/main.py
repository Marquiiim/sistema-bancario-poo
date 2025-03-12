from templates.templates import menu

def cancel_operation(prohibited):
    if prohibited.upper() == "C":
        return True
    return False

def execute_operation(operation, *args):
    while True:
        prohibited = input(operation(*args))
        if cancel_operation(prohibited):
            return None
        return prohibited

def deposit():
    pass

def withdraw():
    pass

def extract():
    pass

def close_system():
    pass

sections = {
    "D": deposit,
    "S": withdraw,
    "E": extract,
    "X": close_system
}

while True:
    options = input(menu).upper()

    action = sections.get(options, lambda: print("Operação não encontrada, tente novamente"))
    action()