import random


seccion_A = []
seccion_B = []
seccion_C = []
seccion_D = []


def generar_id():
    return random.randint(1, 100)


def registrar_comic():
    print("Ingrese los datos del nuevo cómic:")
    nombre = input("Nombre del cómic: ")
    precio = float(input("Precio unitario del cómic: "))
    descripcion = input("Descripción del cómic: ")
    casa = input("Casa a la que pertenece el cómic (Marvel, DC, etc.): ")
    referencia = input("Referencia del cómic (código alfanumérico): ")
    pais_origen = input("País de origen del cómic: ")
    unidades_compradas = int(input("Número de unidades compradas del cómic: "))
    garantia_extendida = input("Cómic con garantía extendida (Sí/No): ").lower() == "si"
    
   
    id_comic = generar_id()
    
    
    ubicacion = input("En qué sección desea guardar el cómic (A, B, C, D): ").upper()
    while ubicacion not in ['A', 'B', 'C', 'D']:
        print("Sección inválida. Por favor, seleccione A, B, C o D.")
        ubicacion = input("En qué sección desea guardar el cómic (A, B, C, D): ").upper()
    
    
    if ubicacion == 'A':
        seccion = seccion_A
    elif ubicacion == 'B':
        seccion = seccion_B
    elif ubicacion == 'C':
        seccion = seccion_C
    else:
        seccion = seccion_D
        
    if len(seccion) + unidades_compradas > 50:
        print(f"No hay suficiente espacio en la sección {ubicacion} para agregar este cómic.")
        return
    
    
    comic = {
        "ID": id_comic,
        "Nombre": nombre,
        "Precio": precio,
        "Ubicación": ubicacion,
        "Descripción": descripcion,
        "Casa": casa,
        "Referencia": referencia,
        "País": pais_origen,
        "Unidades": unidades_compradas,
        "Garantía_extendida": garantia_extendida
    }
    seccion.extend([comic]*unidades_compradas)
    
    print("Cómic registrado con éxito.")


def mostrar_comics():
    print("Cómics en bodega:")
    mostrar_seccion("Sección A", seccion_A)
    mostrar_seccion("Sección B", seccion_B)
    mostrar_seccion("Sección C", seccion_C)
    mostrar_seccion("Sección D", seccion_D)


def mostrar_seccion(nombre_seccion, seccion):
    print(nombre_seccion + ":")
    for comic in seccion:
        print(f"ID: {comic['ID']}, Nombre: {comic['Nombre']}, Precio: {comic['Precio']}, Descripción: {comic['Descripción']}, Unidades: {comic['Unidades']}, Ubicación: {comic['Ubicación']}")


def buscar_comic(nombre):
    encontrado = False
    for seccion in [seccion_A, seccion_B, seccion_C, seccion_D]:
        for comic in seccion:
            if comic["Nombre"] == nombre:
                print(f"ID: {comic['ID']}, Nombre: {comic['Nombre']}, Precio: {comic['Precio']}, Descripción: {comic['Descripción']}, Unidades: {comic['Unidades']}, Ubicación: {comic['Ubicación']}")
                encontrado = True
    if not encontrado:
        print("Cómic no encontrado.")


def modificar_unidades(nombre, nuevas_unidades):
    for seccion in [seccion_A, seccion_B, seccion_C, seccion_D]:
        for comic in seccion:
            if comic["Nombre"] == nombre:
                if nuevas_unidades <= comic["Unidades"]:
                    comic["Unidades"] = nuevas_unidades
                    print("Unidades modificadas exitosamente.")
                    return
                else:
                    print("La modificación no puede ser mayor al número inicial de unidades.")
                    return
    print("Cómic no encontrado.")


def eliminar_comic(nombre):
    secciones = [seccion_A, seccion_B, seccion_C, seccion_D]
    for seccion in secciones:
        for i, comic in enumerate(seccion):
            if comic["Nombre"] == nombre:
                confirmacion = input("¿Está seguro que desea eliminar este cómic? (Sí/No): ").lower()
                if confirmacion == "si":
                    del seccion[i]
                    print("Cómic eliminado.")
                    return
                else:
                    print("Operación cancelada.")
                    return
    print("Cómic no encontrado.")






while True:
    print("\nMenú de opciones:")
    print("1. Registrar un nuevo cómic")
    print("2. Mostrar todos los cómics en bodega")
    print("3. Buscar y mostrar un cómic por nombre")
    print("4. Modificar el número de unidades compradas de un cómic")
    print("5. Eliminar un cómic por nombre")
    print("6. Salir")
    
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    if opcion == "1":
        registrar_comic()
    elif opcion == "2":
        mostrar_comics()
    elif opcion == "3":
        nombre_comic = input("Ingrese el nombre del cómic que desea buscar: ")
        buscar_comic(nombre_comic)
    elif opcion == "4":
        nombre_comic = input("Ingrese el nombre del cómic cuyas unidades desea modificar: ")
        nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
        modificar_unidades(nombre_comic, nuevas_unidades)
    elif opcion == "5":
        nombre_comic = input("Ingrese el nombre del cómic que desea eliminar: ")
        eliminar_comic(nombre_comic)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor ingrese un número válido.")