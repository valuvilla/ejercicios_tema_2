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

        opcion = input(colored(Fore.LIGHTGREEN_EX+"> "))
        helpers.limpiar_pantalla()

        if opcion == '1':
            input_x = int(input("Ingrese la coordenada X: "))
            input_y = int(input("Ingrese la coordenada Y: "))
            punto = ej2.Punto(input_x, input_y)
            print(f"El punto creado es: {ej2.Punto.__str__(punto)}")


        if opcion == '9':
            print(Back.MAGENTA+"SALIENDO\n")
            break

        input("\nPresiona ENTER para continuar...")

iniciar()
