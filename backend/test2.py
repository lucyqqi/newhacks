from bs4 import BeautifulSoup
import requests

# Function to extract links from a single page


if __name__ == '__main__':
    # Headers for request
    HEADERS = ({'User-Agent':
	        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	        'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL with the search query

    URL = f"https://www.amazon.com/s?k=ps4"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    # Extract links from the current page
    links = soup.find_all("a", attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

    # Print or process the links as needed
    print(links)