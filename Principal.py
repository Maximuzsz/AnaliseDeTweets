from tkinter import *
from busca import Busca_tweet



class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10", "bold")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 5
        self.quartoContainer["pady"] = 5
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados do Meio Ambiente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Digite Aqui:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.texto = Entry(self.segundoContainer)
        self.texto["width"] = 30
        self.texto["font"] = self.fontePadrao
        self.texto.pack(side=LEFT)
 
  
        self.buscar = Button(self.terceiroContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.twite
        self.buscar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.grafi = Button(self.quartoContainer)
        self.grafi["text"] = "Analisar"
        self.grafi["font"] = ("Calibri", "8")
        self.grafi["width"] = 12
        self.grafi["command"] = self.analise
        self.grafi.pack()
  
        
  
    #Método que busca no twitter
    def twite(self):
        chave = str(self.texto.get())
        Busca_tweet.busca(chave)
        self.mensagem["text"] = 'Busca finalizada'
    

    #método que chama a analise dos dados
    def analise(self):
        tt= Teste.sentimento()
   
       

  
  
janela = Tk()
janela.columnconfigure(0, minsize=250)
janela.rowconfigure([0, 1], minsize=300)
Application(janela)
janela.mainloop()

