import tweepy as tw
import sys
from datetime import datetime, timedelta 
import unicodedata
import re

class Busca_tweet:
    def busca(tema):
        #chaves de autenticação
        consumer_key = 'rO5fC7yEVz3xT792do8FUMXTc'
        consumer_secret = 'DQ5hyracv91MUSaSe3026zpKEfoYap80eqdpFS0dvY8M7QdQSK'
        access_token = '924617913721552896-amDvizFkto8KeUGmJSMpR8Khs5gbZvm'
        access_token_secret = '4dFC58oDQR1k2gX1LCCYt3I7FkjYIAfzBhF9AC6kDo7hR'

        #efetuando a autenticação com o twiter
        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        twitter = tw.API(auth)
        api = tw.API(auth)

        #adciona o filtro de retweet
        search_words =tema + "-filter:retweets"

        #adciona apartir de qual dia os tweets serão buscados
        data_atual = datetime.today() - timedelta(days=4)
        data_atual=data_atual.date()

        #busacando os tweets de acordo os parâmetros definidos
        tweets = tw.Cursor(api.search, q=search_words, since =data_atual).items(2000)



        #base de dados de cada dia
        dia1= open('C:\\Users\\Maximuz\\Documents\\dia1.txt', 'w')
        dia2= open('C:\\Users\\Maximuz\\Documents\\dia2.txt', 'w')
        dia3= open('C:\\Users\\Maximuz\\Documents\\dia3.txt', 'w')
        dia4= open('C:\\Users\\Maximuz\\Documents\\dia4.txt', 'w')
        dia5= open('C:\\Users\\Maximuz\\Documents\\dia5.txt', 'w')



        for tweet in tweets:


               # Unicode normalize transforma um caracter em seu equivalente em latin.
               nfkd = unicodedata.normalize('NFKD', tweet.text)
               palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

               # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
               te =re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
               
               print(tweet.created_at)
               #condicional que verifica o dia do tweet e o adciona na base do seu respectivo dia
               if tweet.created_at.date() == (datetime.today().date()):
                   dia1.write(te +'\n')

               elif  tweet.created_at.date() == (datetime.today() - timedelta(days=1)).date():
                   dia2.write(te +'\n')

               elif  tweet.created_at.date() == (datetime.today() - timedelta(days=2)).date():
                   dia3.write(te +'\n')

               elif tweet.created_at.date() == (datetime.today() - timedelta(days=3)).date():
                   dia4.write(te +'\n')

               elif tweet.created_at.date() == (datetime.today() - timedelta(days=4)).date():
                   dia5.write(te +'\n')

   

        #fechando a base de dados
        dia1.close()
        dia2.close()
        dia3.close()
        dia4.close()
        dia5.close()
                



