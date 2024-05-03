def responsavel(frase):
    palavras = ''
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
    print(pessoa)
frase = input()
responsavel(frase)
