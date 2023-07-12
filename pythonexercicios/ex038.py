print('COMPARANDO NÚMEROS')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo valor é maior')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('Resposta inválida')