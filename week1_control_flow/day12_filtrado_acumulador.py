productos = [
    {"id": "A", "precio": 10, "activo": True},
    {"id": "B", "precio": 20, "activo": False},
    {"id": "C", "precio": 15, "activo": True},
    {"id": "D", "precio": 5, "activo": True}
]

contador = 0
suma_total = 0

for p in productos:
    if p['activo']:
        contador += 1
        suma_total += p['precio']
    
if contador > 0:
    promedio = suma_total / contador
else:
    promedio = 0

print("\n--- RESULTADOS---")
print(f"Cantidad de ACTIVOS: {contador}")
print(f"Suma de precios ACTIVOS: {suma_total}")
print(f"Promedio de ACTIVOS: {promedio:.2f}")