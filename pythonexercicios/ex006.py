n = int(input('digite um número:'))
d = n * 2
t = n * 3
r = n **(1/2)
print('o dobro de {} vale {} .'.format(n,d))
print('o triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n, t, r))

m = int(input('digite um número:'))
print('o dobro de {}.'.format(m, (n*2)))
print('o triplo de {}. vale {}. \nA raiz quadrada de {} é igual a {:.2f}. '.format(m, (n*3), m, (m**(1/2))))