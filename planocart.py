

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"

    def vector(self, otro):
        """Devuelve el vector resultante entre este punto y otro."""
        return (otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        """Calcula y devuelve la distancia entre este punto y otro."""
        from math import sqrt
        return sqrt((otro.x - self.x)**2 + (otro.y - self.y)**2)
    
# Experimentación

# Crear los puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir los puntos
print("Puntos:")
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)


# Consulta de cuadrantes
print("Cuadrantes:")
print(f"A: {A.cuadrante()}")
print(f"C: {C.cuadrante()}")
print(f"D: {D.cuadrante()}")


# Consulta vectores AB y BA
print("Vectores:")
print("Vector AB:", A.vector(B))
print("Vector BA:", B.vector(A))


# Consulta distancia entre los puntos
print("Distancias:")
print(f"Distancia A-B: {A.distancia(B):.2f}")
print(f"Distancia B-A: {B.distancia(A):.2f}")


# Determinar cuál está más lejos del origen
dist_A = A.distancia(D)
dist_B = B.distancia(D)
dist_C = C.distancia(D)
dists = {'A': dist_A, 'B': dist_B, 'C': dist_C}
mas_lejos = max(dists, key=dists.get)
print(f"El punto más lejano del origen es: {mas_lejos} (Distancia: {dists[mas_lejos]:.2f})")


# Crear un rectángulo utilizando los puntos A y B
base = abs(B.x - A.x)
altura = abs(B.y - A.y)
area = base * altura
print("Rectángulo formado por A y B:")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área: {area}")