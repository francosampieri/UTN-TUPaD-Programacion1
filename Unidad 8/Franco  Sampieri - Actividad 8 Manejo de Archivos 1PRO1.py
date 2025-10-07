with open ("Unidad 8/productos.txt", "r") as archivo:
    for linea in archivo:
        elementos = linea.strip().split(",")
        print(f"Producto: {elementos[0]} | Precio: {elementos[1]} | Cantidad: {elementos[2]}")

nuevo_producto = []
nuevo_producto.append(input("Ingrese el nombre del nuevo producto: "))
nuevo_producto.append(input(f"Ingrese el precio de {nuevo_producto[0]}: ") + ",")
nuevo_producto.append(input(f"Ingrese la cantidad de stock de {nuevo_producto[0]}: ") + "\n")
nuevo_producto[0] += "," #lo agrego al final para poder llamarlo correctamente en los input de precio y cantidad

with open("Unidad 8/productos.txt", "a") as archivo:
    archivo.writelines(nuevo_producto)

productos = []
with open("Unidad 8/productos.txt", "r") as archivo:
    for linea in archivo:
        elementos = linea.strip().split(",")
        productos.append({"Nombre":elementos[0], "Precio":elementos[1], "Cantidad":elementos[2]})

producto_buscado = input("Ingrese el nombre del producto a buscar: ")
nombres_productos = [dict["Nombre"] for dict in productos]
if producto_buscado in nombres_productos:
    i = 0
    for producto in productos:
        if producto["Nombre"] == producto_buscado:
            break
        i+=1

    print(f"Nombre: {producto_buscado}, Precio: {productos[i]["Precio"]}, Cantidad: {productos[i]["Cantidad"]}")
else:
    print(f"ERROR: El producto {producto_buscado} no existe en el documento")

with open("Unidad 8/productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(producto["Nombre"] + ",")
        archivo.write(producto["Precio"] + ",")
        archivo.write(producto["Cantidad"] + "\n")