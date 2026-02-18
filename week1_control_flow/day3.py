numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero entero positivo: "))
        if numero < 0:
             print("Escribe un número positivo")
    except ValueError:
        print("Escribe un número entero positivo")
        