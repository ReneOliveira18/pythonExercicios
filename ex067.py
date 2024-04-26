print('=-='*7)
print('Vamos calcular a Tabuada...\n'
      'Digite um número negativo (-1) se desejar sair.')
print('=-='*7)
num = c = 0
while True:
    num = int(input('Digite o número no qual você deseja saber a tabuada: '))
    if num >= 0:
        print('=-=' * 7)
        for c in range(0, 11):
            tabuada = num * c
            print(f'{c:2} x {num:2} = {tabuada}')
        print('=-=' * 7)
    elif num < 0:
        break
    else:
        break
print('=-='*7)
print('=-=-FIM-=-=')