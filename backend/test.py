from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"class": 'a-size-medium a-color-base a-text-normal'})
        title_value = title.string
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'a-price-whole'}).string.strip()
    except AttributeError:
        price = ""
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""
    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()
    except AttributeError:
        available = ""
    return available

# Function to extract Product Information from a search results page
def get_product_info(soup):
    product_info = []
    product_listings = soup.find_all("div", attrs={"class": "s-result-item"})
    for listing in product_listings[:100]:
        title = get_title(listing)
        price = get_price(listing)
        rating = get_rating(listing)
        review_count = get_review_count(listing)
        availability = get_availability(listing)

        product_data = {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Review Count': review_count,
            'Availability': availability
        }
        product_info.append(product_data)
    return product_info

if __name__ == '__main__':
    # Headers for request
    HEADERS = ({'User-Agent':
	        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	        'Accept-Language': 'en-US, en;q=0.5'})


    # The webpage URL with the search query
    SEARCH_QUERY = "ps4"
    URL = f"https://www.amazon.com/s?k={SEARCH_QUERY}"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    # Extract product information
    product_info = get_product_info(soup)

    # Print or process the product information as needed
    for i, product in enumerate(product_info, start=1):
        print(f"Product {i} Information:")
        print("Title =", product['Title'])
        print("Price =", product['Price'])
        print("Rating =", product['Rating'])
        print("Review Count =", product['Review Count'])
        print("Availability =", product['Availability'])
        print()