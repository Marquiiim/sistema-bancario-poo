from templates.templates import menu
from models.usuario import Client

def deposit():
    deposit_template = f"""
============= ÁREA DE DEPÓSITO =============
Saldo atual da conta: R$ {usuario.view_balance()}
            
            [C] Cancelar
            
Digite o valor do deposito:
=>"""
    
    while True:
        deposit_value = input(deposit_template)
        if deposit_value.upper() == "C":
            print("Operação cancelada.")
            break
        try:
            deposit_value = float(deposit_value)
            if usuario.deposit_client(deposit_value):
                break
            else:
                print("[ERROR] Não foi possível realizar o depósito, tente novamente.")
        except ValueError:
            print("[ERROR] Valor inválido, digite um número.")

def withdraw():
    withdraw_template = f"""
============= ÁREA DE SAQUE =============
Saldo atual da conta: R$ {usuario.view_balance()}
            
            [C] Cancelar
            
Digite o valor do saque:
=>"""
    
    while True:
        withdraw_value = input(withdraw_template)
        if withdraw_value.upper() == "C":
            print("Operação cancelada.")
            break
        try:
            withdraw_value = float(withdraw_value)
            if usuario.withdraw_client(withdraw_value):
                break
            else:
                print("[ERROR] Não foi possível realizar o saque, tente novamente.")
        except ValueError:
            print("[ERROR] Valor inválido, digite um número.")

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

usuario = Client(0)

while True:
    options = input(menu).upper()

    action = sections.get(options, lambda: print("Operação não encontrada, tente novamente"))
    action()