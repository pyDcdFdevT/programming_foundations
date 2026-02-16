#"""
# Day 2 - While Loops
# Objetivo:
# -Entender que While evalúa la condición antes de ejecutar cada iteración.
# -Practicar el uso de 'continue'.
# -Comprender como el orden del incremento afecta la salida.
# 
# Conclusión:
# El orden de las instrucciones dentro del bucle cambia el estado antes o después
# de la evaluación, lo que altera completamente el comportamiento del programa
# """

contador = 0 

while contador < 10:
    contador +=1
    if contador == 5:
        continue
    print(contador)