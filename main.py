from models.Arquivo import Arquivo
from models.Ordenacao import Ordenacao

arquivo = Arquivo('dados.txt')
arquivo.inicializarBaseDeDados()

lista_original = arquivo.listarNomes()
print(lista_original)

lista_quicksort = Ordenacao.quicksort(lista_original)
lista_por_selecao = Ordenacao.porSelecao(lista_original)
lista_por_insercao = Ordenacao.porSelecao(lista_original)

print(lista_quicksort)
print(lista_por_selecao)
print(lista_por_insercao)
