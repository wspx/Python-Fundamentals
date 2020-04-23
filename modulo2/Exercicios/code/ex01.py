'''
/////////////////////////////////////////////////
TOPICOS EM COMPUTACAO II - Modulo 02

Exercicio 01:
Listar os nomes em maiúscula dos deputados que 
tenham mais de 50 anos de idade:

NOME:  WILLIAM DA SILVA PEREIRA
R.A:   100942
TURMA: CI73A
/////////////////////////////////////////////////
'''

from scrapy_dadosAbertos import DadosAbertos
from datetime import date, datetime

#Iniciando a classe
api = DadosAbertos()

#Puxando a lista de todos os deputados
listaDeputados = api.deputados()


#Pegando a data atual
anoAtual = date.today().year


for deputado in listaDeputados:
    #Puxando os dados gerais do deputado pelo ID
    idDeputado   = deputado['id']
    nomeDeputado = deputado['nome']

    #Pegando as informacoes detalhadas do deputado
    infoDeputado = api.deputado_id(idDeputado)

    #Puxando a data de nascimento e pegando apenas o ano de nascimento
    anoNascimento = datetime.strptime(infoDeputado['dataNascimento'], '%Y-%m-%d').date().year

    #Sabendo a idade do deputado
    idadeDeputado = anoAtual - anoNascimento

    #Mascara de saida na tela
    mask = " Id: {0}\n Nome: {1}\n Idade: {2}\n ==========================\n"

    if idadeDeputado > 50:
        print(mask.format(idDeputado, nomeDeputado.upper(), idadeDeputado))
    else:
        print(mask.format(idDeputado, nomeDeputado.lower(), idadeDeputado))


