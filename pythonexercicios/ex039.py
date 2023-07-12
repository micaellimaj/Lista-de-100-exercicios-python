from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Está exatemente na hora de se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('Você é muito novo para se alistar, ainda faltam {} anos.'.format(saldo))
    alistamento = atual + saldo
    print('Seu alistamento será em {}.'.format(alistamento))
else :
    saldo = idade - 18
    print('Você já passou do tempo de alistamento, você deveria ter se alistado há {} anos.'.format(saldo))
    alistamento = atual - saldo
    print('Seu alistamento foi em {}.'.format(alistamento))