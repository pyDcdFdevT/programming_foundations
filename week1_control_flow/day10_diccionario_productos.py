id_producto = input("Ingresa el ID del producto: ")
nombre_producto = input("Ingresa el nombre del producto: ")


precio_producto = 0

while True:
    try:
        precio_producto = float(input("Ingresa precio del producto: "))
        break
    except ValueError:
        print("Valor ingresado inválido.")

producto = {
    "id_producto": id_producto,
    "nombre_producto": nombre_producto,
    "precio_producto": precio_producto
}

print(producto)

print("\n--- ID PRODUCTO ---")
print(f"Producto ID: {producto['id_producto']}")
print("\n--- NOMBRE PRODUCTO ---")
print(f"Producto: {producto['nombre_producto']}")
print("\n--- PRECIO PRODUCTO ---")
print(f"Precio: {producto['precio_producto']}")