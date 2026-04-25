menu = """

=====================================================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=====================================================

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

def depositar(saldo, valor):
    if valor > 0:
        return saldo + valor
    return saldo

def sacar(saldo, valor_saque, numero_saques, LIMITE_SAQUES, limite):
    if saldo <= 0 or valor_saque > saldo:
        print("Saldo Insuficiente!")
        return saldo, numero_saques, False
    
    elif numero_saques >= LIMITE_SAQUES:
        print("Voce excedeu o número de saques diários!")
        return saldo, numero_saques, False
    
    elif valor_saque > limite:
        print("O limite de saque é R$ 500,00")
        return saldo, numero_saques, False

    else:
        saldo -= valor_saque
        numero_saques += 1
        return saldo, numero_saques, True


while True:
    opcao = input(menu).strip().lower()
    if opcao == "d":
        print("Depósito")
        valor = float(input("Valor a ser depositado: "))
        saldo = depositar(saldo, valor)
        depositos.append(valor)
        print(f"Depósito concluido!\nSeu saldo é de: R$ {saldo:.2f}".replace(".", ","))

    
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Valor a ser sacado: "))
        saldo, numero_saques, sucesso = sacar(saldo, valor_saque, numero_saques, LIMITE_SAQUES, limite)
        if sucesso:
            print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}\nSaques disponíveis: {LIMITE_SAQUES - numero_saques}".replace(".", ","))
            saques.append(valor_saque)
        else:
            print(f"Seu saldo é: {saldo:.2f}".replace(".", ","))

    elif opcao == "e":
        print("Extrato")
        print("Seus Depósitos:")
        if not depositos:
            print("Nenhum depósito realizado.")
        for d in depositos:
            print(f"R$ {d:.2f}".replace(".", ","))

        print("\nSeus Saques:")
        for s in saques:
            print(f"R$ {s:.2f}".replace(".", ","))
        
        print(f"\nSeu saldo atual: R$ {saldo:.2f}".replace(".", ","))
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")