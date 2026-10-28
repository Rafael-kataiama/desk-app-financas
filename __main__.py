from conta_bancaria import Conta_bancaria


def main(): # entrada dos usuarios:

    print('== sistema finaceiro pessoal ==')
    usuario = input('Digite o nome do usuario: ')
    numero_conta = input('Digite o numero da conta: ')
    conta_usuario = Conta_bancaria(usuario, numero_conta)

    while True:
        
        print(f'\nUsuario: {conta_usuario._usuario}, Numero da conta: {conta_usuario._numero_conta}, saldo: {conta_usuario._saldo}')
        print(f'\n1. Adicionar receita\n2. Adicionar despesa\n3. Ver transacoes\n4. Sair\n')

        opcao = input('Digite a opcao desejada: ')

        if opcao == '1':
            descricao = input('Digite a descricao da receita: ')
            
            try:
                valor = float(input('Digite o valor da receita: '))
            
            except ValueError:
                
                print('Valor invalido, tente novamente!')
                continue
            
            categoria = input('Digite a categoria da receita: ')
            conta_usuario.processar_receitas(descricao, valor, categoria)

        elif opcao == '2':
            descricao = input('Digite a descricao da despesa: ')
            
            try:
                valor = float(input('Digite o valor da despesa: '))
            
            except ValueError:
                print('Valor invalido, tente novamente!')
                continue
            
            categoria = input('Digite a categoria da despesa: ')
            conta_usuario.processar_despesas(descricao, valor, categoria)

        elif opcao == '3':
            conta_usuario.imprimir_transacoes()

        elif opcao == '4':
            print('Operação finalizada')
            break
        
        else:
            print('Opcao invalida, tente novamente!')


if __name__ == "__main__":
    
    main()

