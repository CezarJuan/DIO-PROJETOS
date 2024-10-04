import textwrap
def funcao_menu():
    menu = """
    ===BANCO NOVO V2 ===
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar contas
    [q] Sair
    
    => """

    return input(textwrap.dedent(menu))

def funcao_deposito(saldo, valor, extrato):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        
        return saldo, extrato
    
    else:
        print("Operação falhou! O valor informado é inválido.")

def funcao_saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

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
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")

def funcao_extrato(extrato, saldo):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def funcao_usuario(usuarios):
    cpf = int(input("Informe o CPF(Somente Numeros): "))
    usuario = filtrar_usuario(cpf, usuarios)    
    
    if usuario:
        print("CPF Já Cadastrado")
        return
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco =  input("Insira o seu endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereco": endereco})
    print("========USUÁRIO CRIADO COM SUCESSO========")
    
def filtrar_usuario(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF(Somente Numeros): "))
    usuario = filtrar_usuario(cpf, usuarios)  
    
    if usuario:
        print("\n========CONTA CRIADA COM SUCESSO========")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, encerrando Criação de conta\nENCERRANDO...")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\t
            Agência: \t{conta['agencia']}
            C/C: \t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}        
        """
    print("=" * 100)
    print(textwrap.dedent(linha))
    
def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    
    
    while True:
        
        opcao = funcao_menu()
        
        match opcao:
            
            case 'd':
                
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = funcao_deposito(saldo=saldo, valor=valor, extrato=extrato)
                
            case 's':
                saldo, extrato, numero_saques = funcao_saque(saldo = saldo, valor = valor, extrato= extrato, limite= limite, numero_saques= numero_saques, LIMITE_SAQUES= LIMITE_SAQUES)
                
            case 'e':
                extrato = funcao_extrato(extrato= extrato, saldo = saldo)
                
                
            case "nu": 
                funcao_usuario(usuarios)
            
            case "nc": 
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)
            
            case "lc": 
                listar_contas(contas)
                
            case 'q':
                
                break
            case _ :
                print("Operação inválida, por favor selecione novamente a operação desejada.")

main()