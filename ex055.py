#Leia o peso de cinco pessoas. No final, mostre qual foi o maior
# e o menor peso lidos.
print('=--='*9)

for c in range(1,6):
    peso = float(input('Digite peso(kg) da {}ª pessoa: '.format(c)))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso

print('O maior peso foi de {}kg \n'
      'O menor peso foi de {}kg.'.format(maiorpeso, menorpeso))
print('=--='*9)