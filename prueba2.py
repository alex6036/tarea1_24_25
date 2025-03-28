class Punto:
    def __init__(self, x, y):
        self.x = x  # Coordenada X
        self.y = y  # Coordenada Y
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
    