import random

class ContaBancaria:
    
    valor_total_banco = 0
    
    def __init__(self, titular, numero_conta, saldo, senha):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.senha = senha
        ContaBancaria.valor_total_banco += saldo
        
    @staticmethod
    def abrir_conta(cpf):
        cpf = cpf.replace(".", "").replace("-", "")
        if len(cpf) != 11 or not cpf.isdigit():
            return False

        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[9]):
            return False

        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[10]):
            return False

        return True

    def depositar(self, valor):
        self.saldo += valor
        ContaBancaria.valor_total_banco += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}')

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            ContaBancaria.valor_total_banco -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}')

    def transferir(self, valor, conta_destino):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            ContaBancaria.valor_total_banco == valor
            print(f'Transferência de R${valor:.2f} realizada com sucesso. Saldo atual: R${self.saldo:.2f}')


contas = []
conta_atual = None


while True:
    print('\n=== Banco da Indústria ===')
    print('1. Criar nova conta')
    print('2. Fazer login')
    print('0. Sair do sistema')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        cpf = input('Digite o CPF do titular da conta: ')
        if not ContaBancaria.abrir_conta(cpf):
            print('CPF inválido. Tente novamente.')
            continue
        numero = ''
        while not numero or any(conta.numero_conta == numero for conta in contas):
            numero = ''.join(random.choices('0123456789', k=6))
        while True:
            nome = input("Cadastre seu nome: ")
            if nome.strip():
                if all(c.isalpha() for c in nome):
                    break
                else:
                    print("Somente letras!")
            else:
                print("Nome não pode ser vazio!")

        while True:
            senha = input("Cadastre sua senha: ")
            if senha.strip():
                if all(c.isnumeric() for c in senha):
                    break
                else:
                    print("Somente números!")
            else:
                print("Senha não pode ser vazia!")
        while True:
            saldo_str = input('Digite o saldo inicial: ')
            if saldo_str.isdigit():
                try:
                    saldo = float(saldo_str)
                    break
                except ValueError:
                    print('Valor inválido. Digite apenas números.')
            else:
                print('Valor inválido. Digite apenas números.')
        conta_atual = ContaBancaria(nome, numero, saldo, senha)
        contas.append(conta_atual)
        print(f'Conta criada com sucesso {conta_atual.titular}! Anote o Número da sua conta: {numero}')
        print('Quantidade total do Banco da Indústria: R$',ContaBancaria.valor_total_banco)

    elif opcao == '2':
        while True:
            numero = input('Digite o número da conta: ')
            senha = input('Digite a senha da conta: ')
            if numero.strip() and senha.strip():
                if all(c.isnumeric() for c in senha):
                    break
                else:
                    print("Somente números!")
            else:
                print("Número da conta ou senha não pode ser vazia!")
        encontrada = False
        for conta in contas:
            if conta.numero_conta == numero and conta.senha == senha:
                conta_atual = conta
                encontrada = True
                break
        if encontrada:
            print(f'Bem vindo(a) de volta {conta_atual.titular}...')
        else:
            print('Conta ou senha incorretos.')

    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Tente novamente')
    while True:
        if not conta_atual:
            break

        print(f'\n=== Conta {conta_atual.numero_conta} ===')
        print('1. Verificar saldo')
        print('2. Depositar')
        print('3. Sacar')
        print('4. Transferir')
        print('5. Sair da conta')

        opcao_conta = input('Digite uma opção: ')
        if opcao_conta == '1':
            print(f'Saldo atual: R${conta_atual.saldo:.2f}')
            print('Quantidade total do Banco da Indústria: R$',ContaBancaria.valor_total_banco)
        elif opcao_conta == '2':
            while True:
                valor_str = input('Digite o valor a ser depositado: ')
                if valor_str.isdigit():
                    try:
                        valor = float(valor_str)
                        break
                    except ValueError:
                        print('Valor inválido. Digite apenas números.')
                else:
                    print('Valor inválido. Digite apenas números.')
            conta_atual.depositar(valor)
            print('Quantidade total do Banco da Indústria: R$',ContaBancaria.valor_total_banco)

        elif opcao_conta == '3':
            while True:
                valor_str = input('Digite o valor a ser sacado: ')
                if valor_str.isdigit():
                    try:
                        valor = float(valor_str)
                        break
                    except ValueError:
                        print('Valor inválido. Digite apenas números.')
                else:
                    print('Valor inválido. Digite apenas números.')
            conta_atual.sacar(valor)
            print('Quantidade total do Banco da Indústria: R$',ContaBancaria.valor_total_banco)

        elif opcao_conta == '4':
            while True:
                valor_str = input('Digite o valor a ser transferido: ')
                if valor_str.isdigit():
                    try:
                        valor = float(valor_str)
                        break
                    except ValueError:
                        print('Valor inválido. Digite apenas números.')
                else:
                    print('Valor inválido. Digite apenas números.')
            while True:
                numero_destino = input('Digite o número da conta de destino: ')
                if numero_destino.strip():
                    encontrada = False
                    for conta in contas:
                        if conta.numero_conta == numero_destino:
                            conta_destino = conta
                            encontrada = True
                            break
                    if encontrada:
                        conta_atual.transferir(valor, conta_destino)
                        print('Quantidade total do Banco da Indústria: R$',ContaBancaria.valor_total_banco)
                        break
                    else:
                        print('Conta de destino não encontrada.')
                        break
                else:
                    print("A conta não pode ser vazia!")

        elif opcao_conta == '5':
            print(f'Saindo da conta {conta_atual.titular}...')
            conta_atual = None
            break

        else:
            print('Opção inválida. Tente novamente.')