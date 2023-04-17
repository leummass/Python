import sys
import time
from tableroreinas import ChessboardGUI
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
        print("No hay solucion")
        return
    EA = Frontera.pop(0)
    print(EA)
    visitados.append(EA)
    if GoalTest(EA):
        print(EA, " es solución")
        print("--- %s seconds ---" % (time.time() - start_time))
        gui = ChessboardGUI(4, visitados)
        return
    else:
        OS = Expand(EA)
        Frontera += OS
    B_Ancho(Frontera)

def B_Profundo(Frontera):
    if not Frontera:
        print("No hay solucion")
        return
    EA = Frontera.pop(0)
    visitados.append(EA)
    if GoalTest(EA):
        print(EA, " es solución")
        print("--- %s seconds ---" % (time.time() - start_time))
        gui = ChessboardGUI(4, visitados)
        return
    else:
        OS = Expand(EA)
        OS+=Frontera
    B_Profundo(OS)

def Expand(EA):
    V = []
    for i in range(len(EA)):
        listAux = list(EA)
        posicion = listAux[i]
        if (posicion < len(EA)-1):
            posicion += 1
            listAux[i] = posicion
            if(listAux not in visitados):
                V.append(listAux)
                
    return V

Frontera = [[0, 0, 0, 0]]
visitados =[]
start_time = time.time()

B_Ancho(Frontera)
#B_Profundo(Frontera)





