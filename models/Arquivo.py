class Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def inicializarBaseDeDados(self):
        try:
            with open(f"databases/{self.nome_arquivo}", 'r') as file:
                file.read()
        except FileNotFoundError:
            with open(f"databases/{self.nome_arquivo}", 'w') as file:
                file.write('')

    def adicionarNome(self, nome):
        try:
            with open(f"databases/{self.nome_arquivo}", 'a') as file:
                file.write(nome + '\n')
        except:
            print('Não foi possível adicionar o nome.')
        else:
            print('Nome adicionado com sucesso.')

    def exibirNomes(self):
        try:
            arquivo = open(f"databases/{self.nome_arquivo}", 'r')
            self.nomes = self.listarNomes()
        except:
            print('Não foi possível exibir o nome.')
        else:
            return "\n".join(self.nomes)

    def listarNomes(self):
        nomes = []
        with open(f"databases/{self.nome_arquivo}", 'r') as file:
            for linha in file:
                nomes.append(str(linha[:-1]))

        return nomes

    def salvarLista(self, lista):
        with open(f"databases/{self.nome_arquivo}", 'w') as file:
            for nome in lista:
                file.write(str(nome))

    def excluirNome(self):
        nomes = self.listarNomes()
        if len(nomes) == 0:
            print('Não há nomes registrados.')
            return False

        nome = input('Digite o nome que deseja excluir: ')
        if nome in nomes:
            nomes.remove(nome)
            self.salvarLista(nomes)
            print('Nome excluído com sucesso.')
            return True

        print('Nome não encontrado.')
        return False

    def excluirTodos(self):
        with open(f"databases/{self.nome_arquivo}", 'w') as file:
            file.write('')
            print('Toda a base de dados foi deletada')
            return True
