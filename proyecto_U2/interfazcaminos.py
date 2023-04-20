import tkinter as tk

# Configuración del tablero
N = 8
M = 8
WIDTH = 50
HEIGHT = 50

# Coordenadas de las casillas a dibujar en otro color
coords = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (1, 2), (2, 1), (3, 0), (1, 3), (2, 2), (3, 1)]

# Creación de la ventana y del lienzo (canvas)
root = tk.Tk()
canvas = tk.Canvas(root, width=N*WIDTH, height=M*HEIGHT)
canvas.pack()

# Dibujo de las casillas del tablero
for i in range(N):
    for j in range(M):
        x0 = i*WIDTH
        y0 = j*HEIGHT
        x1 = x0 + WIDTH
        y1 = y0 + HEIGHT
        if (i, j) in coords:
            canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white")

# Inicio del bucle principal de la aplicación
root.mainloop()