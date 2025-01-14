import random
import pprint
import funciones_v2
import variables

if __name__ == "__main__": # Se activa solo, sin llamar a una función.
    
    valor_incorrecto = True

    while valor_incorrecto == True:

        jugar_manual = int(input("Quieres jugar manualmente o automático\nInserta 0 para automatico o 1 para manual: "))

        if (jugar_manual == 1) or (jugar_manual == 0):
            valor_incorrecto = False
    
    if jugar_manual == 1:
        jugar_manual = True

    else:
        jugar_manual = False # Empieza el modo automático.

    # Ganador y FIN DEL JUEGO
    ganador = funciones_v2.jugar(jugador_juega_manual = jugar_manual) # Ganador es lo que nos devuelve el while del juego.
    print("########GANADOR DEL JUEGO#########\n")
    print(ganador)