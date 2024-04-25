class Ordenacao:
    @staticmethod
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivo = array[0]
            menores = [x for x in array[1:] if x <= pivo]
            maiores = [x for x in array[1:] if x > pivo]
            return Ordenacao.quicksort(menores) + [pivo] + Ordenacao.quicksort(maiores)

    @staticmethod
    def porSelecao(array):
        array_copia = array.copy()
        nova_lista = []

        while array_copia:
            menor_valor = min(array_copia)
            nova_lista.append(menor_valor)
            array_copia.remove(menor_valor)

        return nova_lista

    @staticmethod
    def porInsercao(array):
        for i in range(1, len(array)):
            valor = array[i]
            j = i - 1
            while j >= 0 and array[j] > valor:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = valor
        return array
