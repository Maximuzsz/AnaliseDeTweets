import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta 

class Gerador():
    def resultado(dia1_positivo,dia1_negativo,dia2_positivo,dia2_negativo,dia3_positivo,dia3_negativo,dia4_positivo,dia4_negativo,dia5_positivo,dia5_negativo):
        
        #pega cada dia da análise
        dia1= datetime.today().strftime('%d')
        dia2=(datetime.today() - timedelta(days=1)).strftime('%d')
        dia3=(datetime.today() - timedelta(days=2)).strftime('%d')
        dia4=(datetime.today() - timedelta(days=3)).strftime('%d')
        dia5=(datetime.today() - timedelta(days=4)).strftime('%d')

        # seta nas labels do gráfico cada dia que foi análisado
        labels = [dia1,dia2,dia3,dia4,dia5]

        #seta o array com os dados da análise
        dias_negativos = [dia1_negativo,dia2_negativo,dia3_negativo,dia4_negativo,dia5_negativo]
        dias_positivos = [dia1_positivo,dia2_positivo,dia3_positivo,dia4_positivo,dia5_positivo]
        
        #define o tamanho da visualização
        x = np.arange(len(labels))  
        width = 0.40

        fig, ax = plt.subplots()
        #cria as barras com seus devidos dados
        rects1 = ax.bar(x - width/2, dias_negativos, width, label='Twites Negativos')
        rects2 = ax.bar(x + width/2, dias_positivos, width, label='Twites Positivos')

        #cria o titulo do gráfico
        ax.set_title('Dados Referente ao mês'+ datetime.today().strftime('%m'))
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        #gera o gráfico
        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3), 
                            textcoords="offset points",
                            ha='center', va='bottom')


        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        plt.show()


