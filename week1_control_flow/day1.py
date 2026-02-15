# Uso try / except para que no explote el programa
try:
    numero = int(input())
    
# Se hace la función con la condición primero para que se adelante a la ejecución
    if numero > 10000:
        print("Número demasiado grande")
    
    else:
        acumulador = 0
        for n in range(1, numero + 1):
            acumulador += n
    
        print(acumulador)

except ValueError:
    print("Entrada inválida")
        
        
    
   