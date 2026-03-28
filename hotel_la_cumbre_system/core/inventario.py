import csv
import os
from .productos import cargar_productos


def cargar_transacciones():

    directorio_actual = os.path.dirname(__file__)

    ruta_archivo = os.path.join(directorio_actual, "..", "data", "transacciones.csv")

    transacciones = []

    with open(ruta_archivo, newline="", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            transaccion = {
                "fecha": fila["fecha"],
                "tipo": fila["tipo"],
                "producto_id": fila["producto_id"],
                "cantidad": float(fila["cantidad"]),
                "precio_unitario": float(fila["precio_unitario"])
            }

            transacciones.append(transaccion)

    return transacciones

def reconstruir_stock(producto_id):

    transacciones = cargar_transacciones()

    stock = 0

    for t in transacciones:

        if t["producto_id"] != producto_id:
            continue

        if t["tipo"] == "COMPRA":
            stock += t["cantidad"]

        elif t["tipo"] == "VENTA":
            stock -= t["cantidad"]

        elif t["tipo"] == "MERMA":
            stock -= t["cantidad"]

    return stock

def calcular_estado_producto(producto_id, transacciones):

    stock = 0
    costo_promedio = 0
    costo_total_ventas = 0

    for t in transacciones:

        if t["producto_id"] != producto_id:
            continue

        tipo = t["tipo"]
        cantidad = t["cantidad"]
        precio = t["precio_unitario"]

        if tipo == "COMPRA":

            valor_actual = stock * costo_promedio
            valor_compra = cantidad * precio

            nuevo_stock = stock + cantidad

            if nuevo_stock > 0:
                costo_promedio = (valor_actual + valor_compra) / nuevo_stock

            stock = nuevo_stock


        elif tipo == "VENTA":

            costo_venta = cantidad * costo_promedio
            costo_total_ventas += costo_venta

            stock -= cantidad


        elif tipo == "MERMA":

            stock -= cantidad


    valor_inventario = stock * costo_promedio

    return {
        "producto_id": producto_id,
        "stock": stock,
        "costo_promedio": costo_promedio,
        "valor_inventario": valor_inventario,
        "costo_total_ventas": costo_total_ventas
    }

def calcular_estado_todos_productos():
    
    productos = cargar_productos()
    estados = {}
    transacciones = cargar_transacciones()
    
    for producto_id in productos:
        estado = calcular_estado_producto(producto_id, transacciones)
        
        estados[producto_id] = estado
    return estados

def validar_stock(producto_id, cantidad):
    
    if cantidad <= 0:
        return False
    
    stock_actual = reconstruir_stock(producto_id)
    
    if cantidad > stock_actual:
        return False
    
    return True

def registrar_venta(producto_id, cantidad):
    
    if not validar_stock(producto_id, cantidad):
        print("No hay stock suficiente.")
        return
    
    directorio_actual = os.path.dirname(__file__)
    ruta_archivo = os.path.join(directorio_actual, "..", "data", "transacciones.csv")
    
    import datetime
    
    with open(ruta_archivo, "rb+") as f:
        f.seek(0, os.SEEK_END)
    
    if f.tell() > 0:
        f.seek(-1, os.SEEK_END)
        ultimo = f.read(1)
        
        if ultimo != b"\n":
            f.write(b"\n")
    
    with open(ruta_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            datetime.date.today(),
            "VENTA",
            producto_id,
            cantidad,
            0
        ])



    
    print("Venta registrada.")

if __name__ == "__main__":

    estados = calcular_estado_todos_productos()
    
    for producto_id, estado in estados.items():
        print(f"\nProducto: {producto_id}")
        for clave, valor in estado.items():
            print(f"  {clave}: {valor}")

    print("\n--- PRUEBA VALIDACIÓN ---")
    print("Venta 5 ARROZ1KG:", validar_stock("ARROZ1KG", 5))
    print("Venta 100 ARROZ1KG:", validar_stock("ARROZ1KG", 100))
    print("Venta 0 ARROZ1KG:", validar_stock("ARROZ1KG", 0))
    
    print("\n--- PRUEBA VENTA ---")
    registrar_venta("ARROZ1KG", 2)