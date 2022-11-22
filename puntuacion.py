"""
Módulo que agrupa todas las funcionalidades
relacionadas con la obtencion de la puntuacion en el juego del BlackJack
"""
#1# --------------------IMPORTACIONES------------------------------------

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
def valor_carta(carta):
    return cartas[carta] # devuelve el valor asociado a la carta

def puntuacion_cartas(lista):
    return sum( [valor_carta(lista_cartas[c]) for c in lista] )
