from typing import List

def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo."""
    # Verificamos que las filas y las columnas sean mayores o iguales a 3
    if n_filas >= 3 and n_columnas >= 3:
        print("Los valores ingresados son correctos ¡Que comience el juego!")  # Solo imprimir si los valores son correctos
        tablero = []
        for f in range(n_filas):
            f_tablero = []
            for c in range(n_columnas):
                f_tablero.append(' ')
            tablero.append(f_tablero)  # Agregar la fila al tablero
        return tablero
    else:
        if not int(n_filas) or not int(n_columnas):
            return("El número de filas y columnas deben ser enteros positivos mayores a tres..")
        return []
    
def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    contador_x = sum(fila.count('X') for fila in tablero)
    contador_o = sum(fila.count('O') for fila in tablero)
    
    return contador_x == contador_o

def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado """
    if columna < 0 or columna >= len(tablero[0]):
        return False  # La columna no es válida
    for fila in reversed(tablero):#Recorremos las filas de abajo hacia arriba el tablero.
        if fila[columna] == ' ':
            fila[columna] = 'X' if es_turno_de_x(tablero) else 'O'
            return True
    return False  # La columna está llena

def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    return all('X' in fila and 'O' in fila for fila in tablero)

def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`"""

    for fila in tablero:
        #Si son todos iguales en forma horizontal , hay ganador
        for i in range(len(fila) - 3):
            if all(fila[i + j] == 'X' for j in range(4)):
                return 'X'
            if all(fila[i + j] == 'O' for j in range(4)):
                return 'O'

    for columna in range(len(tablero[0])):
        #Si son todos iguales en forma vertical , hay ganador
        for i in range(len(tablero) - 3):
            if all(tablero[i + j][columna] == 'X' for j in range(4)):
                return 'X'
            if all(tablero[i + j][columna] == 'O' for j in range(4)):
                return 'O'

    for i in range(len(tablero) - 3):
        #Si son todos iguales en la diagonales ascendentes , hay gandor
        for j in range(len(tablero[0]) - 3):
            if all(tablero[i + k][j + k] == 'X' for k in range(4)):
                return 'X'
            if all(tablero[i + k][j + k] == 'O' for k in range(4)):
                return 'O'

    for i in range(len(tablero) - 3):
        #Si son todos iguales en la diagonales descendente , hay gandor
        for j in range(3, len(tablero[0])):
            if all(tablero[i + k][j - k] == 'X' for k in range(4)):
                return 'X'
            if all(tablero[i + k][j - k] == 'O' for k in range(4)):
                return 'O'

    return ' '

def imprimir_tablero(tablero):
    """" Imprimimos el tablero en un formato agradable al usuario"""
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")




def pedir_entero(mensaje):
    """Preguntamos si el valor ingresado es una s , en ese caso se termina el juego.
    Si el valor ingresado es un digito entonces el juego sigue , sino se imprime un mensaje que indica que
    el  valor ingresado no es un digito. 
       """
    while True:
        entrada = input(mensaje)
        if entrada.lower() == 's':
            print("El juego se ha detenido a pedido del usuario.")
            exit()
        if entrada.isdigit():
            return int(entrada)
        else:
            print("El valor ingresado no es un número entero válido. Intente nuevamente.")

def main():
    n_filas = pedir_entero("Ingrese el número de filas para el tablero: ")
    n_columnas = pedir_entero("Ingrese el número de columnas para el tablero: ")

    if n_filas < 1 or n_columnas < 1:
        print("El número de filas y columnas debe ser al menos 1.")
        return

    tablero = crear_tablero(n_filas, n_columnas)
    imprimir_tablero(tablero)

    jugador_actual = 'X'

    while True:
        #Hacemos -1 ya que los indices arrancan en 0
        columna = pedir_entero(f"Jugador {jugador_actual}, elige una columna (1-{n_columnas}) o presione s para salir : ") - 1
        if insertar_simbolo(tablero, columna):
            imprimir_tablero(tablero)

            if obtener_ganador(tablero) == jugador_actual:
                print(f"¡Jugador {jugador_actual} ha ganado!")
                break

            if tablero_completo(tablero):
                print("El juego ha terminado en empate.")
                break

            jugador_actual = 'X' if jugador_actual == 'O' else 'O'

main()