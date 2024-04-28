class Ordenacao:
    @staticmethod
    def quicksort(array, steps=0):
        if len(array) < 2:
            steps += 1
            return {'lista_ordenada': array, 'operacoes': steps}
        else:
            pivo = array[0]
            menores = [x for x in array[1:] if x <= pivo]
            maiores = [x for x in array[1:] if x > pivo]

            resultado_menores = Ordenacao.quicksort(menores, steps)
            resultado_maiores = Ordenacao.quicksort(
                maiores, resultado_menores['operacoes'])

            lista_ordenada = resultado_menores['lista_ordenada'] + \
                [pivo] + resultado_maiores['lista_ordenada']
            steps = resultado_maiores['operacoes'] + len(array)

            return {'lista_ordenada': lista_ordenada, 'operacoes': steps}

    @staticmethod
    def porSelecao(array):
        array_copia = array.copy()
        nova_lista = []
        steps = 0

        while array_copia:
            steps += 1
            menor_valor = min(array_copia)
            steps += len(array_copia)
            nova_lista.append(menor_valor)
            array_copia.remove(menor_valor)

        json = {'lista_ordenada': nova_lista,
                'operacoes': steps}
        return json

    @staticmethod
    def porInsercao(array):
        steps = 0
        for i in range(1, len(array)):
            steps += 1
            valor = array[i]
            j = i - 1
            while j >= 0 and array[j] > valor:
                steps += 1
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = valor
        steps += 1

        json = {'lista_ordenada': array,
                'operacoes': steps}
        return json

    @staticmethod
    def calcularBigO(tamanho_lista, algoritmo, caso='pior'):
        from math import log2
        if algoritmo == 'quicksort':
            if caso == 'medio':
                notacao_bigO = tamanho_lista * log2(tamanho_lista)
                notacao_bigO = int(notacao_bigO)
                return notacao_bigO
            elif caso == 'pior':
                return pow(tamanho_lista, 2)
        elif algoritmo in ['por_selecao', 'por_insercao']:
            return pow(tamanho_lista, 2)
