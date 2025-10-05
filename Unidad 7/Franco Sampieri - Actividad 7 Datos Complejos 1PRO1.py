import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__))) #agrega al path la carpeta donde esta funciones.py para evitar errores     

from funciones import menu_ejercicios, pedir_int_rango, pedir_float_rango

def ejercicio_1():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
    print("Diccionario original:", precios_frutas)

    precios_frutas["Naranja"] = 1200
    precios_frutas["Manzana"] = 1500
    precios_frutas["Pera"] = 2300

    print("Diccionario modificado:", precios_frutas)

def ejercicio_2():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, "Naranja": 1200, "Manzana": 1500, "Pera": 2300} 
    print("Diccionario Original:", precios_frutas)

    precios_frutas["Banana"] = 1330
    precios_frutas["Manzana"] = 1700
    precios_frutas["Melón"] = 2800

    print("Diccionario modificado:", precios_frutas)

def ejercicio_3():
    precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, "Naranja": 1200, "Manzana": 1700, "Pera": 2300}
    frutas = list(precios_frutas.keys())
    print("Frutas disponibles:", frutas)

def ejercicio_4():
    def crear_contacto():
        repetido = True
        while repetido:
            nombre_contacto = input("Ingrese el nombre del nuevo contacto: ")
            if nombre_contacto in contactos.keys(): #verifica si el nombre esta en uso
                print("Ya tienes un contacto con ese nombre")
                continue
            telefono_contacto = pedir_int_rango("Ingrese el numero telefonico del contacto: ")
            repetido = False
        contactos[nombre_contacto] = telefono_contacto

    contactos = {}
    for i in range(5): crear_contacto()
    
    nombre_buscado = input("Ingrese el nombre del contacto que desea buscar: ")
    numero_encontrado = contactos.get(nombre_buscado)
    if numero_encontrado != None: print(f"Nombre: {nombre_buscado}\nTelefono: {numero_encontrado}")
    else: print("No tiene ningun contacto agendado con ese nombre")

def ejercicio_5():
    """ 
    Solicita al usuario una frase e imprime:
    - Las palabras únicas (usando un set).
    - Un diccionario con la cantidad de veces que aparece cada palabra.
    """
    frase = input("Ingrese una frase para mostrar sus palabras unicas y contar cada palabra")
    palabras_frase = frase.split()
    unicas = set(palabras_frase)
    apariciones = {}
    for palabra in palabras_frase:
        apariciones[palabra] = palabras_frase.count(palabra)

    print("Palabras unicas:", unicas)
    print("Apariciones:", apariciones)

def ejercicio_6():
    def asignar_notas():
        notas_1 = pedir_float_rango("Ingrese la primer nota del alumno: ", 1, 10)
        notas_2 = pedir_float_rango("Ingrese la segunda nota del alumno: ", 1, 10)
        notas_3 = pedir_float_rango("Ingrese la tercer nota del alumno: ", 1, 10)
        return (notas_1, notas_2, notas_3)

    def crear_alumno():
        nombre = input("Ingrese el nombre del alumno: ")
        alumnos[nombre] = asignar_notas()

    #main
    alumnos = {}
    cant_notas = 3
    for i in range(cant_notas):
        crear_alumno()

    for alumno in alumnos.items():
        promedio = (alumno[1][0] + alumno[1][1] + alumno[1][2]) / cant_notas
        print(f"El promedio del alumno {alumno[0]} es {promedio}")

def ejercicio_7():
    parcial_1 = (10,6,4,2,9)
    parcial_2 = (6,2,5,8,6)
    ambos_aprobados = []
    alguno_aprobado = []
    uno_aprobado = []

    for i in range(len(parcial_1)):
        primer_aprobado = parcial_1[i] >= 6
        segundo_aprobado = parcial_2[i] >= 6

        if primer_aprobado or segundo_aprobado: #verificar si aprobo alguno
            alguno_aprobado.append(i+1)
            if primer_aprobado and segundo_aprobado: ambos_aprobados.append(i+1) #verificar si aprobo los dos
            else: uno_aprobado.append(i+1)

    print(f"Estudiantes que aprobaron ambos: {ambos_aprobados}\nEstudiantes que aprobaron solo uno {uno_aprobado}\nEstudiantes que aprobaron algun parcial {alguno_aprobado}")
            
def ejercicio_8():
    def agregar_stock():
        producto_elegido = input("Ingrese un producto para agregar stock: ")

        #si el producto existe
        if producto_elegido in productos.keys():
            print(f"El producto {producto_elegido} tiene {productos.get(producto_elegido)} unidades en stock.")
            unidades_agregar = pedir_int_rango("Cuantas unidades desea agregar: ",1)
            productos[producto_elegido] += unidades_agregar

        #si no existe
        else:
            print(f"{producto_elegido} es un nuevo producto")
            unidades_agregar = pedir_int_rango("Cuantas unidades desea agregar: ",1)
            productos[producto_elegido] = unidades_agregar

    def consultar_stock():
        producto_elegido = None
        while producto_elegido not in productos.keys():
            if producto_elegido != None:
                print("ERROR: El producto ingresado no existe en el stock. Intentalo de nuevo")
            producto_elegido = input("Ingrese el nombre del producto para saber su stock: ")
        print(f"El producto {producto_elegido} tiene {productos[producto_elegido]} unidades en stock")

    def menu_stock():
        seguir = True
        while seguir:
            eleccion = pedir_int_rango("Ingresa la accion a realizar\n0- Terminar ejecucion\n1- Consultar stock de un producto\n2- Agregar stock\n",0,2)
            if eleccion == 0: seguir = False
            elif eleccion == 1: consultar_stock()
            else: agregar_stock()
   
    #main
    productos = {"Oreo":10,
    "Pepitos":5,
    "Toddy":2,
    "Rumba":12,
    "Sonrisas":21}

    menu_stock()

def ejercicio_9():
    def imprimir_dias():
        print(f"Dias en la agenda:", devolver_dias())

    def devolver_dias():
        #retorna lista con los dias en la agenda sin repetir y ordenados
        dias = [i[0] for i in list(agenda.keys())]
        return (list(dict.fromkeys(dias))) #Elimina duplicados sin perder orden

    def devolver_horas(dia):
        #retorna lista con los dias en la agenda sin repetir y ordenados
        horas = [i[1] for i in list(agenda.keys()) if i[0] == dia]
        return horas
    
    def imprimir_horas(dia):
        print(f"Horas con actividades el dia {dia}:", devolver_horas(dia))

    #main
    agenda = {("Lunes", "08:00"):"Matemática",
    ("Lunes", "19:30"):"Futsal",
    ("Martes", "08:00"):"Organización",
    ("Martes", "16:00"):"Inglés",
    ("Miercoles", "08:00"):"Arquitectura",
    ("Miercoles", "19:30"):"Futsal",
    ("Jueves", "08:00"):"Programación",
    ("Viernes", "08:00"):"Programación",
    ("Viernes", "19:30"):"Futsal",
    }

    seguir = True
    while seguir:
        eleccion_dia = None
        while eleccion_dia not in devolver_dias() and eleccion_dia != "0":
            if eleccion_dia != None: print("ERROR: Ingrese un dia de la agenda")
            imprimir_dias()
            eleccion_dia = input("Ingrese el dia del que quiere consultar una actividad o 0 para finalizar: ").capitalize()

        if eleccion_dia == "0":
            seguir = False
            continue
        
        print()
        eleccion_hora = None
        while eleccion_hora not in devolver_horas(eleccion_dia):
            if eleccion_hora != None: print(f"ERROR: Ingrese una hora con alguna actividad en el dia {eleccion_dia}")
            imprimir_horas(eleccion_dia)
            eleccion_hora = input(f"Ingrese una hora para saber si hay una actividad a esa hora el dia {eleccion_dia} (formato hh:mm): ")

        print(f"El dia {eleccion_dia} a las {eleccion_hora} tienes {agenda[eleccion_dia, eleccion_hora]}")
        print()

def ejercicio_10():
    paises = {"Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París",
    "Japón": "Tokio"
}
    print("Diccionario original:", paises)
    paises_invertido = {i[1]:i[0] for i in paises.items()}
    print("Diccionario invertido:", paises_invertido)


ejercicios = [None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10]
menu_ejercicios(ejercicios)
