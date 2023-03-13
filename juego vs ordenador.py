import random
import time
player1=input("INGRESA TU NOMBRE")
player2="ORDENADOR"
xn=0
gameover=False
NumeroPalitos=int(input('Ingrese numero total de palos a jugar'))
np = int(input('Ingrese  numero maximo de palitos a retirar '))

def remueveOrdenador():
    global np
    global NumeroPalitos
    numeroRemovido = random.randint(1, np)
    if np>=NumeroPalitos:
        numeroRemovido=NumeroPalitos
    NumeroPalitos-=numeroRemovido
    return NumeroPalitos

def remueveHumano():
    global NumeroPalitos
    NumeroPalitos-=xn
    return NumeroPalitos

def jugadaHumano():
    global np
    global xn
    movimiento=False
    while not movimiento:
        print("Es tu turno, ",player1)
        print("(de 1 a ", np, ")")
        xn=int(input("Cuantos palitos se van a remover?"))
        if  xn>np or xn<1:
            print("Ingrese un numero entre el rango")
        else:
            movimiento=True
    while xn>NumeroPalitos:
        print("El número ingresado es mayor que el número de palitos restantes.")
        print("(de 1 a ", np, ")")
        xn=int(input("Cuantos palitos se van a remover?"))
    return xn

def ganador(player):
    if NumeroPalitos==0:
        print(player," GANA!!!.")
        global gameover
        gameover=True
        return gameover

def resetGameover():
    global gameover
    gameover=False
    return gameover

def game():
    global NumeroPalitos
    while gameover==False:
        jugadaHumano()
        print("El numero de palitos restantes es: ", remueveHumano())
        ganador(player1)
        if gameover==True:
            break
        print("Es el turno del ",player2)
        print("Pensando...")
        time.sleep(2)
        print("El numero de palitos restantes es: ",remueveOrdenador())
        ganador(player2)
        if gameover==True:
            break

def juegaDenuevo():
    resp=input("Quieres jugar denuevo?(s/n)")
    resetGameover()
    while resp=="s":
        game()
    else:
        print("Gracias por jugar")

game()
juegaDenuevo()