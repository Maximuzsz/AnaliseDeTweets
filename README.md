# IA_Analise_Tweets

O Programa em questão  faz buscas no twiter atrávez de uma chave digitada pelo usuário, e retorna através de um gráfico os dados obtidos ao analisar cada tweet e se foi algo positivo ou negativo.

analise.py - Classe que utiliza o algoritmo de Naives Bayes e analisa cada tweet obtido e guarda seu resultado para ser apresentado ao usuário.
busca.py  - utiliza a api do twiter através do tweepy para obter os tweets apartir de uma palavra chave.
grafico.py - utiliza o matplotlib para criar um gráfico de barras apresentando cada dia de tweets obtidos e o resutado da análise dos tweets daquele referido dia.
principal.py  - Utilisa o tkinter para apresentar ao usuário uma interface básica para que possa obter a palavra chave de busca de tweets.
