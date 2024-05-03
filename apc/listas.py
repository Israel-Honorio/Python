
'''lista_numeros = list(map(int,input().split( )))
counter = lista_numeros[0]
for i in range(1,len(lista_numeros)):
    counter *= 2
    counter += lista_numeros[i] / 2
print(f'{counter:.2f}')'''
    
def numero(frase):
    telefones = []

    for i in range(len(frase)):
        if frase[i] == "-":
            telefone = frase[i-9:i]
            if len(telefone) >= 9 and telefone[-1].isdigit() and telefone.count('-') == 1:
                telefones.append(telefone)

    if len(telefones) == 1:
        print("Telefone:", telefones[0])
    elif len(telefones) >= 2:
        print("Telefones:", ", ".join(telefones))

frase = input()
numero(frase)