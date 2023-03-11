import os
import re
import ejercicio2 as ej2
import helpers
from colorama import *
from termcolor import colored, cprint
init(autoreset=True)

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=(Fore.GREEN+"=="*21)

        print(lineas)
        print(colored(("BIENVENIDO AL MENÚ DE PUNTOS Y RECTANGULOS").center(36), 'white', attrs=['bold'], on_color='on_green'))
        print(colored(Fore.GREEN+("¿Qué desea hacer?").center(42)))
        print( lineas)
        print(colored(Fore.LIGHTGREEN_EX+"[1]"),"Crear punto")
        print(colored(Fore.LIGHTGREEN_EX+"[2]"),"Mostrar cuadrante de un punto")
        print(colored(Fore.LIGHTGREEN_EX+"[3]"),"Mostrar vector entre dos puntos")
        print(colored(Fore.LIGHTGREEN_EX+"[4]"),"Mostrar distancia entre dos puntos")
        print(colored(Fore.LIGHTGREEN_EX+"[5]"),"Crear rectángulo")
        print(colored(Fore.LIGHTGREEN_EX+"[6]"),"Mostrar base de un rectángulo")
        print(colored(Fore.LIGHTGREEN_EX+"[7]"), "Mostrar altura de un rectángulo")
        print(colored(Fore.LIGHTGREEN_EX+"[8]"), "Mostrar área de un rectángulo")
        print(colored(Fore.LIGHTGREEN_EX+"[9]"), "Salir")
        print(lineas)

        opcion = input(colored(Fore.LIGHTGREEN_EX+"> "))
        helpers.limpiar_pantalla()

        if opcion == '1':
            print(colored(Fore.LIGHTGREEN_EX+"Creación de punto".center(42)))
            input_x = int(input("Ingrese la coordenada X: "))
            input_y = int(input("Ingrese la coordenada Y: "))
            punto1=ej2.Punto(input_x, input_y)
            print(ej2.Punto.__str__(punto1))
            print(colored(Fore.LIGHTGREEN_EX+"Punto creado con éxito".center(42)))
        
        elif opcion == '2':
            print(colored(Fore.LIGHTGREEN_EX+"Cuadrante de un punto".center(42)))
            input_x = int(input("Ingrese la coordenada X: "))
            input_y = int(input("Ingrese la coordenada Y: "))
            punto1=ej2.Punto(input_x, input_y)
            print(ej2.Punto.cuadrante(punto1))
            print(colored(Fore.LIGHTGREEN_EX+"Cuadrante obtenido con éxito".center(42)))
        
        elif opcion == '3':
            print(colored(Fore.LIGHTGREEN_EX+"Vector entre dos puntos".center(42)))
            # primer punto
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            print(ej2.Punto.__str__(punto1))

            # segundo punto
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.__str__(punto2))

            # vector
            print(ej2.Punto.vector(punto1, punto2))
            print(colored(Fore.LIGHTGREEN_EX+"Vector obtenido con éxito".center(42)))
        
        elif opcion == '4':
            print(colored(Fore.LIGHTGREEN_EX+"Distancia entre dos puntos".center(42)))

            # primer punto
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            print(ej2.Punto.__str__(punto1))

            # segundo punto
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.__str__(punto2))

            # distancia
            print(ej2.Punto.distancia(punto1, punto2))
            print(colored(Fore.LIGHTGREEN_EX+"Distancia obtenida con éxito".center(42)))
        
        elif opcion == '5':
            print(colored(Fore.LIGHTGREEN_EX+"Creación de rectángulo".center(42)))

            # primer punto
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            print(ej2.Punto.__str__(punto1))


            # segundo punto
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.__str__(punto2))

            # rectángulo
            rectangulo1=ej2.Rectangulo(punto1, punto2)
            print(colored(Fore.LIGHTGREEN_EX+"Rectángulo creado con éxito".center(42)))
          
        
        elif opcion == '6':
            print(colored(Fore.LIGHTGREEN_EX+"Base de un rectángulo".center(42)))

            # primer punto
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            print(ej2.Punto.__str__(punto1))

            # segundo punto
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.__str__(punto2))

            # rectángulo
            rectangulo1=ej2.Rectangulo(punto1, punto2)

            # base
            print(ej2.Rectangulo.base(rectangulo1))

            print(colored(Fore.LIGHTGREEN_EX+"Base obtenida con éxito".center(42)))
        
        elif opcion == '7':
            print(colored(Fore.LIGHTGREEN_EX+"Altura de un rectángulo".center(42)))

            # primer punto
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            print(ej2.Punto.__str__(punto1))

            # segundo punto
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.__str__(punto2))

            # rectángulo
            rectangulo1=ej2.Rectangulo(punto1, punto2)

            # altura
            print(ej2.Rectangulo.altura(rectangulo1))

            print(colored(Fore.LIGHTGREEN_EX+"Altura obtenida con éxito".center(42)))
        
        elif opcion == '8':
            print(colored(Fore.LIGHTGREEN_EX+"Área de un rectángulo".center(42)))

            # primer punto
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            print(ej2.Punto.__str__(punto1))

            # segundo punto
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto2=ej2.Punto(punto2_x, punto2_y)

            # rectángulo
            rectangulo1=ej2.Rectangulo(punto1, punto2)

            # área
            print(ej2.Rectangulo.area(rectangulo1))
        
        if opcion == '9':
            print(Back.MAGENTA+"SALIENDO\n")
            break

        input("\nPresiona ENTER para continuar...")

iniciar()
