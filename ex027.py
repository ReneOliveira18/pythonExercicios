#leia o nome compeleto de uma pessoa, mostrando
#em seguida o primeiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip().lower()
#dividir nome em lista
n = nome.split()

print('Prazer em te conhecer {}.'.format(nome).title())
print('Seu primeiro nome é {}'.format(n[0].capitalize()))
print('Seu ultimo nome é {}'.format(n[len(n)-1].capitalize()))
