import customtkinter as ctk
from models.Arquivo import Arquivo
from models.Ordenacao import Ordenacao as sort


class AnalisarAlgoritmos:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Analisar Algoritmos")
        self.janela.geometry("785x348")
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

        self.titulo_janela = ctk.CTkLabel(
            self.janela,
            text="Analisar Algoritmos",
            font=('arial', 30))
        self.titulo_janela.grid(row=0, column=0, pady=10)

        self.label_lista = ctk.CTkLabel(
            self.janela,
            text=f'{lista[0]}, {lista[1]}, {lista[2]}, [...], {
                lista[-3]}, {lista[-2]}, {lista[-1]}'
        )
        self.label_lista.grid(row=1, column=0)

        self.btn_ordenar_lista = ctk.CTkButton(
            self.janela,
            text='VOLTAR',
            command=lambda: self.voltar()
        )
        self.btn_ordenar_lista.grid(row=2, column=0, pady=10)

        self.btn_ordenar_lista = ctk.CTkButton(
            self.janela,
            text='Ordenar lista',
            command=lambda: self.mostrarResultado(lista)
        )
        self.btn_ordenar_lista.grid(row=3, column=0)

        # Criando layout de Quicksort
        self.label_lista_ordenada = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.label_lista_ordenada.grid(row=4, column=0)

        self.titulo_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.titulo_quicksort.grid(row=5, column=0, pady=0, padx=0)

        self.operacoes_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.operacoes_quicksort.grid(row=6, column=0, pady=0, padx=0)

        self.caso_medio_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.caso_medio_quicksort.grid(row=7, column=0, pady=0, padx=0)

        self.pior_caso_quicksort = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.pior_caso_quicksort.grid(row=8, column=0, pady=0, padx=0)

        # Criando layout de Ordenação por seleção
        self.lista_ordenada_por_selecao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.lista_ordenada_por_selecao.grid(row=4, column=1)

        self.titulo_por_selecao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.titulo_por_selecao.grid(row=5, column=1, pady=0, padx=0)

        self.operacoes_por_selecao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.operacoes_por_selecao.grid(row=6, column=1, pady=0, padx=0)

        self.caso_medio_por_selecao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.caso_medio_por_selecao.grid(row=7, column=1, pady=0, padx=0)

        self.pior_caso_por_selecao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.pior_caso_por_selecao.grid(row=8, column=1, pady=0, padx=0)

        # Criando layout de Ordenação por inserção
        self.lista_ordenada_por_insercao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.lista_ordenada_por_insercao.grid(row=4, column=2)

        self.titulo_por_insercao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.titulo_por_insercao.grid(row=5, column=2, pady=0, padx=0)

        self.operacoes_por_insercao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.operacoes_por_insercao.grid(row=6, column=2, pady=0, padx=0)

        self.caso_medio_por_insercao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.caso_medio_por_insercao.grid(row=7, column=2, pady=0, padx=0)

        self.pior_caso_por_insercao = ctk.CTkLabel(
            self.janela,
            text=f''
        )
        self.pior_caso_por_insercao.grid(row=8, column=2, pady=0, padx=0)

    def mostrarResultado(self, lst):
        # Mostrando resultado do algoritmo quicksort
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

        # Mostrando resultado do algoritmo de ordenação por seleção
        resultado_por_selecao = sort.porSelecao(lst)
        lista_ordenada = resultado_por_selecao['lista_ordenada']
        operacoes_por_seleção = resultado_por_selecao['operacoes']

        self.titulo_por_selecao.configure(
            text='ORDENAÇÃO POR SELEÇÃO'
        )

        self.lista_ordenada_por_selecao.configure(
            text=f'{lista_ordenada[0]}, {lista_ordenada[1]}, {lista_ordenada[2]}, ..., {lista_ordenada[-3]}, {lista_ordenada[-2]}, {lista_ordenada[-1]}')
        self.operacoes_por_selecao.configure(
            text=f'Operações realizadas: {operacoes_por_seleção}')

        caso_medio = sort.calcularBigO(
            tamanho_lista=len(lst),
            algoritmo='por_selecao',
            caso='medio')

        pior_caso = sort.calcularBigO(
            tamanho_lista=len(lst),
            algoritmo='por_selecao',
            caso='pior')

        self.caso_medio_por_selecao.configure(
            text=f'Caso médio: {caso_medio}'
        )
        self.pior_caso_por_selecao.configure(
            text=f'Pior caso: {pior_caso}'
        )

        # Mostrando resultado do algoritmo de ordenação por inserção
        resultado_por_insercao = sort.porInsercao(lst)
        lista_ordenada = resultado_por_insercao['lista_ordenada']
        operacoes_por_seleção = resultado_por_insercao['operacoes']

        self.titulo_por_insercao.configure(
            text='ORDENAÇÃO POR INSERÇÃO'
        )

        self.lista_ordenada_por_insercao.configure(
            text=f'{lista_ordenada[0]}, {lista_ordenada[1]}, {lista_ordenada[2]}, ..., {lista_ordenada[-3]}, {lista_ordenada[-2]}, {lista_ordenada[-1]}')
        self.operacoes_por_insercao.configure(
            text=f'Operações realizadas: {operacoes_por_seleção}')

        caso_medio = sort.calcularBigO(
            tamanho_lista=len(lst),
            algoritmo='por_insercao',
            caso='medio')

        pior_caso = sort.calcularBigO(
            tamanho_lista=len(lst),
            algoritmo='por_insercao',
            caso='pior')

        self.caso_medio_por_insercao.configure(
            text=f'Caso médio: {caso_medio}'
        )
        self.pior_caso_por_insercao.configure(
            text=f'Pior caso: {pior_caso}'
        )

        # Centralizando botões
        self.titulo_janela.grid(row=0, column=1)
        self.label_lista.grid(row=1, column=1)
        self.btn_ordenar_lista.grid(row=2, column=1)

    def voltar(self):
        from Menu import Menu
        self.janela.destroy()
        menu = Menu()
        menu.janela.mainloop()