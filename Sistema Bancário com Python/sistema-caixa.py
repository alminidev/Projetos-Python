from datetime import datetime
data_atual = datetime.now()
data_em_texto = data_atual.strftime('%d/%m/%Y')

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do despósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito em {data_em_texto}: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor excede o número limite de saques diários.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque em {data_em_texto}: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n------------ EXTRATO --------------")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo em {data_em_texto}: R$ {saldo:.2f}")
        print("\n-----------------------------------")

    elif opcao == "0":
        print("Obrigado por utilizar nosso Sistema. O Banco Almini agradeçe!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
