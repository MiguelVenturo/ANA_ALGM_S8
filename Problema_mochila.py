print(" ")
print("*** Bienvenidos al problema de la mochila ***\n")

def mochila(pesos, valores, capacidad):
    n = len(valores)
    objetos = []

    for i in range(n):
        ratio = valores[i] / pesos[i]
        objetos.append((ratio, pesos[i], valores[i]))

    objetos.sort(reverse=True)

    valor_total = 0.0
    mochila = []

    for ratio, peso, valor in objetos:
        if capacidad == 0:
            break

        if peso <= capacidad:
            capacidad -= peso
            valor_total += valor
            mochila.append((peso, valor, 1.0)) 
        else:
            fraccion = capacidad / peso
            valor_total += valor * fraccion
            mochila.append((peso, valor, fraccion))
            capacidad = 0

    return valor_total, mochila

pesos = [4, 5, 9]
valores = [6, 10, 18]
capacidad = 7

valor_obtenido, contenido_mochila = mochila(pesos, valores, capacidad)

print(f"Capacidad máxima de la mochila: 7 kg\n")
print(f"{'Peso':<10}{'Valor':<10}{'Fracción tomada'}")
print("-" * 35)

for peso, valor, fraccion in contenido_mochila:
    print(f"{peso:<10}{valor:<10}{fraccion:.2f}")

print("-" * 35)
print(f"\nValor total obtenido: {valor_obtenido:.2f} unidades\n")









 
