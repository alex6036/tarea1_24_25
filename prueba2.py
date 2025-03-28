class Punto:
    def __init__(self, x=0, y=0):
        self.x = x  # Coordenada X
        self.y = y  # Coordenada Y
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

if __name__ == "__main__":
    p1 = Punto(3, 4)    # Ambas coordenadas especificadas
    p2 = Punto(5)       # Solo X especificada, Y será 0
    p3 = Punto()        # Ninguna coordenada, ambas serán 0
    
    print(p1)  # Imprime: Punto(3, 4)
    print(p2)  # Imprime: Punto(5, 0)
    print(p3)  # Imprime: Punto(0, 0)