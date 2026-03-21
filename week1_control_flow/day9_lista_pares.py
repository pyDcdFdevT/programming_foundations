lista_numeros = []

print("\n--- INSTRUCCIONES ---")
print("Si se ingresa el NÚMERO '0' sale del sistema")
print("\nEn este script puedes ingresar números y calcular:")
print("- Cantidad total de números pares ingresados")
print("- Suma total de números pares")
print("- Promedio de los números pares\n")

while True:
    try:
        numero = int(input("Introduce un número: "))
        if numero == 0:
            break
        lista_numeros.append(numero)
        
    except ValueError:
        print("ERROR, ingresa un NÚMERO.")       
        
lista_pares = []

for n in lista_numeros:
    if n %2 == 0:
        lista_pares.append(n)       

print(f"\nLa lista original es: {lista_numeros}")

if lista_pares:
    total_numeros_pares = len(lista_pares)
    suma_pares_total = sum(lista_pares)
    promedio = suma_pares_total / total_numeros_pares
    
    print(f"\nTotal de números pares ingresados: {total_numeros_pares} ")
    print(f"Suma total: {suma_pares_total}")
    print(f"Promedio de pares: {promedio:.2f}")
    
else:
    print("\nNo se ingresaron números pares.")