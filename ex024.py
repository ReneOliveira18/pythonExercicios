#crie um programa que leia o nome de uma cidade
#e diga se ela começa ou não com a palavra "Santo"

cidade = str(input('Digite o nome da sua cidade: ')).strip() #strip tirar os caracteres de espaço antes e depois da frase
print(cidade[:5].lower() == 'santo')



