# Módulo 1  - Python Fundamentals

## Objetivo
Capacitar estudantes com nenhum ou prévio conhecimento na linguagem Python a desenvolver aplicações ricas com acesso a banco de dados e interface WEB

## Conteúdo:
   - [História](#historia)
   - [Filosofia da Linguagem](#conceitodalinguagem)
   - [Ambiente de Desenvolvimento](#ambientededesenvolvimento)
   - [Sintaxe básica](#sintaxebasica)
   - [Variável](#variavel)
   - [Operadores](#operadores)
   - [Controle de fluxo](#controlefluxo)
   - [Estrutura de dados](#estruturadedados)


## 1 História
No Brasil em 1989, Collor de Melo vencia a primeira eleição direta, na Alemanha caia o muro de Belim e na Holanda o Guido Van Rossum criava a linguagem Python.

A história da linguagem é fantástica e seu aprendizado vai se tornar mais divertido após tomar conhecimento de alguns eventos que aconteceram.

Não vou escrever sobre a história do Python porque já tem muita coisa boa escrita, segue alguns links que vale a pena ler:

* [http://mindbending.org/pt/a-historia-do-python](http://mindbending.org/pt/a-historia-do-python)
* [https://www.python-course.eu/python3_history_and_philosophy.php](https://www.python-course.eu/python3_history_and_philosophy.php)
* [https://wiki.python.org.br/HistoriaDoPython](https://wiki.python.org.br/HistoriaDoPython)

## 2 Filosofia da Linguagem
## 3 Ambiente de Desenvolvimento;
## 4 Sintaxe básica
## 5 Variável
```python
   dados=10
```
Atribuição em cadeia
```python
   dados=x=filho=10
```
### 5.1 Escopo de Variável
### 5.2 Estrutura de Dados
   #### 5.2.1 String 
   String é uma sequencia de caracteres Unicode. Para representar uma string pode ser utilizado aspas simples e aspa duplas.
   Exemplo:
   ```python
       texto="As vezes voce tem que levantar sozinho e seguir em frente"
   ```
   Para declarar multiplas linhas utilize 3 aspas simple.
   Exemplo:
   ```python
        texto='''
               Tudo é possivel. 
               O impossível apenas demora mais
               '''
   ```
  Semelhante a lista e Tuplas, as string também utilizam o operador [ ]. Dessa forma é possível obter apenas parte da string.
  Exemplo:
  ```python
  texto="As vezes voce tem que levantar sozinho e seguir em frente" 
  # Recuperar o caractere da posição 5
  texto[6]   # Retorno "z"
   
  # Recuperar do inicio da string ate posição 10
  texto[0:10]  # Retorno "As vezes vo"
  
  # Recuperar da posição 10 até a posição 15
  texto[10:15] # retorno "
  ```
   
   #### 5.2.2 Numbers
   Com python é possível utilizar 3 tipos de variável para números. São os Inteiros (int), Ponto Flutuante (float) e os números complexos (complex).
   
   Não é necessário declarar os tipos que deseja utilizar, apenas declarar o conteúdo que o tipo automáticamente é alocado.
   
   Exemplo:
   
  
  > No exemplo abaixo utilizamos a função `type()` para mostrar o tipo da classe da variável. Também usamos a função `isinstance()` para verificar/comparar o tipo da váriavel. Se for o mesmo tipo ele retorno true.
  
```python
a = 5
print(a, "do tipo", type(a))

a = 2.0
print(a, "do tipo", type(a))

a = 1+2j
print(a, "numero complexo?", isinstance(1+2j,complex))
```
   #### 5.2.3 List
 Lista é Python é uma sequencia de item, equivale os array de outras linguagem. A lista é um dos tipos de dados mais utilizados em Python por ser muito flexivel.Todos os items de uma lista NÃO precisam ser do mesmo tipo.  
   
Exemplo:

```python 
lista=[10,60,'jose','45234234',50.9]
# Mostrando a lista
print("Conteudo da lista, lista)
```
Nas listas podemos utilizar o operador [ ]. Dessa forma podemos obter um elementro especifico da lista ou mostrar uma conjunto de elemento.

Exemplo:
```python
lista=[10,30,50,90,100,1,5,19]

# lista[2] = 50
print("lista[2] = ", lista[2])

# lista[0:3] = [10, 30, 50]
print("lista[0:3] = ", lista[0:3])

# lista[5:] = [1, 5, 19]
print("lista[5:] = ", lista[5:])
```
A lista podem ser alteradas.
```python
a = [1,2,3]
a[2]=4

# [1, 2, 4]
print(a)
```
#### 5.2.4 Tuple
As tuple são uma sequencia de itens, semelhante a uma lista. A diferença que a tuples são imultavél. Uma vez que a tupla são criadas,não podem ser modificadas.

As tuplas são usadas para dados que são protegidas contra gravação e por não serem modificadas dinamicamente, elas são usualmente mais rapidas que as listas. 

Exemplo:
```python
t = (10,40,'jose','maria',6.5)

print(t[1])
```
#### 5.2.5 Dictionary
Dicionário são estrutura de dados com um par conhecido como `chave/valor`. 

Geralmente é usado quando temos uma quantidade enorme de dados. Os dicionários são otimizados para recuperar dados. Nós devemos conhecer a chave para recuperar o valor.

No Python, os dicionários são definidos entre chaves {}, sendo cada item um par na chave do formulário: valor. Chave e valor podem ser de qualquer tipo de variável.

```python
login = {"user": "jose","passwd":"okri"}

print("Tipo", type(login))

#Recuperando o valor
print(login['uesr']

#Recuperando o valor
print(login['passwd'])
```
Usamos a chave para recuperar o valor. Mas o contrário não funciona.

#### 5.2.6 Set
Set é uma coleção não ordenada de itens exclusivos (não pode ter itens repetidos). Set é definido por valores separados por vírgula entre chaves {}.

Podemos realizar operações de conjunto como união, interseção em dois conjuntos. Conjunto tem valores exclusivos. Eles eliminam duplicatas.

Como o conjunto é uma coleção não ordenada, a indexação não funciona. Portanto, o operador [ ] não funciona.
```python
posicao_chegada={3,4,1,7,8}
print(posicao_chegada)
```

#### 5.2.7 Conversão entre tipos
Nós podmeos converter entre diferentes tipo de dados usando diferentes funções de conversão semelhante a `int()`, `float()`, `str()`...etc.

| S| Descrição| Função | Exemplo |
|--|--------|-----------|
|1 | Converts x to an integer. The base specifies the base if x is a string.|  int(x [,base]) | |
|2 | Converts x to a floating-point number.|float(x) | |
|3 | Creates a complex number.|complex(real [,imag]) |  |
|4 | Converts object x to a string representation.|str(x) |  |
|5 | Converts object x to an expression string.|repr(x) | |
|6 | Evaluates a string and returns an object.|eval(str) | |
|7 | Converts s to a tuple.|tuple(s) | |
|8 | Converts s to a list.|list(s) | |
|9 | Converts s to a set.|set(s) | |
|10| Creates a dictionary. d must be a sequence of (key,value) tuples.| dict(d) | |
|11| Converts s to a frozen set.| frozenset(s) | |
|12| Converts an integer to a character.|chr(x) | |
|13| Converts an integer to a Unicode character.|unichr(x) | |
|14| Converts a single character to its integer value.| ord(x) | |
|15| Converts an integer to a hexadecimal string.| hex(x) | |
|16| Converts an integer to an octal string.| oct(x) | |


## 5.3 Operadores
## 5.3 Controle de Fluxo
O controle de fluxo de dados no Python podem ser realizado utilizado
If
```python
x=10
if x > 10:
    print("Maior que 10")
```   
Case
While
For
Until
