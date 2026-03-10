import csv
import os


def cargar_productos():

    directorio_actual = os.path.dirname(__file__)

    ruta_archivo = os.path.join(directorio_actual, "..", "data", "productos.csv")

    productos = {}

    with open(ruta_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        columnas_obligatorias = ["id", "nombre", "unidad_base", "precio_venta_actual", "activo"]

        for columna in columnas_obligatorias:
            if columna not in lector.fieldnames:
                raise KeyError(f"Falta columna: {columna}")

        for fila in lector:

            id_producto = fila["id"]

            productos[id_producto] = {
                "nombre": fila["nombre"],
                "unidad_base": fila["unidad_base"],
                "precio_venta_actual": float(fila["precio_venta_actual"]),
                "activo": fila["activo"] == "True"
            }

    return productos


def buscar_producto(productos, id_producto):
    return productos.get(id_producto)


def producto_existe(productos, id_producto):
    return id_producto in productos


if __name__ == "__main__":

    productos = cargar_productos()

    print("Productos cargados:")

    for id_producto, datos in productos.items():
        print(id_producto, datos)