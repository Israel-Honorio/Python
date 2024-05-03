def valor(frase):
    num = '123456789'
    if 'R$' not in frase and 'reais' not in frase:
        print(f'Valor: nao informado')
    else: 
        frase = frase.split()
        for i in frase:
            if 'R$' in i:
                if i[2] in num:
                    if i[-1] == '.' or i[-1] == ',':
                        print(f'Valor:{i[2:-1]}')
                    else:
                        print(f'Valor:{i[2:]}')
        for j in range(len(frase)):
            if frase[j][0] in num and 'reais' in frase[j + 1]:
                print(f'valor: {frase[j]}')

valor(frase)