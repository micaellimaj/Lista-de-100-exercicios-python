resp = 's'
cont = ('Zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while resp in 'Ss':
    while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:
            break
        print('Tente novamente. ', end=' ')
    print(f'Você digitou o número {cont[núm]}')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]


