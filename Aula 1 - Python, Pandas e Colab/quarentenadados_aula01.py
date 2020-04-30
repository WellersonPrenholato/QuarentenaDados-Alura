# -*- coding: utf-8 -*-
"""QuarentenaDados - aula01

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U27_RSEJtMk6eHpQ3atCNIgHln2y7kl9

##Lendo os dados do MovieLens
- Importação a biblioteca pandas, um poderoso projeto open source para análise de manipulação de dados. O primeiro passo é ler uma base de dados e podemos fazer isso com o comando `pd.read_csv()`.

- Estamos lendo um arquivo CSV (Comma-separated values), neste tipo de arquivo os valores são separados por vírgulas e podem ser abertos em outras ferramentas como excel e google-sheet. CSV não é o único formato lido pelo pandas, temos o `pd.read_excel()` que lê arquivos xlsx entre diversos outros formatos, você pode encontrar mais informações na seção de input/output da documentação.

- Depois de ler o dataset, nós trocamos os nomes das colunas pelos termos em português, logo em seguida utilizamos o método `filmes.head()` para visualizar as primeiras 5 linhas do nosso dataframe. Outra forma de visualizar as informações dos dados é utilizando o método `filmes.sample()`, se você tentar, vai verificar que ele retorna uma linha aleatória do seus dados. Para escolher aleatoriamente mais de 1 linha, por exemplo 5, é só passar esse valor desejado como parâmetro `(filmes.sample(5))`.
"""

#Importar Biblioteca
import pandas as pd

filmes = pd.read_csv("https://raw.githubusercontent.com/WellersonPrenholato/QuarentenaDados-Alura/master/Aula%201%20-%20Python%2C%20Pandas%20e%20Colab/ml-latest-small/movies.csv")
# filmes é um DataFrame
filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()

# lendo a documentação de um método/atributo
#?filmes.head

# lendo a documentação do tipo (docstring)
#?filmes

avaliacoes = pd.read_csv("https://raw.githubusercontent.com/WellersonPrenholato/QuarentenaDados-Alura/master/Aula%201%20-%20Python%2C%20Pandas%20e%20Colab/ml-latest-small/ratings.csv")
avaliacoes.head()

"""Para visualizar algumas linhas estamos usando o .head(), como ela mostra apenas as 5 primeiras linhas não sabemos qual é a quantidade de linhas que temos. Para descobrir a "forma" dos nossos dados podemos utilizar o avaliacoes.shape, retornando uma tupla, onde o primeiro termo indica o número de linhas e o segundo o número de colunas."""

avaliacoes.shape

len(avaliacoes)

"""Substituição dos nomes das colunas de inglês para português e o que significa cada coluna:

usarioId => ID para para usuário que votou em determinado filme.

filmeId => ID para identificar um filme votado.

nota => A nota dada para pelo usuário para o respectivo filme.

momento => A data da votação que não está formatada como data

Como cada linha contém um voto para o respectivo filme é de se esperar que um filme tenha diversos votos, mas repare que nas 5 primeiras linhas temos o filme 1, 3, 6, 47, 50. Mas e se eu quiser analisar apenas as notas do filme 1, como posso separar essa informação?
"""

avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]
avaliacoes.head()

"""Uma forma para "separar" as informações apenas do filmeId 1 é chamando o método avaliacaoes.query("filmeId==1"), esse método retornará apenas as linhas para quais a expressão booleana, "filmeId==1", for verdadeira.

Tendo as informações do filmeId 1 podemos chamar o avaliacoes_do_filme_1.describe(), para analisar as estatítiscas gerais dos dados.
"""

avaliacoes_do_filme_1 = avaliacoes.query("filmeId==1")
avaliacoes_do_filme_1.head()

avaliacoes_do_filme_1.describe()

"""Caso queira uma estatística particular, podemos apenas chamar o método desajado, repare abaixo como calculamos apenas a média das avaliações do filmeId 1."""

avaliacoes_do_filme_1.mean()

"""Calculamos as estatísicas apenas para o filmeId 1, mas também podemos chamar o método .describe() para a base completa (avaliacões)."""

avaliacoes.describe()

avaliacoes["nota"]

"""Com o comando avaliacoes["nota"], obtemos os valores da coluna nota (repare que o tipo retornado é uma Série pandas, por isso o index de cada nota é mantido). Para calcular a média de todas as notas executamos avaliacoes["notas"].means()"""



avaliacoes["nota"].mean()

"""Nós calculamos uma média geral, uma média para o filmeId 1. Agora eu quero calcular a média das notas para todos os filmes, podemos fazer isso usando o método `.groupby(filmeId)`, o parâmetro passado é para indicar qual coluna ele deve utilizar para "agrupar" os dados. Depois só calcular a média como fizemos anteriormente."""

notas_medias_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
notas_medias_por_filme.head()

"""Temos as notas médias calculadas, mas agora precisamos juntar as informações de notas médias com a base de dados filmes.

Poderíamos criar uma nova coluna e atribuir a váriável `notas_medias_por_filme`, de forma direta:

`filmes["nota_media"] = notas_medias_por_filme`

essa não é uma boa prática pois precisamos garantir que a nota média seja do respectivo filme.

Para garantir essa condição vamos utilizar o `.join()`, criando um novo dataframe `(filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId"))`.
"""

filmes

notas_medias_por_filme

filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
filmes_com_media.head()

"""Dataframe ordenado pela nota de forma decrescente."""

filmes_com_media.sort_values("nota", ascending=False).head(15)

"""O pandas facilita muito o plot de alguns gráficos simples, apenas selecionamos a informação que gostaríamos de visualizar e chamamos o método .plot()"""

avaliacoes.query("filmeId == 1")["nota"].plot()

"""Por padrão o método plotou um gráfico de linhas, o que não é adequado para os dados que estamos analisando.

Precisamos mudar o tipo de gráfico para realizar uma análise mais adequada, para fazer isso apenas alteramos o parâmetro kind do método .plot. Vamos plotar um histograma rodando a célula a seguir.
"""

avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist')

"""Antes de analisar o histograms de outros filmes, quero colocar um título na imagem."""

avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist',
                                              title="Avaliações do filme Toy Story")

"""Claro que python tem outras ferramentas muito poderosas para manipular gráficos, uma delas é o matplotlib.
Importação da lib e adição do título no gráfico usando o matplotlib,
"""

import matplotlib.pyplot as plt

avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist')
plt.title("Avaliações do filme Toy Story")
plt.show()

avaliacoes.query("filmeId == 2")["nota"].plot(kind='hist',
                                              title="Avaliações do filme Toy Jumanji")

avaliacoes.query("filmeId == 102084")["nota"].plot(kind='hist',
                                                   title="Avaliações do filme Justice League: Doom")

"""A primeira coisa que preciso saber é o que cada eixo do meu gráfico significa. Então, eixo x mostra a nota, enquanto eixo y a frequência das notas (quantas vezes determinada nota foi dada).

Entendido nosso gráfico, vamos contextualizar o cenário que estamos analisando:

Temos 3 filmes, dois muito populares (Toy story e Jumanji) e outro que nenhuma pessoa presente no momento da aula conhecia (animação da liga da justiça). O ponto que chamou a atenção, foi que a animação tinha média de nota maior que dois filmes, aparentemente mais popular, Jumaji e Toy Story. Será que a animação é um filme tão bom assim?
Dado esse cenário a primeira coisa que me chama a atenção é a animação da liga da justiça ter média de nota igual a 5. Ao analisar o histograma do respectivo filme, verificamos que ele só teve uma avaliação igual a 5, logo, fica evidente que a quantidade de votos é um aspecto importante na avaliação das médias. Com apenas uma avaliação, não conseguimos garantir que o filme é realmente bom, tornando a avaliação muito "volátil". Imagina que Liga da Justiça receba mais uma avaliação, com nota 0, assim a média seria 2.5. Apenas com mais essa avaliação o filme passaria a ser considerada um "pior" que Jumanji e Toy Story.

Outro ponto interessante é comparar o histograma de Toy Story e Jumanji, ambos tem médias "relativamente próximas". Mas repare que a distribuição de notas são diferentes, Toy Story recebe mais notas 5 e 4 que qualquer outra nota, enquanto Jumanji recebe mais notas 4 e 3, assim concluímos que a distribuição das notas também é um fator importante na avaliação das médias.

## Desafios

**Desafio 1**
- Determine quantos filmes não tem avaliações e quais são esses filmes.
"""

selecao = filmes_com_media['nota'].isnull()
filmes_com_media[selecao]

"""**Desafio 2**
- Mudar o nome da coluna nota do dataframe filmes_com_media para nota_média após o join.
"""

filmes_com_media = filmes_com_media.rename(columns={'nota': 'nota_media'})
filmes_com_media.head()

"""**Desafio 3** 
- Colocar o número de avaliações por filme, isto é, não só a média mas o TOTAL de votos por filme.
"""

total_votos_por_filme = avaliacoes.groupby('filmeId')['nota'].count()
total_votos_por_filme.head()

filmes_com_media_e_votos = filmes_com_media.join(total_votos_por_filme, on='filmeId')
filmes_com_media_e_votos = filmes_com_media_e_votos.rename(columns={'nota': 'total_votos'})
filmes_com_media_e_votos.head()

"""**Desafio 4**
- Arredondar as médias (coluna de nota média) para duas casas decimais.
"""

filmes_com_media_e_votos['nota_media'] = filmes_com_media_e_votos['nota_media'].round(2)
filmes_com_media_e_votos

"""**Desafio 5**
- Descobrir os generos dos filmes (quais são eles, únicos).
"""

generos_df = filmes_com_media_e_votos.generos.str.get_dummies('|')
generos = generos_df.columns.to_list()
generos

"""**Desafio 6**
- Contar o número de aparições de cada genero.
"""

total_filmes_por_genero = filmes_com_media_e_votos.generos.str.get_dummies().sum()
total_filmes_por_genero

"""**Desafio 7**
- Plotar o gráfico de aparições de cada genero. Pode ser um gráfico de tipo igual a barra.
"""

total_filmes_por_genero.sort_values(ascending=False).plot(kind='bar', figsize=(16, 6))