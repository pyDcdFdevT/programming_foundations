estado = {
    "suma_total": 0,
    "contador_total": 0,
    "positivos": 0,
    "negativos": 0,
    "pares": 0,
    "impares": 0
}

def pedir_numero():
   
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            return numero
        except ValueError:
            print("Opción inválida, ingresa un NÚMERO.")

def procesar_numero(numero, estado):
    
    estado["suma_total"] += numero
    estado["contador_total"] += 1
    
    if numero > 0:
        estado["positivos"] += 1
    if numero < 0:
        estado["negativos"] += 1
    
    if numero % 2 == 0:
        estado["pares"] += 1
    else:
        estado["impares"] += 1
    
    return estado

def mostrar_resultados(estado):
    
    if estado["contador_total"] > 0:
        promedio = estado["suma_total"] / estado["contador_total"]
    else:
        promedio = 0
    
    print("\n--- RESULTADOS FINALES ---")
    print(f"Positivos: {estado['positivos']}")
    print(f"Negativos: {estado['negativos']}")
    print(f"Pares: {estado['pares']}")
    print(f"Impares: {estado['impares']}")
    print(f"Suma Total: {estado['suma_total']}")
    print(f"Promedio: {promedio:.2f}")
    
def main():
    print("### PROCESADOR DE NÚMEROS ###\n")

    while True:
        numero = pedir_numero()

        if numero == 0:
            break

        estado_actualizado = procesar_numero(numero, estado)

    mostrar_resultados(estado)

if __name__ == "__main__":
    main()