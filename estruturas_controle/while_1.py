from random import randint
# while True:
#     print('Vai demorar muitoooo')


numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))
