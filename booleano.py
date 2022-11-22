"""
Módulo que agrupa todas las funcionalidades
que permiten pedir una entrada cuya respuesta es VERDADERO/SI o FALSO/NO
"""

#----------------------------#1# IMPORTACIONES

#----------------------------#2# DECLARAR VARIABLES
SI = ("s", "si", "y", "yes", "1")
VERDADERO = ("v", "verdadero", "t", "true", "1")


#----------------------------#3# DEFINIR FUNCIONES

def pedir_entrada_si_o_no(mensaje):
    try:
        entrada = input(mensaje).lower()
        if entrada in SI:
            return True
    except:
        return False
