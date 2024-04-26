#Leia uma frase qualquer e diga se ela é um palíndromo
#desconsidera os espaços
print('=--='*9)
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
tudojunto = ''.join(palavras)
aocontrario = ''

for letras in range(len(tudojunto) -1, -1, -1):
    aocontrario += tudojunto[letras]
print('A frase invertida de {} é {}'.format(tudojunto, aocontrario))
if aocontrario == tudojunto:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não forma um palíndromo!')

print('=--='*9)
