from mimetypes import init

class VectorConAtaque:
    def __init__ (self, V):
        self.Vector = V
        self.Ataques = None
    def AsignarAtaque(self,A):
        self.Ataques = A 
    def getVector(self):
        return self.Vector

def Expand(V):

    copia = V.copy()
    arregloBi = []
    for j in range(len(V)):
        for x in range(len(V)):
            var = V[x]+(j)
            print(var)
            if(var > len(V)): 
                V[x] = var-V[x]
                arregloBi.append(V.copy())
                V = copia.copy()
                print(arregloBi)
                continue
            V[x] = var
            arregloBi.append(V.copy())
            V = copia.copy()
            print(arregloBi)

    return arregloBi    

def MandarError():
    print("No se encontro el elemento")
    exit()
def Ataques(V):
    atq = 0
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if(V[i] == V[j]):
                atq += 2
            elif abs(i-j) == abs(V[i]-V[j]):
                atq += 2
    return atq

def LimitarB(E_A):  
    return 1 not in E_A

def Goaltest(V):
    return Ataques(V) == 0

def B_G(F):

    if(len(F) != 0):

        E_A = F.pop(0)
        print("ElementoSeleccionado",E_A.getVector(), E_A.Ataques)

        if(Goaltest(E_A.getVector())): 
            end_time = datetime.now()
            print('Duration: {}'.format(end_time - start_time))
            
            muestraResultado(E_A.getVector())
            TerminarPrograma()      
        else:
            OS = Expand(E_A.getVector())
            OS = Evaluo(OS)
            F = F+OS
            F.sort(key  = lambda x: x.Ataques, reverse = False)
            if(len(F) == 0):
                return
            F = [TomaPrimerElemento(F)]
            B_G(F)

def TomaPrimerElemento(F):
    repetidos = 0
    menor = F[0].Ataques   
    for x in range(len(F)-1):
        if(menor == F[x+1].Ataques):
            repetidos = repetidos+1
    numero = random.randint(0,repetidos)
    return F[numero]
    

        
def Evaluo(OS):
    OSNuevo = []
    contador = 0
    for x in range(len(OS)):
        if(LimitarB(OS[x])):
            continue
        OSNuevo.append(VectorConAtaque(OS[x]))
        OSNuevo[contador].AsignarAtaque(Ataques(OS[x]))
        contador = contador+1

    return OSNuevo

def TerminarPrograma():
    exit()

def muestraResultado(E_a):
    print("Elemento encontrado")
    board = np.zeros((len(E_a),len(E_a),3))
    board += 0.5 # "Black" color. Can also be a sequence of r,g,b with values 0-1.
    board[::2, ::2] = 1 # "White" color
    board[1::2, 1::2] = 1 # "White" color
    for x in range(len(E_a)):
        E_a[x] = E_a[x]-1        
    positions = E_a
    print(E_a)

    fig, ax = plt.subplots(nrows=1, num="Tablero Reinas")
    ax.imshow(board, interpolation='nearest')
    for y, x in enumerate(positions):
        ax.text(x, y, u'\u2655', size=18, ha='center', va='center')
    ax.set(xticks=[], yticks=[])
    ax.axis('image')
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math
import random 
from datetime import datetime
import sys
#from CodOptimizado.Utilerias import *
sys.setrecursionlimit(233232323)
start_time = datetime.now()                                                                                           
E_i = VectorConAtaque([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0])
F = [E_i]
B_G(F)

