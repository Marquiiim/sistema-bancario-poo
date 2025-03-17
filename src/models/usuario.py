from datetime import datetime

class Client:
    def __init__(self, balance=0, withdraw_limit=1000):
        self._balance = balance
        self.number_transactions = 0
        self.withdraw_limit = withdraw_limit
        self.extract = {"Depósitos": [], "Saques": []}

    def deposit_client(self, value):  
        if not isinstance(value, (int, float)):
            print("[ERROR] O valor deve conter apenas números.")

        date_now = datetime.now()
        date_str = date_now.strftime('%d/%m/%Y')
        time_str = date_now.strftime('%H:%M:%S')

        if self.number_transactions >= 10:
            print("[ERROR] Você atingiu o número de transações diárias, tente novamente outro dia.")
            return False
        elif value <= 0:
            print("[ERROR] Valor inválido, tente novamente")
            return False
        else:
            self._balance += value
            self.number_transactions += 1
            self.extract["Depósitos"].append(f"R${value:.2f} | Dia: {date_str} às {time_str}")
            print(f"Depósito de R${value:.2f} realizado com sucesso.")
            return True
    
    def withdraw_client(self, value):
        if not isinstance(value, (int, float)):
            print("[ERROR] O valor deve conter apenas números.")
        
        date_now = datetime.now()
        date_str = date_now.strftime('%d/%m/%Y')
        time_str = date_now.strftime('%H:%M:%S')

        if self.number_transactions >= 10:
            print("[ERROR] Você atingiu o número de transações diárias, tente novamente outro dia.")
            return False
        elif value > self.withdraw_limit:
            print("[ERROR] Você não pode sacar mais de R$1000,00")
            return False
        elif value > self._balance:
            print("[ERROR] Saldo insuficiente para o saque, tente novamente.")
            return False
        else:
            self._balance -= value
            self.number_transactions += 1
            self.extract["Saques"].append(f"R${value:.2f} | Dia: {date_str} às {time_str}")
            print(f"Saque de R${value:.2f} realizado com sucesso.")
            return True

    def view_balance(self):
        return f"{self._balance:.2f}"

    def extract_client(self):
        line_break = '\n    '
        print(f"""
========= EXTRATO DE DEPÓSITOS =========
{line_break.join(self.extract["Depósitos"])}
""")
        
        print(f"""
========= EXTRATO DE SAQUES =========
{line_break.join(self.extract["Saques"])}
""")