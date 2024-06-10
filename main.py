def Exibir_painel():
    print('1 Cadastro de produto')
    print('2 Cadastro de departamento')
    print('3 Exibir produto e departamento')
    print('4 Sair do programa')
    opcao_escolhida = int(input('Qual opção deseja escolher ?  '))
    if opcao_escolhida == 1:
        produto_cadastrado = input('Escolha o nome do produto  ')
    elif opcao_escolhida == 2:
        produto_cadastrado = input('Escolha o nome do departamento  ')
               
        
Exibir_painel()
