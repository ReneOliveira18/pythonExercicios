'''
Crie um programa que tenha uma tupla com palavras (não usar acentos)
Depois disso, você deve mostrar, para cada palavra, quais são as suas
vogais.
'''
print('=-=' * 13)

tupla = ('Rene', 'Aline', 'Beatriz', 'Alan', 'Chico', 'Jah', 'Jesus', 'Sananda')

for palavra in tupla:
    print(f'\nNo nome {palavra} temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='')

print('\n')
print('=-=' * 13)