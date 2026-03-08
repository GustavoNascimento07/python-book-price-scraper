import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"

resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

livros = soup.find_all("article", class_="product_pod")

taxa = 5.10

nomes = []
precos = []

for livro in livros:
    nome = livro.h3.a["title"]

    preco_texto = livro.find("p", class_="price_color").text
    preco_libra = preco_texto.replace("Â£", "").replace("£", "")
    preco_libra = float(preco_libra)

    preco_real = preco_libra * taxa

    nomes.append(nome)
    precos.append(round(preco_real, 2))

dados = pd.DataFrame({
    "Livro": nomes,
    "Preço (R$)": precos
})

dados.to_excel("livros.xlsx", index=False)

print("Planilha criada com sucesso!")

import os
os.startfile("livros.xlsx")