"print(input.__doc__)"
"print("" * 20)"
"help(print)"

def somar(a=0, b=0, c=0):
   """
   -> Faz a soma de três valores e mostra o resultado na tela.
   :param a: o primeiro valor
   :param b: o segundo valor
   :param c: o terceiro valor
   Função criada por Gustavo Guanabara do canal cursoemvideo
   """
   s = a + b + c
   print(f'A soma vale {s}')

somar(3)
somar(a=5,c=10)

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na fução teste. x vale {x}')

print("=" * 25)
# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()

print("-*" * 20)

def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')


n1 = 2
funcao()
print(f'n1 fora vale {n1}')

print('-=' * 20)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1},{r2} e {r3}')

print('-+' * 20)
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

print('*-' * 20)
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


