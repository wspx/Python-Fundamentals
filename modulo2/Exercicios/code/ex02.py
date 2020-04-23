'''
/////////////////////////////////////////////////
TOPICOS EM COMPUTACAO II - Modulo 02

Exercicio 02:
Listar as deputadas

NOME:  WILLIAM DA SILVA PEREIRA
R.A:   100942
TURMA: CI73A
/////////////////////////////////////////////////
'''

from scrapy_dadosAbertos import DadosAbertos


#Iniciando a classe
api = DadosAbertos()

#Puxando a lista de todos os deputados
listaDeputados = api.deputados()


for deputado in listaDeputados:

    #Pegando o ID de cada deputado
    idDeputado   = deputado['id']
    nomeDeputado = deputado['nome']

    #Pegando as infomacoes completas de cada deputado
    infoDeputado = api.deputado_id(idDeputado)

    #Pegando o genero do Deputado
    sexoDeputado = infoDeputado['sexo']

    #Criando a mascara de apresentacao no console
    mask = " Id: {0}\n Nome: {1}\n ==========================\n"

    if sexoDeputado == 'F':
        print(mask.format(idDeputado, nomeDeputado))

