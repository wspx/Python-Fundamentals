'''
/////////////////////////////////////////////////
TOPICOS EM COMPUTACAO II - Modulo 02

Exercicio 03:
Mostre a soma dos gastos de um deputados especificos

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

#Soma total dos gastos
totalGastos = 0

#Mascara de apresentacao no console
mask = " ID: {0}\n Nome: {1}\n Total Gasto: R$ {2:.2f}\n ==============================\n"

for deputado in listaDeputados:

    #Pegando o ID de cada deputado
    idDeputado = deputado['id']
    nomeDeputado = deputado['nome']

    #Puxando todos os gastos por deputado
    gastosDeputado = api.deputado_despesas(idDeputado)

    #Somando todos os gastos 
    for gasto in gastosDeputado:
        totalGastos += gasto['valorDocumento']
    
    #Mostrando o total de gasto do deputado
    print(mask.format(idDeputado, nomeDeputado, totalGastos))

    #Zera novamente o variavel para a proxima iteracao
    totalGastos = 0
    
    
    print("++++++++++++++++++++++++ [#] ++++++++++++++++++++++++")
