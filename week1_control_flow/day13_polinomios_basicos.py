def evaluar_polinomio(x):
    resultado = 2*(x**2) + 3* x + 1
    return resultado

lista_resultados = []

for x in range(-5,6):
    resultado = evaluar_polinomio(x)
    lista_resultados.append((x, resultado))
    print(f"x = {x} -> f(x) = {resultado:.2f}")

max_x, max_valor = lista_resultados[0]
min_x, min_valor = lista_resultados[0]

for x, resultado in lista_resultados:
    if resultado > max_valor:
        max_valor = resultado
        max_x = x
        
    if resultado < min_valor:
        min_valor = resultado
        min_x = x
        
print(f"\nMáximo -> x = {max_x}, f(x) = {max_valor}")
print(f"Mínimo -> x = {min_x}, f(x) = {min_valor}")          