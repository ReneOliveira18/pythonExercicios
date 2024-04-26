print('"-" ' * 9)
print('Bem vindo a calculadora de Produto. \n'
      'Descubra qual o valor final a ser pago com acrescímo ou desconto\n')

opcao = int(input('Esconlha uma opção: \n'
                  '1 - À vista no dinheiro ou pix.\n'
                  '2 - À vista no cartão de crédito.\n'
                  '3 - 2x no cartão de crédito.\n'
                  '4 - 3x ou mais no cartão de crédito.\n'
                  '6 - Sair  :'))

if opcao == 1:
    valor = float(input('Digite o valor do produto R$ '))
    valor = valor - (valor*0.1)
    print('Você escolheu a opção à vista no pix ou dinheiro, \n'
    'ganhou 10% de desconto. Valor a ser pago é R${:.2f}\n'.format(valor))

elif opcao == 2:
    valor = float(input('Digite o valor do produto R$ '))
    valor = valor - (valor*0.05)
    print('Você escolheu a opção à vista no crédito, \n'
          'ganhou 5% de desconto. Valor a ser pago é R${:.2f}\n'.format(valor))

elif opcao == 3:
    valor = float(input('Digite o valor do produto R$ '))
    parcela = (valor/2)
    print('Você escolheu a opção 2x no cartão,\n'
          'o valor do produto é R${:.2f}, pagará 2 parcelas de R${:.2f}\n'.format(valor, parcela))

elif opcao == 4:
    valor = float(input('Digite o valor do produto R$ '))
    vezes = int(input('Digite em quantas vezes você quer fazer: '))
    valor = valor + (valor*0.2)
    parcela = (valor/vezes)
    print('Você escolheu a opção 3x ou mais no cartão, \n'
          'o valor do produto com acréscimo ficou R${:.2f}\n'
          'pagara {} parcelas de R${:.2f}\n'.format(valor,vezes, parcela))

elif opcao == 6:
    print('Saindo...\n')

else:
    print('ERROR..')

print('Obrigado por usar nossa calculadora.\n')
print('"-" ' * 9)