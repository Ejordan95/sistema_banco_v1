saldo = 0
limite_diario = 500
LIMITE_SAQUES = 3
registro_saque = 0
extrato = ""

menu = '''
                Bem vindo ao Banco XPTO

Em que posso ajudar?
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair


'''
while True:
    opcao = input(menu)

    if opcao == "1": #Depósito
        valor = float(input("Informe valor para Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Erro".center(10,"!"))
            print("Informe um valor válido.")
    
    elif opcao == "2": #Saque
        valor = float(input("Informa o valor para Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_diario
        excedeu_saque = registro_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite diário.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            registro_saque += 1
        else:
            print("Operação Falhou! O valor informado é inválido.")
    
    elif opcao == "3": #Extrato
        print(" EXTRATO ".center(20,"#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("####################")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida!")