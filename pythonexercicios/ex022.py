nome =str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome tem {} e ele tem {} letras'.format(separa[0],len(separa[0])))

#strip(eleminar os espacos do inicio e fim)
# - nome.count(' ') elininar espacoes entre as palavras
#split ( quebra em uma lista)
