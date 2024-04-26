print('-_- '*7)
print('Bem vindo a calculadora de média.')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

med = (n1 + n2)/2

if med < 5:
    print('Seu aluno REPROVOU, sua média é de {:.2f}'.format(med))
elif med >= 5.0 and med <= 6.9:
    print(('Seu aluno está em RECUPERAÇÂO, sua média é de {:.2f}'.format(med)))
elif med >= 7.0:
    print('Seu aluno está APROVADO, sua média é de {:.2f}'.format(med))
else:
    print('Error'*10)
print('---FIM---')
print(print('-_- '*7))
