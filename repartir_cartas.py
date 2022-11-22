"""
Módulo que agrupa todas las funcionalidades
relacionadas con repartir cartas en el juego del BlackJack
"""

#1# --------------------IMPORTACIONES------------------------------------
import random


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

#3# --------------------FUNCIONES-------------------------------------------------

def repartir_carta_disponible(lista):
    '''
    Esta funcion devuelve una carta aleatoria que no este en la lista de cartas que ya se han repartido
    -INPUT -------------
    lista : list
        lista de indices de cartas ya repartidas
    -OUTPUT ------------
    carta : int
        indice de la carta elegida al azar
    '''
    while True: #bucle para sacar una carta que no se haya repartido antes
        carta = random.randint(0, len(lista_cartas)-1) #cogemos una carta aleatoria
        if carta not in lista:
            return carta


def repartir_dos_cartas_al_jugador():
    '''
    Esta funcion devuelve una lista de dos cartas aleatorias
    -INPUT -------------
    -OUTPUT ------------
    ( c1, c2 ) : list
        c1 : int
            indice de la carta1 en la coleccion
        c2 : int
            indice de la carta2 en la coleccion
    '''
    seleccion = []
    carta1 = random.randint(0, len(lista_cartas)-1) 
        #elegir al azar uno de los indices de la coleccion de cartas
        #randint(a,b) es un numero aleatorio N tq a <= N <= b
    seleccion.append(carta1)

    #carta2 tiene que ser distinta de carta1
    carta2 = repartir_carta_disponible(seleccion)
    seleccion.append(carta2) #añadimos la carta2 a la lista de cartas seleccionadas
    
    return seleccion #lista con los indices de las dos cartas que han tocado


def repartir_dos_cartas_al_croupier():
    '''
    Esta funcion devuelve una lista de dos cartas aleatorias para el croupier
    -INPUT -------------
    -OUTPUT ------------
    ( c1, c2 ) : list
        c1 : int
            indice de la carta1 en la coleccion
        c2 : int
            indice de la carta2 en la coleccion
    '''
    seleccion = []
    cartas_no_disponibles = repartir_dos_cartas_al_jugador() #lista de cartas que ya se han repartido antes

    #se reparte la 1º carta
    carta1 = repartir_carta_disponible(cartas_no_disponibles)
    seleccion.append(carta1)
    cartas_no_disponibles.append(carta1) #añadimos carta1 a la lista de cartas que ya se han repartido

    #se reparte la 2º carta
    carta2 = repartir_carta_disponible(cartas_no_disponibles)
    seleccion.append(carta2)

    return seleccion


def repartir_una_carta_mas(J, C):
    '''
    Esta funcion devuelve una carta aleatoria 
    teniendo en cuenta todas las que ya se han repartido
    -INPUT -------------
    -OUTPUT ------------
    [carta] : list
        lista de un elemento con el indice de la carta
    '''
    #las cartas que ya se han repartido son las que tienen el jugador y el croupier
    cartas_no_disponibles = J + C

    return [repartir_carta_disponible(cartas_no_disponibles)]



