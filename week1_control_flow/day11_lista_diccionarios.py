lista_productos = []

while True:
    producto_id = input("Ingresa el ID del producto: ")
    if producto_id == "fin": 
        break
    
    nombre = input("Ingresa el NOMBRE del producto: ")
    
    while True:
        try:
            precio = float(input("Ingresa el PRECIO del producto: "))
            if precio > 0:
                break
            
            else:
                print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Valor ingresado inválido. Ingrese un NÚMERO.")
        
    producto = {'id': producto_id,
                 'nombre': nombre,
                 'precio': precio}
    
    lista_productos.append(producto)

if lista_productos:
    
    suma_total = 0
    
    print("\nLista completa:")
    print(lista_productos)

    print("\n--- LISTA PRODUCTOS ---")
    
    for p in lista_productos:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: {p['precio']:.2f}")
        suma_total += p['precio']
    
    cantidad = len(lista_productos)
    promedio = suma_total / cantidad
    
    print(f"\nCantidad de productos: {cantidad}")
    print(f"Precio promedio: {promedio:.2f}")
    
else:
    print("Lista vacía.")