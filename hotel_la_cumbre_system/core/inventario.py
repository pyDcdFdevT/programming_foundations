import csv
import os


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


if __name__ == "__main__":

    transacciones = cargar_transacciones()

    print("Transacciones cargadas:")
    for t in transacciones:
        print(t)

    print("\nStock COCA2L:")

    stock = reconstruir_stock("COCA2L")

    print(stock)