
print('~^'*20)
print('Bem vindo ao programa casa sem juros.')
valorcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = float(input('Digite em quantos anos pretende pagar a casa: '))

mensal = (anos * 12)
prestacao = (valorcasa/mensal) # calculo para saber pretacao mensal da compra
aprovsala = (salario * 0.3) #calculo pra saber se a mensalidade passa na aprovação do salário

if aprovsala >= prestacao:
    print('Parabéns, você está prestes a adquirir sua casa.')
    print('O valor de sua prestação mensal é de R${:.2f}'.format(prestacao))
else:
    print('Que pena, não conseguimos aprovar sua compra.')

print('~^'*20)

