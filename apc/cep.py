def eh_cep(frase):
    cep = ''
    frase = frase.split()
    for i in frase:
        if '-' in i:
            if i[i.index('-')+1].isdigit():
                tam = len(i.strip('.').strip(','))
                if (tam - i.index('-')-1) == 3:
                    cep = i.strip('.').strip(',')
                    print(f'CEP:{cep}')
                    return
    print('CEP: nao informado')
frase = input()
eh_cep(frase)
