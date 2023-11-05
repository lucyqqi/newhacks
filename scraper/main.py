import json
import operator
import openai  
from flask import Flask, render_template, jsonify, redirect, url_for, request

app = Flask(__name__)

api_data = {
    "product1": {
        "name": "Monster Trucks Inertia Car Toys - Friction Powered Car Toys for Toddlers Kids Birthday Christmas Party Supplies Gift for Boys and Girls (4 Color)",
        "price": "$20.99",
        "short_description": "About this item \u2705 Easy to Operate: Push the friction car forward slightly then it go and last for quite a long distance.No battery required. We\u2019ve designed the light up toys for boys and girls to be an absolute breeze to operate by kids thanks to the push go mechanism. Children under six should play our car toys only under adult supervision. \u2705Durable and Safe: Heavy duty alloys make it a durable, long-lasting toy gaming device. Monster truck with oversized tires. A great educational and learning toy that teaches your child to feel the inertia of the car and inspire the child's interest. \u2705 Powerful Features: The body of the monster truck is made of high quality metal and large wheels. It has the power to drive on many terrains. It easily breaks through obstacles in indoor and outdoor environments, including lawns, patios and living rooms. This monster truck toy is loved by children. \u2705Holiday Gifts: Congratulations on birthday gifts for children's birthdays, children's day, Halloween, Christmas, New Year and other festivals. In addition, the monster truck can improve the child's ability to improve, improve the child's ability to adapt and thinking, is the perfect toy gift for boys and girls children. \u2705Absolutely Satisfied: 100% safe and 100% return refund. If you met problem with your monster trucks, we will solve the problem within 24 hours, just contact us directly. We can not guarantee 0% defective rate, but we guarantee 100% satisfaction.",
        "images": "{\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SX569_.jpg\":[576,569],\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SX522_.jpg\":[528,522],\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SX425_.jpg\":[430,425],\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SX466_.jpg\":[471,466],\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SY450_.jpg\":[450,445],\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SX679_.jpg\":[687,679],\"https://m.media-amazon.com/images/I/81imCci-eGL._AC_SY355_.jpg\":[355,351]}",
        "rating": "4.6",
        "review_count": "2,664 global ratings",
        "product_description": '',
        "link_to_all_reviews": "/Monster-Trucks-Inertia-Car-Toys/product-reviews/B07SRZ87DF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
        "seller_name": '',
        "seller_link": '',
        "link_five_star": "/product-reviews/B07SRZ87DF/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar",
        "link_one_star": "/product-reviews/B07SRZ87DF/ref=acr_dp_hist_1?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar",
        "best_sellers_rank": "#696 in Toys & Games ( See Top 100 in Toys & Games ) #4 in Kids' Play Cars & Race Cars"
    },
    "product2": {
        "name": "Hamdol Remote Control Car Double Sided 360\u00b0Rotating 4WD RC Cars with Headlights 2.4GHz Electric Race Stunt Toy Car Rechargeable Toy Cars for Boys Girls Birthday Blue&Green",
        "price": "$41.99",
        "short_description": "About this item Offer Different Gaming Experiences: 360\u00b0 Flip-This electric remote control stunt car adopts 4D drive and can drive on both sides; moving forward and backward;turn left and right, and 360\u00b0 rotation. Double motors-the maximum speed can reach 10KM/H. A better gaming experience for childrens Provide Longer Playing Time: 2* 500 mA (3.7V) lithium battery is included for the remote control car, and it can be used for 20 minutes with a single full charge. It only takes 1.5H to fully charge Multiple Cars Playing at The Same TIme: With 2.4GHz anti-interference frequency technology, multiple RC stunt cars can race at the same time. The remote control can reach a max distance of 50M Create Unlimited Fun for Children: Double-rocker control is adopted, which makes the operation more convenient. Double-sided 4 Headlights, with more LED lights than other similar cars, which will be bright during the day and night. Equipped with flexible wheels, allow high speed and better flexibility. Suitable for competitions on all kinds of ground, such as land, beach, grass or wetland Quality Assured: Includes 1*RC Car, 1*remote control, 2*rechargeable lithium batteries, 2*AA batteries, 1*charging cable, 1*screwdriver. It will be the perfect Christmas or Birthday gift for childrens! And a 24-month--period is provided. If you have any questions, please feel free to contact us Included components: Charging Cable, Remote,Battery",
        "images": "{\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SY450_.jpg\":[450,450],\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SY355_.jpg\":[355,355],\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SX522_.jpg\":[522,522],\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SX569_.jpg\":[569,569],\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SX679_.jpg\":[679,679],\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SX425_.jpg\":[425,425],\"https://m.media-amazon.com/images/I/81lPkh1LIzL._AC_SX466_.jpg\":[466,466]}",
        "rating": "4.3",
        "review_count": "866 global ratings",
        "product_description": '',
        "link_to_all_reviews": "/Hamdol-360%C2%B0Rotating-Headlights-Electric-Rechargeable/product-reviews/B092YTJG5H/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
        "seller_name": '',
        "seller_link": '',
        "link_five_star": "/product-reviews/B092YTJG5H/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar",
        "link_one_star": "/product-reviews/B092YTJG5H/ref=acr_dp_hist_1?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar",
        "best_sellers_rank": "#69 in Toys & Games ( See Top 100 in Toys & Games ) #1 in Radio & Remote Control Cars"
    }
}

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'GET':
        return render_template("preferences.html")
    else:
        best_product, explaination_paragraph = get_best_product(request.form['text'])
        return render_template("preferences.html", item={'title': best_product["name"], 'content': explaination_paragraph})


@app.route('/table')
def table():
    with open('/Users/lucyqi/Documents/GitHub/newhacks/scraper/output.json', 'rt') as json_file:
        data = json_file.read()

    return render_template('table.html', api_data = json.loads(data))

@app.route('/query', methods=['POST'])
def post_query():

    print(request.form['text'])

    return redirect(url_for('table'))





# Access your environment variables
api_key = "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"

# Function to generate a recommendation explanation paragraph
def generate_explanation(product, prompt):
    explanation = []

    # Analyze the product's short description
    description = product["short_description"].lower()
    if "educational" in description or "solve the problem" in description:
        explanation.append("The Monster Trucks Inertia Car Toys, is a budget-friendly option with a focus on teaching kids about inertia and friction. It offers a good educational element, and the seller claims responsive customer service. On the other hand, the Hamdol Remote Control Car, offers a more versatile and exciting play experience with 360° flips and rechargeable batteries, although it's pricier. Both products claim responsive customer service, so checking customer reviews may help make your decision.")

    else:
        explanation.append("Product 2, the Hamdol Remote Control Car, may be preferred over Product 1 for its versatility, offering 360° flips and double-sided driving for a more exciting play experience. Additionally, it includes rechargeable batteries, providing long-term cost savings and environmental benefits, and comes with a 24-month warranty for added peace of mind. The flexible wheels make it suitable for diverse play environments. While both products have their merits, Product 2 offers a more versatile and feature-rich option for a fun and engaging gift for your child.")

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

    # first format review_count data
    review_count = product.get("review_count")
    parts = review_count.split()
    review_count = parts[0]
    review_count = float(review_count.replace(",", ""))

    if review_count:
        explanation.append(f"It has {review_count} reviews from customers.")
    else:
        explanation.append("The number of reviews for this product is not specified.")

    # as well format price data
    price = float(product.get("price")[1:]) 

    if product.get("review_count"):
        explanation.append(f"It has {review_count} reviews from customers.")
    else:
        explanation.append("The number of reviews for this product is not specified.")

    # Custom logic based on the prompt
    # Calculate a weighted score based on your criteria and prompt

    score = (
        0.2*price #(Weight: 0.2)
        + ((0.3 * float(product.get("rating")) / 5) if product.get("rating") is not None else 0)  # Average Rating (Weight: 0.3)
        + (0.25 * review_count if review_count is not None else 0)  # Number of ratings (Weight: 0.25)
        + 0.05  ## Description (Weight: 0.05)
        + 0.2  # Reviews (Weight: 0.2)
    )

    # Analyze how well the description matches the prompt
    if any(keyword in description for keyword in prompt.lower().split()):
        score += 0.1  # Increase the score for a better description match

    explanation.append(f"Based on the provided criteria and prompt, this laptop is recommended as the best choice. "
                     f"The weighted score is {score:.2f} out of 100, where a score of 100 or higher means it's perfectly suited for your needs.")

    return explanation


def rank_products(products, needs, prompt):
    ranked_products = []
    for product in products:
        rank_score = 0
        # first format review_count data
        review_count = product.get("review_count")
        parts = review_count.split()
        review_count = parts[0]
        review_count = float(review_count.replace(",", ""))


        # Generate an explanation for the product based on the prompt
        explanation = generate_explanation(product, prompt)

        # Calculate a rank score based on the criteria
        if product["price"]:
            rank_score += 0.2

        if product["rating"] is not None:
            rank_score += 0.3 * (float(product["rating"]) / 5)

        if review_count is not None:
            rank_score += 0.25 * review_count
        # You can also analyze the product's description and factor that into the rank score
        description = product["short_description"].lower()
        if any(keyword in description for keyword in prompt.lower().split()):
            rank_score += 0.05

        # Check if 'reviews' key exists before accessing it
        if "reviews" in product:
            rank_score += 0.2

        ranked_products.append((product, rank_score, explanation))

    # Sort the products by rank score in descending order
    ranked_products.sort(key=operator.itemgetter(1), reverse=True)

    return ranked_products

def get_best_product(prompt: str):

    # Load data from the JSON lines
    products = []
    with open('/Users/lucyqi/Documents/GitHub/newhacks/scraper/output.jsonl', 'r') as file:
        for line in file:
            products.append(json.loads(line))

    while True:
        # Input a prompt

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
            return best_product, explanation_paragraph

        else:
            print("No products match the given criteria.")



if __name__ == '__main__':
    app.run(debug=True)