class ContaBancaria:
    def __init__(self, titular, saldo=0):
      self.titular = titular
      self.saldo = saldo
      self.operacoes = []
    def depositar(self, valor):
      if valor == 0:
        self.operacoes.append(valor)
      else:
        self.saldo += valor
        self.operacoes.append(f"+{valor}")
      return self.saldo
    def sacar(self, valor):
        if valor < 0:
          if self.saldo >= abs(valor):
            self.saldo += valor
            self.operacoes.append(f"{valor}")
          else:
            self.operacoes.append("Saque não permitido")
        return self.saldo
    
    def extrato(self):
      operacoes_formatadas = ", ".join(self.operacoes)
      return f"Operações: {operacoes_formatadas}; Saldo: {self.saldo}"


nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

print(conta.extrato())