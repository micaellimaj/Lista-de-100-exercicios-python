num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('unidade: {}'.format(n[3]))
print('dezena: {}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))

nume = int(input('Informe um número: '))
u = nume // 1 % 10
d = nume // 10 % 10
c = nume // 100 % 10
m = nume // 1000 % 10
print('Analisando o número {}'.format(nume))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
