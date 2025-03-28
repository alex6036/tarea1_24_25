import math
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x  # Coordenada X
        self.y = y  # Coordenada Y
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen"
        elif self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante"
        
    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return Punto(vector_x, vector_y)
    
if __name__ == "__main__":
    p1 = Punto(3, 4)
    p2 = Punto(1, 2)
    v = p1.vector(p2)
    print(f"Punto inicial: {p1}")
    print(f"Punto final: {p2}")
    print(f"Vector resultante: {v}")
    
    # Otro ejemplo
    p3 = Punto(0, 0)
    p4 = Punto(5, -3)
    v2 = p3.vector(p4)
    print(f"\nPunto inicial: {p3}")
    print(f"Punto final: {p4}")
    print(f"Vector resultante: {v2}")

    print(f"\n{v2}: {v2.cuadrante()}")