from models.Arquivo import Arquivo
from models.Ordenacao import Ordenacao

arquivo = Arquivo('dados.txt')
arquivo.inicializarBaseDeDados()

lista_original = arquivo.listarNomes()
# print(lista_original)

lista_quicksort = Ordenacao.quicksort(lista_original)
lista_por_selecao = Ordenacao.porSelecao(lista_original)
lista_por_insercao = Ordenacao.porInsercao(lista_original)

print(f'Operações quicksort: {lista_quicksort['operacoes']}')
bigO = Ordenacao.calcularBigO(len(lista_original), algoritmo='quicksort')
print(f'BigO quicksort: {bigO}')
print('')

print(f'Operações seleção: {lista_por_selecao['operacoes']}')
bigO = Ordenacao.calcularBigO(len(lista_original), algoritmo='por_selecao')
print(f'BigO por seleção: {bigO}')
print('')

print(f'Operações de ordenação por inserção: {
      lista_por_insercao['operacoes']}')
bigO = Ordenacao.calcularBigO(len(lista_original), algoritmo='por_insercao')
print(f'BigO por inserção: {bigO}')
