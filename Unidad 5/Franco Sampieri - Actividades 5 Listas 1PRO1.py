def validar_int_rango(mensaje,rango):
    num = input(mensaje)
    while not num.isnumeric() or int(num) not in range(rango[0],rango[1]+1): #valida primero si es un numero y despues si esta en el rango
        print("ERROR: Elige un numero entero dentro del rango")
        num = input(mensaje)
    return int(num)

def menu_ejercicios(funciones):
    """Menu para seleciconar ejercicios\n
    Recibe list con las funciones de cada ejercicio empezando por None
    """
    seguir = True
    while seguir:
        ejercicio_elegido = validar_int_rango(f"Ingrese el numero de ejercicio que desea ejecutar (1-{len(funciones)-1}) [0] para terminar ", [0, len(funciones)-1])
        if ejercicio_elegido == 0: 
            seguir = False
            continue
        else: 
            print(f"\n -----EJERCICIO {ejercicio_elegido}-----")
            funciones[ejercicio_elegido]()
            print() #salto de linea
            input("Presione ENTER para volver") #para no sobrecargar consola

def ejercicio_1():
    multiplos_cuatro = list(range(4,101,4))
    print(multiplos_cuatro)

def ejercicio_2():
    mi_lista = [1, 2, 3, 4, 5]
    print(mi_lista[-2])

def ejercicio_3():
    lista = []
    lista.append("palabra")
    lista.append("hola")
    lista.append("chau")
    print(lista)

def ejercicio_4():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[-1] = "oso"
    animales[-2] = "loro"
    print(animales)

def ejercicio_5():
    print("Ese programa remueve de la lista el numero mas grande, en este caso el 22")

def ejercicio_6():
    lista = list(range(10,31,5))
    print(lista[:2])

def ejercicio_7():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["fiesta", "sandero"]
    print(autos)

def ejercicio_8():
    dobles = []
    for i in range(5,16,5):
        dobles.append(i*2)
    print(dobles)

def ejercicio_9():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)

def ejercicio_10():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print (lista_anidada)

#main
funciones = [None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10]
menu_ejercicios(funciones)