'''
Pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km
para viagem de até 200km e R$0,45 para viagens maiores
'''
km = float(input('Você deseja viajar por quantos Km?'))

if km <= 200:
    preco = (km * 0.50)
    print('O valor da sua passagem é R${:.2f},pois você viajará {}km'.format(preco, km))
else:
    preco = (km * 0.45)
    print('Você vai fazer uma viagem de {}km, sua passagem vai custar R${:.2f}'.format(km, preco))

print('Boa viagem!')