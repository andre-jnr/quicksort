import customtkinter as ctk
from models.Arquivo import Arquivo
from models.Ordenacao import Ordenacao as sort


class AnalisarAlgoritmos:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Analisar Algoritmos")
        self.janela.geometry("500x348")
        self.arquivo = Arquivo('dados200.txt')
        self.janela.grid_columnconfigure(0, weight=1)

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
            font=('arial', 30)).grid(row=0, column=0, pady=10)

        label_lista = ctk.CTkLabel(
            self.janela,
            text=f'{lista[0]}, {lista[1]}, {lista[2]}, [...], {
                lista[-3]}, {lista[-2]}, {lista[-1]}'
        ).grid(row=1, column=0)

        btn_ordenar_lista = ctk.CTkButton(
            self.janela,
            text='Ordenar lista',
            command=lambda: self.quicksort(lista)
        ).grid(row=2, column=0)

        self.label_lista_ordenada = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.label_lista_ordenada.grid(row=3, column=0)

        self.titulo_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.titulo_quicksort.grid(row=4, column=0, pady=0, padx=0)

        self.operacoes_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.operacoes_quicksort.grid(row=5, column=0, pady=0, padx=0)

        self.caso_medio_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.caso_medio_quicksort.grid(row=6, column=0, pady=0, padx=0)

        self.pior_caso_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.pior_caso_quicksort.grid(row=7, column=0, pady=0, padx=0)

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
            text=f'Operações realizadas: {operacoes_quicksort}')

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
