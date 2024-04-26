'''
Pergunte o salario de um funcionário e calcule o valor
do seu aumento.
Salários superiores a R$1250,00 aumento de 10%
Salários inferiores aumento de 15%
'''
sal = float(input('Digite seu salário para ver quanto ele vai ficar depois do aumento R$'))
if sal > 1250:
    aumento = (sal*0.1)+sal
    print('Seu salário com o aumento ficou R${:.2f}'.format(aumento))
else:
    aumento = (sal*0.15)+sal
    print('Seu salário com o aumento ficou R${:.2f}'.format(aumento))
