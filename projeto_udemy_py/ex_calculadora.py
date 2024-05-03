while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um número: ')
    operador = input('Digite o operador (+-*/): ')

    numeros_validos = None
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Operador inválido.')
        continue
    resultado = 0
    if operador == '+':
        resultado = numero_1 + numero_2
        print(f'{resultado}')
    elif operador == '-':
        resultado = numero_1 - numero_2
        print(f'{resultado}')
    elif operador == '*':    
        resultado = numero_1 * numero_2
        print(f'{resultado}')
    elif operador == '/':
        resultado = numero_1 / numero_2
        print(f'{resultado}')
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Você quer [s]air?').lower().startswith('s')

    if sair is True:
        break
