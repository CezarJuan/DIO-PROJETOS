menu = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair


=>"""
#Variaveis padrões do usuário
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    match opcao:
        #Deposito
        case "d":
            print("Depósito")
            valor_deposito =  float(input("Digite o valor a ser depositado: "))
            if valor_deposito>0:
                saldo += valor_deposito
                extrato += f"\n Depósito no valor de R$ {valor_deposito:.2f}"               
            else:
                print("Valor invalido")
                
        #Saque
        case "s":
            print("Saque")
            if numero_saques< LIMITE_SAQUES:
                valor_saque =  float(input("Digite o valor para sacar: "))
                if valor_saque <=500:
                    if valor_saque<= saldo:
                        numero_saques += 1
                        extrato += f"\n Saque no valor de R$ {valor_saque:.2f}"
                        saldo -= valor_saque
                    else:
                        print(f"Valor de saque maior que o saldo. \nSaldo atual R$ {saldo:.2f}")
                else:
                    print("Valor de saque acima do permitido( R$ 500.00)")
            else:
                print("Limite de saques excedido.") 
            
            
            
        #Extrato
        case "e":
            if not extrato:
                print("Nenhuma movimentção realizada")
            else:
                print("-----------EXTRATO-----------")
                print(extrato)
                print(f"Saldo: R$ {saldo:.2f}")
                print("=============================")
            
        #Opção de sair
        case "q":
            print("Saindo...")
            break
        
        case _:
            print("Opção invalida, Por favor insira uma opção disponivel")