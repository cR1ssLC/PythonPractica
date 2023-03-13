import time
import random
import os

def inicio_juego():
    print("*** Bienvenido ***")
    time.sleep(1)
    while True:
        ficha = input("Seleccione su ficha X / O :")
        ficha = ficha.upper()
        if ficha == "X":
            tu = "X"
            cp = "O"
            break
        elif ficha == "O":
            tu = "O"
            cp = "X"
            break
        else:
            print("Debe seleccionar X u O!!!")
    return tu,cp

def tablero():
    print("*** TRES EN RAYA ***")
    print()
    print("           |           |           ")
    print("      {}    |     {}     |     {}    ".format(matriz[0], matriz[1], matriz[2]))
    print("1          |2          |3          ")
    print("-----------------------------------")
    print("           |           |           ")
    print("      {}    |     {}     |     {}    ".format(matriz[3], matriz[4], matriz[5]))
    print("4          |5          |6          ")
    print("-----------------------------------")
    print("           |           |           ")
    print("      {}    |     {}     |     {}    ".format(matriz[6], matriz[7], matriz[8]))
    print("7          |8          |9          ")

def empate(matriz):
    empate=True
    i=0
    while empate==True and i < 9:
        if matriz[i]==" ":
            empate=False
        i=i+1
    return empate

def victoria(matriz):
    if matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " or matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" ":
        return True
    else:
        return False

def movimiento_jugador():
    while True:
        posiciones = [1,2,3,4,5,6,7,8,9]
        casilla = int(input("Seleccione casilla a jugar:"))
        if casilla not in posiciones:
            print("Error en seleccion de casilla!!!")
        else:
            if matriz[casilla-1] ==" ":
                matriz[casilla-1] = tu
                break
            else:
                print("Casilla no disponible!!!")

def movimiento_ordenador():
    posiciones=[0,1,2,3,4,5,6,7,8]
    casilla=9
    parar=False
    for i in posiciones:
        copia=list(matriz)
        if copia[i]==" ":
            copia[i]=cp
            if victoria(copia)==True:
                casilla=i
    if casilla==9:
        for j in posiciones:
            copia=list(matriz)
            if copia[j]==" ":
                copia[j]=tu
            if victoria(copia)==True:
                casilla=j
    if casilla==9:
        while not parar:
            casilla = random.randint(0,8)
            if matriz[casilla]==" ":
                parar = True
    matriz[casilla]=cp

#programa princpal
GameOver = True
while GameOver:
    matriz = [" "] * 9
    os.system("cls")
    tu, cp = inicio_juego()
    partida = True
    ganador = 0

    while partida:
        ganador += 1
        os.system("cls")
        tablero()
        if victoria(matriz):
            if ganador % 2 == 0:
                print("Gana el Jugador")
                print("Fin del Juego")
                resp=input("Quieres jugar denuevo?(s/n)")
                if resp.upper() == "N":
                    print("Gracias por jugar")
                    GameOver=False
                print("\n\nReiniciando...")
                time.sleep(3)
                partida = False
            else:
                print("Gana el Ordenador")
                print("Fin del Juego")
                resp=input("Quieres jugar denuevo?(s/n)")
                if resp.upper()=="N":
                    print("Gracias por jugar")
                    GameOver = False
                print("\n\nReiniciando...")
                time.sleep(3)
                partida = False
        elif empate(matriz):
            print("EMPATE!!!")
            print("Fin del Juego")
            resp=input("Quieres jugar denuevo?(s/n)")
            if resp.upper() == "N":
                print("Gracias por jugar")
                GameOver = False
            print("\n\nReiniciando...")
            time.sleep(3)
            partida = False
        elif ganador % 2 == 0:
            print("Computadora...  pensando...")
            time.sleep(2)
            movimiento_ordenador()
        else:
            movimiento_jugador()