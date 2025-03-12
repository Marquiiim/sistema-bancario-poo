from datetime import datetime

class Client:

    # VARIÁVEIS DE FLUXO.
    LIMIT = 500 # LIMITE DE SAQUE (VALOR) POR DIA.
    number_withdrawals = 0 # 5 SAQUES POR DIA.
    number_transactions= 0 # 10 TRANSAÇÕES POR DIA.

    def __init__(self, balance = 0, extract = {}):
        self.balance = balance
        self.extract = extract

    def deposit_client(self, value):
        date_now = datetime.now()

        if Client.number_transactions <= 10:
            if value > 0:
                self.balance += value
                Client.number_transactions += 1
                self.extract.append(f"[DEPÓSITO] R${value} | Dia: {date_now.strftime('%d/%m/%Y')} ás {date_now.strftime('H%:%M:%S')}")
            else:
                print("[ERROR] Valor inválido, tente novamente")
        else:
            print("[ERROR] Você atingiu o número de transações diárias, tente novamente outro dia.")
    
    def withdraw_client(self, value):
        date_now = datetime.now()

        if Client.number_transactions <= 10:
            if Client.number_withdrawals <= 5:
                self.balance -= value
                Client.number_transactions += 1
                Client.number_withdrawals += 1
                self.extract.append(f"[SAQUE] R${value} | Dia: {date_now.strftime('%d/%m/%Y')} ás {date_now.strftime('%H:%M:%S')}")
            else:
                print("[ERROR] Você atingiu o número de saques diários, tente novamente outro dia.")
        else:
            print("[ERROR] Você atingiu o número de transações diárias, tente novamente outro dia.")

    def extract_client(self):
        print('\n'.join(self.extract))