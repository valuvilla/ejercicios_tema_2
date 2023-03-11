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
            input_x = int(input("Ingrese la coordenada X: "))
            input_y = int(input("Ingrese la coordenada Y: "))
            punto1=ej2.Punto(input_x, input_y)
            print(ej2.Punto.__str__(punto1))
        
        elif opcion == '2':
            input_x = int(input("Ingrese la coordenada X: "))
            input_y = int(input("Ingrese la coordenada Y: "))
            punto1=ej2.Punto(input_x, input_y)
            print(ej2.Punto.cuadrante(punto1))
        
        elif opcion == '3':
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.vector(punto1, punto2))
        
        elif opcion == '4':
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            punto2=ej2.Punto(punto2_x, punto2_y)
            print(ej2.Punto.distancia(punto1, punto2))
        
        elif opcion == '5':
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            punto2=ej2.Punto(punto2_x, punto2_y)
            rectangulo1=ej2.Rectangulo(punto1, punto2)
            print(ej2.Rectangulo.__str__(rectangulo1))
        
        elif opcion == '6':
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            punto2=ej2.Punto(punto2_x, punto2_y)
            rectangulo1=ej2.Rectangulo(punto1, punto2)
            print(ej2.Rectangulo.base(rectangulo1))
        
        elif opcion == '7':
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            punto2=ej2.Punto(punto2_x, punto2_y)
            rectangulo1=ej2.Rectangulo(punto1, punto2)
            print(ej2.Rectangulo.altura(rectangulo1))
        
        elif opcion == '8':
            punto1_x = int(input("Ingrese la coordenada X del primer punto: "))
            punto1_y = int(input("Ingrese la coordenada Y del primer punto: "))
            punto2_x = int(input("Ingrese la coordenada X del segundo punto: "))
            punto2_y = int(input("Ingrese la coordenada Y del segundo punto: "))
            punto1=ej2.Punto(punto1_x, punto1_y)
            punto2=ej2.Punto(punto2_x, punto2_y)
            rectangulo1=ej2.Rectangulo(punto1, punto2)
            print(ej2.Rectangulo.area(rectangulo1))
        
        if opcion == '9':
            print(Back.MAGENTA+"SALIENDO\n")
            break

        input("\nPresiona ENTER para continuar...")

iniciar()
