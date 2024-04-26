'''Refaça o ex062 com que o usuário escolha a
quantidades de termos da PA
'''
print('=--='*9)
print('Bem vindo a calculadora de Progressão Aritimética\n')

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 0
termo = int(input('Quantos termos deseja que sua PA possua: '))#questiona o usuario quantos termos a PA deve possuir
x = 0 #variavel de controle
while termo != 0:
    x += termo

    while cont < x:
        print('{} '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('\n')
    termo = int(input('Deseja adicionar mais termos a sua PA? '))
print('')
print('PA teve {} termos exibidos.'.format(x))
print('--FIM--')
print('=--='*9)
