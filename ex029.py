'''
Escreva um programa que leia a velocidade de um carro.
Se o carro ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.
a multa vai custar R$07.00 por cada km acima do limite.
'''
vel = float(input('Digite a velocidade que o carro passou pelo radar: '))

if vel > 80:
    limvel = (vel - 80)
    multa = (vel - 80) * 7
    print('Excedeu o limite de velocidade em {}km/h, foi multado em R${:.2F} '.format(limvel, multa))

print('=== FIM ===')
