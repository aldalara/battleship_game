import random
import pprint
import variables
import time


# CREA EL TABLERO 10x10
def crear_tablero():
  tablero = [["." for _ in range(10)] for _ in range(10)]
  return tablero 


# FUNCION QUE AÑADE LA FLOTA DE MANERA ALEATORIA
def añadir_flota(tablero, largura):
    largura = largura

    while True:
        fila = int(random.randint(0, 9)) 
        columna = int(random.randint(0, 9))

        if tablero[fila][columna] == '.':
            break  # Encuentra una casilla vacía para comenzar
    
    while True:
        orientacion = random.choice(["norte", "sur", "este", "oeste"])  # Seleccionar orientación aleatoria

        # Llamamos a la función good_orientation para que lo verifique.
        if good_orientation(fila, columna, largura, orientacion, tablero):
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

            return tablero  # Termina la función si el barco ha sido colocado
        
        else:
            # Si la orientación no es válida, intenta de nuevo con nuevas coordenadas
            fila = int(random.randint(0, 9)) 
            columna = int(random.randint(0, 9))


# FUNCION QUE ACOTA MÁRGENES DEL TABLERO Y SUPERPOSICIONES DE LOS BARCOS
def good_orientation(fila, columna, largura, orientacion, tablero):
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

    return True  # Si todas las posiciones son válidas


# CREADOR TABLERO Y AÑADE FLOTA ALEATORIA
def tablero_flota():

    tablero = [["." for _ in range(10)] for _ in range(10)]

    for largura in variables.flota.values():
        tablero = añadir_flota(tablero, largura)
    
    return tablero


# FUNCION DISPARAR (CON COORDENADAS)
def disparar_barcos(tablero):

    fila = int(input("Introduce el número de la fila, un número del 0 al 9:"))
    columna = int(input("Introduce el número de la columna, un número del 0 al 9:"))

    if 0 <= fila < 10 and 0 <= columna < 10:

        if tablero[fila][columna] == "b":
            tablero[fila][columna] = "X"
            resultado = True
        
        elif tablero[fila][columna] == "X" or tablero[fila][columna] == "-":
            print("Estas coordenadas ya las has introducido, vuelve a disparar:")
            resultado = True
        
        else:
            tablero[fila][columna] = "-"
            resultado = False
        

    return tablero, fila, columna, resultado


# FUNCIÓN DISPARAR AUTOMÁTICO
def disparo_automatico(tablero):
    

    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
        
    if tablero[fila][columna] == "b":
        print("Te ha dado!")
        tablero[fila][columna] = "X"
        resultado = True

    elif tablero[fila][columna] == "X" or tablero[fila][columna] == "-":
            print("Estas coordenadas ya las has introducido, vuelve a disparar:")
            resultado = True
        
    else:
        print("Agua! Te has librado")
        tablero[fila][columna] = "-"
        resultado = False    

    return tablero, resultado


# FUNCION ACTUALIZAR TABLERO PLAYBOARD
def actualizar_tablero_playboard(tablero, play_board, fila, columna, resultado): #Actualiza el tablero del ordenador y me devuelve un tablero con el disparo hecho.
    # Si fue un acierto ("X" por barco hundido)
    if resultado: 
        
        play_board[fila][columna] = "X"  # Actualiza el tablero visible para el jugador
        print("¡Le has dado a un barco!")
    
    else:
        print("¡Agua! No has dado a ningún barco.")
        play_board[fila][columna] = "-"  # Actualiza el tablero visible para el jugador
    
    return play_board


# FUNCION CONTADOR    
def counter(tablero):
    contador = 0  

    for fila in tablero:
        for celda in fila:
            if celda == "X": 
                contador += 1  

    return contador


# MAIN MENU
def presenta_menu():# Sin parametros
    print("¡Bienvenido a hundir la flota! Pulsa 1 para JUGAR o 2 para SALIR")
    print(f"'1'- jugar")
    print(f"'2'- salir")
    opcion= input("¿Qué quieres hacer?")
    
    while True:

        if opcion == "2":
            print("Has salido del juego.")
            break

        elif opcion == "1":
            jugar()
            break
    
        else: 
            print("El opción que has introducido no es válida.")
            break


# FUNCION JUGAR
def jugar():

    tablero_jugador = tablero_flota()
    tablero_computer = tablero_flota()
    play_board = crear_tablero()
    
    x_computer = 0  
    x_jugador = 0 

    while True:
        
        # Empieza mi turno
        while True:

            print("Es tu turno de disparar.")
            tablero_computer, fila, columna, resultado = disparar_barcos(tablero_computer)
            play_board = actualizar_tablero_playboard(tablero_computer, play_board, fila, columna, resultado)
            #print(f"Has disparado a la fila {fila}, columna {columna}")
            
            # Actualizamos mi contador de aciertos
            x_computer = counter(tablero_computer)
            print("Tus disparos:")
            pprint.pprint(play_board)
            
            if resultado == False:
                break 

            # Verificamos que no he ganado
            if x_computer >= 20: 
                print("¡Has ganado!")
                break  # Sale del bucle y termina el juego si el jugador ha ganado
            else:
                print(f"Te faltan {20 - x_computer} aciertos para ganar.")
                break

        # Turno del computer
        while True:
            
            print("¡Es el turno de tu oponente!")
            tablero_jugador, resultado = disparo_automatico(tablero_jugador)
            time.sleep(0.5)
            x_jugador = counter(tablero_jugador)
            print(f"Tu oponente te ha dado {x_jugador} golpes.")
            print("Tu tablero:")
            pprint.pprint(tablero_jugador)
            
            if resultado == False:
                break 

            # Verificamos si la computadora ha ganado
            if x_jugador >= 20:
                print("Has perdido, la computadora ha ganado.")
                break
            #ciclos = ciclos + 1
            #print(ciclos)
            time.sleep(0.5)