'''
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador Perder, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
from time import sleep
print('=-=' * 7)
print('Vamos jogar Par ou Ímpar.')

s = c = 0
while True:
    computer = randint(0, 10)
    print('=-=' * 7)
    opcao = str(input('Digite P para Par e I para Ímpar. [P/I] ')).upper().strip()[0]
    num = int(input('Digite um número. '))
    print('=-=' * 7)
    print('PAR OU ÍMPAR...')
    sleep(0.5)
    s = num + computer
    par = s % 2
    if opcao == 'P':
        if par == 0:
            print(f'Você VENCEU!! Você jogou {num} e o PC jogou {computer}. Total {s} .')
            c += 1
        else:
            print(f'Você PERDEU!! Você jogou {num} e o PC jogou {computer}. Total {s} .')
            break
        print('Vamos jogar de novo.')

    if opcao == 'I':
        if par == 0:
            print(f'Você PERDEU!! Você jogou {num} e o PC jogou {computer}. Total {s} .')
            break
        else:
            print(f'Você VENCEU!! Você jogou {num} e o PC jogou {computer}. Total {s} .')
            c += 1
        print('Vamos jogar de novo.')
print(f' \nVocê ganhou {c} vez(es)!!')
print('=-=-FIM-=-=')
print('=-=' * 7)

