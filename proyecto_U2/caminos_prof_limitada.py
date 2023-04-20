import copy
import random
import time


def GoalTest(EA):
    return EA==objetivo

def B_Profundo_Lim(Frontera,limite):
    if not Frontera:
        print("No se encontró solucion")
        return
    EA = Frontera.pop(0)
    print(EA)
    nv_act=EA[2]
    if GoalTest(EA[0]):
        print(EA[1])
        print("Nivel de la solución: ", nv_act)
        print("--- %s seconds ---" % (time.time() - start_time))
        return
    elif nv_act<limite:
        OS = Expand(EA,nv_act)
        Frontera = OS + Frontera
    else:
        print("No se encontró solución en el limite")
    B_Profundo_Lim(Frontera,limite)

movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def Expand(EA,nv_act):
    V = []
    nv_act=nv_act+1
    if EA[0] not in visitados:
        aux=EA[1]+[copy.deepcopy(EA[0])]
        visitados.append(EA[0])
        print("Visitados", visitados)
        for addx, addy in movs:
            print("Posicion actual: ",EA[0])
            x= EA[0][0] + addx 
            y= EA[0][1] + addy
            print("x,y: ",x, y)
            if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != 1 and (x,y) not in visitados:
                V.append([(x,y),aux,nv_act])
    return V

ancho_tablero=15
largo_tablero=15
porcentaje_bloqueo=0
tablero = [[0]*ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
bloqueados = []
for k in range(bloqueos):
    i = random.randint(0, largo_tablero-1)  
    j = random.randint(0, ancho_tablero-1)  
    while tablero[i][j] == 1:  
        i = random.randint(0, largo_tablero-1)
        j = random.randint(0, ancho_tablero-1)
    tablero[i][j] = 1
    bloqueados.append((i,j))
print(tablero)
print(bloqueados)
objetivo = (14,14)
visitados = []
start_time = time.time()
B_Profundo_Lim([[(0,0), [], 0]],29)