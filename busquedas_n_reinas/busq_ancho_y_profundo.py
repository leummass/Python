import sys
import time

from busquedas_n_reinas.tableroreinas import ChessboardGUI
sys.setrecursionlimit(10000000)

def CalcularAtaques(lista):
    length = len(lista)
    Ataques = 0
    for i in range(length):
        for j in range(i + 1, length):
            if (lista[i] == lista[j]):
                Ataques += 2
            elif ((abs(i - j) - abs(lista[i] - lista[j])) == 0):
                Ataques += 2
    return Ataques

def GoalTest(lista):
    return CalcularAtaques(lista) == 0

def B_Ancho(Frontera):
    if not Frontera:
        return
    EA = Frontera.pop(0)
    print(EA)
    if GoalTest(EA):
        EA.reverse()
        print(EA, " es solución")
        print("--- %s seconds ---" % (time.time() - start_time))
        gui = ChessboardGUI(len(EA), EA)
        return
    else:
        OS = Expand(EA)
        Frontera += OS
    B_Ancho(Frontera)

def B_Profundo(Frontera):
    if not Frontera:
        return
    EA = Frontera.pop(0)
    print(EA)
    if GoalTest(EA):
        EA.reverse()
        print(EA, " es solución")
        print("--- %s seconds ---" % (time.time() - start_time))
        gui = ChessboardGUI(len(EA), EA)
        return
    else:
        OS = Expand(EA)
        OS+=Frontera
        print("Frontera",Frontera)
    B_Profundo(OS)

def Expand(EA):
    V = []
    visitados.append(EA)
    for i in range(len(EA)):
        listAux = list(EA)
        posicion = listAux[i]
        if (posicion < len(EA)-1):
            posicion += 1
            listAux[i] = posicion
            V.append(listAux)
    return V

def Evaluate(V):
    listAux = []
    V2=[]
    for i in range(len(V)):
        listAux= listAux + [CalcularAtaques(V[i])]
    listAux.sort()
    print(listAux)
    for i in range(len(V)):
        if CalcularAtaques(V[i]) == listAux[0]:
            V3=V[i]
            V2.append(V3)
            return V2

Frontera = [[0, 0, 0, 0]]
visitados =[]
start_time = time.time()
B_Ancho(Frontera)
#B_Profundo(Frontera)





