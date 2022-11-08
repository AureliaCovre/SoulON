# #-- -------------------------------------------------------------------------------------
# # AULA 1 - INTRODUÇÃO
# #-- -------------------------------------------------------------------------------------

""" O Numpy é para codigos matematicos """
""" O Pandas é uma biblioteca para se trabalhar com tratamento de dados """

# #-- -------------------------------------------------------------------------------------
# # AULA 2 - SÉRIES
# #-- -------------------------------------------------------------------------------------
# import numpy as np
# import pandas as pd

# """ Séries nada mais é do que uma cadeia de dados unidimensional, ou seja só tem uma dimensão. é basicamenta
# uma cadeia de arrays, onde temos qqer tipo de dados nessa estrutura """

# #CRIANDO A SÉRIE
# notas = pd.Series([10,5,7.5,9,10])
# print(notas) # imprime o indice e os valores
# print(notas.values) #imprime apenas os valores: [10.   5.   7.5  9.  10. ]
# print(notas.index) #imprime os index : RangeIndex(start=0, stop=5, step=1) * step é que ele pula de um em um

# notas2 = pd.Series([10,5,7.5,9,10], index=["José", "Carlos", "André", "Pedro", "Maria"]) #Atribuir indices
# print(notas2)

# print(notas.describe()) # Apresenta dados estatisticos 
# print(notas.mean()) #printou a media 
# print(notas**2) #printou ao quadrado


# #-- -------------------------------------------------------------------------------------
# # AULA 3 - DATAFRAME
# #-- -------------------------------------------------------------------------------------

# """ DATAFRAME é um arranjo de dados bidimensional. Eles tem varias linhas e colunas enquanto a serie so
# tem uma coluna"""

# import numpy as np
# import pandas as pd

# df = pd.DataFrame({"Aluno": ["josé", "calos", "ana", "julia", "debora"],
#                    "Faltas":[3,4,2,4,3],
#                    "Prova": [2,7,8,5.5,9.2],
#                    "Seminario": [ 8.5,5,8.2,6,9.5]})

# print(df)

# #-- -------------------------------------------------------------------------------------
# # MODULO 2 - 
# #-- -------------------------------------------------------------------------------------
# ### AULA 4 - EXIBIÇÃO DE DADOS
# #-- -------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd

# df = pd.DataFrame({'Aluno':["José", "Carlos", "Ana", "Júlia", "Débora"],
#                    'Faltas':[3,4,2,4,3],
#                    'Prova': [2,7,8,5.5,9.2],
#                    'Seminário':[8.5,5,8.2,6,9.5]})
# #print(df)
# #print(df.dtypes)
# #print(df.columns)
# #print(df['Aluno'])
# #print(df.describe())
# #print(df.sort_values(by="Seminário"))
# #print(df.loc[3]) # para exibir um valor por índice
# #print(df[df["Seminário"] > 8.0])
# print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])

# #-- -------------------------------------------------------------------------------------
# ### AULA 5 - IMPORTANDO CSV / AULA 6 - MANIPULAÇÃO DE DADOS
# #-- -------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd

# df_csv = pd.read_csv("COLOQUE AQUI O ENDEREÇO DO ARQUIVO, SE FOR INTERNET COLOQUE O ENDEREÇO")
# #print(df_csv)
# #print(df_csv.head(3))
# print(df_csv.tail(3))

# #------------------------------------

# #print(df_csv['bairro'].unique())           # UNIQUE: filtra um dado sem repetição
# #print(df_csv['bairro'].value_counts())     # VALUE_COUNTS : para contar valores de um df
# #print(df_csv.groupby("bairro").mean())     # Apresenta a média de valores por bairro

# #------------------------------------
# # Criando um novo dataframe com os 5 primeiros itens do df anterior
# df2 = df_csv.head() 
# #print(df2)

# # Substituindo um valor por nan / replace - substitui
# df3 = df2.replace({"pm2":{12031.25:np.nan}})
# print(df3)


# df4 = df3.dropna() # remove as linhas com erro
# print(df4)


# #-- -------------------------------------------------------------------------------------
# ### AULA 7 - IMPORTANTO JSON
# #-- -------------------------------------------------------------------------------------
# import pandas as pd

# # df = pd.read_json("CAMINHO DO ARQUIVO")
# # print(df.to_string())


# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409.1,
#     "1":479.0,
#     "2":340.0,
#     "3":282.4,
#     "4":406.0,
#     "5":300.5
#   }
# }

# df = pd.DataFrame(data)
# print(df)


# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# # MODULO 3 - INTRODUÇÃO A MANIPULAÇÃO DE DADOS COM PYSPARK 
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# #-- -------------------------------------------------------------------------------------
# ### AULA 8 - HADOOP
# #-- -------------------------------------------------------------------------------------
"""    
    O QUE É?
            Hadoop é "um framework para desenvolvimento de aplicações distribuidas",
        com alta escalabilidade, confiabilidade e tolerância a falhas, subdividido em 
        três projetos: Hadoop, Commons, haddop Distribuited File System e Hadoop MapReduce.
        
    Armazenamento de dados.
        O Hadoop Distributed File System (HDFS) fornece armazenamento escalável e 
    tolerante a falhas, o custo_eficiente para o seu lago de dados grande.
    
    Processamento de dados:
        MapReduce é o quadro original para escrever aplicações massivamente paralelas que 
    que processam grandes quantidades de dados estruturados e não estruturados armazenados 
    em HDFS.  
    
    Acesso e análise de dados:
        Os aplicativos podem interagir com os dados no Hadoop usando lote ou SQL interativa
    (Apache Hive) ou o acesso de baixa latência com NoSQL (HBase).
    
    VANTAGENS:
    - Capacidade de armazenar e processar grandes quantidades de qualquer tipo de dado, e 
    rapidamente.
    - Poder computacional;
    - Tolerância a falhas;
    - Flexibilidade;
    - Custo baixo;
    - Escalabilidade;
    
    """
    
# #-- -------------------------------------------------------------------------------------
# ### AULA 9 - APACHE SPARK
# #-- -------------------------------------------------------------------------------------    
"""    
    O QUE É?
        O Apache Spark é uma ferramenta Big Data que tem o objetivo de processar grandes
    conjuntos de dados de forma paralela e distribuída.        
    
    * Principal diferença entre Hadoop x Spark:
        Enquanto o Haddop é um frame para desenvolvimento de aplicações distribuidas o Spark é 
    uma ferramenta para BIG Data. Basicamente o Spark é para processamento e manipulação de dados.  
        
    Usado por: Java, Python e Scala.
    
    CORE:
    - Spark SQL: Para utilização de SQL na realização de consultas e processamento sobre os dados no Spark. 
    - Spark Streaming: possibilita o processamento de fluxos em tempo real.
    - MLlib (machine learning): é a biblioteca de apresndizado de máquina, com diferentes algoritmos para 
    as mais diversas atividades, como clustering.
    - GraphX (graph): realiza o processamento sobre grafos.
    
    ESTRUTURA:
    Driver Program (SparkContext) --> Cluster Manager --> - Worker Node: Executor: Cache / Task / Task
                                                          - Worker Node: Executor: Cache / Task / Task 
                                                       
    -- Driver Program: é a aplicação principal, que gerencia a criação e quem executa os processamentos 
    definidos pelos programas.     
    -- Cluster Manager: é um componente opcional, só é necessario se o Spark for executado de forma distribuida.
    -- Worker Node: são os nós de execução       
    
    PRINCIPAIS COMPONENTES:
    - Resilient Distributed Datasets (RDD): Abstraem conjuntos de objetos distribuidos em um cluster, 
    geralmente executados na memoria principal. Podemos programar com ou sem eles. 
    - Operações: são as transformações que executamos.
    - Spark Context: é o contexto , propriamente dito a estrutura das nossas instruções que vamos fazer 
    utilizando o Apache Spark.                  
"""
# #-- -------------------------------------------------------------------------------------
# ### AULA 10 - PYSPARK
# #-- -------------------------------------------------------------------------------------   
"""
O QUE É?
    PySpark é uma biblioteca spark escrita em Python para executar o aplicativo Python usando recursos
Apache Spark. usando o PySpark podemos ececutar aplicativos paralelamente no cluster distribuído
(vários nós).

VANTAGENS:
- PySpark é um mecanismo de processamento distribuido de propodito geral, na memoria, que permite 
processar dados de forma eficiente de forma distribuida.
- As aplicações em execução no PySpark são 100x mais rapidas que os sistemas tradicionais. 
- Você terá grandes beneficios usando PySpark para ingestão de dados.
- Usando o PySpark, podemos processar dados de hadoop HDFS, AWS S3 e muitos sistemas de arquivos.
- Usando o streaming pySpark, você também pode transmitir arquivos do sistema de arquivos e tambem 
transmitir a partir do soquete.
- PySpark tem bibliotecas de aprendizado de máquina e gráficos. 


GERENCIADORES:
- Autônomo
- Apache Mesos
- Hadoop YARN
- Kubernetes

AMBIENTE:
--> Apache Spark Eco System:
                        - Spark SQL
                        - Spark Streaming
                        - Spark MLlib
                        - GraphX
                                --> Apache Spark Core API: 
                                                        - R
                                                        - Python
                                                        - Scala
                                                        - Java
                                                        - SQL
"""    
    
# #-- -------------------------------------------------------------------------------------
# ### AULA 11 - CONFIGURAÇÃO DO AMBIENE WINDOWS / AULA 12 - CONFIGURAÇÃO DO AMBIENE LINUX
# #-- -------------------------------------------------------------------------------------      


# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# # MODULO 4 - MANIPULAÇÃO DE DADOS COM PYSPARK
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=

# #-- -------------------------------------------------------------------------------------
# ### AULA 12 - INTRODUÇÃO, MONTANDO RDD / AULA 13 - LISTAGEM DE DADOS
# #-- -------------------------------------------------------------------------------------   
# import findspark
# findspark.init()

# from pyspark.sql import SparkSession

# # INICIANDO A SESSÃO COM SPARK
# spark = SparkSession.builder.master("local").appName("Aula Introdutória PySpark").config("spark.executor.memory", "1gb").getOrCreate()

# sc = spark.sparkContext

# rdd = sc.textFile("Salary_Data.csv")
# print("Concluído com sucesso!")    

# # COMANDOS DE LISTAGEM DE DADOS
# # rdd.take(5)
# rdd.first()

# rdd_new = rdd.map(lambda line: line.split(","))
# rdd_new.take(7)

# #-- -------------------------------------------------------------------------------------
# ### AULA 14 - ABORDANDO COLUNAS / 15 - ALTERANDO TIPOS DE DADOS / 16 - CONSULTA SIMPLES / 
# ### AULA 17 - CONSULTAS POR CONDIÇÕES
# #-- ------------------------------------------------------------------------------------- 
# import findspark
# findspark.init()

# from pyspark.sql import SparkSession
# from pyspark.sql import Row
# from pyspark.sql.types import *

# spark = SparkSession.builder \
#     .master("local") \
#     .appName("Aula Introdutória PySpark") \
#     .config("spark.executor.memory", "1gb") \
#     .getOrCreate()

# sc = spark.sparkContext

# rdd = sc.textFile("Salary_Data.csv")
# rdd = rdd.map(lambda line: line.split(","))

# df = rdd.map(lambda line: Row(AnosExperiencia=line[0], Salario=line[1])).toDF()
# # df.show()
# # df.printSchema()


# def converterColuna(dataframe, nomes, novoTipo):
#     for nome in nomes:
#         dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
#     return dataframe

# colunas = ['AnosExperiencia', 'Salario']

# #CONVERTENDO DE STRING PARA FLOAT
# df = converterColuna(df, colunas, FloatType())

# df.show()
# df.printSchema()

# CONSULTAS SIMPLES:
#df.select('Salario').show(10)  # DF.SELECT("COLUNA QUE DESEJA EXIBIR").SHOW(QTD DE ITENS)
#df.groupby('Salario').count().sort('Salario', ascending=False).show() 
#df.select('Salario').count()
#df.describe().show()
#df.describe('Salario').show()
#df.collect()

# CONSULTAS POR CONDIÇÕES:
#df.filter(df['Salario'] > 5000).show()
#df.select('Salario').filter(df['Salario'] > 5000).show()
#df.filter((df['Salario'] > 5000) | (df['AnosExperiencia'] > 2)).show()

# #-- -------------------------------------------------------------------------------------
# ### AULA 18 - DEFINIÇÃO DE ESQUEMA / 19 - OPERAÇÕES E CONSULTAS COM DF
# #-- ------------------------------------------------------------------------------------- 
# from pyspark.sql.session import SparkSession

# from pyspark.sql.types import (ArrayType, BooleanType, FloatType, IntegerType, StringType, StructField, StructType, TimestampType)

# import pyspark.sql.functions as F

# spark = SparkSession.builder.appName('fisrtSession')\
#     .config('spark.master', 'local[4]')\
#     .config('spark.executor.memory', '1gb')\
#     .config('spark.shuffle.partitions', 1)\
#     .getOrCreate()

# schema = StructType([
#                 StructField('case_id', IntegerType()),
#                 StructField('province', StringType()),
#                 StructField('city', StringType()),
#                 StructField('group', BooleanType()),
#                 StructField('infection_case', StringType()),
#                 StructField('confirmed', IntegerType()),
#                 StructField('latitude', StringType()),
#                 StructField('longitude', StringType())
# ])

# path = "covid_cases.csv"

# df = spark.read.format('csv')\
#     .schema(schema)\
#     .load(path)

# # df.printSchema()

# # CONSULTAS E OPERAÇÕES
# #cases = df.withColumnRenamed('infection_case', 'Casos de Infecção')
# #cases = df.toDF(*['ID', 'Província', 'Cidade', 'Grupo', 'Casos de Infecção', 'Confirmados', 'Latitude', 'Longitude'])
# #cases.show()

# df2 = df.select('province', 'city', 'confirmed')
# df2.show()
# df3 = df.sort(F.desc('confirmed'))
# df3.show()

# #-- -------------------------------------------------------------------------------------
# ### AULA 20 - IMPORTANDO ARQUIVOS JSON 
# #-- ------------------------------------------------------------------------------------- 
# from pyspark.sql.session import SparkSession
# from pyspark.sql.types import (ArrayType, BooleanType, FloatType, IntegerType, StringType, StructField, StructType, TimestampType, DoubleType)
# import pyspark.sql.functions as F

# spark = SparkSession.builder.appName('fisrtSession')\
#     .config('spark.master', 'local[4]')\
#     .config('spark.executor.memory', '1gb')\
#     .config('spark.shuffle.partitions', 1)\
#     .getOrCreate()

# schema = StructType([
#       StructField("RecordNumber",IntegerType()),
#       StructField("Zipcode",IntegerType()),
#       StructField("ZipCodeType",StringType()),
#       StructField("City",StringType()),
#       StructField("State",StringType()),
#       StructField("LocationType",StringType()),
#       StructField("Lat",DoubleType()),
#       StructField("Long",DoubleType()),
#       StructField("Xaxis",IntegerType()),
#       StructField("Yaxis",DoubleType()),
#       StructField("Zaxis",DoubleType()),
#       StructField("WorldRegion",StringType()),
#       StructField("Country",StringType()),
#       StructField("LocationText",StringType()),
#       StructField("Location",StringType()),
#       StructField("Decommisioned",BooleanType()),
#       StructField("TaxReturnsFiled",StringType()),
#       StructField("EstimatedPopulation",IntegerType()),
#       StructField("TotalWages",IntegerType()),
#       StructField("Notes",StringType())
#   ])

# df = spark.read.schema(schema)\
#     .json('E:\python_soul_on\zipcodes.json')

# df.printSchema()
# df.show()

# #-- -------------------------------------------------------------------------------------
# ### AULA 21 - MANIPULAÇÃO DE DADOS COM SQL
# #-- ------------------------------------------------------------------------------------- 
# from pyspark.sql.session import SparkSession
# from pyspark.sql.types import (ArrayType, BooleanType, FloatType, IntegerType, StringType, StructField, StructType, TimestampType, DoubleType)
# import pyspark.sql.functions as F

# spark = SparkSession.builder.appName('fisrtSession')\
#     .config('spark.master', 'local[4]')\
#     .config('spark.executor.memory', '1gb')\
#     .config('spark.shuffle.partitions', 1)\
#     .getOrCreate()

# schema = StructType([
#       StructField("RecordNumber",IntegerType()),
#       StructField("Zipcode",IntegerType()),
#       StructField("ZipCodeType",StringType()),
#       StructField("City",StringType()),
#       StructField("State",StringType()),
#       StructField("LocationType",StringType()),
#       StructField("Lat",DoubleType()),
#       StructField("Long",DoubleType()),
#       StructField("Xaxis",IntegerType()),
#       StructField("Yaxis",DoubleType()),
#       StructField("Zaxis",DoubleType()),
#       StructField("WorldRegion",StringType()),
#       StructField("Country",StringType()),
#       StructField("LocationText",StringType()),
#       StructField("Location",StringType()),
#       StructField("Decommisioned",BooleanType()),
#       StructField("TaxReturnsFiled",StringType()),
#       StructField("EstimatedPopulation",IntegerType()),
#       StructField("TotalWages",IntegerType()),
#       StructField("Notes",StringType())
#   ])

# df = spark.read.schema(schema)\
#     .json('E:\python_soul_on\zipcodes.json')

# df.registerTempTable('zipcodes')
# #output = spark.sql('SELECT * FROM zipcodes')
# #output = spark.sql('SELECT RecordNumber, Notes FROM zipcodes')
# output = spark.sql('SELECT RecordNumber FROM zipcodes WHERE RecordNumber > 10')
# output.show()


# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# # Módulo 05 – Introdução à visualização de dados
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# #-- ---------------------------------------------------------------------------------------------------------
# ### AULA 22 - INTRODUÇÃO A DATA VISUALIZATION COM PYTHON / 23 - DATA VISUALIZATION COM PANDAS
# ### AULA 24 - Data visuazliation com Seaborn / 25 - Data visualization com Matplotlib – Gráfico de barras
# #-- --------------------------------------------------------------------------------------------------------- 
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# #print(iris.head())
# wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
# #wine_reviews.head()

# # IRIS É O DATASET / PLOT = METODO DO PANDAS PARA PLOTAR UM GRAFICO / SCATTER É O NOME DO GRAFICO
# # iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')
# # wine_reviews['volatile_acidity'].plot.hist()
# # wine_reviews['style'].value_counts().sort_index().plot.bar()

# ### 24
# #sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)
# #sns.displot(wine_reviews['volatile_acidity'], bins=10, kde=True)
# #sns.countplot(wine_reviews['volatile_acidity'])

# ### 25 
# fig, ax = plt.subplots()

# data = wine_reviews['style'].value_counts()

# style = data.index
# frequency = data.values

# ax.bar(style,frequency)

# ax.set_title('Wine Review Scores')
# ax.set_xlabel('Style')
# ax.set_ylabel('Frequency')

# #-- -------------------------------------------------------------------------------------
### AULA 26 - Data visualization com Matplotlib – Gráfico de histograma
# #-- -------------------------------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt

# iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

# fig, ax = plt.subplots()

# ax.hist(wine_reviews['style'])

# ax.set_title('Wine Reviwe Scores')
# ax.set_xlabel('Style')
# ax.set_ylabel('Frequency')

# #-- -------------------------------------------------------------------------------------
### AULA 27 - Data visualization com Matplotlib – Gráfico de linha
# #-- -------------------------------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt

# iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

# columns = iris.columns.drop(['class'])
# x_data = range(0, iris.shape[0])
# fig, ax = plt.subplots()

# for column in columns:
#     ax.plot(x_data, iris[column], label=column)

# ax.set_title('Iris Dataset')
# ax.legend()

# #-- -------------------------------------------------------------------------------------
### AULA 28 - Data visualization com Matplotlib – Gráfico de scatter
# #-- -------------------------------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt

# iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

# fig, ax = plt.subplots()

# ax.scatter(iris['sepal_length'], iris['sepal_width'])

# ax.set_title('Iris Dataset')
# ax.set_xlabel('sepal_length')
# ax.set_ylabel('sepal_width')

# #-- -------------------------------------------------------------------------------------
### AULA 29 - Data visualization com Plotly
# #-- -------------------------------------------------------------------------------------
#pip install plotly==5.3.1
#pip install nbformat

# import plotly.express as px

# #Dataset Geral
# df = px.data.gapminder().query("country=='Canada'")

# #Linha
# '''
# fig = px.line(df,x="year", y="lifeExp", title='Life expectancy in Canada')
# fig.show()
# '''
# #Histograma
# '''
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill")
# fig.show()

# '''
# #Scatter
# fig = px.scatter(x=[0,1,2,3,4], y=[0,1,4,9,16])
# fig.show()


# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# # Módulo 06 –  Processo de ETL
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# #-- ---------------------------------------------------------------------------------------------------------
# ### AULA 30 - INTRODUÇÃO 
# #-- --------------------------------------------------------------------------------------------------------- 
"""
O QUE É ETL? EXTRACT (EXTRAÇÃO), TRANSFORM (TRANSFORMAÇÃO),  LOAD(CARREGAMENTO)  
"""

from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, 
                               TimestampType, StructType,
                               StructField, ArrayType,
                               FloatType)

import pyspark.sql.functions as F

spark = SparkSession.builder.appName('firstSeesion')\
   .config('spark.master', 'local')\
   .config("spark.executor.memory", "2gb") \
   .config('spark.shuffle.sql.partitions', 2)\
   .getOrCreate() 

#EXTRACT
## _id = pq no MongoDB isso significa que ele é o id principal
schema = StructType([StructField('target', StringType()),
                    StructField('_id', IntegerType()),
                    StructField('date', StringType()),
                    StructField('flag', StringType()),
                    StructField('user', StringType()),
                    StructField('text', StringType())
])

path = "E:/python_soul_on/training.1600000.processed.noemoticon.csv"

df = spark.read.format('csv')\
    .schema(schema)\
    .load(path)

df.printSchema()
df.show(5)


#TRANSFORM
df = df.drop('target', 'flag')

df = df.withColumn('day_week', df.date.substr(1,3))\
    .withColumn('day', df.date.substr(9,2))\
    .withColumn('month', df.date.substr(5,3))\
    .withColumn('time', df.date.substr(12,8))\
    .withColumn('year', df.date.substr(25,4))\
    .drop('date')

def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

colunas_string = ['day_week', 'month']
colunas_inteiro = ['day']
colunas_time = ['time']

df = converterColuna(df, colunas_string, StringType())
df = converterColuna(df, colunas_inteiro, IntegerType())
df = converterColuna(df, colunas_time, TimestampType())

df.printSchema()

#LOAD

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.qqxjf.mongodb.net"

    client = MongoClient(CONNECTION_STRING)

    return client['etl_soul_on']

dbname = get_database()
collection_name = dbname['data_load']

df = df.limit(20)
df = df.toPandas()
data_dict = df.to_dict('records')
collection_name.insert_many(data_dict)
print('Data Frame importado com sucesso!')
