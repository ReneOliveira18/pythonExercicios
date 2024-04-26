
print('=~'*20)
print(('Bem vindo a calculadora de conversão.'))

num = int(input('Digite um numero inteiro: '))
print(('Escolha uma opção de calculo'))
selecao = int(input('1 - para calculo Bináro\n'
                    '2 - para calculo Octal\n'
                    '3 - para calculo Hexadecimal\n'
                    '4 - para Sair \n'
                    'Sua opção: '))
if selecao == 1:
        print('{} em Binário é: {}'.format(num,bin(num)[2:]))#[2:] para cortar o incio da resposta
elif selecao == 2:
    octal = oct(num)[2:]
    print('{} em Octal é: {}'.format(num,octal))
elif selecao == 3:
    hexadecimal = hex(num)[2:]
    print('{} em Hexadecimal é: {}'.format(num, hexadecimal))
elif selecao == 4:
    print('Saindo...')
else:
    print('Comando inválido.')
print('Obrigado por usar nossa calculadora.')
print('=~'*20)
