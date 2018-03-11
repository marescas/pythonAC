import numpy as np
import matplotlib.pyplot as plt

def reglas(numRegla):
    """
    Codifica utilizando números de Wolfram
    :param numRegla: numero a codificar a números de Wolfram
    """
    sol = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    binary = []
    decimal = numRegla
    while decimal // 2 != 0:
        binary.append(decimal%2)
        decimal = decimal // 2
    for i in range(0,len(sol)):
        if i<len(binary):
            sol[i].insert(3,binary[i])
        else:
            sol[i].insert(3,0)
    return sol
def buscarEstadoSiguiente(conjReglas,anterior,actual,siguiente):
    """
    Dado un conjunto de reglas el estado actual y el estado de los vecinos
    busca aquellas entradas que hacen matching con conjReglas
    para encontrar el estado siguiente.
    """
    resAnterior = []
    resActual = []
    resSiguiente =[]
    res = []
    for i in range(0,len(conjReglas)):
        if conjReglas[i][0] == anterior:
            resAnterior.append(conjReglas[i])
        if conjReglas[i][1] == actual:
            resActual.append(conjReglas[i])
        if conjReglas[i][2] ==siguiente:
            resSiguiente.append(conjReglas[i])
    for lista in resAnterior:
        if lista in resActual and lista in resSiguiente:
            res.append(lista)
    return res[0][3]

def iteracion(ArrayInicial,numRegla):
    """
    Realiza una iteración del autómata.
    Utilizamos frontera periódica
    """
    res = []
    conjReglas = reglas(numRegla)
    for i in range(0,len(ArrayInicial)):
        anterior = i-1
        siguiente = i+1
        if siguiente == len(ArrayInicial):
            siguiente = 0
        if anterior <0:
            anterior = len(ArrayInicial)-1
        estadoSiguiente = buscarEstadoSiguiente(conjReglas,ArrayInicial[anterior],ArrayInicial[i],ArrayInicial[siguiente])
        res.insert(i,estadoSiguiente)
    return res
def AC(EstadoInicial,numRegla,numIteraciones):
    """
    Autómata celular
    :param EstadoInicial: estado inicial del autómata
    :param numRegla: número a codificar en números de Wolfram
    :param numIteraciones: número de iteraciones que realizara en AC
    """
    matriz =np.zeros((numIteraciones,len(EstadoInicial)))
    matriz[0] =EstadoInicial
    for i in range(1,numIteraciones):
        matriz[i] = iteracion(matriz[i-1],numRegla)
    return matriz

if __name__ == '__main__':
    g = AC([0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1],240,50)
    plt.imshow(g)
    #plt.imshow(g, cmap='Greys',  interpolation='nearest')
    plt.savefig('blkwht.png')
    plt.show()
