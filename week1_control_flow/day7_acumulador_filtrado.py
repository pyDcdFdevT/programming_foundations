positivos = 0
negativos = 0
pares = 0
impares = 0
suma_total = 0
contador_total = 0

print("\n### INTRODUCCIÓN ###")
print("---- Éste código procesará los números ingresados y los sumará o restará a un contador, también los separará en positivos/negativos, pares/impares y sacará el promedio. ---\n")

while True:
    try:
        numero = int(input("Introduce un número: "))
        if numero == 0:
            break
        
        suma_total += numero
        contador_total += 1
        
        if numero > 0:
            positivos += 1
        else:
            negativos += 1
            
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
            
    except ValueError:
        print("Opción inválida, introduce un NÚMERO.") 
        
if contador_total > 0:
    promedio = suma_total / contador_total
else:
    promedio = 0

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Suma total = {suma_total}")
print(f"Promedio: {promedio:.2f}")