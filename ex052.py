print('=--='*9)
print('Descobrindo se o número é PRIMO.\n')
n = int(input('Digite um número: '))
primo = 0

for c in range(2,n):
    if (n % c == 0):
        print('Multiplo de',c)
        primo += 1
if (primo == 0):
    print('{} é número primo.'.format(n))
else:
    print('Tem {} multiplos. Não é primo.'.format(primo))

