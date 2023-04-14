import sys
import time

sys.setrecursionlimit(10000000)
visitados = []


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
    if (CalcularAtaques(lista) == 0):
        return True
    else:
        return False


def B_Ancho(Frontera):
    if (len(Frontera) == 0):
        return
    Edo_Actual = Frontera[0]
    Frontera.pop(0)
    print(Edo_Actual)
    if (GoalTest(Edo_Actual)):
        Edo_Actual.reverse()
        print("Estado actual ", Edo_Actual)
        print("SOLUCION ENCONTRADA")
        return
    else:
        V = Expand(Edo_Actual)
        Frontera += V
    ##        print("Frontera",Frontera)
    B_Ancho(Frontera)

def B_Profundo(Frontera):
    if (len(Frontera) == 0):
        return
    Edo_Actual = Frontera[0]
    Frontera.pop(0)

    if (GoalTest(Edo_Actual)):
        Edo_Actual.reverse()
        print("Estado actual ", Edo_Actual)
        print("SOLUCION ENCONTRADA")
        return
    else:
        V = Expand(Edo_Actual)
        V+=Frontera
    ##        print("Frontera",Frontera)
    B_Profundo(V)

def B_Voraz(Frontera):
    if (len(Frontera) == 0):
        return
    Edo_Actual = Frontera[0]
    Frontera.pop(0)

    if (GoalTest(Edo_Actual)):
        Edo_Actual.reverse()
        print("Estado actual ", Edo_Actual)
        print("SOLUCION ENCONTRADA")
        return
    else:
        V = Expand(Edo_Actual)
        V= Evaluate(V)
        V+=Frontera
    ##  print("Frontera",Frontera)
    B_Voraz(V)


def Expand(Edo_Actual):
    V = []

    visitados.append(Edo_Actual)
    for i in range(len(Edo_Actual)):
        listAux = list(Edo_Actual)
        posicion = listAux[i]
        if (posicion < len(Edo_Actual)):
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




Frontera = [[1, 1, 1, 1]]
print(Frontera)
start_time = time.time()
#B_Ancho(Frontera)
#B_Profundo(Frontera)
B_Voraz(Frontera)
print("--- %s seconds ---" % (time.time() - start_time))




