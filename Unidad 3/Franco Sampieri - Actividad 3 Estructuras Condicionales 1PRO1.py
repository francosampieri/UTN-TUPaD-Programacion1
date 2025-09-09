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
    mayoria_edad = 18
    edad_usuario = int(input("Ingrese su edad "))  #solicitar edad casteada como int
    if edad_usuario >= mayoria_edad: print("Es mayor de edad") #verificar si es mayor
    elif edad_usuario >= 0: print("Es menor de edad") #verificar si es menor
    else: print("ERROR: La edad ingresada es menor a 0") #por si ingreso una edad negativa

def ejercicio_2():
    aprobacion = 6
    nota = int(input("Ingresa tu nota ")) #solicitar nota casteada como int
    if nota >= aprobacion: print("Aprobado") #verificar si aprobo
    elif nota >= 0: print("Desaprobado") #verificar si desaprobo
    else: print ("ERROR: La nota no puede ser menor a 0") #por si ingresa una nota negativa

def ejercicio_3():
    numero_usuario = int(input("Ingresa un numero par ")) #solicitar numero casteado como int
    print("Ha ingresado un numero par") if numero_usuario % 2 == 0 else print ("Por favor, ingrese un número par") #condicional ternario que verifica si es par o impar

def ejercicio_4():
    #asignacion de limites
    limite_niño = 12
    limite_adolescente = 18
    limite_adulto_joven = 30
    edad_usuario = int(input("Ingrese su edad "))
    if edad_usuario >= limite_adulto_joven: print ("Eres un adulto") #verificar si es adulto
    elif edad_usuario >= limite_adolescente: print ("Eres un adulto joven") #verificar si es adulto joven
    elif edad_usuario >= limite_niño: print ("Eres un adolescente") #verificar si es adolescente
    elif edad_usuario >= 0: print ("Eres un niño") #verificar si es niño
    else: print ("ERROR: Ingresa una edad mayor a 0") #por si ingresa una edad menor a 0

def ejercicio_5():
    #asignacion de limites
    minimos_caracteres = 8
    maximos_caracteres = 14
    contraseña_usuario = input(f"Ingresa una contraseña de entre {minimos_caracteres} y {maximos_caracteres} caracteres ") #solicitar contraseña
    print("Ha ingresado una contraseña correcta") if maximos_caracteres >= len(contraseña_usuario) >= minimos_caracteres else print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") #condicional ternario que verifica si la contraseña esta dentro del rango valido

def ejercicio_6():
    import random
    from statistics import mode, mean, median
    numeros_aleatorios = [random.randint(1,100) for i in range(50)] #creacion lista 50 aleatorios
    moda_lista = mode(numeros_aleatorios) #calculo de la moda
    media_lista = mean(numeros_aleatorios) #calculo de la media
    mediana_lista = median(numeros_aleatorios) #calculo de la mediana
    if media_lista == mediana_lista == moda_lista: sesgo = "No hay sesgo" #verificar si no hay sesgo
    elif media_lista > mediana_lista > moda_lista: sesgo = "Positivo" #verificar si el sesgo es positivo
    else: sesgo = "Negativo" #En el resto de casos el sesgo es negativo
    print(f"La moda es {moda_lista}\nLa media es {media_lista}\nLa mediana es {mediana_lista}\nEl sesgo es: {sesgo}") #Resultados

def ejercicio_7():
    string_usuario = input("Ingrese una frase o palabra ") #solicitar string
    ultima_letra = string_usuario.lower()[-1] #almaceno la ultima letra del string en una variable para comparar mas facil
    if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u": string_usuario = string_usuario + "!" #verificar si es una vocal y agregar ! al string
    print(string_usuario)

def ejercicio_8():
    nombre_usuario = input("Ingrese su nombre ") #solicitar nombre
    numero_elegido = int(input("Ingrese un numero para transformar su nombre\n1 - Nombre en mayusculas\n2 - Nombre en minusculas\n3 - Primera letra del nombre en mayuscula\n")) #solicitar numero entre el 1 y el 3
    if numero_elegido in range (1,4): #condicional para ver si se eligio un numero valido
        if numero_elegido == 1: nombre_transformado = nombre_usuario.upper() #transformar nombre en mayusculas
        elif numero_elegido == 2: nombre_transformado = nombre_usuario.lower() #transformar nombre en minusculas
        elif numero_elegido == 3: nombre_transformado = nombre_usuario.capitalize() #capitalizar nombre
        print (f"Tu nombre transformado es {nombre_transformado}")
    else: print ("ERROR: Elija un numero entre el 1, el 2 y el 3") #mensaje por si elijio un numero invalido

def ejercicio_9():
    magnitud_terremoto = float(input("Ingrese la magnitud del terremoto ")) #solicitar magnitud del terremoto casteado en float
    if magnitud_terremoto < 3: print("Fue un terremoto muy leve") #verificar si fue muy leve
    elif magnitud_terremoto < 4: print("Fue un terremoto leve") #verificar si fue leve
    elif magnitud_terremoto < 5: print("Fue un terremoto moderado") #verificar si fue moderado
    elif magnitud_terremoto < 6: print("Fue un terremoto fuerte") #verificar si fue fuerte
    elif magnitud_terremoto < 7: print("Fue un terremoto muy fuerte") #verificar si fue muy fuerte
    else: print("Fue un terremoto extremo") #el resto de casos es extremo

def ejercicio_10():
    hemisferio_usuario = input("Ingrese en que hemisferio se encuentra [N/S] ").lower() #solicitar hemisferio del usuario y transformar en minusculas para comparar facilmente
    if hemisferio_usuario == "n" or hemisferio_usuario == "s": #verificar si ingreso hemisferio valido
        mes = int(input("Ingrese el numero de mes en el que se encuentra ")) #solicitar mes casteado en int
        dia = int(input("Ingrese el dia en el que se encuentra ")) #solicitar dia casteado en int
        if 0 < mes < 13 and 0 < dia < 32: #verificar si ingreso una fecha valida

            #realizo los calculos para el hemisferio Norte y luego solo los invierto en caso de que sea hemisferio sur para ahorrar codigo innecesario
            if mes == 12 or mes == 1 or mes == 2 or mes == 3: #verificar si es invierno
                if mes == 12 and dia < 21: estacion = "otoño" #por si son los primeros dias de diciembre
                elif mes == 3 and dia >= 21: estacion = "primavera" #por si son los ultimos dias de marzo
                else: estacion = "invierno"
            elif mes == 4 or mes == 5 or mes == 6: #verificar si es primavera
                if mes == 6 and dia >= 21: estacion = "verano" #por si son los ultimos dias de junio
                else: estacion = "primavera" 
            elif mes == 7 or mes == 8 or mes == 9: #verificar si es verano
                if mes == 9 and dia >= 21: estacion = "otoño" #por si son los ultimos dias de septiembre
                else: estacion = "verano"
            else: estacion = "otoño" #todos los dias restantes son de otoño
            if hemisferio_usuario == "s": #verificar si es hemisferio sur para invertir resultados
                if estacion == "verano": estacion = "invierno"
                elif estacion == "invierno": estacion = "verano"
                elif estacion == "primavera": estacion = "otoño"
                else: estacion = "primavera" #el resto de casos es otoño y se transforman en primavera
            print (f"Estas en {estacion}")
        else: print("ERROR: Ingrese una fecha valida") #por si ingresa fecha invalida
    else: print ("ERROR: Ingrese un hemisferio entre N y S") #por si ingresa hemisferio invalido

#main
funciones = [None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10]
menu_ejercicios(funciones)