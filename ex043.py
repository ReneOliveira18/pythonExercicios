# cauclo do IMC

print('"-" ' * 7)
print('Bem vindo a calculadora do IMC, descubra qual seu Indice de Massa Corporal\n')
print(('Separe sua altura e seu peso com o caractere de ponto.\n'))

altura = float(input('Digite qual a sua altura em metros: '))
peso = float(input('Digite quantos Kg você pessa: '))

imc = (peso)/(altura**2)

if imc <= 18.5:
    print('Seu IMC é {:.2f}, você está ABAIXO do seu peso ideal. Procure um médico.\n'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f}, você está no PESO ideal. \n'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}, você está com SOBREPESO. Cuide-se.\n'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f}, você está OBESO. Procure um médico.\n'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}, você está com OBESIDADE MÓRBIDA. Procure um Médico URGENTE!\n'.format(imc))
else:
    print('ERROR..\n')

print('Obrigado por usar nossa calculadora. Esperamos ter te ajudado.')
print('"-" ' * 7)