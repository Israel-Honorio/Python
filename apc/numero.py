
frase = input()
def numero(frase):
    telefones = []

    for i in range(len(frase)):
        if frase[i] == "-":
            telefone = frase[i-5:i+5].strip()
            if len(telefone) >= 9 and telefone[-1].isdigit():
                telefones.append(telefone)

    if len(telefones) == 1:
        print("telefone:", telefones[0])
    elif len(telefones) >= 2:
        print("telefones:", ", ".join(telefones))
numero(frase)