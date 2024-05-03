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
        print("Endereco:",endereco[:-1])
    else:
        return None

frase = input()
endereco(frase)
