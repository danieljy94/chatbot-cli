import requests


def search_cep(cep: str):
    cep = cep.replace("-", "").strip()

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code != 200:
        print("Erro ao encontrar o CEP")

    return response.json()

