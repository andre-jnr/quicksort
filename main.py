from models.Arquivo import Arquivo
from models.Ordenacao import Ordenacao as sort

# arquivo = Arquivo('dados200.txt')
# arquivo.inicializarBaseDeDados()

# lista_original = arquivo.listarNomes()
# print(lista_original)

class Menu:
    def opcoes(self):
        print('MENU PRINCIPAL')
        print('Escolha um número para continuar...')
        print('[1] - Consultar dados')
        print('[2] - Analisar algoritmo')
        print('[Qualquer tecla] - Sair')
        escolha = str(input('-> '))

        match escolha:
            case '1':
                escolha = self.consultarDados()
            case '2':
                pass
            case _:
                return

    def consultarDados():
        print('[1] - Adicionar nome')
        print('[2] - Visualizar nomes')
        print('[3] - Deletar nome')
        print('[4] - Deletar todos os nomes')
        print('[5] - Voltar para o menu principal')
        escolha = str(input('-> '))

        if escolha in ['1', '2', '3', '4', '5']:
            return escolha
        
        print('Digite uma escolha válida!')