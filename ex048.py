#Calcule a soma entre todos os números impares que são multiplos
#de 3 e que se encontram no intervalo 1 até 500

print('=--='*6)
soma = 0
cont = 0

for c in range(1,501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {}nºs multiplos de 3 entre 1 a 500 é = {}'.format(cont,soma))
print('=--='*6)