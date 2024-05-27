import customtkinter as ctk
from models.Arquivo import Arquivo
from screens.VisualizarNomes import VisualizarNome


class ConsultarDados:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Consultar Dados")
        self.janela.geometry("785x348")
        self.arquivo = Arquivo('dados200.txt')
        self.janela.grid_columnconfigure(0, weight=1)

        self.criar_componenetes()
        self.janela.mainloop()

    def criar_componenetes(self):
        self.arquivo.inicializarBaseDeDados()
        self.lista = self.arquivo.listarNomes()

        self.titulo = ctk.CTkLabel(
            self.janela,
            text="Consultar Dados",
            font=('arial', 50)
        )
        self.titulo.grid(row=0, column=0, pady=10, padx=0)

        btn_adicionar_nome = ctk.CTkButton(
            self.janela,
            text="Adicionar nome",
            font=('arial', 30),
            command='adicionar função aqui'
        )
        btn_adicionar_nome.grid(row=1, column=0, pady=7.5, padx=0)

        btn_visualizar_nomes = ctk.CTkButton(
            self.janela,
            text="Visualizar nomes",
            font=('arial', 30),
            command=self.visualizar_nomes
        )
        btn_visualizar_nomes.grid(row=2, column=0, pady=7.5, padx=0)

        btn_deletar_nome = ctk.CTkButton(
            self.janela,
            text="Deletar nome",
            font=('arial', 30),
            command='adicionar função aqui'
        )
        btn_deletar_nome.grid(row=3, column=0, pady=7.5, padx=0)

        btn_deletar_todos_nomes = ctk.CTkButton(
            self.janela,
            text="Deletar todos os nomes",
            font=('arial', 30),
            command="Adiconar função aqui"
        )
        btn_deletar_todos_nomes.grid(row=4, column=0, pady=7.5, padx=0)

    def visualizar_nomes(self):
        self.janela.destroy()
        tela = VisualizarNome()
