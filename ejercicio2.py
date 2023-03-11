import math


# Crear clase llamada Puno, que tenga como atributos x e y. 
# Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
# Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si x == 0 e y != 0 se sitúa sobre el eje Y, si x != 0 e y == 0 se sitúa sobre el eje X y si x == 0 e y == 0 está sobre el origen.
# Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
# Añade un método llamado distancia, que tome otro pu Creanto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente: distancia = raíz cuadrada de (x2 - x1)2 + (y2 - y1)2
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return(f"El punto creado es ({self.x}, {self.y})")

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return("El punto se encuentra en el origen")
        elif self.x == 0:
            return("El punto se encuentra sobre el eje Y")
        elif self.y == 0:
            return("El punto se encuentra sobre el eje X")
        elif self.x > 0 and self.y > 0:
            return("El punto se encuentra en el primer cuadrante")
        elif self.x < 0 and self.y > 0:
            return("El punto se encuentra en el segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            return("El punto se encuentra en el tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            return("El punto se encuentra en el cuarto cuadrante")

    def vector(self, punto):
        
        return(f"El vector entre los puntos es ({punto.x - self.x}, {punto.y - self.y})")

    def distancia(self, punto):
        punto1=Punto(self.x, self.y)
        punto2=Punto(punto.x, punto.y)
        distancia = math.sqrt((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)
        return((distancia))
        return(type(distancia))
        

# Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
# Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
# Añade al rectángulo un método llamado base que muestre la base.
# Añade al rectángulo un método llamado altura que muestre la altura.
# Añade al rectángulo un método llamado area que muestre el area.
class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return(f"La base del rectángulo es {abs(self.punto2.x - self.punto1.x)}")

    def altura(self):
        return(f"La altura del rectángulo es {abs(self.punto2.y - self.punto1.y)}")

    def area(self):
        return(f"El área del rectángulo es {abs(self.punto2.x - self.punto1.x) * abs(self.punto2.y - self.punto1.y)}")

    
# Experimentación
if __name__ == "__main__":
    # Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla
    A=Punto(2,3)
    A.__str__()
    B=Punto(5,5)
    B.__str__()
    C=Punto(-3,-1)
    C.__str__()
    D=Punto(0,0)
    D.__str__()

    # Consulta a que cuadrante pertenecen el punto A, C y D
    A.cuadrante()
    C.cuadrante()
    D.cuadrante()


    # Consulta los vectores AB y BA
    A.vector(B)
    B.vector(A)

    # Consulta la distancia entre los puntos 'A y B' y 'B y A'
    A.distancia(B)
    B.distancia(A)

    # Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)

    # Crea el rectángulo utilizando los puntos A y B
    rectangulo=Rectangulo(A,B)

    # Consulta la base, altura y área del rectángulo
    rectangulo.base()
    rectangulo.altura()
    rectangulo.area()




