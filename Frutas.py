
frutas = []


N = int(input('Ingrese la cantidad de frutas: '))

for i in range(N):
    nombre = input(f'Ingrese el nombre de la fruta {i + 1}: ')
    precio_unitario = float(input(f'Ingrese el precio unitario de {nombre}: '))
    cantidad = int(input(f'Ingrese la cantidad de {nombre}: '))
    frutas.append({'nombre': nombre, 'precio_unitario': precio_unitario, 'cantidad': cantidad})

costo_total = sum(fruta['precio_unitario'] * fruta['cantidad'] for fruta in frutas)
print(f'Costo total del salpicón: ${costo_total:.2f}')

frutas_ordenadas = sorted(frutas, key=lambda fruta: fruta['precio_unitario'], reverse=True)


for fruta in frutas_ordenadas:
    print(fruta['nombre'], fruta['precio_unitario'] * fruta['cantidad'])

fruta_mas_barata = min(frutas, key=lambda fruta: fruta['precio_unitario'])
print(f'La fruta más barata es {fruta_mas_barata["nombre"]} con un precio unitario de ${fruta_mas_barata["precio_unitario"]:.2f}')