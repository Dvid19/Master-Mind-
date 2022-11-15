
from platform import system
import random 
import time 
import os 


def presentacion_1():

    print("***  JUEGO DE LOS PALILLOS  ***")
    print()
    print()
    print("***      ESCOGE NIVEL       ***")
    print("    Facil = 1 | Dificil = 2")
    print()
    while True:
        nivel = int(input(" Nivel -->  "))
        if nivel == 1 or nivel == 2:
            break
    return nivel


def presentacion_2(palillos, quitas, nivel):

    if nivel == 1:
        nivel = "FACIL"
    elif nivel == 2:
        nivel = "DIFICIL"

    print("***  JUEGO DE LOS PALILLOS  ***")
    print(f"  HABRA {palillos} PALILLOS EN TOTAL")
    print(f"Se podran quitar de 1 a {quitas} palillos")
    print("***      ESCOGE NIVEL       ***")
    print(f"          {nivel}")
    print()
    input(" Presiona 'enter' para empezar  ")

def palillos_y_quitas():

    palillos = random.randint(16, 23)
    quitas = random.randint(3,5)

    return palillos, quitas


def mesa_de_juego(palillos, quitas):

    print()
    print()
    for fila in range(4):
        print(end=" ")
        for p in range(1, palillos+1):
            print("|", end=" ")
            if p % quitas == 0:
                print(end=" ")
        print()
    print()
    print()
    print()


def movimiento_jugador(palillos, quitas):

    while True:
        quita_palillos = int(input(f" Palillos a quitar (1/{quitas})  "))
        if quita_palillos > quitas or quita_palillos > palillos:
            if quita_palillos > quitas:
                print(f"El numero de palillos a quitar es solo de 1 a {quitas}")

            elif quita_palillos > palillos:
                print(f"Solo hay {palillos} palillos ")
            
        elif quita_palillos <= quitas and quita_palillos <= palillos:
            return quita_palillos


def movimiento_cpu(palillos, quitas):

    while True:
        quita_palillos = random.randint(1, quitas)
        if quita_palillos > palillos:
            quita_palillos = random.randint(1, quitas)
        elif quita_palillos <= palillos:
            return quita_palillos


def movimiento_cpu_ia(palillos, quitas):

    quita_palillos = 0

    if quitas == palillos:
        quita_palillos = palillos
    
    if quitas == 5:
        if palillos % 6 == 0:
            quita_palillos = 4
        elif palillos % 6 == 1:
            quita_palillos = 1
        elif palillos % 6 == 2:
            quita_palillos = 2
        elif palillos % 6 == 3:
            quita_palillos = 3
        elif palillos % 6 == 5:
            quita_palillos = 5
        else:
            quita_palillos = 1

    elif quitas == 4:

        if palillos % 5 == 0:
            quita_palillos = 1
        elif palillos % 5 == 1:
            quita_palillos = 1
        elif palillos % 5 == 2:
            quita_palillos = 2
        elif palillos % 5 == 3:
            quita_palillos = 3
        elif palillos % 5 == 4:
            quita_palillos = 4
        else:
            quita_palillos = 1

    elif quitas == 3:

        if palillos % 4 == 0:
            quita_palillos = 1
        elif palillos % 4 == 1:
            quita_palillos = 1
        elif palillos % 4 == 2:
            quita_palillos = 2
        elif palillos % 4 == 3:
            quita_palillos = 3
        else:
            quita_palillos = 1

    
    
    return quita_palillos
    


def mostrar_ganador(turno, nivel):

    if nivel == 1:
        nivel = "FACIL"
    elif nivel == 2:
        nivel = "DIFICIL"

    if turno == 2:
        print("***       FELICIDADES       ***")
        print()
        print()
        print("*** LE HAS GANADO A LA CPU  ***")
        print(f"      Nivel | {nivel}")
        print()
    elif turno == 1:
        print("***       HAZ PERDIDO :(    ***")
        print()
        print()
        print("***  TE HA GANADO A LA CPU  ***")
        print(f"      Nivel | {nivel}")
        print()

################### FLUJO PROGRAMA ##############################
os.system("cls")
turno = 1
palillos, quitas = palillos_y_quitas()

nivel = presentacion_1()
os.system("cls")
presentacion_2(palillos, quitas, nivel)
os.system("cls")

################# BUCLE PRINCIPAL ###############################

jugando = True
while jugando:

    os.system("cls")

    mesa_de_juego(palillos, quitas)

    if turno == 1:
        jugada = movimiento_jugador(palillos, quitas)
        turno = 2

    elif turno == 2:
        print(" CPU esta pensando... ")
        time.sleep(2)
        if nivel == 1:
            jugada = movimiento_cpu(palillos, quitas)
            turno = 1
        elif nivel == 2:
            jugada = movimiento_cpu_ia(palillos, quitas)
            turno = 1


    palillos -= jugada

    if palillos == 0:
        os.system("cls")
        mostrar_ganador(turno, nivel)
        break



