'''
/////////////////////////////////////////////////
TOPICOS EM COMPUTACAO II - Modulo 02

Exercicio 04:
Mostre o nome dos 3 deputados com maiores gastos:

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

#Dicionario com ID do deputdo e o total de seus gastos
totalGastosDeputado = {}


#Soma total dos gastos
totalGastos = 0

#Mascara de apresentacao no console
mask = " ID: {0}\n Nome: {1}\n Total Gasto: R$ {2:.2f}\n ==============================\n"

#Contador de iteracoes com API
i = 1

for deputado in listaDeputados:

    #Pegando o ID de cada deputado
    idDeputado = deputado['id']
    nomeDeputado = deputado['nome']

    #Puxando todos os gastos por deputado
    gastosDeputado = api.deputado_despesas(idDeputado)

    #Somando todos os gastos 
    for gasto in gastosDeputado:
        totalGastos += gasto['valorDocumento']
    

    #Armazenando no Dicionario - A chave eh o ID do deputado
    totalGastosDeputado[idDeputado] = totalGastos

    #Zera novamente o variavel para a proxima iteracao
    totalGastos = 0
    
    #Apenas para acompanha na tela
    print("Deputado " + str(i))
    i += 1


#Lista que ira armazenar o dicionario anterior para ordenacao
listaTotalGastosDeputados = list(totalGastosDeputado.values())

#Ordena os valores
listaTotalGastosDeputados.sort()


#Tamanha da lista de gastos
tamanhoLista = len(listaTotalGastosDeputados)

#Amazena os 3 maiores valores
maioresGastos = []

#Colocando em uma lista os 3 maiores gastos
maioresGastos.append(listaTotalGastosDeputados[tamanhoLista-1])
maioresGastos.append(listaTotalGastosDeputados[tamanhoLista-2])
maioresGastos.append(listaTotalGastosDeputados[tamanhoLista-3])


#Funcao para encontrar o Id responsavel pelo gasto passado como parametro
def procuraValor(termo):
    for chave, valor in totalGastosDeputado.items():
        if termo == valor:
            return chave
    
    return None

#Laco para encontrar o ID dos 3 deputados com maiores gastos
for gasto in maioresGastos:

    id = procuraValor(gasto)
    deputado = api.deputado_id(id)

    print(mask.format(id, deputado['ultimoStatus']['nome'], totalGastosDeputado[id]))


