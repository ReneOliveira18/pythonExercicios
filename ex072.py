'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de 0 até 20
Seu programa deverá ler um número pelo telcado(entre 0 e 20) e
mostrá-lo por extenso.
'''

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Número inválido, tente novamente. ', end='')
print(f'Você digitou {contagem[num]}')