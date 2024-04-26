print('~=~'*7)
print('Bem ao comparador numerico.')
n1 = float(input('Digite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))

if n1 > n2:
    print('{:.2f} é maior que {:.2f}'.format(n1,n2))
elif n2 > n1:
    print('{:.2f} é maior que {:.2f}'.format(n2,n1))
else:
    print('{:.2f} é igual a {:.2f}'.format(n1,n2))

print('Obrigado por usar nosso comparador numérico.')
print('~=~'*7)