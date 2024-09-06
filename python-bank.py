import textwrap 

def menu():
    menu = """

    [ls] listar Contas
    [u] Cadastrar Usuario
    [c] Cadastrar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(textwrap.dedent(menu))

def main():
    
    saldo=0
    limite = 500
    extrato =f""
    numero_saques=0
    LIMITE_SAQUES =3
    AGENCIA = "0001"
    usuarios =[]
    contas =[]
    
    while True:
       
        opcao = menu()
       
        if opcao == "d":
          saldo,extrato= depositar(saldo,extrato)
    
        elif opcao == "s":
           saldo,extrato = sacar(limite,extrato,LIMITE_SAQUES,saldo,numero_saques) 
        
        elif opcao == "e":
           extrato_print(saldo,extrato)
        elif opcao == "u":
           cadastrar_Usuario(usuarios)
        elif opcao == "c":
           numero_conta=len(contas)+1
           conta=criar_conta(AGENCIA,numero_conta,usuarios)
           if conta:
               contas.append(contas)
        elif opcao == "ls":
            listar_contas(contas)    
        elif opcao == "q":
            break
        else:
            print("Opção inválida!")
    
    
           

def depositar(saldo,extrato):
        valor = float(input("Informe o valor do depósito: "))#-
        if valor > 0:#-
            saldo += valor#-
            extrato += f"Deposito de: R$ {valor:.2f}\n"#-
            return saldo, extrato
        else:
            print("Valor inválido!")#-

def sacar(limite,extrato,LIMITE_SAQUES,saldo,numero_saques):
        valor = float(input("informe o valor do saque:"))
        excedeu_saldo=valor > saldo
        excedeu_limite = valor > limite
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
            extrato+= f"Saque de:\t\t R$ {valor:.2f}\n"
            return saldo,extrato

        else:
            print("Valor inválido!")

        
def extrato_print(saldo:float,extrato):
        print("\n================== EXTRATO ==================")
        print("Nao foram realizadas movimentacoes " if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}\n")
        print("==============================================")
    
def cadastrar_Usuario(usuarios):
    cpf= input("digite o cpf(somente numeros):")
    usuario = filtrar_Usuario(cpf,usuarios)
    if usuario:
        print("\n Ja existe usuario com esse cpf")
        return
    nome = input("digite o nome completo:")
    data_nascimento= input("digite a data de nascimento(dd-mm-aaaa):")
    endereco = input("informe p enderecp(logadouro, nro - bairo - cidade/sigla estado):")
    
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
    
    print("Usuario criado com sucesso")
    
    
def filtrar_Usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"]==cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf= input("informe o cpf do usuario")
    usuario =filtrar_Usuario(cpf,usuarios)
    if usuario:
        print("\n Conta criada com sucesso...")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    else:
        print("\n Usuario nao encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""Agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

main()