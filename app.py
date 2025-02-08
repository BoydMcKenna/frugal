from flask import Flask, request, jsonify
import web
import re

app = Flask(__name__)

class SmartShoppingAgent:
    def __init__(self, location="Ann Arbor, MI", radius=20):
        self.location = location
        self.radius = radius
        self.stores = ["Walmart", "Best Buy", "Target", "Amazon"]

    def search_product_prices(self, product):
        """Search for the product across multiple stores and find the best price."""
        best_price = float('inf')
        best_store = None
        best_link = None

        for store in self.stores:
            query = f"{product} price at {store} near {self.location}"
            results = web.search(query)

            for result in results:
                price_match = re.search(r"\$\d+(?:\.\d+)?", result.get("snippet", ""))
                if price_match:
                    price = float(price_match.group().replace("$", ""))
                    if price < best_price:
                        best_price = price
                        best_store = store
                        best_link = result['link']

        return {"product": product, "store": best_store, "price": best_price, "link": best_link}

    def find_best_shopping_plan(self, shopping_list):
        """Finds the best stores to minimize total cost for the given shopping list."""
        shopping_plan = []
        total_cost = 0

        for product in shopping_list:
            best_deal = self.search_product_prices(product)
            shopping_plan.append(best_deal)
            total_cost += best_deal["price"]

        return {"shopping_plan": shopping_plan, "total_cost": total_cost}

shopping_agent = SmartShoppingAgent()

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    shopping_list = data.get("shopping_list", [])
    if not shopping_list:
        return jsonify({"error": "No products provided"}), 400
    
    result = shopping_agent.find_best_shopping_plan(shopping_list)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
