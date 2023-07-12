from random import randint
from time import sleep
print('JOGO DE ADIVINHAÇÃO')
computador = randint(0,5)
print('-$-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advimhar...')
print('-#-' * 20)
jogador = int(input('Em que número eu pensei? '))
#print('Pensei no número {}'.format(computador))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÈNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {} !'.format(computador, jogador))