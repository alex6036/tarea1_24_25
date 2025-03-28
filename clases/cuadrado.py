from Punto import Punto

class Rectangulo:
    def __init__(self, punto_inicial, punto_final):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def __str__(self):
        return f"Rectángulo con diagonal desde {self.punto_inicial} hasta {self.punto_final}"

if __name__ == "__main__":
    p1 = Punto(1, 1)
    p2 = Punto(4, 3)
    rect = Rectangulo(p1, p2)
    print(rect)