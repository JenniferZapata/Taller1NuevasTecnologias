frutas = []

N = int(input('Ingrese la cantidad de frutas: '))

for i in range(N):
    nombre = input(f'Ingrese el nombre de la fruta {i + 1}: ')
    precio_unitario = float(input(f'Ingrese el precio unitario de {nombre}: '))
    cantidad = int(input(f'Ingrese la cantidad de {nombre}: '))
    fruta = {'nombre': nombre, 'precio_unitario': precio_unitario, 'cantidad': cantidad}
    frutas.append(fruta)

costo_total = 0
for fruta in frutas:
    costo_total += fruta['precio_unitario'] * fruta['cantidad']

print(f'Costo total del salpicón: ${costo_total:.2f}')

def get_precio_unitario(fruta):
    return fruta['precio_unitario']

frutas_ordenadas = sorted(frutas, key=get_precio_unitario, reverse=True)

print('Frutas ordenadas de mayor a menor costo:')
for fruta in frutas_ordenadas:
    print(fruta['nombre'], fruta['precio_unitario'] * fruta['cantidad'])

fruta_mas_barata = frutas[0]
for fruta in frutas:
    if fruta['precio_unitario'] < fruta_mas_barata['precio_unitario']:
        fruta_mas_barata = fruta

print(f'\nLa fruta más barata es {fruta_mas_barata["nombre"]} con un precio unitario de ${fruta_mas_barata["precio_unitario"]:.2f}')