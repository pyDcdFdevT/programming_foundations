total = 0

while True:
    print("----- Menú -----")
    print("1. Sumar número")
    print("2. Ver total")
    print("3. Reiniciar total")
    print("4. Salir")
    
    try:
        opcion = int(input("Elije una opción: "))

    except ValueError:
        print("Elija una opción válida")
        continue
    
    if opcion == 1:
        try:
            variable_suma = int(input("Sumar: "))
        except ValueError:
            print("Escribre un número entero positivo")
            continue
        if variable_suma >= 1:
                total += variable_suma
        else:
            print("Sólo números mayores que 0")
    
    elif opcion == 2:
        print(f"Total = {total}")
        
    elif opcion == 3:
        total = 0
    
    elif opcion == 4:
        break
    
    else:
        print("Opción inválida")