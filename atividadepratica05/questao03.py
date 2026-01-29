def calcular_desconto(valor_produto, porcetagem_desconto):
    desconto = valor_produto * (porcetagem_desconto / 100)
    valor_final = valor_produto - desconto
    return valor_final

valor = float(input("Digite o valor do produto: "))
porcentagem = float(input("Digite a porcentagem do desconto: "))

desconto = calcular_desconto(valor, porcentagem)

print(f"O valor do desconto é de {desconto:.2f}")



