#1# --------------------IMPORTACIONES------------------------------------

from repartir_cartas import (
    repartir_dos_cartas_al_jugador,
    repartir_dos_cartas_al_croupier,
    repartir_una_carta_mas
)

from puntuacion import (
    puntuacion_cartas,
)

from booleano import pedir_entrada_si_o_no

#2# --------------------DECLARACION VARIABLES-------------------------------------------------
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

lista_cartas = list(cartas.keys()) #para poder escoger una carta, hacemos una lista de las claves del dict

J = [] #lista vacía con las cartas del jugador
C = [] #lista vacía con las cartas del croupier
#3# --------------------FUNCIONES-------------------------------------------------

def mostrar_cartas(lista):
    '''
    Esta funcion muestra las cartas (gráficas), dado una lista de indices de cartas
    -INPUT -------------
    lista : list
        lista de indices de cartas
    -OUTPUT ------------
    lista de cartas (gráficas)
    '''
    return [lista_cartas[c] for c in lista]



def decision_jugador(J, C):
    '''
    Esta funcion pregunta al jugador si quiere  otra carta o plantarse y ejecuta la decision
    -INPUT -------------
    J : list
        lista de cartas del jugador
    C : list
        lista de cartas del croupier
    -OUTPUT ------------
    cartas del jugador actualizadas
    '''
    #se pregunta al jugador si quiere otra carta
    if pedir_entrada_si_o_no('¿Quieres otra carta? (s/n): '):
        #si quiere otra carta, se le reparte una carta al azar
        J.append( repartir_una_carta_mas(J,C) )
        print('Tus cartas ahora son: ', mostrar_cartas(J))
    else: #si no quiere otra carta
        print('Te plantas con: ', mostrar_cartas(J))


def accion_croupier(J, C):
    '''
    Esta funcion modeliza las acciones del croupier según las reglas del juego
    -INPUT -------------
    J : list
        lista de cartas del jugador
    C : list
        lista de cartas del croupier
    -OUTPUT ------------
    cartas del croupier actualizadas
    '''
    #si el croupier tiene 16 o menos, se le reparte una carta
    if puntuacion_cartas(C) >= 17:
        print('El croupier se planta con: ', mostrar_cartas(C))
    else:
        print('El croupier saca otra carta')
        C.append( repartir_una_carta_mas(J,C) )
        print('Las cartas del croupier son: ', mostrar_cartas(C))



def ronda_inicial():
    #se reparten dos cartas visibles al jugador
    global J
    J.extend( repartir_dos_cartas_al_jugador() ) #añadimos las dos cartas repartidas al azar a la lista de cartas del jugador
    print('Tus cartas son: ', mostrar_cartas(J))
    
    #se reparten dos cartas al croupier
    global C
    C.extend( repartir_dos_cartas_al_croupier(J) ) #añadimos las dos cartas repartidas al azar a la lista de cartas del croupier
    print('Las cartas del croupier son: ', mostrar_cartas(C))

    #se pregunta al jugador si quiere otra carta
    decision_jugador(J,C)

    #el crupier realiza su accion
    accion_croupier(J,C)




