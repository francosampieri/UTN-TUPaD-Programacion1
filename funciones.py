def pedir_int_rango(mensaje, limite_inf = -float("inf"), limite_sup = float("inf")):
    """
    Pide un numero entero y valida que este dentro dentro del rango solicitado\n
    mensaje = mensaje a mostrar en input\n
    limite_inf = limite inferior del rango\n
    limite_sup = limite superior del rango\n
    retorna int
    """
    while True:
        n = input(mensaje)
        try: n = int(n)
        except: 
            print("ERROR: Ingresa un numero entero")
            continue
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n
    

def pedir_float_rango(mensaje, limite_inf = -float("inf"), limite_sup = float("inf")):
    """Pide un numero flotante y valida que este dentro dentro del rango solicitado"""
    while True:
        n = input(mensaje)
        try: n = float(n)
        except: 
            print("ERROR: Ingresa un numero")
            continue
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n
    
def menu_ejercicios(funciones):
    """Ejecuta menu para seleciconar ejercicios\n
    Recibe list con las funciones de cada ejercicio empezada por None
    """
    seguir = True
    while seguir:
        ejercicio_elegido = pedir_int_rango(f"Ingrese el numero de ejercicio que desea ejecutar (1-{len(funciones)-1}) [0] para terminar ", 0, len(funciones)-1)
        if ejercicio_elegido == 0: 
            seguir = False
            continue
        else: 
            print(f"\n -----EJERCICIO {ejercicio_elegido}-----")
            funciones[ejercicio_elegido]()
            print() #salto de linea
            input("Presione ENTER para volver") #para no sobrecargar consola
