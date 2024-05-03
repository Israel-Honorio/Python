frase = input()


lista_venda = [
    'Venda','venda','Vendo','vendo','Vender', 'vender'
]
lista_aluguel = [
    'Aluguel','aluguel','alugo','Alugo','alugar','Alugar'
]
for i in lista_aluguel:
    if i in frase:
        print('Modalidade: Aluguel')
        break
for i in lista_venda:
    if i in frase:
        print('Modalidade: Venda')
        break


lista_casa = [
    'Casa', 'casa'
]
lista_apartamento = [
    'Apartamento', 'apartamento'
]
for i in lista_casa:
    if i in frase:
        print('Tipo: Casa')
        break
for i in lista_apartamento:
    if i in frase:
        print('Tipo: Apartamento')
        break

def endereco(frase):
    palavras = frase.split()
    endereco = []
    numero_encontrado = False

    for palavra in palavras:
        if not numero_encontrado:
            if palavra == "Rua" or palavra == "Avenida":
                endereco.append(palavra)
                numero_encontrado = True
        else:
            if any(char.isdigit() for char in palavra):
                endereco.append(palavra)
                break
            else:
                endereco.append(palavra)

    if endereco:
        endereco = " ".join(endereco)
        print("Endereco:",endereco.strip())
    else:
        return None

endereco(frase)


def eh_cep(frase):
    cep = ''
    frase = frase.split()
    for i in frase:
        if '-' in i:
            if i[i.index('-')+1].isdigit():
                tam = len(i.strip('.').strip(','))
                if (tam - i.index('-')-1) == 3:
                    cep = i.strip('.').strip(',')
                    print(f'CEP: {cep}')
                    return
    print('CEP: nao informado')
eh_cep(frase)

def area(frase):
    if 'm2' not in frase and 'metros' not in frase:
        print(f'Area: nao informado')
    else:
        frase = frase.split()
        for i in range(len(frase)):
            if frase[i].isdigit() and ('m2'in frase[i+1] or 'metros' in frase[i+1]):
                area = frase[i]
                print(f'Area: {area}')
area(frase)

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

def numero(frase):
    telefones = []

    for i in range(len(frase)):
        if frase[i] == "-":
            telefone = frase[i-5:i+5].strip()
            if len(telefone) >= 9 and telefone[-1].isdigit() and telefone.count('-') == 1:
                digitos_apos_hifen = telefone.split('-')[1]
                if len(digitos_apos_hifen) == 4:
                    telefones.append(telefone)

    if len(telefones) == 1:
        print("Telefone:", telefones[0])
    elif len(telefones) >= 2:
        print("Telefones:", ", ".join(telefones))

numero(frase)


def responsavel(frase):
    pessoa = ''
    frase = frase.split('. ')
    ultima_frase = frase[-1]
    ultima_frase = list(ultima_frase.split( ))
    
    for i in range(len(ultima_frase)):
        if i == len(ultima_frase)-1:
            if ultima_frase[i-1][0].isupper()and ultima_frase[i][0].isupper():
                pessoa += ultima_frase[i].strip('.').strip(',') +' '
        elif i == 0:
            if ultima_frase [i+1][0].isupper() and  ultima_frase [i][0].isupper():
                pessoa += ultima_frase[i].strip('.').strip(',') +' '
        else:
            if (ultima_frase[i+1][0].isupper() or ultima_frase[i-1][0].isupper()) and ultima_frase[i][0].isupper():
                pessoa += ultima_frase[i].strip('.').strip(',') +' '
    print('Responsavel:',pessoa)
responsavel(frase)

