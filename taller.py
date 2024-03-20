print("******TIENDA DE COMICS******")
print("*********BIENVENIDO*********")
print("POR FAVOR ELIJE UNA OPCION")


import random

inventario = []

while True:
    print("\nMenú de opciones:")
    print("1. Registrar un producto")
    print("2. Mostrar productos en bodega")
    print("3. Buscar producto por nombre")
    print("4. Modificar número de unidades compradas")
    print("5. Eliminar un producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1": 
        producto = {}
        producto["id"] = random.randint(1, 100)  
        producto["nombre"] = input("Ingrese el nombre del producto: ")
        producto["precio"] = float(input("Ingrese el precio unitario del producto: "))
        producto["ubicacion"] = input("Ingrese la ubicación del producto (A, B, C o D): ").upper()
        producto["descripcion"] = input("Ingrese la descripción del producto: ")
        producto["casa"] = input("Ingrese la casa a la que pertenece el producto (Marvel, DC, etc): ")
        producto["referencia"] = input("Ingrese la referencia del producto (código alfanumérico): ")
        producto["pais_origen"] = input("Ingrese el país de origen del producto: ")
        producto["unidades"] = int(input("Ingrese el número de unidades compradas del producto: "))
        producto["garantia"] = input("¿El producto tiene garantía extendida? (True/False): ").lower() == "true"

        
        total_unidades_ubicacion = sum(p["unidades"] for p in inventario if p["ubicacion"] == producto["ubicacion"])
        if total_unidades_ubicacion + producto["unidades"] > 50:
            print(f"No hay disponibilidad en esta ubicación para agregar más unidades. La cantidad actual es: {total_unidades_ubicacion}.")
        else:
            inventario.append(producto)
            print("Producto registrado exitosamente.")

    elif opcion == "2":  
        print("Productos en bodega:")
        for p in inventario:
            print(f"ID: {p['id']}, Nombre: {p['nombre']}, Ubicación: {p['ubicacion']}")

    elif opcion == "3":  
        nombre = input("Ingrese el nombre del producto: ")
        encontrado = False
        for p in inventario:
            if p["nombre"].lower() == nombre.lower():
                print(f"ID: {p['id']}, Nombre: {p['nombre']}, Precio: {p['precio']}, Descripción: {p['descripcion']}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "4":  
        nombre = input("Ingrese el nombre del producto: ")
        for p in inventario:
            if p["nombre"].lower() == nombre.lower():
                nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
                if nuevas_unidades <= p["unidades"]:
                    p["unidades"] = nuevas_unidades
                    print("Unidades modificadas exitosamente.")
                else:
                    print("Error: Las nuevas unidades no pueden ser mayores a las unidades iniciales.")
                break
        else:
            print("Producto no encontrado.")

    elif opcion == "5":  
        nombre = input("Ingrese el nombre del producto: ")
        encontrado = False
        for p in inventario:
            if p["nombre"].lower() == nombre.lower():
                encontrado = True
                confirmacion = input(f"¿Estás seguro de eliminar el producto '{nombre}'? (Sí/No): ").lower()
                if confirmacion == "si":
                    inventario.remove(p)
                    print("Producto eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "6":  
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
