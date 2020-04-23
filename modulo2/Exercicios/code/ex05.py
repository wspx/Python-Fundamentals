'''
/////////////////////////////////////////////////
TOPICOS EM COMPUTACAO II - Modulo 02

Exercicio 05:
Mostre as informações formatadas da comissão sobre 'PEC57402':

*Como não existe a 'PEC57402' no endpoint da API,
*Estarei trocando pela SIGLA 'CSPCCO'
*Comissão de Segurança Pública e Combate ao Crime Organizado

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

#Puxando a lista de todos os orgaos
listaOrgaos = api.orgaos()

#Sigla a ser pesquisada
siglaPesquisar = 'CSPCCO'

mask = " ================================\n ID: {0}\n SIGLA: {1}\n NOME: {2}\n Mais informacoes: {3}\n ================================"

for orgao in listaOrgaos:
    if orgao['sigla'] == siglaPesquisar:
        print(mask.format( orgao['id'], orgao['sigla'], orgao['nome'], orgao['uri']))
        break



