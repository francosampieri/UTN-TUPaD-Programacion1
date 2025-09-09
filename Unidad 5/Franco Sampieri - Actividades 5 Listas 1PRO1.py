"""EJERCICIO 1"""
multiplos_cuatro = list(range(4,101,4))
print(multiplos_cuatro)

"""EJERCICIO 2"""
# Crear una lista con cinco elementos (colocar los que más te gusten) y mostrar el penúltimo.
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[-2])

"""EJERCICIO 3"""
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista = []
lista.append("palabra")
lista.append("hola")
lista.append("chau")
print(lista)

"""EJERCICIO 4"""
animales = ["perro", "gato", "conejo", "pez"]
animales[-1] = "oso"
animales[-2] = "loro"
print(animales)

"""EJERCICIO 5"""
print("Ese programa remueve de la lista el numero mas grande, en este caso el 22")

"""EJERCICIO 6"""
lista = list(range(10,31,5))
print(lista[:1])

"""EJERCICIO 7"""
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fiesta", "sandero"]
print(autos)

"""EJERCICIO 8"""
dobles = []
for i in range(5,16,5):
    dobles.append(i*2)
print(dobles)

"""EJERCICIO 9"""
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

"""EJERCICIO 10"""
# Elaborar una lista anidada llamada “lista_anidada” con los siguientes elementos:
# [0] = 15
# [1] = True
# [2][0] = 25.5
# [2][1] = 57.9
# [2][2] = 30.6
# [3] = False
# Imprimir la lista resultante.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print (lista_anidada)