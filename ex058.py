'''
Melhore o jogo do Ex 28 onde o pc vai pensar em um nº entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários até vencer
'''

from random import randint
from time import sleep
print('=-='*7)
print('Vamos brincar de adivinhação,\n'
      'Vamos ver se você consegue adivinhar o número que estou pensando...\n')
cont = 0
sorteio = randint(0,10)
while True:
    cont += 1
    num = int(input('Digite um número entre 0 e 10: '))
    print('Vamos ver se você acertou o numero que eu estava pensando...')
    sleep(0.5)
    if num == sorteio:
        print('Uauuu, o número que pensei foi {} igual o seu.!'.format(sorteio))
        break
    else:
        print('Erroooooou.'.format(sorteio))
        if num > sorteio:
            print('Estou pensando em um numéro menor, tente novamente.')
        elif num < sorteio:
            print('Estou pensando em um numéro maior, tente novamente.')

print('Você precisou de {} tentativar para ganhar'.format(cont))
print('=-='*7)
