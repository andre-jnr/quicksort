import customtkinter as ctk
from AnalisarAlgoritmos import AnalisarAlgoritmos


class Menu:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Menu")
        self.janela.geometry("785x348")

        self.criar_componenetes()

    def criar_componenetes(self):
        self.titulo = ctk.CTkLabel(
            self.janela,
            text="Quicksort"
        )

        titulo_janela = ctk.CTkLabel(
            self.janela,
            text="Menu principal",
            font=('arial', 40)).pack(pady=50)

        self.frame_botoes = ctk.CTkFrame(self.janela, fg_color="transparent")
        self.frame_botoes.pack(
            expand=True, fill='both', padx=20, pady=0)

        btn_consultar_dados = ctk.CTkButton(
            self.frame_botoes,
            text="CONSULTAR DADOS",
            command=self.analisar_algoritmos,
            font=('arial', 20)
        )

        btn_consultar_dados.pack(pady=10, padx=0)

        btn_analisar_algoritmos = ctk.CTkButton(
            self.frame_botoes,
            text="ANALISAR ALGORITMOS",
            command=self.analisar_algoritmos,
            font=('arial', 20)
        )
        btn_analisar_algoritmos.pack(pady=0, padx=0)

    def analisar_algoritmos(self):
        self.janela.destroy()
        tela_analise = AnalisarAlgoritmos()


if __name__ == "__main__":
    menu = Menu()
    menu.janela.mainloop()
