distancia_percorrida = float(input("Digite a distancia percorrida em km: "))
combustivel_gasto = float(input("Digite o combustivel gasto em litros: "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Consumo médio: {consumo_medio:.2f} km/l")