usuarios_filmes = {}
lista_filmes = []


while True:

   

    while True:
        try:
            operacao = int(input('----MENU----\n\n1- Adicionar Filme\n2- Remover Film\n3- Ver filmes de um usuário\n4- Ver todos os usuários\n0- Sair\nDigite qual operação gostaria de executar?: '))
            break
        except ValueError:
            print('\nDIGITE UM NÚMERO VÁLIDO\n')

    match operacao:
        case 0:
            break
        case 1:
            while True:
                try:
                    nome= input('\nDigite o nome do usuário: ').title()      
                    if not nome.isalpha():#tratamento de excessão para verificar se a entrada de dados é alfabética
                            raise ValueError('Digite uma resposta válida')
                    break
                except ValueError as e:
                    print(e)
            while True:
                try:
                    filme= input('\nDigite o nome do filme: ').title()      
                    if not filme.isalpha():#tratamento de excessão para verificar se a entrada de dados é alfabética
                            raise ValueError('Digite uma resposta válida')
                    break
                except ValueError as e:
                    print(e)
            lista_filmes.append(filme)
            usuarios_filmes [nome]= lista_filmes
            print('Filme adicionado com sucesso')
                

        case 2:
            while True:
                try:
                    nome= input('\nDigite o nome do usuário: ').title()      
                    if not nome.isalpha():#tratamento de excessão para verificar se a entrada de dados é alfabética
                            raise ValueError('Digite uma resposta válida')
                    break
                except ValueError as e:
                    print(e)
            while True:
                try:
                    filme= input('\nDigite o nome do filme: ').title()      
                    if not filme.isalpha():#tratamento de excessão para verificar se a entrada de dados é alfabética
                            raise ValueError('Digite uma resposta válida')
                    break
                except ValueError as e:
                    print(e)
            lista_filmes.remove(filme)
            usuarios_filmes [nome]= lista_filmes
            print('Filme removido com sucesso')
            
        case 3:
            while True:
                try:
                    nome= input('\nDigite o nome do usuário: ').title()      
                    if not nome.isalpha():#tratamento de excessão para verificar se a entrada de dados é alfabética
                            raise ValueError('Digite uma resposta válida')
                    break
                except ValueError as e:
                    print(e)

            op=usuarios_filmes.get(nome,'\nEsse usuário não existe')
            if op != 'Esse usuário não existe': 
                print(f'Filmes assistidos: {op}')
           
         
        case 4:
            print(usuarios_filmes.items())
        case _:
            print('Opção inválida')
