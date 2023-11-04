import json
import operator

# Load the API key
api_key = "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"

# Function to generate an explanation paragraph
def generate_explanation(product):
    explanation = []

    # Analyze the product's short description
    description = product["short_description"].lower()
    if "gaming" in description or "graphics" in description:
        explanation.append("The product description mentions gaming or graphics.")
    else:
        explanation.append("The product description does not specifically mention gaming or graphics.")

    # Consider the product's price
    if product["price"]:
        explanation.append(f"The product's price is {product['price']} which is competitive for the features it offers.")
    else:
        explanation.append("No product price is available.")

    # Consider product reviews and number of reviews
    if product["rating"]:
        explanation.append(f"The product has a rating of {product['rating']} out of 5.")
    else:
        explanation.append("No product rating is available.")

    if product["number_of_reviews"]:
        explanation.append(f"It has {product['number_of_reviews']} reviews from customers.")
    else:
        explanation.append("The number of reviews for this product is not specified.")

    return explanation

# Function to rank products based on different criteria
def rank_products(products, needs):
    ranked_products = []
    for product in products:
        rank_score = 0

        # Generate an explanation for the product
        explanation = generate_explanation(product)

        # Calculate a rank score based on your needs or criteria
        # Here, you can customize the scoring based on your needs

        # If you find more information or criteria specific to gaming, you can add them here

        ranked_products.append((product, rank_score, explanation))

    # Sort the products by rank score in descending order
    ranked_products.sort(key=operator.itemgetter(1), reverse=True)

    return ranked_products

# Load data from the JSON lines
products = []
with open('output.jsonl', 'r') as file:
    for line in file:
        products.append(json.loads(line))

# Define your needs and criteria
needs = ["play League of Legends", "highest speed", "highest graphics"]

# Rank the products based on the criteria
ranked_products = rank_products(products, needs)

# Select the best product based on ranking
best_product, best_rank_score, explanation = ranked_products[0]

# Generate the explanation paragraph
explanation_paragraph = "\n".join(explanation)

# Print the recommendation with the explanation
print("Recommendation:")
print("Product Title: ", best_product["name"])
print("Explanation:")
print(explanation_paragraph)
