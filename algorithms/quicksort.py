def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivo = array[0]
    menores = [x for x in array[1:] if x <= pivo]
    maiores = [x for x in array[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)