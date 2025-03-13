from datetime import datetime

class Client:
    def __init__(self, balance = 0):
        self.balance = balance
        self.extract = {"Depósitos": [], "Saques": []}

        # VARIÁVEIS DE FLUXO.
        self.limit = 500 # LIMITE DE SAQUE (VALOR) POR DIA.
        self.number_withdrawals = 0 # 5 SAQUES POR DIA.
        self.number_transactions= 0 # 10 TRANSAÇÕES POR DIA.

    def deposit_client(self, value):
        date_now = datetime.now()

        if self.number_transactions == 10:
            print("[ERROR] Você atingiu o número de transações diárias, tente novamente outro dia.")
        else:
            if value == 0:
                print("[ERROR] Valor inválido, tente novamente")
            else:
                self.balance += value
                self.number_transactions += 1
                self.extract["Depósitos"].append(f"R${value} | Dia: {date_now.strftime('%d/%m/%Y')} às {date_now.strftime('%H:%M:%S')}")
                return True
    
    def withdraw_client(self, value):
        date_now = datetime.now()

        if self.number_transactions == 10:
            print("[ERROR] Você atingiu o número de transações diárias, tente novamente outro dia.")
        elif self.number_withdrawals == 5:
            print("[ERROR] Você atingiu o número de saques diários, tente novamente outro dia.")
        elif value > self.balance:
            print("[ERROR] Saldo insuficiente para o saque, tente novamente.")
        else:
                self.balance -= value
                self.number_transactions += 1
                self.number_withdrawals += 1
                self.extract["Saques"].append(f"R${value} | Dia: {date_now.strftime('%d/%m/%Y')} às {date_now.strftime('%H:%M:%S')}")
                return True


    def view_balance(self):
        return self.balance

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