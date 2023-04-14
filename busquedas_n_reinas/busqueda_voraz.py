import time
import sys
import random
from tableroreinas import ChessboardGUI
sys.setrecursionlimit(10000)

def CalcularAtaques(lista):
    length = len(lista)
    Ataques = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            if (lista[i] == lista[j]):
                Ataques += 2
            elif ((abs(i - j) - abs(lista[i] - lista[j])) == 0):
                Ataques += 2
    return Ataques


def GoalTest(lista):
    Numero_Ataques = CalcularAtaques(lista)
    if (Numero_Ataques == 0):
        return True
    else:
        return False


lista_negra = []


def Expand(V):
    copia = V.copy()
    arregloBi = []
    reina_n = len(V)
    lista_negra.append(V)
    for j in range(0, reina_n):
        for x in range(0, reina_n):
            var = V[x] + j
            if var >= reina_n:
                V[x] = var - reina_n
                #print(V)
                V not in lista_negra and arregloBi.append(V.copy())
                V = copia.copy()
                continue
            V[x] = var
            V not in lista_negra and arregloBi.append(V.copy())
            V = copia.copy()
    return arregloBi


def Evaluar(offSpring):
    lista = []
    for i in offSpring:
        Naataques = CalcularAtaques(i)
        lista.append([i, Naataques])
    return lista


def TomaPrimerElemento(F):
    repetidos = 0
    menor = F[0][1]
    for x in range(len(F) - 1):
        if (menor == F[x + 1][1]):
            repetidos = repetidos + 1
        else:
            break
    return F[random.randint(0, repetidos)][0]


def voraz(F):
    if not F:
        return
    Edo_act = F.pop(0)
    print("ESTADO ACTUAL")
    print(Edo_act)
    if (GoalTest(Edo_act)):
        print(Edo_act, " es solucion")
        print("--- %s seconds ---" % (time.time() - start_time))
        gui = ChessboardGUI(len(Edo_act), Edo_act)
        return
    else:
        offSpring = Expand(Edo_act)
        print(offSpring)
        offSpring = Evaluar(offSpring)

        offSpring.sort(key=lambda x: x[1])
        F = [TomaPrimerElemento(offSpring)]
        voraz(F)


F = [[]]
for k in range(50):
    F[0].append(0)

start_time = time.time()
voraz(F)

