import csv
import requests
from bs4 import BeautifulSoup

# URL da página que queremos fazer scraping
url = "https://www.lojasrenner.com.br/c/feminino/-/N-4zo6za"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Conexão: Enviar uma solicitação GET para a URL
# response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre os elementos HTML que contêm os títulos de notícias
    product_names = soup.find_all("h3", class_="ProductBox_title__x9UGh")
    
    #cria arquivo csv
    file = open('export_data.csv', 'w', newline='')
    writer = csv.writer(file)
    headers = ['Produtos']
    writer.writerow(['Nome do Produto'])

    # Loop pelos elementos e imprimir os títulos
    for product in product_names:
        print(product.text)
        #cada produto
        produto = [product.text]

        #salvar noticia no arquivo
        file = open('export_data.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow(product)
        file.close()

else:
    print("Falha ao acessar a página:", response.status_code)
