teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('++' * 15)
grupo = [['joão',19],['joaquim',16],['hugo',44]]
print(grupo[2][1])
print(grupo[1][0])
print('--' * 15)
print('nome e idade')
for p in grupo:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print()

rapaziada = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    rapaziada.append(dado[:]) #[:] criar uma copis dos dados
    dado.clear()

for p in rapaziada:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
