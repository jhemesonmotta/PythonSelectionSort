def selectionSort(vetor):
   for ultimaPos in range(len(vetor)-1,0,-1):
       posMaior=0
       for pos in range(1,ultimaPos+1):
           if vetor[pos]>vetor[posMaior]:
               posMaior = pos

       aux = vetor[ultimaPos]
       vetor[ultimaPos] = vetor[posMaior]
       vetor[posMaior] = aux

vetor = [54,26,93,17,77,31,44,55,20]
selectionSort(vetor)
print(vetor)


# EXPLICAÇÃO

# ultimaPost = ultima posição comparável... depois que o algoritmo for para a segunda iteração do for, ele não precisará mais comparar com a ultima posição (absoluta)
                                            # pois já terá certeza que esta posição contém o maior valor.
                            # esta variável, irá percorrer o vetor de entrada de trás pra frente (da ultima posição para a primeira)

# posMaior = guardará o indice do maior valor, entre os percorridos

# pos = irá percorrer o vetor de entrada da primeira posição até a última avaliada

# troco o valor contido na ultima posição com o valor contido na posição do maior... ou seja, o maior vai para a última posição...
    # a partir da proxima iteração do for do "ultimaPos", a ultima posição já será a ultima posição atual - 1.
