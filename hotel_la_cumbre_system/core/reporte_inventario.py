from .inventario import calcular_estado_todos_productos

def mostrar_reporte():
    estados = calcular_estado_todos_productos()
    
    print("\n--- REPORTE DE INVENTARIO ---")
    
    for producto_id, estado in estados.items():
        print(f"\nProducto: {producto_id}")
        print(f"Stock: {estado['stock']}")
        print(f"Costo promedio: {estado['costo_promedio']}")
        print(f"Valor inventario: {estado['valor_inventario']}")
        print(f"Costo total ventas: {estado['costo_total_ventas']}")

if __name__ == "__main__":
    mostrar_reporte()