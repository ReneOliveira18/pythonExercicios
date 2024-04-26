#usuario escolho um nº no qual ele deseja saber a tabuada
print('=--='*9)
print('Bem vindo a calculadora de tabuada:')

num = int(input('Digite o número no qual você deseja saber a tabuada: '))

tabuada = 0

for c in range(0,11):
    tabuada = num * c
    print('{:2} x {:2} = {}'.format(c, num, tabuada))
print('=--='*6)