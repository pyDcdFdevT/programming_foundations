
contador = 0
while True:
    try:
        numero = int(input("Ingresa un número: "))
        if numero == 0:
            break
        elif numero < 0:
            print("Número negativo ingresa uno positivo")
            continue
        else:
            contador += numero
            print(f"Contador = {contador}")
            
    except ValueError:
        print("Valor ingresado no válido ingresa un número entero positivo")