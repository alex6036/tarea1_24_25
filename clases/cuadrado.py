from punto import Punto

class Rectangulo:
    def __init__(self, x_inicial=0, y_inicial=0, x_final=0, y_final=0):
        self.punto_inicial = Punto(x_inicial, y_inicial)  # Punto inicial por defecto (0,0)
        self.punto_final = Punto(x_final, y_final)        # Punto final por defecto (0,0)
    
    def __str__(self):
        return f"Rectángulo con diagonal desde {self.punto_inicial} hasta {self.punto_final}"

    def base(self):
        # Calcula la longitud de la base como la diferencia absoluta en X
        longitud_base = abs(self.punto_final.x - self.punto_inicial.x)
        print(f"La base del rectángulo es: {longitud_base}")
        return 
    
    def altura(self):
        # Calcula la altura como la diferencia absoluta en Y
        longitud_altura = abs(self.punto_final.y - self.punto_inicial.y)
        print(f"La altura del rectángulo es: {longitud_altura}")
        return longitud_altura
    
if __name__ == "__main__":
    # Crear rectángulo con valores específicos
    rect1 = Rectangulo(1, 1, 4, 3)
    print(rect1)
    rect1.base()
    rect1.altura()
    
    # Crear rectángulo con solo punto inicial (final será (0,0))
    rect2 = Rectangulo(2, 2)
    print(rect2)
    rect2.base()
    rect2.altura()
    
    # Crear rectángulo sin parámetros (ambos puntos en (0,0))
    rect3 = Rectangulo()
    print(rect3)
    rect3.base()
    rect3.altura()