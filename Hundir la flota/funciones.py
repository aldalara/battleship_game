import random
import pprint
import variables
import time

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
        añadir_flota(tablero, largura)
    
    return tablero


# FUNCION DISPARAR (CON COORDENADAS)
def disparar_barcos(tablero):

    fila = int(input("Introduce el número de la fila, un número del 0 al 9:"))
    columna = int(input("Introduce el número de la columna, un número del 0 al 9:"))
    
    
   
    if 0 <= fila < 10 and 0 <= columna < 10:

        if tablero[fila][columna] == "b":
            print("Le has dado!")
            tablero[fila][columna] = "X"
            resultado = True
        
        else:
            print("Agua!")
            tablero[fila][columna] = "-"
            resultado = False
        

    return tablero, resultado


# FUNCIÓN DISPARAR AUTOMÁTICO
def disparo_automatico(tablero):
    

    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
        
    if tablero[fila][columna] == "b":
        print("Te ha dado!")
        tablero[fila][columna] = "X"
        resultado = True
                
        
    else:
        print("Agua! Te has librado")
        tablero[fila][columna] = "-"
        resultado = False
            


    return tablero, resultado


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
    opcion= input("¡Bienvenido a hundir la flota! ¿Qué quieres hacer?")
    print(f"'1'- jugar")
    print(f"'2'- salir")
    
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
    ciclos = 0

    while True:
        #Primero dispara el usuario.
        
        while True:
            tablero_computer, resultado = disparar_barcos(tablero_computer)

            print('Tablero computer')
            pprint.pprint(tablero_computer)
            time.sleep(0.5)
            x_computer = counter(tablero_computer)

            if x_computer >= 20:
                print("¡Has ganado!")
                break  # Sale del bucle y termina el juego si ha ganado
            else:
                print(f"Te faltan {20 - x_computer} aciertos para ganar.")
        
        while True:
            print("¡Su turno!")
            tablero_jugador, resultado = disparo_automatico(tablero_jugador)

            print('Tablero jugador')
            pprint.pprint(tablero_jugador)
            time.sleep(0.5)
            x_jugador = counter(tablero_jugador)

            # Verificamos si la computadora ha ganado
            if x_jugador >= 20:
                print("Has perdido, la computadora ha ganado.")
                break
            ciclos = ciclos + 1
            print(ciclos)
            time.sleep(0.5)