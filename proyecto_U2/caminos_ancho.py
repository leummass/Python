import random


def GoalTest(lista):
    return 

def B_Ancho(Frontera):
    if not Frontera:
        print("No hay solucion")
        return
    EA = Frontera.pop(0)
    
    #visitados.append(EA)
    if GoalTest(EA):
        print(EA, " es solución")
        #print("--- %s seconds ---" % (time.time() - start_time))
        
        return
    else:
        OS = Expand(EA)
        Frontera += OS
    B_Ancho(Frontera)

def Expand(EA):
    V = []
    for i in range(len(EA)):
        listAux = list(EA)
        posicion = listAux[i]
        if (posicion < len(EA)-1):
            posicion += 1
            listAux[i] = posicion
            #if(listAux not in visitados):
                #V.append(listAux)
                
    return V
posb_movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ancho_tablero=10
largo_tablero=10
porcentaje_bloqueo=15
tablero = [[0]*ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
for k in range(bloqueos):
    i = random.randint(0, largo_tablero-1)  # fila aleatoria
    j = random.randint(0, ancho_tablero-1)  # columna aleatoria
    while tablero[i][j] == 1:  # si el espacio ya fue cambiado, elegir otro aleatorio
        i = random.randint(0, largo_tablero-1)
        j = random.randint(0, ancho_tablero-1)
    tablero[i][j] = 1


