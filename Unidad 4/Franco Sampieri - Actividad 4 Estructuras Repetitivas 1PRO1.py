"""EJERCICIO 1"""
for i in range(0,101): print(i) #for de 0 a 100 en una linea

"""EJERCICIO 2"""
numero_usuario = int(input("Ingrese un numero entero para calcular sus digitos ")) #solicita numero casteado en int
cifras = len(str(numero_usuario)) #calcula las cifras con len casteando el numero_usuario a str
if numero_usuario < 0: cifras -= 1 #si es negativo resta una cifra (ya que el - es un caracter pero no una cifra)
print(f"El numero {numero_usuario} tiene {cifras} digitos")

"""EJERCICIO 3"""
limite_inferior = int(input("Ingresa desde donde queres que empiece a sumar los numeros ")) #solicita limite inferior
limite_superior = int(input("Ingresa hasta que numero queres que sume los numeros ")) #solicita limite inferior
while limite_inferior > limite_superior:
    print("ERROR: El primer numero ingresado debe ser menor al segundo. Intentalo de nuevo")
    limite_inferior = int(input("Ingresa desde donde queres que empiece a sumar los numeros "))
    limite_superior = int(input("Ingresa hasta que numero queres que sume los numeros "))

sumatoria = 0 #inicializacion de variable sumatoria
for i in range(limite_inferior+1, limite_superior): sumatoria += i #for en una linea que suma los numeros entre limite infeiror y superior
print (f"La suma de los numeros entre {limite_inferior} y {limite_superior} es {sumatoria}")


"""EJERCICIO 4"""
sumatoria = 0 #inicializar sumatoria en 0
numero_usuario = 1 #inicializar numero del usuario en resultado ditinto a 0 para poder entrar al while
while numero_usuario != 0:
    numero_usuario = int(input("Ingresa un numero para sumar. [0] para cortar "))
    sumatoria += numero_usuario
print (f"La sumatoria de los numeros ingresados es {sumatoria}")

"""EJERCICIO 5"""
from random import randint
numero_azar = randint(0,9)
intentos = 1 #inicializar contador de intentos en 1
numero_usuario = int(input("Ingresa un numero entre 0 y 9 ")) #solicita el primer intento del usuario para entrar al while de error
while numero_usuario != numero_azar: 
    intentos += 1
    numero_usuario = int(input("ERROR. Intentalo de nuevo "))
print (f"Felicitaciones, encontraste al {numero_azar} en {intentos} intentos")

"""EJERCICIO 6"""
for i in range(98,0,-2): print (i) #for en una linea

"""EJERCICIO 7"""
numero_usuario = int(input("Ingrese un numero entero positivo para sumar todos sus antecesores "))
while numero_usuario < 0:
    numero_usuario = int(input("ERROR: Ingresa un numero entero POSITIVO"))
sumatoria = 0 #inicializar sumador en 0
for i in range (numero_usuario-1,0,-1): sumatoria += i #for en una linea
print (f"La sumatoria de todos los numeros entre 0 y {numero_usuario} es {sumatoria}")

"""EJERCICIO 8"""
#inicializacion de variables para empezar bucle
cantidad_numeros = 100
contador_pares = 0
contador_impares = 0
contador_ceros = 0
contador_positivos = 0
contador_negativos = 0
for i in range(cantidad_numeros):
    numero_usuario = int(input(f"Ingresa un numero[{i+1}]: "))
    #verificar par, impar o cero
    if numero_usuario == 0: 
        contador_ceros += 1
        continue #pasa a la siguiente iteracion
    elif numero_usuario % 2 == 0: contador_pares +=1
    else: contador_impares +=1

    #verificar positivo o negativo
    if numero_usuario > 0: contador_positivos += 1
    else: contador_negativos += 1

print (f"{contador_ceros} ceros\n{contador_pares} pares\n{contador_impares} impares\n{contador_positivos} positivos\n{contador_negativos} negativos")

"""EJERCICIO 9"""
cantidad_numeros = 100
sumatoria = 0
for i in range(cantidad_numeros): 
    numero_usuario = int(input(f"Ingresa un numero[{i+1}]: "))
    sumatoria += numero_usuario
promedio = sumatoria / cantidad_numeros
print(f"La media de los {cantidad_numeros} numeros que ingresaste es {promedio}")

"""EJERCICIO 10"""
numero_usuario = int(input("Ingresa un numero para invertirlo "))
cifras = len(str(numero_usuario)) #obtener cifras con funcion len casteando el numero a str
numero_nuevo = ""
for i in range(cifras, 0, -1):
    if numero_usuario < 0 and i==1: #si es negativo añade el menos adelante y saltea la ultima iteracion
        numero_nuevo = "-" + numero_nuevo
        continue

    numero_nuevo = numero_nuevo + str(numero_usuario)[i-1] #suma a la cadena numero_nuevo el digito opuesto de numero_usuario
numero_nuevo = int(numero_nuevo) #pasar str a int para resultado numerico
print (numero_nuevo)