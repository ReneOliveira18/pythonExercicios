#leia o primeiro termo e a razão de uma PA. No final, mostre os 10
#primeiros termos dessa progressão.
print('=--='*9)
print('Bem vindo a calculadora de Progressão Aritimética\n')

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

n = 10

pa = primeiro + ((n-1)*razao)
pa += 1

for c in range (primeiro, pa, razao):
    print(c, end=' ')
print('')
print('--FIM--')
print('=--='*9)