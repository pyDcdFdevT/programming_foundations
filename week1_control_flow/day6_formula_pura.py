def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Suma 1..n")
    print("2. Suma de Cuadrados 1²..n²")
    print("3. Salir")

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Elije una opción: "))
            if opcion in (1,2,3):
                return opcion
            print("Opción inválida.")
        except ValueError:
            print("Introduce un número válido.")
    
def pedir_numero():
    while True:
        try:
            n = int(input("Introduce un número entero positivo: "))
            if n > 0:
                return n
            print("Error: El número debe ser mayor que 0.")
        except ValueError:
            print("Error: Introduce un número entero válido.")

def calcular_suma(n):
    return n * (n + 1) // 2

def calcular_suma_cuadrados(n):
    return n * (n + 1) * (2 * n + 1) // 6

def mostrar_resultado(resultado):
    print(f"\n>>> Resultado: {resultado}")

def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 3:
            print("Saliendo del sistema...")
            break
        
        elif opcion == 1:
            n = pedir_numero()
            resultado = calcular_suma(n)
            mostrar_resultado(resultado)
            
        elif opcion == 2:
            n = pedir_numero()
            resultado = calcular_suma_cuadrados(n)
            mostrar_resultado(resultado)
            
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()