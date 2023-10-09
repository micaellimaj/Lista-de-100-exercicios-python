def lin():
    print('-' * 30)


# Programa Principal
lin()
print('     CURSO EM VÍDEO     ')
lin()
print('     APRENDA PYTHON     ')
lin()
print('    GUSTAVO GUANABARA     ')
lin()
print()

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
titulo('   CURSO EM VÍDEO   ')
titulo('   PUTHON É MUITO BOM!   ')
titulo('oi')
print()

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa Principal
soma(b=4,a=9)
soma(a=8,b=9)
soma(2,1)
print()

def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores{núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
print()

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
