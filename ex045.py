#Faça o pc jogar Jokenpô com vc
from random import randint
from time import sleep

print('"-" ' * 9)
print('Bem vindo ao nosso mini game\n'
      '=== JOKENPÔ ===')

opcao = int(input('Escolha sua opção:\n'
                  '0 - Pedra \n'
                  '1 - Papel \n'
                  '2 - Tesoura \n'
                  'Sua opção: '))

jogadas = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)

print('=~= ' * 9)
print('\nJogador jogou {}'.format(jogadas[opcao]))
print('Computador jogou {}\n'.format(jogadas[computer]))
print('=~= ' * 9)

if computer == 0: #pc jogou pedra
      if opcao == 0:
            print('Jogada terminou em EMPATE!')
      elif opcao == 1:
            print('Jogador VENCEU!')
      elif opcao == 2:
            print('Computador VENCEU!')
      else:
            print('ERROR...')

elif computer == 1: #pc jogou papel
      if opcao == 0:
            print('Computador VENCEU!')
      elif opcao == 1:
            print('Jogada EMPATADA.')
      elif opcao == 2:
            print('Jogador VENCEU!')
      else:
            print('ERROR...')

elif computer == 2: # pc jogou tesoura
      if opcao == 0:
            print('Jogador VENCEU!')
      elif opcao == 1:
            print('Computador VENCEU!')
      elif opcao == 2:
            print('Jogada EMPATADA')
      else:
            print('ERROR...')

print('"-" ' * 9)