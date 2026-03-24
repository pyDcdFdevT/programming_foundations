from .inventario import calcular_estado_todos_productos

def mostrar_reporte():
    estados = calcular_estado_todos_productos()
    
    print("\n--- REPORTE DE INVENTARIO ---")
    
    for producto_id, estado in estados.items():
        print(f"\nProducto: {producto_id}")
        print(f"Stock: {estado['stock']:.2f}")
        print(f"Costo promedio: {estado['costo_promedio']:.2f}")
        print(f"Valor inventario: {estado['valor_inventario']:.2f}")
        print(f"Costo total ventas: {estado['costo_total_ventas']:.2f}")
        print("-" * 30)

if __name__ == "__main__":
    mostrar_reporte()