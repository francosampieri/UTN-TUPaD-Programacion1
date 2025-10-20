import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__))) #agrega al path l carpeta donde esta funciones.py para evitar errores     

from funciones import menu_ejercicios, pedir_int_rango, pedir_float_rango, pedir_palabra

def ejercicio_1():
    def factorial(num):
        if num == 0: return 1
        else: return num * factorial(num-1)

    numero_usuario = pedir_int_rango("Ingresa un numero para calcular el factorial de todos los numeros entre 1 y tu numero: ", 1)
    for i in range(1,numero_usuario+1): print(f"{i}! = {factorial(i)}")

def ejercicio_2():
    def posicion_fibonacci(n):
        if n == 0 or n == 1: return n
        else: return posicion_fibonacci(n-1) + posicion_fibonacci(n-2)

    posicion_usuario = pedir_int_rango("Ingresa un numero mayor o igual a 0 para mostrar la serie de Fibonacci hasta esa posicion: ", 0)
    for i in range(posicion_usuario+1): print(posicion_fibonacci(i), end=" ")

def ejercicio_3():
    def potencia_recursiva(base,exp):
        if exp == 0: return 1
        else: return base * potencia_recursiva(base,exp-1)

    base = pedir_int_rango("Ingresa la base de la potencia: ")
    exponente = pedir_int_rango("Ingrese un exponente positivo de la potencia: ", 0)
    print(f"{base}^{exponente} = {potencia_recursiva(base, exponente)}")

def ejercicio_4():
    def decimal_a_binario(num):
        if num == 1: return "1"
        else:
            cociente = num // 2
            resto = num % 2
            return decimal_a_binario(cociente) + str(resto)
        
    decimal = pedir_int_rango("Ingrese un numero entero positivo en base decimal para convertirlo a un numero binario: ", 1)
    print(f"{decimal} decimal = {decimal_a_binario(decimal)} binario")

def ejercicio_5():
    def es_palindromo(palabra):
        if len(palabra) <= 1: return True
        else:
            if palabra[0] == palabra[-1]: return es_palindromo(palabra[1:-1])
            else: return False
    
    palabra = pedir_palabra("Ingresa una palabra para calcular si es palindromo o no: ")
    if es_palindromo(palabra): print(f"La palabra {palabra} es un palindromo")
    else: print(f"La palabra {palabra} no es un palindromo")

def ejercicio_6():
    def suma_digitos(n):
        if n //10 > 0: return n % 10 + suma_digitos(n//10)
        else: return n

    numero_usuario = pedir_int_rango("Ingrese un numero entero positivo para sumar sus cifras: ", 1)
    print(f"La suma de las cifras de {numero_usuario} es {suma_digitos(numero_usuario)}")

def ejercicio_7():
    def contar_bloques(n):
        if n == 1: return 1
        else: return n + contar_bloques(n-1)

    base = pedir_int_rango("Ingresa la base de la piramide para calcular cuantos bloque necesitas para construirla: ", 1)
    print(f"Una piramide de base {base} requiere {contar_bloques(base)} ladrillos para ser construida")

def ejercicio_8():
    def contar_digito(numero, digito):
        if numero // 10 == 0:
            if numero == digito: return 1
            else: return 0
        if numero % 10 == digito: return 1 + contar_digito(numero // 10, digito)
        else: return 0 + contar_digito(numero // 10, digito)

    numero_usuario = pedir_int_rango("Ingrese un numero entero positivo: ", 1)
    digito_usuario = pedir_int_rango(f"Ingrese un digito para saber cuantas veces se encuentra en el numero {numero_usuario}: ", 0, 9)
    print(f"El digito {digito_usuario} aparece {contar_digito(numero_usuario, digito_usuario)} veces en el numero {numero_usuario}")

ejercicios = [None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6, ejercicio_7, ejercicio_8]
menu_ejercicios(ejercicios)