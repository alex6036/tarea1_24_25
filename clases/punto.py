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
    
    def distancia(self, otro_punto):
        # Calcula la distancia euclidiana entre los dos puntos
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        print(f"La distancia entre {self} y {otro_punto} es: {distancia}")
        return distancia

