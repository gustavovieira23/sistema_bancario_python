menu = """
=======================================
              MENU PRINCIPAL
=======================================
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair
=======================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("\nOperação falhou! O valor informado é inválido.\n")

    elif opcao == "s":
        valor = float(input("\nInforme o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.\n")
        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.\n")
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.\n")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("\nOperação falhou! O valor informado é inválido.\n")

    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("================================================")

    elif opcao == "q":
        print("\nObrigado por utilizar nossos serviços. Até logo!")
        break

    else:
        print("\nOperação inválida, por favor selecione uma opção válida.\n")
