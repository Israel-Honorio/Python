import random


nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

cpf = nove_digitos
numeros_cpf = ''
# checando se possui outros caracteres que não sejam numeros
for i in cpf:
    if i.isdigit():
        numeros_cpf += i
        numeros_cpf = numeros_cpf[0:9]
#checando se todos os caracteres são iguais, exemplo: "111.111.111-11"
tam_cpf = len(numeros_cpf)
if cpf[0]*tam_cpf == numeros_cpf:
    print('CPF inválido')
else:

    #código para checar o primeiro digito após o "-"
    resultado = []
    multiplicacao = 10
    for i in numeros_cpf:
        numeros = int(i)
        conta = numeros*multiplicacao
        multiplicacao -= 1
        resultado.append(conta)
    soma = 0
    for item in resultado:
        soma += item
    soma *= 10
    soma = (soma% 11)
    digito = 0
    if soma > 9:
        digito = 0
    else:
        digito = soma

#código para checar o segundo dígito após o "-"
    numeros_cpf += str(digito)

    resultado = []
    multiplicacao = 11
    for i in numeros_cpf:
        numeros = int(i)
        conta = numeros * multiplicacao
        multiplicacao -= 1
        resultado.append(conta)
    soma = 0
    for item in resultado:
        soma += item
    soma *= 10
    soma = (soma % 11)
    digito_2 = 0
    if soma > 9:
        digito_2 = 0
    else:
        digito_2 = soma
#soma o digito 2 aos numeros do cpf, gerando assim um novo cpf
    numeros_cpf += str(digito_2)
    print(numeros_cpf)
#checando se o cpf é válido
    if numeros_cpf[-2:] == str(digito) + str(digito_2):
        print('CPF válido')
    else:
        print('CPF inválido')

# caso teste 746.824.890-70