
# cria as datas e converte
import datetime
data_inicial = (datetime.datetime.now())
data = data_inicial.strftime("%d/%m/%Y %H:%M:%S")

# cria o usuario dos servicos do banco
usuario = "Silvana Nadalin"

# Mensagem de boas vindas
print("\n*************** SISTEMA BANCARIO - DESAFIO DIO *************** \n")
 
print(f"Olá, {usuario} , bem vinda !")

# cria o menu
menu = """

Digite o numero da opcao desejada

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Opcao escolhida => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Desenvolvimento dos servicos bancarios, a serem solicitados pelo usuario

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = int(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato +=  f"Depósito: R$ {valor:.2f} - Data {data}\n"
            print("Deposito efetuado com sucesso !")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = int(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f} - Data {data}\n"
            numero_saques += 1
            print(" Saque efetuado com sucesso !")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO BANCARIO ================")
        print(f"\nCliente: {usuario} \n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f} - Data {data}")
        print("====================================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")