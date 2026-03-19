lista_numeros = []

print("\n--- INSTRUCCIONES ---")
print("Si se ingresa el NÚMERO '0' sale del sistema")
print("En este script puedes ingresar números y calcular: \n-Cantidad total \n-Suma total \n-Promedio \n-Máximo \n-Mínimo \n")

while True:
    
    try:
        numero = int(input("Número ingresado: "))

        if numero == 0:
            break
       
        lista_numeros.append(numero)
    
    except ValueError:
        print("ERROR, ingresa un NÚMERO.")

if lista_numeros:
    total_numeros = len(lista_numeros)
    suma_total = sum(lista_numeros)
    promedio = suma_total / total_numeros
    numero_maximo = max(lista_numeros)
    numero_minimo = min(lista_numeros)


    print(f"\nHas ingresado {total_numeros} números")
    print(f"La suma total es: {suma_total}")
    print(f"El promedio es: {promedio:.2f}")
    print(f"El número máximo es: {numero_maximo}")
    print(f"El número minimo es: {numero_minimo}")
else:
    print("No se ingresaron números, no hay nada que calcular.")