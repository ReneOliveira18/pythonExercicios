'''
Leia dois valores e mostre um menu na tela
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair
Seu programa deverá realizar a operação solicitada
em cada caso
'''
print('=-='*7)
print('Vamos Calcular...\n')

while True:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))

    opcao = int(input('[1] SOMAR \n'
                      '[2] MULTIPLICAR \n'
                      '[3] MAIOR \n'
                      '[4] NOVOS NÚMEROS \n'
                      '[5] SAIR \n'
                      'Escolhar uma opção: '))
    if opcao == 1:
        print('Seu calculo foi a soma entre {} + {} = {}'.format(num1, num2, (num1 + num2)))

    if opcao == 2:
        print('Seu calculo foi a multiplicação de {} x {} = {}'.format(num1, num2, (num1 * num2)))

    if opcao == 3:
        maior = num1
        if num2 > maior:
            print('O {} é maior que {}'.format(num2, num1))
        else:
            print('O {} é maior que {}'.format(num1, num1))

    if opcao == 4:
        print('Digite novos números...')

    if opcao == 5:
        print('Saindo...')
        break
    print('=-=' * 7)
print('Obrigado por usar nosso programa.\n')
print('=-='*7)

