menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo=0
limite = 500
extrato =""
numero_saques=0
LIMITE_SAQUES =3

while True:

    opcao =input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato = f"Depósito de : R$ {valor:.2f}\n"

        else:
            print("Valor inválido!")
    
    elif opcao == 's':
        valor = float(input("informe o valor do saque:"))

        excedeu_saldo=valor >saldo
        excedeu_limite = valor >limite
        excedeu_saques=numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("valor do saque excede o limite")
        elif excedeu_saques:
            print("Limite de saques excedido!")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque de: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")
    
    elif opcao == 'e':
        print("\n================== EXTRATO ==================")
        print("Nao foram realizadas movimentacoes " if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==============================================")
    
    elif opcao == 'q':
        break
    else:
        print("Opção inválida!")
                
