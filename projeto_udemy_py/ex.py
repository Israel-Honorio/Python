'''nome = input()
altura = float(input())
peso = int(input())
imc = peso / altura**2
print(f'{imc:.2f}')'''

'''numero = input('Digite um número inteiro: ')
if numero.isdigit():
    numero = int(numero)
    if numero % 2 ==0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
else:
    print(f'{numero} não é um número inteiro.')'''

'''n = int(input('numero'))
lista = []
lista2 = []


for i in range(n):
    pascal = 11**i
    lista2.append(pascal)
    lista.append(lista2)

print(lista)'''
'''n = int(input('numero'))
lista = []

for i in range(n):
    lista2 = []  # Criar uma nova lista vazia em cada iteração
    for j in range(i + 1):
        if j == 0 or j == i:
            lista2.append(1)
        else:
            # O valor em cada posição é a soma dos dois valores acima na linha anterior
            lista2.append(lista[i - 1][j - 1] + lista[i - 1][j])
    lista.append(lista2)

print(lista)'''

nome = input('digite um nome ')
tam = len(nome)
indice = 0
novo_nome = ''
while indice < tam:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1
novo_nome += '*'
print(novo_nome)




