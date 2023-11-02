from ex115.lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('opção 1')
    elif resposta == 2:
        cabeçalho('opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')


