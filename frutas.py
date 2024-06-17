def ingresar_frutas():
    """
    Función para ingresar las frutas para el salpicón.
    Retorna una lista de diccionarios con la información de cada fruta.
    """
    n = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    frutas = []
    for i in range(n):
        id_fruta = i + 1
        nombre = input(f"Ingrese el nombre de la fruta {id_fruta}: ")
        precio_unitario = float(input(f"Ingrese el precio unitario de {nombre}: "))
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
        fruta = {'id': id_fruta, 'nombre': nombre, 'precio_unitario': precio_unitario, 'cantidad': cantidad}
        frutas.append(fruta)
    return frutas

def costo_total(frutas):
    """
    Calcula el costo total del salpicó n.
    """
    total = 0
    for fruta in frutas:
        total += fruta['precio_unitario'] * fruta['cantidad']
    return total

def mostrar_frutas_ordenadas(frutas):
    """
    Muestra todas las frutas ordenadas de mayor a menor costo.
    """
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'], reverse=True)
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']}: ${fruta['precio_unitario']} por unidad")

def fruta_mas_barata(frutas):
    """
    Encuentra la fruta más barata en el salpicón.
    """
    fruta_barata = min(frutas, key=lambda x: x['precio_unitario'])
    return fruta_barata['nombre']

def main():
    print("Programa para gestionar un salpicón de frutas\n")

    frutas = ingresar_frutas()

    print("\nCosto total del salpicón:", costo_total(frutas))

    print("\nFrutas en el salpicón ordenadas de mayor a menor costo:")
    mostrar_frutas_ordenadas(frutas)

    print("\nFruta más barata en el salpicón:", fruta_mas_barata(frutas))

if __name__ == "__main__":
    main()
