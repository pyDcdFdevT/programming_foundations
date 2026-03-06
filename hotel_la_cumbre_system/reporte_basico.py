import csv

def normalizar_texto(texto):
    return texto.strip().title()

def leer_ingresos(ruta):
    total = 0
    por_concepto = {}

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            monto = float(fila["Monto"])
            concepto = normalizar_texto(fila["Concepto"])

            total += monto

            if concepto not in por_concepto:
                por_concepto[concepto] = 0

            por_concepto[concepto] += monto

    return total, por_concepto


def leer_egresos(ruta):
    total = 0
    por_categoria = {}

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            monto = float(fila["Monto"])
            categoria = normalizar_texto(fila["Categoria"])

            total += monto

            if categoria not in por_categoria:
                por_categoria[categoria] = 0

            por_categoria[categoria] += monto

    return total, por_categoria


def imprimir_desglose(titulo, diccionario, total_general):
    print(f"\n--- {titulo} ---")

    # Ordenar de mayor a menor
    ordenado = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

    for nombre, monto in ordenado:
        porcentaje = (monto / total_general) * 100 if total_general > 0 else 0
        barra = "█" * int(porcentaje // 2)
        print(f"{nombre:15} {monto:10.2f} ({porcentaje:6.2f}%) {barra}")


def main():
    ingresos_total, ingresos_por_concepto = leer_ingresos("ingresos_operativos.csv")
    egresos_total, egresos_por_categoria = leer_egresos("egresos_operativos.csv")

    consumo_familiar = 0
    if "Consumo_Familiar" in egresos_por_categoria:
        consumo_familiar = egresos_por_categoria.pop("Consumo_Familiar")

    egresos_operativos = egresos_total - consumo_familiar

    balance_total = ingresos_total - egresos_total
    balance_operativo = ingresos_total - egresos_operativos

    margen_total = (balance_total / ingresos_total) * 100 if ingresos_total > 0 else 0
    margen_operativo = (balance_operativo / ingresos_total) * 100 if ingresos_total > 0 else 0

    reporte = []
    reporte.append("========= REPORTE FINANCIERO =========")
    reporte.append(f"Total Ingresos        : {ingresos_total:10.2f}")
    reporte.append(f"Total Egresos         : {egresos_total:10.2f}")
    reporte.append(f"Balance Total         : {balance_total:10.2f}")
    reporte.append(f"Margen Total (%)      : {margen_total:10.2f}%")

    reporte.append("\n--- Separación Interna ---")
    reporte.append(f"Egresos Operativos    : {egresos_operativos:10.2f}")
    reporte.append(f"Consumo Familiar      : {consumo_familiar:10.2f}")
    reporte.append(f"Balance Operativo     : {balance_operativo:10.2f}")
    reporte.append(f"Margen Operativo (%)  : {margen_operativo:10.2f}%")

    reporte.append("\n--- Egresos Operativos por Categoría ---")
    ordenado_egresos = sorted(egresos_por_categoria.items(), key=lambda x: x[1], reverse=True)
    for categoria, monto in ordenado_egresos:
        porcentaje = (monto / egresos_operativos) * 100 if egresos_operativos > 0 else 0
        reporte.append(f"{categoria:15} {monto:10.2f} ({porcentaje:6.2f}%)")

    reporte.append("\n--- Ingresos por Concepto ---")
    ordenado_ingresos = sorted(ingresos_por_concepto.items(), key=lambda x: x[1], reverse=True)
    for concepto, monto in ordenado_ingresos:
        porcentaje = (monto / ingresos_total) * 100 if ingresos_total > 0 else 0
        reporte.append(f"{concepto:15} {monto:10.2f} ({porcentaje:6.2f}%)")

    # Imprimir en consola
    print("\n".join(reporte))

    # Guardar en archivo
    with open("reporte_mensual.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(reporte))
        
if __name__ == "__main__":
    main()