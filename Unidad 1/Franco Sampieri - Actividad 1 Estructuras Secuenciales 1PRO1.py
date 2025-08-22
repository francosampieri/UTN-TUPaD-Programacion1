import math

print("Hola Mundo!")


nombre = input("Ingrese su nombre ")
print (f"Hola {nombre}!")


nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = int(input("Ingrese su edad "))
residencia = input("Ingrese su lugar de residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


radio = int(input("Ingrese el radio del circulo "))
perimetro = 2 * math.pi  * radio
area = math.pi * (radio**2)
print(f"El perimetro del circulo es {perimetro} y el area es {area}")


segundos = int(input("Ingrese los segundos para calcular en horas "))
horas = segundos / 60 / 60
print(f"{segundos} segundos equivalen a {horas} horas")


numero = int(input("Ingrese un numero para conocer su tabla de multiplicar "))
print(f"{numero} X 1 = {numero}")
print(f"{numero} X 2 = {numero * 2}")
print(f"{numero} X 3 = {numero * 3}")
print(f"{numero} X 4 = {numero * 4}")
print(f"{numero} X 5 = {numero * 5}")
print(f"{numero} X 6 = {numero * 6}")
print(f"{numero} X 7 = {numero * 7}")
print(f"{numero} X 8 = {numero * 8}")
print(f"{numero} X 9 = {numero * 9}")
print(f"{numero} X 10 = {numero * 10}")


numero1 = int(input("Ingresa el primer numero entero distinto de cero "))
numero2 = int(input("Ingresa el segundo numero entero distinto de cero "))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} / {numero2} = {division}")
print(f"{numero1} * {numero2} = {multiplicacion}")


peso_usuario = float(input("Ingresa tu peso en kilogramos "))
altura_usuario =  float(input("Ingresa tu altura en centimetros ")) / 100 #centimetros a metros
indice_masa_corporal = peso_usuario / (altura_usuario**2)
print(f"Tu indice de masa corporal es {indice_masa_corporal}")


temp_celsius = float(input("Ingrese la temperatura en grados celsius "))
temp_fahrenheit = temp_celsius * (9/5) + 32
print(f"{temp_celsius}º Celcius equivalen a {temp_fahrenheit}º Fahrenheit")


numero1 = float(input("Ingrese el primer numero "))
numero2 = float(input("Ingrese el segundo numero "))
numero3 = float(input("Ingrese el tercer numero "))
cant_numeros = 3
promedio = (numero1 + numero2 + numero3) / cant_numeros
print(f"El promedio entre {numero1}, {numero2} y {numero3} es {promedio}")