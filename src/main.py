from templates.templates import menu
from models.usuario import Client

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
    deposit_template = f"""
============= ÁREA DE DEPÓSITO =============
Saldo atual da conta: R$ {usuario.view_balance()}

Digite o valor do deposito:
=>"""
    
    while True:
        deposit_value = float(input(deposit_template))
        if usuario.deposit_client(deposit_value):
            break
        else:
            print("[ERROR] Não foi possível realizar o depósito, tente novamente.")

def withdraw():
    withdraw_template = f"""
============= ÁREA DE SAQUE =============
Saldo atual da conta: R$ {usuario.view_balance()}

Digite o valor do deposito:
=>"""
    
    while True:
        withdraw_value = float(input(withdraw_template))
        if usuario.withdraw_client(withdraw_value):
            break
        else:
            print("[ERROR] Não foi possível realizar o saque, tente novamente.")

def extract():
    usuario.extract_client()

def close_system():
    raise SystemExit("Sistema finalizado com sucesso.")

sections = {
    "D": deposit,
    "S": withdraw,
    "E": extract,
    "X": close_system
}

while True:
    usuario = Client(0)
    options = input(menu).upper()

    action = sections.get(options, lambda: print("Operação não encontrada, tente novamente"))
    action()