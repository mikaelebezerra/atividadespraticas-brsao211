def calcular_gorjeta(valor_conta, porcetagem_gorjeta):
    gorjeta = valor_conta * (porcetagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorjeta é de {gorjeta:.2f}")



