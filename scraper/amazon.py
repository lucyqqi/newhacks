from selectorlib import Extractor
import requests 
import json 
from time import sleep


# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml')

def scrape(url):  

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

# Initialize a list to store individual product dictionaries
product_data_list = []

# Initialize a dictionary to store the product data in nested format
product_data_nested = {}

with open("urls.txt", 'r') as urllist:
    for index, url in enumerate(urllist.read().splitlines(), 1):
        data = scrape(url)
        if data:
            # Create a dictionary for the product
            product_dict = {
                "name": data.get("name", ""),
                "price": data.get("price", ""),
                "short_description": data.get("short_description", ""),
                "images": data.get("images", ""),
                "rating": data.get("rating", ""),
                "review_count": data.get("review_count", ""),
                "product_description": data.get("product_description", ""),
                "link_to_all_reviews": data.get("link_to_all_reviews", ""),
                "seller_name": data.get("seller_name", ""),
                "seller_link": data.get("seller_link", ""),
                "link_five_star": data.get("link_five_star", ""),
                "link_one_star": data.get("link_one_star", ""),
                "best_sellers_rank": data.get("best_sellers_rank", "")
            }
            product_data_list.append(product_dict)

            # Add the data to the nested dictionary using a key like "product1", "product2"
            product_key = f"product{index}"
            product_data_nested[product_key] = data

# Write individual product dictionaries to "output.jsonl" file
with open('output.jsonl', 'w') as outfile:
    for product_dict in product_data_list:
        json.dump(product_dict, outfile)
        outfile.write('\n')  # Add a newline after each JSON object

# Write the nested dictionary to "output.json" file
with open('output.json', 'w') as outfile_nested:
    json.dump(product_data_nested, outfile_nested, indent=4)
