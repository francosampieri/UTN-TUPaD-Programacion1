from funciones import pedir_int_rango, pedir_float_rango, menu_ejercicios
import math

def ejercicio_1():
    def imprimir_hola_mundo():
        print("Hola mundo!")

    #main
    imprimir_hola_mundo()

def ejercicio_2():
    def saludar_usuario(nombre):
        print(f"Hola {nombre}!")

    #main
    saludar_usuario(input("Ingrese su nombre: "))

def ejercicio_3():
    def informacion_personal(nombre, apellido, edad, residencia):
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

    #main
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = pedir_int_rango("Ingresa tu edad: ", 0)
    residencia = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

def ejercicio_4():
    def calcular_area_circulo(radio):
        return math.pi*(radio**2)

    def calcular_perimetro_circulo(radio):
        return math.pi*(radio*2)

    #main
    radio = pedir_float_rango("Ingresa el radio del circulo: ", 0)
    print("El área del circulo es", calcular_area_circulo(radio))
    print("El perimetro del circulo es", calcular_perimetro_circulo(radio))

def ejercicio_5():
    def segundos_a_horas(segundos):
        return segundos/360
    
    #main
    segundos = pedir_int_rango("Ingresa cuantos segundos quieres pasar a horas: ", 0)
    print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.")


def ejercicio_6():
    def tabla_multiplicar(numero):
        print (f"----TABLA DEL {numero}----")
        for i in range(1,11):
            print(f"{numero} X {i} = {numero*i}")

    #main
    numero = pedir_int_rango("Ingresa un numero entero para saber su tabla de multiplicar ")
    tabla_multiplicar(numero)

def ejercicio_7():
    def suma(a,b):
        return a+b
    
    def resta(a,b):
        return a-b
    
    def multiplicacion(a,b):
        return a*b
    
    def division(a,b):
        if b == 0: return None
        return a/b

    def operaciones_basicas(a, b):
        return (suma(a,b), resta(a,b), division(a,b), multiplicacion(a,b))  
    
    #main
    a = pedir_float_rango("Ingrese el primer numero para operar: ")
    b = pedir_float_rango("Ingrese el segundo numero para operar: ")
    print(f"Tupla con resultados: {operaciones_basicas(a,b)}")

def ejercicio_8():
    def calcular_imc(peso, altura):
        return peso/altura
    
    #main
    peso = pedir_float_rango("Ingrese su peso en kilogramos: ", 0)
    altura = pedir_float_rango("Ingrese su estatura en metros: ", 0)
    print("IMC =", calcular_imc(peso, altura))

def ejercicio_9():
    def celsius_a_fahrenheit(celsius):
        return (celsius * 1.8) + 32
    
    #main
    grados_celsius = pedir_float_rango("Ingrese una temperatura en grados Celsius para conocer su equivalente en Fahrenheit: ")
    print(f"{grados_celsius}ºC = {celsius_a_fahrenheit(grados_celsius)}ºF")

def ejercicio_10():
    def calcular_promedio(a, b, c):
        cant_numeros = 3
        sumatoria = a + b + c
        promedio = sumatoria / cant_numeros
        return promedio
    
    #main
    a = pedir_float_rango("Ingrese el primer numero a promediar: ")
    b = pedir_float_rango("Ingrese el segundo numero a promediar: ")
    c = pedir_float_rango("Ingrese el tercer numero a promediar: ")
    print(f"El promedio entre {a}, {b} y {c} es: {calcular_promedio(a,b,c)}")


#main
ejercicios = (None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10)
menu_ejercicios(ejercicios)