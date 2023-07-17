print('EXEMPLO1')
n=1
while n != 0:
    n= int(input('Digite um valor: '))
print('FIM')

print('EXEMPLO2')
r = 'S'
while r == 'S':
    nu = int(input('Digite um valor: '))
    r = str(input('quer continuar? [S/N] ')).upper()
print('FIM')

print('EXEMPLO3')
n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} númeroes pares e {} números ímpares!'.format(par, impar))

