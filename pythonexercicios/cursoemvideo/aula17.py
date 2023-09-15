num = [2,8,9,1]
print(num)
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
num.pop(4)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print("-*-" * 20)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print("*-*" * 20)
valores2 = list()
for cont in range(0,3):
    valores2.append(int(input('Digite um valor: ')))

for d, b in enumerate(valores2):
    print(f'Na posição {d} encontrei o valor {b}!')
    print('Cheguei ao final da lista.')
print("-*-" * 20)

a = [2,3,4,5]
b = a[:] #copia de a
b[2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')
