import os
import re
import database as db
import helpers
from colorama import *
from termcolor import colored, cprint
init(autoreset=True)

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=(Fore.GREEN+"=="*18)
        print(lineas)
        print(colored("  BIENVENIDO AL GESTOR DE CLIENTES  ", 'white', attrs=['bold'], on_color='on_green'))
        print( lineas)
        print(colored(Fore.LIGHTGREEN_EX+"[1]"),"Listar clientes")
        print(colored(Fore.LIGHTGREEN_EX+"[2]"),"Buscar un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[3]"),"Añadir un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[4]"),"Modificar un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[5]"),"Borrar un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[6]"),"Cerrar el Gestor")# CERRAR EL MANAGER
        print(lineas)

        opcion = input(colored(Fore.LIGHTGREEN_EX+"> "))
        helpers.limpiar_pantalla()

        if opcion == '1':