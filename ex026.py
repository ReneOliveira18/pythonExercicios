#leia uma frase pelo teclado e mostre:

frase = str(input("Escreva uma frase: ")).strip().lower()

#quantas vezes aparece a letra "A"

#quantas vezes a letra 'a' aparece na frase
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a')))
#qual posição o primeiro 'a' aparece na frase
print('A primeira letra "A" aparece na posição {}.'.format(frase.find('a')+1))
#qual posição o ultimo 'a' aparece na frase
print('A ultima letra "A" aparece na posição {}.'.format(frase.rfind('a')+1))