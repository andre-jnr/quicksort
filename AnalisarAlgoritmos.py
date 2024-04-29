import customtkinter as ctk
from models.Arquivo import Arquivo
from models.Ordenacao import Ordenacao as sort


class AnalisarAlgoritmos:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Analisar Algoritmos")
        self.janela.geometry("500x348")
        self.arquivo = Arquivo('dados200.txt')

        self.criar_componenetes()
        self.janela.mainloop()

    def criar_componenetes(self):
        self.arquivo.inicializarBaseDeDados()
        lista = self.arquivo.listarNomes()

        self.titulo = ctk.CTkLabel(
            self.janela,
            text="Quicksort"
        )

        titulo_janela = ctk.CTkLabel(
            self.janela,
            text="Analisar Algoritmos",
            font=('arial', 30)).pack(pady=10)

        label_lista = ctk.CTkLabel(
            self.janela,
            text=f'{lista[0]}, {lista[1]}, {lista[2]}, [...], {
                lista[-3]}, {lista[-2]}, {lista[-1]}'
        ).pack()

        btn_ordenar_lista = ctk.CTkButton(
            self.janela,
            text='Ordenar lista',
            command=lambda: self.quicksort(lista)
        ).pack()

        self.label_lista_ordenada = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.label_lista_ordenada.pack()

        self.titulo_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.titulo_quicksort.pack()

        self.operacoes_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.operacoes_quicksort.pack()

        self.caso_medio_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.caso_medio_quicksort.pack()

        self.pior_caso_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.pior_caso_quicksort.pack()

    def quicksort(self, lst):
        json = sort.quicksort(lst)
        lista_ordenada = json['lista_ordenada']
        operacoes_quicksort = json['operacoes']

        self.titulo_quicksort.configure(
            text='QUICKSORT'
        )

        self.label_lista_ordenada.configure(
            text=f'{lista_ordenada[0]}, {lista_ordenada[1]}, {lista_ordenada[2]}, ..., {lista_ordenada[-3]}, {lista_ordenada[-2]}, {lista_ordenada[-1]}')
        self.operacoes_quicksort.configure(
            text=f'Operações: {operacoes_quicksort}')

        caso_medio = sort.calcularBigO(
            tamanho_lista=len(lst),
            algoritmo='quicksort',
            caso='medio')

        pior_caso = sort.calcularBigO(
            tamanho_lista=len(lst),
            algoritmo='quicksort',
            caso='pior')

        self.caso_medio_quicksort.configure(
            text=f'Caso médio: {caso_medio}'
        )
        self.pior_caso_quicksort.configure(
            text=f'Pior caso: {pior_caso}'
        )
