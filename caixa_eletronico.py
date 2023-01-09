import getpass
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    '''     OU
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')'''

'''outraop = ''
def outra_op():
    outraop = input('\nDESEJA REALIZAR OUTRA OPERAÇÃO?\nS/N:')'''

def continuar():
    input('aperte <ENTER> para continuar...')

def cria_conta(nome,senha,saldo,admin):
    conta_nova = {
        'nome':nome,
        'senha':senha,
        'saldo': saldo,
        'admin': admin
    }
    qtd_contas=0
    for x in lista_contas:
        qtd_contas+=1
    conta = '0'+str(qtd_contas+1)
    lista_contas[conta] = conta_nova


lista_contas = {
    '01': {
        'nome':'user1',
        'senha':'111',
        'saldo': 1000,
        'admin': False,
    },
    '02': {
        'nome':'user2',
        'senha':'222',
        'saldo': 2000,
        'admin': False,
    },
    '03': {
        'nome':'Adriano',
        'senha':'333',
        'saldo': 3000,
        'admin': True,
    }
}

cedulas_maquina = {
    '10':10,
    '20':10,
    '50':10,
    '100':10,
}

while True:
    print("*************************************")
    print("********* CAIXA  ELETRÔNICO *********")
    print("*************************************")

    operacao = '0'
    numconta = input('Número da conta: ')
    saldo_int = int(lista_contas[numconta]['saldo'])


    if numconta in lista_contas:
        numsenha = getpass.getpass('Senha: ')
        if numsenha == lista_contas[numconta]['senha']:
            
            limpar_terminal()
            while operacao != '4':
                print('\n-------Bem vindo(a) %s-------' % lista_contas[numconta]['nome'])
                print('\n-------ESCOLHA UMA OPERAÇÃO:-------\n\n1 - EXIBIR SALDO \n\n2 - SAQUE \n\n3 - EXIBIR NOME \n\n4 - SAIR \n\n5 - ALTERAR SENHA')
                if lista_contas[numconta]['admin'] == True:
                    print('\n6 - EXIBIR CÉDULAS DO CAIXA  \n\n7 - INCLUIR CÉDULAS \n\n8 - CRIAR NOVA CONTA\n')
                operacao = input('INFORME A OPERAÇÃO: ')
                if operacao == '1':
                    limpar_terminal()
                    #print('SALDO: R$ %s' % lista_contas[numconta]['saldo'])
                    print('SALDO: R$ %d' % saldo_int)

                    continuar()
                    limpar_terminal()
                elif operacao == '2':
                    limpar_terminal()
                    valor_saque = input('Valor do saque: ')
                    

                    cedulas_maquina_saque = {} 
                    valor_saque_int = int(valor_saque)
                    reduzir_saldo = valor_saque_int
                    #saldo_conta = {}
                    saldo_int = int(lista_contas[numconta]['saldo'])
                    if valor_saque_int > 0 and valor_saque_int <= saldo_int:

                        if valor_saque_int // 100 > 0 and valor_saque_int // 100 <= cedulas_maquina['100']:
                            cedulas_maquina_saque['100'] = valor_saque_int // 100
                            valor_saque_int = valor_saque_int - valor_saque_int // 100 * 100
                        
                        if valor_saque_int // 50 > 0 and valor_saque_int // 50 <= cedulas_maquina['50']:
                            cedulas_maquina_saque['50'] = valor_saque_int // 50
                            valor_saque_int = valor_saque_int - valor_saque_int // 50 * 50

                        if valor_saque_int // 20 > 0 and valor_saque_int // 20 <= cedulas_maquina['20']:
                            cedulas_maquina_saque['20'] = valor_saque_int // 20
                            valor_saque_int = valor_saque_int - valor_saque_int // 20 * 20

                        if valor_saque_int // 10 > 0 and valor_saque_int // 10 <= cedulas_maquina['10']:
                            cedulas_maquina_saque['10'] = valor_saque_int // 10
                            valor_saque_int = valor_saque_int - valor_saque_int // 10 * 10

                        if valor_saque_int != 0:
                            print('Sem cédulas para este valor, tente um valor menor!')
                        else:
                            for valor_ced in cedulas_maquina_saque:
                                cedulas_maquina[valor_ced] -= cedulas_maquina_saque[valor_ced]
                            saldo_int = saldo_int - reduzir_saldo
                            lista_contas[numconta]['saldo'] = saldo_int
                            
                            print('Retire o dinheiro:')
                            print(cedulas_maquina_saque)
                    elif valor_saque_int <= 0:
                        print('Valor não aceito.')

                    else:
                        print('Saldo insuficiente.')
                    continuar()
                    limpar_terminal()
                elif operacao == '3':
                    limpar_terminal()
                    print('SENHA: %s' % lista_contas[numconta]['nome'])

                    continuar()
                    limpar_terminal()
                elif operacao == '4':
                    limpar_terminal()

                elif operacao == '5':
                    limpar_terminal()

                elif operacao == '6' and lista_contas[numconta]['admin'] == True:
                    limpar_terminal()
                    print(cedulas_maquina)

                    continuar()
                    limpar_terminal()
                elif operacao == '7' and lista_contas[numconta]['admin'] == True:
                    limpar_terminal()
                    quantidade_ced = input('QUANTIDADE DE CÉDULAS: ')
                    valor_ced = input('VALOR DA CÉDULA: ')
                    #cedulas_maquina[valor_ced] = cedulas_maquina[valor_ced] + int(quantidade_ced)
                    # OU
                    cedulas_maquina[valor_ced] += int(quantidade_ced)
                    print(cedulas_maquina)

                    continuar()
                    limpar_terminal()
                elif operacao == '8' and lista_contas[numconta]['admin'] == True:
                    limpar_terminal()
                    print('Criando nova conta:')
                    nome_novo = input('informe o nome:')
                    senha_nova = input('Informe a senha:')
                    saldo_novo = int(input('Informe o saldo:'))
                    admin_nova = input('ADMIN?(true/false):')
                    if admin_nova=='true':
                        admin = True
                    else:
                        admin = False
                    cria_conta(nome_novo,senha_nova,saldo_novo,admin_nova)
                    print(lista_contas)

        else:
            limpar_terminal()
            print('SENHA INCORRETA')
    else:
        limpar_terminal()
        print('CONTA INEXISTENTE')


