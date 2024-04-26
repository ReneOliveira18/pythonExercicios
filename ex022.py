#Crie um programa que leia o nome completo
#de uma pessoa e mostre:

nome = str(input('Digite seu nome completo: '))

#nome com todas as letras maiusculas
print('Seu nome em letras maiúsculas é {}' .format(nome.upper()))

#nome com todas as letras minusculas
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))

#quantas letras ao total sem considerar os espaços
nome0 = len(nome.replace(" ", ""))
print('Seu nome tem {} letras ao total.'.format(nome0))

#quantas letras tem seu primeiro nome:
nome1 = nome.split()
nome2 = len(nome1[0])
print('Seu primeiro nome tem {} letras'.format(nome2))

