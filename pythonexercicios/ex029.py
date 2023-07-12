print('RADAR ELETRÔNICO')
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! você excedeu o limite que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')