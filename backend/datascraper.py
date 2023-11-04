import requests
from bs4 import BeautifulSoup

def scrape_amazon(query_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    response = requests.get(query_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_results = soup.find_all('div', {'class': 's-result-item'})

        top_100_products = []
        for product in product_results[:100]:
            product_info = {
                'title': product.find('span', {'class': 'a-text-normal'}).text,
                'price': product.find('span', {'class': 'a-offscreen'}).text,
                'url': 'https://www.amazon.com' + product.find('a', {'class': 'a-link-normal'})['href'],
            }
            top_100_products.append(product_info)

        return top_100_products
    else:
        return None

# Usage example:
query_url = 'https://www.amazon.ca/s?k=%22Custom-made+Japanese+wooden+chopsticks+under+%24100%22'
top_100_products = scrape_amazon(query_url)
if top_100_products:
    for product in top_100_products:
        print(f'Title: {product["title"]}')
        print(f'Price: {product["price"]}')
        print(f'URL: {product["url"]}')






