#Leia seis numeros inteiros e mostre a soma apenas daqueles
#que forem pares. se o valor digitado for impar, descosidere-o

print('=--='*7)
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('O somatório dos {} números pares é igual a {}'.format(cont, soma))
print('=--='*7)
