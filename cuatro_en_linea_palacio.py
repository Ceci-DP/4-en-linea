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
    # Verificamos que las filas y las columnas sean mayores o iguales a 3 para la creacion del tablero.
    #Imprimimos un mensaje que incica que inica el juego
    #Imprimimos un tablero vacio si las dimensiones se ajustan a las caracteristicas solicitadas.
    #
    
    
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
    #Contamos los simbolos "X"  y "O" de cada fila del tablero dentro del tablero.
    #Si la los dos contadores son iguales significa que sigue "X"
    #Verificamos que sea el turno de "X"  sino es el turno de "O"  


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
    #Si la columna no es cero , no es valida  ya que no se podria insertar el simbolo
    #Si verificamos  que la columna es valida entonces insertarmos el simbolo sino esta llena.

def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    #Verificamos si en todas las filas del tablero hay un simbolo de "X" o "O".
  

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
    #Recorremos el tablero en busca de algun patron ya sea en forma vertical , horizontal o en diagonal.
    #Si son todos iguales en forma horizontal , hay ganador
    #Si son todos iguales en forma vertical , hay ganador
    #Si son todos iguales en la diagonales ascendentes , hay gandor
    #Si son todos iguales en la diagonales descendente , hay gandor
    #Si hay ganador devuelve el simbolo que gano sino devuelve un vacio.

    

def imprimir_tablero(tablero):
    """" Imprimimos el tablero en un formato agradable al usuario"""
    #Imprimimos las filas del tablero.




def pedir_entero(mensaje):
    """Preguntamos si el valor ingresado es una s , en ese caso se termina el juego.
    Si el valor ingresado es un digito entonces el juego sigue , sino se imprime un mensaje que indica que
    el  valor ingresado no es un digito. 
       """


def main():# main 
    """Iniciamos el juego pidiendo al usuario las dimensiones del tablero y lo creamos visualmente
    El primer jugador es "X" asi que este inicia hasta que haya un ganador o se produzca un empate.
    """
   