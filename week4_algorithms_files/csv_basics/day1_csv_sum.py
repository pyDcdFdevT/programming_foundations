import os
import csv

def calcular_estadisticas(ruta_archivo):
    total = 0
    cantidad = 0

    with open(ruta_archivo, newline="") as archivo:
        lector = csv.DictReader(archivo)

        if "precio" not in lector.fieldnames:
            raise KeyError("La columna 'precio' no existe en el archivo.")

        for fila in lector:
            precio = float(fila["precio"])
            total += precio
            cantidad += 1

    promedio = total / cantidad if cantidad > 0 else 0
    return total, cantidad, promedio


def main():
    base_dir = os.path.dirname(__file__)
    ruta = os.path.join(base_dir, "ventas.csv")

    try:
        total, cantidad, promedio = calcular_estadisticas(ruta)

        print("\n--- REPORTE DE VENTAS ---")
        print(f"Cantidad de productos: {cantidad}")
        print(f"Total de ventas: {total}")
        print(f"Promedio por producto: {promedio:.2f}")

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")

    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()