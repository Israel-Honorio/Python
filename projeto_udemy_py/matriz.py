
numero = input()
numero = int(numero)
print(numero, end = ' ')

while numero != 1:

    if numero%2==0:

        numero = numero // 2
        print(numero, end = ' ')
    else:

        numero = (numero*3) + 1
        print(numero, end = ' ')