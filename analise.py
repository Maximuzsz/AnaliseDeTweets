from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from grafico import Gerador

def exibir_resultado(valor):
    frase, resultado = valor
    resultado = "Frase positiva" if resultado[0] == '1' else "Frase negativa"
    print(frase, ":", resultado)

def analisar_frase(classificador, vetorizador, frase):
        return frase, classificador.predict(vetorizador.transform([frase]))

def obter_dados_das_fontes():
        diretorio_base = 'C:\\Users\\Maximuz\\Documents\\treino.txt'

        with open(diretorio_base , "r") as arquivo_texto:
            dados = arquivo_texto.read().split('\n')
         
        return dados

def tratamento_dos_dados(dados):
        dados_tratados = []
        for dado in dados:
            if len(dado.split("\t")) == 2 and dado.split("\t")[1] != "":
                dados_tratados.append(dado.split("\t"))

        return dados_tratados

def dividir_dados_para_treino_e_validacao(dados):
        quantidade_total = len(dados)
        percentual_para_treino = 0.75
        treino = []
        validacao = []

        for indice in range(0, quantidade_total):
            if indice < quantidade_total * percentual_para_treino:
                treino.append(dados[indice])
            else:
                validacao.append(dados[indice])

        return treino, validacao

def pre_processamento():
        dados = obter_dados_das_fontes()
        dados_tratados = tratamento_dos_dados(dados)

        return dividir_dados_para_treino_e_validacao(dados_tratados)


def realizar_treinamento(registros_de_treino, vetorizador):
        treino_comentarios = [registro_treino[0] for registro_treino in registros_de_treino]
        treino_respostas = [registro_treino[1] for registro_treino in registros_de_treino]

        treino_comentarios = vetorizador.fit_transform(treino_comentarios)

        return BernoulliNB().fit(treino_comentarios, treino_respostas)

def realizar_avaliacao_simples(registros_para_avaliacao):
        avaliacao_comentarios = [registro_avaliacao[0] for registro_avaliacao in registros_para_avaliacao]
        avaliacao_respostas = [registro_avaliacao[1] for registro_avaliacao in registros_para_avaliacao]

        total = len(avaliacao_comentarios)
        acertos = 0
        for indice in range(0, total):
            resultado_analise = analisar_frase(classificador, vetorizador, avaliacao_comentarios[indice])
            frase, resultado = resultado_analise
            acertos += 1 if resultado[0] == avaliacao_respostas[indice] else 0

        return acertos * 100 / total

def realizar_avaliacao_completa(registros_para_avaliacao):
        avaliacao_comentarios = [registro_avaliacao[0] for registro_avaliacao in registros_para_avaliacao]
        avaliacao_respostas = [registro_avaliacao[1] for registro_avaliacao in registros_para_avaliacao]

        total = len(avaliacao_comentarios)
        verdadeiros_positivos = 0
        verdadeiros_negativos = 0
        falsos_positivos = 0
        falsos_negativos = 0

        for indice in range(0, total):
            resultado_analise = analisar_frase(classificador, vetorizador, avaliacao_comentarios[indice])
            frase, resultado = resultado_analise
            if resultado[0] == '0':
                verdadeiros_negativos += 1 if avaliacao_respostas[indice] == '0' else 0
                falsos_negativos += 1 if avaliacao_respostas[indice] != '0' else 0
            else:
                verdadeiros_positivos += 1 if avaliacao_respostas[indice] == '1' else 0
                falsos_positivos += 1 if avaliacao_respostas[indice] != '1' else 0

        return (verdadeiros_positivos * 100 / total, 
                 verdadeiros_negativos * 100 / total,
                 falsos_positivos * 100 / total,
                 falsos_negativos * 100 / total)    
registros_de_treino, registros_para_avaliacao = pre_processamento()
vetorizador = CountVectorizer(binary = 'true')
classificador = realizar_treinamento(registros_de_treino, vetorizador)

class Teste:

  
    def sentimento():

        #seta as varáveis que receberão a quantidade de tweeets positivos e negativos de cada dia
        dia1_positivo = dia1_negativo = 0
        dia2_positivo = dia2_negativo = 0
        dia3_positivo = dia3_negativo = 0
        dia4_positivo = dia4_negativo = 0
        dia5_positivo = dia5_negativo = 0

        # abre a base de dados de cada dia
        dia1= open('C:\\Users\\Maximuz\\Documents\\dia1.txt', 'r')
        dia2= open('C:\\Users\\Maximuz\\Documents\\dia2.txt', 'r')
        dia3= open('C:\\Users\\Maximuz\\Documents\\dia3.txt', 'r')
        dia4= open('C:\\Users\\Maximuz\\Documents\\dia4.txt', 'r')
        dia5= open('C:\\Users\\Maximuz\\Documents\\dia5.txt', 'r')

        #lê cada base de dados e conta o resultado da análise
        for linha in dia1:
            if analisar_frase(classificador, vetorizador,linha)[1] == '1':
                dia1_positivo = dia1_positivo + 1     
            else: dia1_negativo = dia1_negativo + 1
                

        for linha in dia2:
            if analisar_frase(classificador, vetorizador,linha)[1] == '1':
                dia2_positivo = dia2_positivo + 1     
            else: dia2_negativo = dia2_negativo + 1
                
        for linha in dia3:
            if analisar_frase(classificador, vetorizador,linha)[1] == '1':
                dia3_positivo = dia3_positivo + 1     
            else: dia3_negativo = dia3_negativo + 1
                
        for linha in dia4:
            if analisar_frase(classificador, vetorizador,linha)[1] == '1':
                dia4_positivo = dia4_positivo + 1     
            else: dia4_negativo = dia4_negativo + 1
                
        for linha in dia5:
            if analisar_frase(classificador, vetorizador,linha)[1] == '1':
                dia5_positivo = dia5_positivo + 1     
            else: dia5_negativo = dia5_negativo + 1


        #fechando a base de dados
        dia1.close()
        dia2.close()
        dia3.close()
        dia4.close()
        dia5.close()
        

        #chama a classe que gera o gráfico
        Gerador.resultado(dia1_positivo,dia1_negativo,dia2_positivo,dia2_negativo,dia3_positivo,dia3_negativo,dia4_positivo,dia4_negativo,dia5_positivo,dia5_negativo)


         