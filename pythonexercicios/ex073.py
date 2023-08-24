times =('Corithians','Palmeiras','Santos','Gremio',
        'cruzeiro','Flumengo','Vasco','Chapecoense',
        'Atlético','Botafogo','Atlético-PR','Bahia',
        'São Paulo','Fluminense','Sport Recife',
        'Ec Vitória','Coritiba','Avaí','Ponte Preta',
        'Atlético-Go')
print('--*--' * 10)
print('Lista de times do Brasileirão:')
for t in times:
    print(t)
print('--*--' * 10)
print(f'Os 5 primeiros são {times[0:5]}')
print('--*--' * 10)
print(f'Os 4 últimos são {times[-4:]}')
print('--*--' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('--*--' * 10)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')