num = input()
num = int(num)
hora = num // 3600
resto = num % 3600
minutos = resto // 60
segundos = resto % 60
print(hora,':',minutos,':',segundos)