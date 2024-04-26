'''
Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta.
'''
expressao = str(input('Digite a expressão: '))
list = []
for simbolo in expressao:
    if simbolo == '(': #cada parenteses aberto vai entrar na lista aqui
        list.append('(')
    elif simbolo == ')':
        if len(list) > 0: #verificar se o tamanho da lista está certo
            list.pop()
        else:
            list.append(')') #mais parenteses fechando que abrindo
            break
if len(list) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')