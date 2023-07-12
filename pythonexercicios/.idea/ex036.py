casa =float(input('Qual o valor da casa ? R$ '))
salário_comprador = float(input('Qual o salário do comprador ? R$ '))
anos = int(input('quantos anos de pagamento ?'))
prestação = casa / (anos * 12)
mínimo = salário_comprador * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser Concedido!')
else:
    print('Emprestimo NEGADO!')
