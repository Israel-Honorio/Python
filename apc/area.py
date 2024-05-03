def area(frase):
    if 'm2' not in frase and 'metros' not in frase:
        print(f'Area: nao informado')
    else:
        frase = frase.split()
        for i in range(len(frase)):
            if frase[i].isdigit() and ('m2'in frase[i+1] or 'metros' in frase[i+1]):
                area = frase[i]
                print(f'Area: {area}')
frase = input()
area(frase)