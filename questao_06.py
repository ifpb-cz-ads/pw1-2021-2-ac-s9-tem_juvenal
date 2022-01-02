import os
#6) Altere o programa de forma que a mensagem saldo insuficiente seja exibida caso haja 
#tentativa de sacar mais dinheiro que o saldo disponível (classe Conta).

class Conta:

    def __init__(self,clientes,numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacao = []
        self.deposito(saldo)

    def resumo(self):
       print(f" Conta Corrente Nº {self.numero} Saldo: {self.saldo:10.2f}")

    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacao.append(["Saque",valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self,valor):
        self.saldo +=valor
        self.operacao.append(["Déposito", valor])

    def extrato(self):
        print(f"Extrato Conta Corrente Nº {self.numero}\n")
        for o in self.operacao:
             print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}\n")

    


opc = 0
while opc !=6:
    
    print('''
            [1] Criar conta Corrente
            [2] Dépositar
            [3] Sacar
            [4] Ver extrato
            [5] Ver resumo
            [6] Sair                 ''')
    opc = int(input("Digite opção: "))
    if opc == 1:
        nome = input("Digie seu nome: ")
        numero = int(input("Digite seu número: "))
        c = Conta(nome,numero)
        

    elif opc == 2:
        valor = float(input("Digite valor para deposito: "))
        c.deposito(valor)
    elif opc == 3:
        valor = float(input("Digite valor para sacar: "))
        c.saque(valor)
    elif opc == 4:
        c.extrato()
    elif opc == 5:
        c.resumo()
    else:
        print("OPÇÃO INVALIDA. Tente novamente")
    

    



    

