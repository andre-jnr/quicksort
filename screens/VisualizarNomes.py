import customtkinter as ctk
from models.Arquivo import Arquivo


class VisualizarNome:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Visualizar nomes")
        self.janela.geometry("785x348")
        self.arquivo = Arquivo('dados200.txt')
        self.janela.grid_columnconfigure(0, weight=1)

        self.criar_componenetes()
        self.janela.mainloop()

    def criar_componenetes(self):

        botao_voltar = ctk.CTkButton(
            self.janela,
            text="Voltar",
            command=self.voltar
        )
        botao_voltar.pack(pady=10)

        titulo_janela = ctk.CTkLabel(
            self.janela,
            text="Visualizar nomes",
            font=('arial', 40)
        )
        titulo_janela.pack(pady=(5, 10))

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.janela,
            width=700,
            height=150
        )
        self.scrollable_frame.pack(
            pady=(10, 20), padx=20, fill="both", expand=True)

        nomes = ctk.CTkLabel(
            self.scrollable_frame,
            text=self.listarNomes()
        )
        nomes.pack()

    def listarNomes(self):
        self.arquivo.inicializarBaseDeDados()
        nomes = self.arquivo.exibirNomes()
        nomes_numerados = "\n".join(
            f"{i+1}. {nome}" for i, nome in enumerate(nomes.splitlines()))
        return nomes_numerados

    def voltar(self):
        from Menu import Menu
        self.janela.destroy()
        menu = Menu()
        menu.janela.mainloop()
