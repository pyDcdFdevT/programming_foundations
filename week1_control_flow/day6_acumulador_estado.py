def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Suma")
    print("2. Potencia")
    print("3. Resultado")
    print("4. Resetear acumulador (Volver a 0).")
    print("5. Salir")

def pedir_opcion():
    try:
        return int(input("Elije una opción: "))
    except ValueError:
        return -1
    
def pedir_numero():
    while True:
        try:
            return int(input("Introduce el número a procesar: "))
        except ValueError:
            print("Error: Introduce un número válido.")

def mostrar_resultado(resultado):
    print(f"Resultado: {resultado} ")
    
def acumular_valor(total_actual, n):
    return total_actual + n

def acumular_potencia(n):
    return n ** 2

def main():
    ultimo_resultado = 0
    
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 5:
            print("Saliendo del sistema...")
            break
        
        elif opcion == 1:
            num = pedir_numero()
            ultimo_resultado = acumular_valor(ultimo_resultado, num)
            print("Cálculo suma realizado. El total ha crecido.")
        
        elif opcion == 2:
            num = pedir_numero()
            valor_potencia = acumular_potencia(num)
            ultimo_resultado = acumular_valor(ultimo_resultado, valor_potencia)
            print(f"Potencia de {num} añadida al total.")
            
        elif opcion == 3:
            mostrar_resultado(ultimo_resultado)
            
        elif opcion == 4:
            ultimo_resultado = 0
            print("\n*** ACUMULADOR RESETEADO A 0 ***")
            
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()