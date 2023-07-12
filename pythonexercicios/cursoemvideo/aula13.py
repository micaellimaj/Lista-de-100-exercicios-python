for c in range(1,6):
    print(c)
print("FIM")

for B in range (6, 0, -1):
    print(B)
    print("FIM")

for C in range(0,7,2):
    print(C)
print("FIM")

n = int(input("Digite um número: "))
for A in range(0, n + 1):
    print(A)
print("FIM")

i = int(input('Início: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for D in range(i, f + 1, p):
    print(D)
print('FIM')

s = 0
for S in range(0,4):
    n1 = int(input('Digite um número: '))
    s += n1
print('O somatório de todos os valores foi {}'.format(s))