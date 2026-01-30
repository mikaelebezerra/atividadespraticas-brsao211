import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()[f"{moeda.upper()}BRL"]

        cotacao = f"{float(dados["bid"]):.2f}"
        alta = float(dados["hight"])
        baixa = float(dados["low"])
        data = dados["create_date"]

        return f"Cotação: R${cotacao:.2f}\nAlta: R${alta:.2f}\nBaixa: R${baixa:.2f}\n Data: {data}"

    except requests.RequestException as e:
        return f"Erro ao consultar cotação: {e}"
    

moeda = input("Digite a moeda (ex: USAD, EUR, BTC, GBO): ")
resultado = consultar_cotacao(moeda)
print(resultado)