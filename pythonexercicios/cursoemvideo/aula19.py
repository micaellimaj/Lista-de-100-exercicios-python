pessoas = {'nome': 'Gustavo','sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas['nome'])
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for i in pessoas.items():
    print(i)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(pessoas)
print()
brasil = []
estado1 = {'uf':'Rio de Janeiro','Sigla':'RJ'}
estado2 = {'uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print()
print(brasil[0]['uf'])
print(brasil[1]['Sigla'])
print()
Estado = dict()
Brasil = list()
for c in range(0,3):
    Estado['uf'] = str(input('Unidade Federativa: '))
    Estado['Sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(Estado.copy())
for e in Brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')