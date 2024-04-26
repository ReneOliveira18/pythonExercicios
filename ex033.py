'''
Leia 3 numeros e mostre qual o maior e qual o menor
'''
n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))
'''
if (n1>n2 and n1>n3) and (n2<n3):
    print('O maior numero é {} e o menor é {}'.format(n1,n2))
elif (n1>n2 and n1>n3) and (n3<n2):
    print('O maior numero é {} e o menor é {}'.format(n1,n3))
elif (n2>n1 and n2>n3) and (n1<n3):
    print('O maior numero é {} e o menor é {}'.format(n2,n1))
elif (n2>n1 and n2>n3) and (n3<n1):
    print('O maior numero é {} e o menor é {}'.format(n2,n3))
elif (n3>n1 and n3>n2) and (n1<n2):
    print('O maior numero é {} e o menor é {}'.format(n3,n1))
elif (n3>n2 and n3>n1) and (n2<n1):
    print('O maior numero é {} e o menor é {}'.format(n3,n1))
'''
#guanabara
#verificando menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
