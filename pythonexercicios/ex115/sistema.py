from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq ='cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq):

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('opção 2')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

