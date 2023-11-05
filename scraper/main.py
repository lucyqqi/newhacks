import json
import operator
import openai  
from decouple import config

# Access your environment variables
api_key = config("OPENAI_API_KEY")
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)



# Function to generate a recommendation explanation paragraph
def generate_explanation(product, prompt):
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
    if product.get("rating"):
        rating = float(product["rating"])  # Convert the rating to a float
        explanation.append(f"The product has a rating of {rating} out of 5.")
    else:
        explanation.append("No product rating is available.")

    if product.get("review_count"):
        explanation.append(f"It has {product['review_count']} reviews from customers.")
    else:
        explanation.append("The number of reviews for this product is not specified.")

    # Custom logic based on the prompt
    # Calculate a weighted score based on your criteria and prompt
    score = (
        0.2  # Price (Weight: 0.2)
        + (0.3 * (product.get("rating") / 5) if product.get("rating") is not None else 0)  # Average Rating (Weight: 0.3)
        + (0.25 * product.get("review_count") if product.get("review_count") is not None else 0)  # Number of ratings (Weight: 0.25)
        + 0.05  # Description (Weight: 0.05)
        + 0.2  # Reviews (Weight: 0.2)
    )

    # Analyze how well the description matches the prompt
    if any(keyword in description for keyword in prompt.lower().split()):
        score += 0.1  # Increase the score for a better description match

    explanation.append(f"Based on the provided criteria and prompt, this laptop is recommended as the best choice. "
                     f"The weighted score is {score:.2f} out of 1.0, where higher scores indicate a better fit for your needs.")

    return explanation


def rank_products(products, needs, prompt):
    ranked_products = []
    for product in products:
        rank_score = 0

        # Generate an explanation for the product based on the prompt
        explanation = generate_explanation(product, prompt)

        # Calculate a rank score based on the criteria
        if product.get("price"):
            rank_score += 0.2

        if product.get("rating") is not None:
            rank_score += 0.3 * (product.get("rating") / 5)

        if product.get("review_count") is not None:
            rank_score += 0.25 * product.get("review count")

        # You can also analyze the product's description and factor that into the rank score
        description = product.get("short_description").lower()
        if any(keyword in description for keyword in prompt.lower().split()):
            rank_score += 0.05

        # Check if 'reviews' key exists before accessing it
        if "reviews" in product:
            rank_score += 0.2

        ranked_products.append((product, rank_score, explanation))

    # Sort the products by rank score in descending order
    ranked_products.sort(key=operator.itemgetter(1), reverse=True)

    return ranked_products



# Load data from the JSON lines
products = []
with open('output.jsonl', 'r') as file:
    for line in file:
        products.append(json.loads(line))

while True:
    # Input a prompt
    prompt = input("Please enter a prompt (e.g., 'I need a laptop for gaming and high-speed performance.'): ")

    # Rank the products based on the criteria and the input prompt
    ranked_products = rank_products(products, [], prompt)

    if ranked_products:
        # Select the best product based on ranking
        best_product, best_rank_score, explanation = ranked_products[0]

        # Generate the explanation paragraph
        explanation_paragraph = " ".join(explanation)  # Merge explanation sentences into one paragraph

        # Print the recommendation with the explanation
        print("\nRecommendation:")
        print("Product Title: ", best_product["name"])
        print("Explanation:")
        print(explanation_paragraph)

        # Generate a one-paragraph response for OpenAI
        response = f"Based on your request for {prompt}, the recommended product is '{best_product['name']}' because it meets your criteria. {explanation_paragraph}"


    else:
        print("No products match the given criteria.")
