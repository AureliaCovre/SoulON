# #-- -------------------------------------------------------------------------------------
# # AULA 1 - INTRODUÇÃO A ORIENTAÇÃO A OBJETOS
# #-- -------------------------------------------------------------------------------------

""" O TERMO DE PROGRAMAÇÃO ORIENTADA A OBJETO (POO) FOI CRIADO POR ALAN KAY, 
AUTOR DA LINGUAGEM DE PROGRAMAÇÃO SMALLTALK.

PARADIGMAS DE PROGRAMAÇÃO:
- PROGRAMAÇÃO ESTRUTURADA
- PROGRAMAÇÃO IMPERATIVA
- PROGRAMAÇÃO PROCEDURAL
- PROGRAMAÇÃO ORIENTADA A OBJETOS
"""
# Linguagens modernas que usam POO: Python / Java / C++ / C# / Ruby

"""Ideias bases da POO: A POO foi criada para tentar aproximar o mundo real do mundo virtual. Na POO o programador 
é responsavel por moldar o mundo dos objetos, e explicar para estes objetos como eles devem interagir entre si;"""


# #-- -------------------------------------------------------------------------------------
# # AULA 2 - CLASSES      /       AULA 3 - OBJETOS
# #-- -------------------------------------------------------------------------------------
# from curses import noecho


# class Veiculo():
#     def __init__(self, tipo, chassi, marca, modelo, ano): #INIT é o contrutor da classe
#         self.tipo = tipo 
#         self.chassi = chassi 
#         self.marca = marca 
#         self.modelo = modelo 
#         self.ano = ano 
        
# class Aviao(): 
#     def __init__(self, tipo, motor, linha_aerea, modelo, ano): 
#         self.tipo = tipo 
#         self.motor = motor 
#         self.linha_aerea = linha_aerea 
#         self.modelo = modelo 
#         self.ano = ano


# #INSTANCIANDO A CLASSE:
# #variavel = classe(estrutura do construtor)
# carro = Veiculo('carro', '78ds77ds87ds8','marcaX', 'X001', '2012')
# #print(vars(carro))
# objeto_aviao = Aviao('Carga', 'Quadrimotor', 'SoulCode Airlines', 'Airbus a380', '2010')
# #print(vars(objeto_aviao))

# #-- -------------------------------------------------------------------------------------
# # AULA 4 - INIT E SELF     /   AULA 5 - ATRIBUTOS E MÉTODOS 
# #-- -------------------------------------------------------------------------------------
""" Self é um parametro que se refere ao proprio objeto, que chama o método. Sempre que utilizamos
o Self estamos dizendo que são caracteristicas relacionadas a ele mesmo.
No Python é obrigatorio seu uso, mas em algumas linguagens é opcional.

Sem o self quer dizer que é variavel qqer e não atribui a variavel á classe.
"""
""" INIT é o contrutor da classe , no python é obrigatorio, mas em outras linguagens não"""

# class Funcionario():
#     def __init__(self, nome, cpf, salario):
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario 
     
#      #Criando os métodos:   
#     def get_salario(self):
#         print("Meu salario é:  ", self.salario)   
    
#     def get_bonificacao(self):
#         return self.salario * 0.15
        
# jose = Funcionario('Jose','78425454', 5000)     #objeto criado   
# jose.get_salario() #chamando os metodos criados
# jose.get_bonificacao        
        
        
# #-- -------------------------------------------------------------------------------------
# # AULA 6 - ENCAPSULAMENTO
# #-- -------------------------------------------------------------------------------------

# class Funcionario():
#     def __init__(self, nome, cargo, valor_hora_trabalhada):
#         self.nome = nome
#         self.cargo = cargo
#         self.valor_hora_trabalhada = valor_hora_trabalhada
#         self.__salario = 0 #private
#         self.__horas_trabalhadas = 0 #private
        
#     """ Aqui foram criados mais 2 atribuitos (self.__salario /self.__horas_trabalhadas) para essa classe e não foram passados pelo construtor, pq esses atributos 
#     não serão fornecidos pelo usuario. Eles serão atribuidos aqui dentro da função ou serão modificados dentro da 
#     função atraves de metodo.
#     * Os dois __ significam que temos um atributo privado (#private)
#     """    
        
#     @property #primeira estrutura do método de encapsulamento
#     def salario(self): #método
#         return self.__salario
    
#     @salario.setter
#     def salario(self, novo_salario): #método Setter. se alguem quiser mudar o salario sem passar pela função da erro    
#         raise ValueError("Impossivel alterar salário diretamente. Use a função calcula_salario().")
    
#     #Criando as funções que alteram salario
#     def registra_hora_trabalhada(self):
#         self.__horas_trabalhadas += 1
        
#     def calcula_salario(self):
#         self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        
        
# jose = Funcionario('José', 'Professor', 50)    
# jose.salario = 10000        

        
# #-- -------------------------------------------------------------------------------------
# # AULA 7 - HERANÇA
# #-- -------------------------------------------------------------------------------------

#classe pai
# class Veiculo(): #classe pai
#     def __init__(self, tipo, chassi, marca, modelo, ano):
#         self.tipo = tipo
#         self.chassi = chassi
#         self.marca = marca
#         self.modelo = modelo 
#         self.ano = ano
        
        
# #classe filha
# class Motocicleta(Veiculo):
#     def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada) :
#         super().__init__(tipo, chassi, marca, modelo, ano)
#         self.cilindrada = cilindrada
        
# v = Veiculo('carro', '4f4d5f4d5f4d5s4f5d4f5dsf6', 'Ferrari', 'F112', '2017')   
# print(vars(v))
# m = Motocicleta('motocicleta', '45d4s5d4sa6d4as5', 'Honda', 'CG', '2008', 150)
# print(vars(m))   

        
# #-- -------------------------------------------------------------------------------------
# # AULA 8 - EXERCÍCIO PRÁTICO
# #-- -------------------------------------------------------------------------------------  
  
# """ Crie uma classe animal com atributos e métodos, posteriormente, crie uma classe que herde seus atributos, 
# e possuía os seus atributos próprios. 
# Crie dois objetos da classe filha.
# """ 

# class Animal():
#     def __init__(self, nome, porte):
#         self.nome = nome
#         self.porte = porte
                    
# class Gato(Animal):
#     def __init__(self, nome, porte, som):
#         super().__init__(nome, porte)   
#         self.som = som
        
# lex = Gato('lex', 'Médio', "Mia")
# lala = Gato('lala', 'pequeno', 'mia')    

# print(vars(lex))
# print(vars(lala))

# #-- -------------------------------------------------------------------------------------
# # AULA 9 - ASSOCIAÇÃO
# #-- -------------------------------------------------------------------------------------  

"""Conceito de associação, é onde criamos um vinculo entre 2 classes dentro das estrutura (varios vinculos
podem existir) """ 

# class Escritor():
#     def __init__(self, nome): #dentro do parenteses são osa atributos
#         self.nome = nome
#         self.__ferramenta = None
        
# @property
# def nome(self):
#     return self.__nome

# @property
# def ferramenta(self):
#     return self.__ferramenta

# #setando a ferramenta 
# @ferramenta.setter
# def ferramenta(self, ferramenta):
#     self.__ferramenta = ferramenta
    
# class Caneta():
#     def __init__(self, marca):
#         self.__marca = marca
        
#     @property
#     def marca(self):
#         return self.__marca
    
#     def escrever(self):
#         print("Caneta está escrevendo...")
        
# escritor = Escritor('José')
# caneta = Caneta('BIC')

# escritor.ferramenta = caneta
# escritor.ferramenta.escrever()   

# #-- -------------------------------------------------------------------------------------
# # AULA 10 - COMPOSIÇÃO
# #-- -------------------------------------------------------------------------------------           
            
# class Cliente():
#     def __init__(self, nome):
#         self.__nome = nome
#         self.__enderecos = []
        
#     @property
#     def nome(self):
#         return self.__nome
    
#     @nome.setter
#     def nome(self, nome):
#         self.__nome = nome  
        
#     def inserir_endereco(self, cidade):
#         self.__enderecos.append(Endereco(cidade))
        
#     def lista_enderecos(self):
#         for endereco in self.__enderecos:
#             print(endereco.cidade) 
            
# class Endereco():
#     def __init__(self, cidade):
#         self.__cidade = cidade
        
#     @property
#     def cidade(self):
#         return self.__cidade
    
#     @cidade.setter
#     def cidade(self, cidade):        
#         self.__cidade = cidade
        
# cliente1 = Cliente('José')
# cliente1.inserir_endereco('São Paulo')
# print(cliente1.nome)
# cliente1.lista_enderecos() 
# del cliente1  

# #-- -------------------------------------------------------------------------------------
# # AULA 11 - AGREGAÇÃO
# #-- -------------------------------------------------------------------------------------           
                
# class Produto():
#     def __init__(self, nome, valor):
#         self.nome = nome
#         self.valor = valor
        
# class CarrinhoCompras():
#     def __init__(self, ):
#         self.produtos = []  
        
#     #METÓDOS
#     def inserir_produto(self, produto):
#         self.produtos.append(produto)
        
#     def lista_produtos(self):
#         for produto in self.produtos:
#             print(f'{produto.nome}:R${produto.valor}')
            
    
#     def soma_total(self):
#         total = 0
#         for produto in self.produtos:
#             total +=produto.valor
#         return f'R${total}'
      
# carrinho = CarrinhoCompras()
# p1 = Produto('Boné', 50)
# p2 = Produto('Tênis', 100)
# p3 = Produto('Camiseta', 39)

# carrinho.inserir_produto(p1)
# carrinho.inserir_produto(p2)
# carrinho.inserir_produto(p3)
# carrinho.lista_produtos()
# print(carrinho.soma_total())    


# #-- -------------------------------------------------------------------------------------
# # AULA 12 - Classes Abstratas
# #-- -------------------------------------------------------------------------------------           

# """ Uma classe abstrata nada mais é que uma classe que vai servir de modelo para as outras classes. 
# O diferencial dessa classe, é que ela não vai ser instanciada diretamente."""

# #Para criar a classe abstrata , é necessario importar essa biblioteca
# from abc import ABC, abstractmethod

# class letras():
#     @abstractmethod #necessario colocar essa arroba.
#     def mostrarTipo(self):
#         print("Eu sou uma classe abastrata!")
        
# class A(letras):
#     def __init__(self, descricao):
#         self.descricao = descricao
        
#     def imprimir(self):
#         print("Aqui é um método diferente!")


# letraa = A("letra A")
# letraa.mostrarTipo()
# letraa.imprimir() 


# #-- -------------------------------------------------------------------------------------
# # AULA 13 - POLIMORFISMO
# #-- -------------------------------------------------------------------------------------    
     
''' Em python o único polimorfismo que a linguagem suporta é por sobreposição, que é o princípio que 
permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura) 
mas comportamentos diferentes.'''

# from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def fala(self, msg):
#         pass

# class B(A):
#     def fala(self, msg):
#         print(f'B está falando {msg}')

# class C(A):
#     def fala(self, msg):
#         print(f'C está falando {msg}')

# # OBJETOS
# b = B()
# c = C()
# b.fala('de Skate')
# c.fala('de futebol')    

# # ----- EXEMPLO 2 ------#

# from abc import ABC, abstractmethod

# class letras():
#     @abstractmethod
#     def mostrarTipo(self):
#         print("Eu sou uma classe abastrata!")
        
# class A(letras):
#     def __init__(self, descricao):
#         self.descricao = descricao
        
#     def imprimir(self):
#         print("Aqui é um método diferente!")


# letraa = A("letra A")
# letraa.mostrarTipo()
# letraa.imprimir()     


### ---------- MODULO 2 - MODULOS E PACOTES ----------------------------------------------

# #-- -------------------------------------------------------------------------------------
# # AULA 14 - Introdução a módulos e pacotes em Python
# #-- -------------------------------------------------------------------------------------

# # -*- iso-8859-1 -*-
# """Módulo principal."""
# import strformat

# """Função principal da aplicação."""
# print (strformat.frmt_bytes(502356))
# print (strformat.strip_html("<b>Texto</b>"))

# #-- -------------------------------------------------------------------------------------
# # AULA 15 - Tabelas de símbolos e namespaces
# #-- -------------------------------------------------------------------------------------
# import math
# print(dir())
# import numpy
# print(dir())
# import pytz
# print(dir())

# #-- -------------------------------------------------------------------------------------
# # AULA 16 - Importando pacotes em Python com pip
# #-- -------------------------------------------------------------------------------------

# Para verificar a versão do pip, no terminal digite: pip--version
# Para verificar quais modulos estão instalados, no terminal digite: pip list
# Para desinstalar um modulos, no terminal digite:pip uninstall numpy
# Para instalar um modulos, no terminal digite:pip install numpy
# Para atualizar modulos, no terminal digite:pip install --upgrade numpy

# #-- -------------------------------------------------------------------------------------
# # AULA 17 - Criando módulos em python
# #-- -------------------------------------------------------------------------------------
# import operacoes as op

# op.somar(2, 4)
# op.subtrair(4,2)
# op.dividir(4,2)
# op.multiplicar(2,4)
# op.imprimir("Uma mensagem qualquer...")

# #-- -------------------------------------------------------------------------------------
# # AULA 18 - QUESTIONÁRIO
# #-- -------------------------------------------------------------------------------------

# #-- -------------------------------------------------------------------------------------
# # AULA 19 - EXERCÍCIO PRÁTICO
# #-- -------------------------------------------------------------------------------------
# """ Crie um módulo onde seja possível, imprimir um texto de trás para frente. 
# Oriente o usuário do seu uso. """

# import reverse as re

# re.reverse("12345")


### ---------- MODULO 03 - Manipulação de dados com MYSQL ------------------------------

# #-- -------------------------------------------------------------------------------------
# # AULA 20 - Introdução ao banco de dados MYSQL
# #-- -------------------------------------------------------------------------------------               
# import MySQLdb 

# #Criando o database
# db = MySQLdb.connect(host="212.1.211.51", user="u948493795_rootx", passwd="Soulcodeacademy1#", db="u948493795_library")

# cursor = db.cursor() 
# cursor.execute('SELECT * FROM `tblbooks`') 
# numrows = int(cursor.rowcount) 
# linhas = cursor.fetchall()

# print("Número total de registros encontrados: ", numrows) 
# print("\nMostrando resultados...") 

# i = 0
# for linha in linhas: 
#     print("-", linha[0]) 
#     print('-', linha[1])           
                

# #-- -------------------------------------------------------------------------------------
# # AULA 21 - Criando database e table
# #-- -------------------------------------------------------------------------------------                    
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="", 
#     database="mydatabase"
# )

# mycursor = mydb.cursor()
# #mycursor.execute("CREATE DATABASE mydatabase")
# #print("Database criada com sucesso!")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# print("Tabela criada com sucesso!")        
        
# #-- -------------------------------------------------------------------------------------
# # AULA 22 - Inserindo dados
# #-- -------------------------------------------------------------------------------------                            
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# #val = ("José", "Piracuruca, PI")
# #mycursor.execute(sql, val)
# val = [
#     ('Pedro', 'São Paulo, SP'), 
#     ('Ana', 'Vitória, ES'),
#     ('Débora', 'Palmas, TO'),
#     ('Clara', 'São Bernardo, SP'),
#     ('Sandy', 'Ubajara, CE')
# ]
# mycursor.executemany(sql,val) # executemany pq ele vai executar varias linhas de uma vez
# mydb.commit()
# print(mycursor.rowcount, "linha(s) alterada(s)!") 

# #-- -------------------------------------------------------------------------------------
# # AULA 23 - Consultas com Select
# #-- -------------------------------------------------------------------------------------         
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECT name, address FROM customers")

# '''
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# '''
# myresult = mycursor.fetchone()
# print(myresult)

# #-- -------------------------------------------------------------------------------------
# # AULA 24 - Filtros com Where
# #-- ------------------------------------------------------------------------------------- 

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# #sql = "SELECT * FROM customers WHERE address = 'São Paulo, SP'" #customers é o nome da tabela dele 

# sql = "SELECT * FROM customers WHERE address LIKE '%SP%'" #Aqui ele busca a/as letra(s) no texto inteiro

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# #-- -------------------------------------------------------------------------------------
# # AULA 25 - Organização com Order By
# #-- ------------------------------------------------------------------------------------- 
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# #sql = "SELECT name FROM customers ORDER BY name"           #customers é o nome da tabela dele 
# sql = "SELECT name FROM  customers ORDER BY name DESC"      #customers é o nome da tabela dele 

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#       print(x)

# #-- -------------------------------------------------------------------------------------
# # AULA 26 - Exclusão de dados
# #-- ------------------------------------------------------------------------------------- 
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# #linha de comando para excluir do banco de dados
# sql = "DELETE FROM customers WHERE address = 'Ubajara, CE'" #customers é o nome da tabela
# mycursor.execute(sql)
# mydb.commit()

# print(mycursor.rowcount, "linha(s) deletada(s).")

# #-- -------------------------------------------------------------------------------------
# # AULA 27 - Atualização de dados
# #-- ------------------------------------------------------------------------------------- 
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()
# sql = "UPDATE customers SET address = 'Manaus, AM' WHERE address = 'Palmas, TO'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "linha(s) afetada(s).")

# #-- -------------------------------------------------------------------------------------
# # AULA 28 - Exclusão de tabelas
# #-- ------------------------------------------------------------------------------------- 
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root"
#     password = "",
#     database = "mydatabase"
# )

# mycursor = mydb.cursor()
# sql = "DROP TABLE customers"

# mycursor.execute(sql)
# print("tabela excluida com sucesso")

# #-- -------------------------------------------------------------------------------------
# # AULA 29 - EXERCICÍO PRÁTICO
# #-- ------------------------------------------------------------------------------------- 
"""
Crie um script contendo as instruções abaixo:
1.	Crie uma base de dados chamada sistema_escolar_soul_on
2.	Crie uma tabela alunos com os campos id, nome, matricula, turma.
3.	Alimente a tabela com os seguintes dados:
Id	Nome	        Matrícula	Turma
1	José Lima	    MAT90551	BCW22
2	Carlos Augusto	MAT90552	BCW22
3	Lívia Lima	    MAT90553	BCW22
4	Sandra Gomes	MAT90554	BCW23
5	João Augusto	MAT90555	BCW23
6	Breno Lima  	MAT90556	BCW24
7	José Vinícius	MAT90557	BCW25

4.	Faça as seguintes consultas:
•	Liste todos os registros de sua tabela.
•	Liste apenas nome e matrícula dos alunos do BCW23.
•	Liste apenas o nome dos alunos que tiverem o sobrenome Lima.

5.	O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25.
6.	O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema.
"""

# import mysql.connector

# def create_database():
#     mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = ""    
#     )

#     mycursor = mydb.cursor()
#     mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
#     print("database criada com sucesso!")
    
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="sistema_escolar_soul_on"
# )
# mycursor = mydb.cursor()

# def create_table():
#     mycursor.execute("CREATE TABLE alunos(Id INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(255), Matrícula VARCHAR(255), Turma VARCHAR(255))")
#     print("Tabela criada com sucedsso!")
 
# def insert_data():
#     sql = "INSERT INTO alunos (Nome, matrícula, turma) VALUES (%s,%s,%s)"
#     val = [
#         ("José Lima", "MAT90551","BCW22"), 
#         ("Carlos Augusto","MAT90552","BCW22"), 
#         ("Lívia Lima", "MAT90553","BCW22"), 
#         ("Sandra Gomes","MAT90554","BCW23"),
#         ("João Augusto","MAT90555","BCW23"), 
#         ("Breno Lima","MAT90556","BCW24"), 
#         ("José Vinícius",	"MAT90557","BCW25")"
#     ]
#     mycursor.executemany(sql,val)
#     mydb.commit()
#     print(mycursor.rowcount, "linha(s) inseridas")
    
# insert_data()


# def select_data():
#     mycursor.execute("SELECT * FROM alunos")
#     mycursor.execute("SELECT * FROM alunos WHERE Nome, Matrícula")
#     mycursor.execute("SELECT * FROM alunos WHERE '%Lima%'")
    
#     myresult = mycursor.fetchall()
#     for x in myresult:
#         print(x)    
        
        
# def change_class():
#     sql = "UPDATE alunos SET Turma = 'BCW25' WHERE id ='2'"
#     mycursor.execute(sql)
#     mydb.commit()
#     print(mycursor.rowcount, "linha(s) alterada(s).")


# def delete_item():
#     sql = "DELETE FROM alunos WHERE id = '7'"
#     mycursor.execute(sql)
#     mydb.commit()
    
#     print(mycursor.rowcount, "linha(s) deletadas(s). ")
    
# delete_item()   


### ---------- MODULO 4 - MANIPULAÇÃO DE DADOS COM PYMONGO ----------------------------------------------
# #-- ---------------------------------------------------------------------------------------------------
# # AULA 30 - ACESSANDO BANCO DE DADOS MONGODB COM PYTHON 
# #-- --------------------------------------------------------------------------------------------------- 
# from pymongo import collection

# def get_databases():
#     from pymongo import MongoClient
#     import pymongo
    
#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['sample_airbnb'] #nome do DB

# get_database()


# #-- ---------------------------------------------------------------------------------------------------
# # AULA 31 - INTRODUÇÃO A MONGO DB COM PYTHON (COLEÇÕES) / AULA 31 - INSERÇÃO DE DADOS (DOCUMENTOS)
# #-- --------------------------------------------------------------------------------------------------- 
# from pymongo import collection

# #função que cria o banco de dados
# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data'] #nome do DB
    
# dbname = get_database()  # chamando a função. O dbname está armazenando o banco de dados da função acima
# collection_name = dbname["itens_soulcode"] # criando uma coleção

# # A estrutura para se criar um item é de dicionario
# item_1 = {
#     "_id":"SC001",
#     "nome_item":"Livro",
#     "desconto_maximo":"10%",
#     "REF":"RRGSFF001",
#     "preco": 340,
#     "categoria":"Físico"
# }

# item_2 = {
#     "_id":"SC002",
#     "nome_item":"Camera",
#     "desconto_maximo":"15%",
#     "REF":"RRGSJ001S4",
#     "preco": 540,
#     "categoria":"Físico"
# }

# item_3 = {
#     "nome_item":"Microfone",
#     "desconto_maximo":"12%",
#     "REF":"RRGSJ0FRSW7854R",
#     "preco": 300,
#     "categoria":"Físico"
# }

# item_4 = {
#     "nome_item":"Aula Remota",
#     "desconto_maximo":"19%",
#     "REF":"RRGS844W7854R",
#     "preco": 400,
#     "categoria":"Online"
# }

# item_5 = {
#     "_id":"SC005",
#     "nome_item":"Apostila",
#     "desconto_maximo":"19%"
# }

# # INSERINDO OS DADOS DESCRITOS ACIMA
# #collection_name.insert_many([item_1,item_2,item_3]) 
# # print("Dados inseridos!")

# #INSERINDO UM ITEM DE CADA VEZ
# collection_name.insert_one(item_4) 
# collection_name.insert_one(item_5)
# print("Dados inseridos!")

# #-- ---------------------------------------------------------------------------------------------------
# # AULA 32 - EXERCICIO PRÁTICO
# #-- ---------------------------------------------------------------------------------------------------
"""
Crie uma base de dados MongoDB contendo as seguintes coleções e suas respectivas quantidades de documentos:
Coleções
Livros: 20 documentos.
Revistas: 15 documentos.
Jornais: 15 documentos.
Mangás: 10 documentos.

Todos os documentos devem ter pelo menos 4 campos.
Deverá haver documentos com mais e menos campos que os demais.
Deverá haver _id do tipo Object e declarados pelo usuário.
Devem haver campos dos tipos: Int, Double, String, ObjectId.
"""

# #-- ---------------------------------------------------------------------------------------------------
# # AULA 33 - LISTAGEM DE DADOS - PARTE 1
# #-- ---------------------------------------------------------------------------------------------------
# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']
    
# dbname = get_database()
# collection_name = dbname["itens_soulcode"]

# # FIND É RESPONSAVEL POR EXIBIR OS DADOS
# """ PARA UTILIZAR O FIND, VOCÊ CRIA UMA VARIAVEL, ATRIBUI O MÉTODO E PERCORRE ESSA VARIAVEL PARA TER A IMPRESSÃO 
# DOS DADOS NO SEU MONGO DB """
# # detalhes_itens = collection_name.find()
# # for item in detalhes_itens:
# #     print(item)   


# #detalhes_itens = collection_name.find()    
# #detalhes_itens = collection_name.find({"categoria":"Online"})
# #detalhes_itens = collection_name.find({"$and" : [{"categoria":"Online"}, {"categoria":"Físico"}]})

# # AQUI ESTOU DIZENDO: ENCONTRE OS ARQUIVOS CUJO NOME ITEM COMECE COM A PALAVRA SE
# detalhes_itens = collection_name.find({"nome_item":{"$regex":"^Mi"}})
# for item in detalhes_itens:
#     print(item)

# #-- ---------------------------------------------------------------------------------------------------
# # AULA 34 - LISTAGEM DE DADOS - PARTE 2
# #-- ---------------------------------------------------------------------------------------------------
# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']
    
# dbname = get_database()
# collection_name = dbname["itens_soulcode"]


# #detalhes_itens = collection_name.distinct("nome_item")
# #detalhes_itens = collection_name.find({"categoria":"Físico"}).limit(1) # limita qtos elementos imprime
# detalhes_itens = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)
# for item in detalhes_itens:
#     print(item)
    
# #-- ---------------------------------------------------------------------------------------------------
# # AULA 35 - ATUALIZAÇÃO DE DADOS / 36 - EXCLUSÃO DE DADOS
# #-- ---------------------------------------------------------------------------------------------------
# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient
    
#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']

# dbname =get_database()
# collection_name = dbname["itens_soulcode"]

# #atualiza desconto_maximo de 10% para 35%.
# collection_name.update_many({"disconto_maximo":"10%"}, 
#     {"$set":{"disconto_maximo": "35%"}})

# #atualiza desconto para 100% onde nome_item tenha a palavra 'Aula'
# collection_name.update_one({ "nome_item": { "$regex": "Aula" } },
#     {"$set":{"disconto_maximo": "100%"}})

# #Exclui documento cujo ID é SC004
# collection_name.delete_one({"_id" : "SC004"})
# print("Dado deletado!")

# #Deleta todos os documentos
# collection_name.drop()
# dbname.drop_collection()

# detalhes_itens = collection_name.find()
# for item in detalhes_itens:
#     print(item)

# #-- ---------------------------------------------------------------------------------------------------
# # AULA 37 - EXERCÍCIO PRÁTICO
# #-- ---------------------------------------------------------------------------------------------------
"""
Crie um script contendo cinco funções:
Criar itens, onde o usuário pode selecionar a quantidade de campos;
Mostrar todos os documentos;
Deletar documentos pelo ID;
Deletar toda a coleção do banco de dados;
Atualizar documentos por ID ou por campos.
OBS: Não precisa criar menu para escolha das funções, elas podem ser chamadas.
"""

from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']

def cadastrarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']

    n = int(input("Quantos campos terá seu documento? "))
    d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
    print(d)
    collection_name.insert_one(d)
    print("Documento inserido com sucesso!")

def mostrarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)

def deletarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']
    documento = str(input("Qual o ID do item a ser deletado?"))
    collection_name.delete_one({"_id":documento})
    print("Documento exluído com sucesso!")
    
def deletarTudo():
    var = str(input("Deseja realmente deletar tudo? S/N"))
    dbname = get_database()
    collection_name = dbname['itens_soulcode']

    if (var == 'S'):
        collection_name.drop()
        dbname.drop_collection()
    elif (var=='N'):
        print("Nenhum dado foi excluído!")    

def atualizarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']
    temp = str(input("O que você deseja alterar?\n1-Atualizar por ID: \n2-Atualizar por campo: "))
    if (temp=="1"):
        id = str(input("Digite o ID as ser alterado: "))
        chave = str(input("Digite o campo a ser aletrado: "))
        valor = str(input("Digite o novo valor do campo digitado: "))

        collection_name.update_one({"_id":id}, {"$set":{chave:valor}})
        print("Modificação realizada!")
    elif (temp=="2"):
        chave = str(input("Digite a chave a ser buscada: "))
        valor = str(input("Digite o valor a ser buscado: "))
        chave2 = str(input("Digite a chave a ser alterada: "))
        valor2 = str(input("Digite o novo valor: "))

        collection_name.update_many({chave:valor}, {"$set":{chave2:valor2}})
        print("Modificação realizada!")

#cadastrarDocumento()
#deletarDocumento()
#deletarTudo()
atualizarDocumento()
mostrarDocumento()


#cadastrarDocumento()
#mostrarDocumento()
#deletarDocumento()
