import os
lista = []
while True:
    print('Selecione uma opção:')
    comando = input('[i]nserir, [a]pagar, [l]istar ou [f]echar: ')
    if len(lista) == 0 and comando == 'l':
        print('Nada para listar')
        os.system('cls')
    elif comando == 'a':
        os.system('cls')
        escolha_do_indice = int(input('Escolha o indice para apagar: '))
        if len(lista) == 0 or escolha_do_indice > len(lista)-1:
            print('Não foi possível apagar esse índice.')
        else:
            del lista[escolha_do_indice]
    elif comando == 'i':
        os.system('cls')
        valor_inserir = input('Digite o que você quer inserir na lista: ')
        lista.append(valor_inserir)
    elif comando == 'l':
        os.system('cls')
        for indice, nome in enumerate(lista):
            print(indice, nome)
    elif comando == 'f':
        os.system('cls')
        for item in lista:
            print(item, end= ' ')
        break
    else:
        print('Por favor escolha uma das opções inserir, apagar, listar ou fechar')
