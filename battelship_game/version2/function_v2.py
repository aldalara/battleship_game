import random
import pprint
from variables import flota
import time



def crear_tablero():
  """
  Función para crear tablero 10x10 vacío.
  """
  tablero = [["." for _ in range(10)] for _ in range(10)]
  return tablero



def coordenadas_iniciales_validas(tablero, fila, columna):
    """
    Funcion para determinar si las coordenadas iniciales son validas.
    """
    valor_coordenada = tablero[fila][columna]
    if valor_coordenada == '.':
        return True
    else:
        return False



def colocar_barco(tablero, orientacion, largura, fila, columna):
    """
    Funcion para colocar un barco en una orientacion determinada
    """
    if orientacion == "norte":
        for i in range(largura):
            tablero[fila - i][columna] = 'b' # Colocar barco
                
    elif orientacion == "sur":
        for i in range(largura):
            tablero[fila + i][columna] = 'b'

    elif orientacion == "este":
        for i in range(largura):
            tablero[fila][columna + i] = 'b'

    elif orientacion == "oeste":
        for i in range(largura):
            tablero[fila][columna - i] = 'b'

    return tablero






def good_orientation(fila, columna, largura, orientacion, tablero):
    """
    Función que verifica que los barcos no se salgan del tablero
    ni se solapen con otros barcos
    """
    if orientacion == "norte":
        if fila - largura + 1 < 0:  # Verifica que no se sale del tablero al norte.
            return False #Porque en la función añadir barcos solo se ejecuta y finalia while True.
        
        for i in range(largura):
            if tablero[fila - i][columna] != '.':  # Comprueba cada casilla para que sea desigual a "b"
                return False
                
    elif orientacion == "sur":
        if fila + largura - 1 > 9:  # Verifica que no se sale del tablero al sur 
            return False
        for i in range(largura):
            if tablero[fila + i][columna] != '.':
                return False

    elif orientacion == "este":
        if columna + largura + 1 > 9: # Verifica que no se sale del tablero al este
            return False
        for i in range(largura):
            if tablero[fila][columna + i] != '.':
                return False

    elif orientacion == "oeste": 
        if columna - largura + 1 < 0:  
            return False
        for i in range(largura):
            if tablero[fila][columna - i] != '.':
                return False

    return True  # Si todas las posiciones son válidas good_orientation devuelve True (IMPORTANTE PARA AÑADIR LA FLOTA)




def añadir_flota(tablero, largura):
    """
    Funcion para añadir los barco. Esta función va dentro de un bucle for.
    Utilizamos good_orientation para verificar que todo está OK.
    """
    all_ok = False
    while all_ok == False: # Solo cuando all_ok es True, sale del bucle.
        fila = int(random.randint(0, 9)) 
        columna = int(random.randint(0, 9))

        if coordenadas_iniciales_validas(tablero, fila, columna):

            orientacion = random.choice(["norte", "sur", "este", "oeste"])

            # Llamamos a la función good_orientation para que lo verifique.
            if good_orientation(fila, columna, largura, orientacion, tablero):
                tablero = colocar_barco(tablero, orientacion, largura, fila, columna)
                return tablero

        


def tablero_flota():
    """
    Función para crear el tablero y añadir la flota 
    al mismo tiempo
    """
    tablero = crear_tablero()

    for nombre_barco, largura in flota.items():
        tablero = añadir_flota(tablero, largura)
    
    return tablero



def coordenadas_validas_tablero(fila, columna):
    """
    Función para asegurarnos de que las coordenadas
    a las que disparamos son válidas
    """
    if (0 <= fila < 10) and (0 <= columna < 10):
        # Este True hace que en la función de introducir las coordenadas salga del bucle, si devuelve False, este se repite.
        return True 
    return False



def disparar_a_coordenadas(tablero, fila, columna):
    """
    Función para registrar 
    los resultados en el resultados.
    """
    if tablero[fila][columna] == "b":
        tablero[fila][columna] = "X"
        disparo_acertado = True
    
    elif tablero[fila][columna] == "X" or tablero[fila][columna] == "O":
        print("Estas coordenadas ya las has introducido.")
        disparo_acertado = False
    
    else:
        tablero[fila][columna] = "O"
        disparo_acertado = False

    return tablero, fila, columna, disparo_acertado



def disparo_manual(tablero):
    """
    Función para utilizar el disparo manual
    e introducir las coordenadas.
    """
    coordenadas_validas = False 
    
    while coordenadas_validas == False:

        fila = int(input("Introduce el número de la fila, un número del 0 al 9:"))
        columna = int(input("Introduce el número de la columna, un número del 0 al 9:"))
        
        coordenadas_validas = coordenadas_validas_tablero(fila, columna) # Utilizamos la función de validar las coordenadas.

        if coordenadas_validas:
            # Si todo es correcto, llama a la función disparar a coordenadas
            tablero, fila, columna, disparo_acertado = disparar_a_coordenadas(tablero, fila, columna) 
            return tablero, fila, columna, disparo_acertado
        


def disparo_automatico(tablero):
    """
    Función para utilizar el disparo automático.
    """
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)

    coordenadas_validas = coordenadas_validas_tablero(fila, columna) # Utilizamos la función de validar las coordenadas.

    if coordenadas_validas:
        # Si todo es correcto, llama a la función disparar a coordenadas
        tablero, fila, columna, disparo_acertado = disparar_a_coordenadas(tablero, fila, columna)
        return tablero, fila, columna, disparo_acertado


 
def counter(tablero):
    """
    Función para crear un contador 
    que registre los disparos acertados.
    """
    contador = 0  

    for fila in tablero:
        for celda in fila:
            if celda == "X": 
                contador += 1  

    return contador



def actualizar_tablero_playboard(tablero, play_board, fila, columna): #Actualiza el tablero del ordenador y me devuelve un tablero con el disparo hecho.
    """
    Funcion que actualiza el tablero de acciones realizadas de un jugador.
    """
    play_board[fila][columna] = tablero[fila][columna]
    return play_board

    


def jugar(jugador_juega_manual):
    """
    Función con el flujo del juego.
    """

    tablero_jugador = tablero_flota()
    tablero_computer = tablero_flota()
    play_board = crear_tablero()
    
    x_computer = 0  
    x_jugador = 0

    valor_ganador = sum(flota.values()) # Cantidad total de la flota.

    contador_ciclos = 0

    # Cuando el contador llegue al valor de la cantidad de barcos, se termina el bucle. 
    while (x_computer < valor_ganador) and (x_jugador < valor_ganador):
        print(f'########## TURNO {contador_ciclos} ###############') # Aviso del turno en el que nos encontramos.
        
        # Turno jugador
        disparo_jugador_acertado = True
        print("Es tu turno de disparar.")
        while disparo_jugador_acertado == True:

            if jugador_juega_manual == True: # En .main puedes elegir jugar manualmenre == 1: True
                tablero_computer, fila, columna, disparo_jugador_acertado = disparo_manual(tablero_computer)

            else: # Si la opción es == 0: False los tableros juegan de manera automática.
                 tablero_computer, fila, columna, disparo_jugador_acertado = disparo_automatico(tablero_computer)

            play_board = actualizar_tablero_playboard(tablero_computer, play_board, fila, columna)
            
            if disparo_jugador_acertado == False:
                print("Agua! Has fallado!")
            else:
                print('Has acertado!')
        
        # Actualizamos mi contador de aciertos
        x_computer = counter(tablero_computer)

        # Verificamos que no he ganado
        print(f"Te faltan {valor_ganador - x_computer} aciertos para ganar.")

        print()
        print("TUS DISPAROS:\n")
        pprint.pprint(play_board)
        print()
        

        # Turno computer
        disparo_computer_acertado = True
        print("Es el turno de computer!")

        while disparo_computer_acertado == True:
            tablero_jugador, fila, columna, disparo_computer_acertado = disparo_automatico(tablero_jugador)
            
            if disparo_computer_acertado == False:
                print("Agua! Te has librado!")
            
            else:
                print('Tocado! El ordenador te ha dado!')
            print('MI TABLERO:\n')
            pprint.pprint(tablero_jugador)
        
        # Actualizamos el contador de la maquina
        x_jugador = counter(tablero_jugador)
        # Verificamos que no he ganado
        print(f"A la máquina le faltan {valor_ganador - x_jugador} aciertos para ganarte.")

        contador_ciclos += 1

    # En el momento que el x_jugador llega a 20
    if x_jugador == 20:
        return "Máquina" # Devolvemos Maquina (Vencedor)
    else:
        return "Jugador" # Sino Jugador vence