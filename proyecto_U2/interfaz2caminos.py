import tkinter as tk

class Tablero:
    def __init__(self, N, M, WIDTH, HEIGHT):
        self.N = N
        self.M = M
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def dibujar_tablero(self, coords_bloqueadas, coords_meta):
        for i in range(self.N):
            for j in range(self.M):
                x0 = i*self.WIDTH
                y0 = j*self.HEIGHT
                x1 = x0 + self.WIDTH
                y1 = y0 + self.HEIGHT
                if (i, j) in coords_bloqueadas:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="red")
                elif (i,j) in coords_meta:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")
                    
    def dibujar_caminos(self, coords_camino, color):
        for i in range(len(coords_camino)):
            x0 = coords_camino[i][0]*self.WIDTH
            y0 = coords_camino[i][1]*self.HEIGHT
            x1 = x0 + self.WIDTH
            y1 = y0 + self.HEIGHT
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.root.update()
            self.root.after(50)

    def dibujar(self, coords_bloqueadas, coords_camino1, coords_camino2, coords_meta):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.N*self.WIDTH, height=self.M*self.HEIGHT)
        self.canvas.pack()
        self.dibujar_tablero(coords_bloqueadas, coords_meta)
        self.dibujar_caminos(coords_camino1, "green")
        self.dibujar_caminos(coords_camino2, "orange")
        self.root.mainloop()