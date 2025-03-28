from punto import Punto
from rectangulo import Rectangulo

# Crear los puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir los puntos por pantalla
print("Puntos creados:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

# Consultar los cuadrantes de A, C y D
print("\nCuadrantes:")
print(f"Cuadrante de A ({A}): {A.cuadrante()}")
print(f"Cuadrante de C ({C}): {C.cuadrante()}")
print(f"Cuadrante de D ({D}): {D.cuadrante()}")

# Consultar los vectores AB y BA
vector_AB = A.vector(B)
vector_BA = B.vector(A)
print("\nVectores:")
print(f"Vector AB (desde {A} hasta {B}): {vector_AB}")
print(f"Vector BA (desde {B} hasta {A}): {vector_BA}")

# Consultar la distancia entre A y B, y B y A
print("\nDistancias:")
dist_AB = A.distancia(B)
dist_BA = B.distancia(A)

# Determinar la distancia de A, B y C al origen (0,0)
origen = Punto(0, 0)
print("\nDistancias al origen (0,0):")
dist_A_origen = A.distancia(origen)
dist_B_origen = B.distancia(origen)
dist_C_origen = C.distancia(origen)

# Comparar las distancias para encontrar el punto más lejano
distancias = {
    "A": dist_A_origen,
    "B": dist_B_origen,
    "C": dist_C_origen
}
punto_mas_lejano = max(distancias, key=distancias.get)
print(f"\nEl punto más lejano del origen es {punto_mas_lejano} con una distancia de {abs(distancias[punto_mas_lejano])}")

# Crear un rectángulo con los puntos A y B
print("\nCreando rectángulo con puntos A y B:")
rectangulo_AB = Rectangulo(A.x, A.y, B.x, B.y)
print(rectangulo_AB)

# Consultar base, altura y área del rectángulo
print("\nPropiedades del rectángulo:")
rectangulo_AB.base()
rectangulo_AB.altura()
rectangulo_AB.area()

