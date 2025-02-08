from flask import Flask, request, jsonify
import re
import random

app = Flask(__name__)

class SmartShoppingAgent:
    def __init__(self, location="Ann Arbor, MI", radius=20):
        self.location = location
        self.radius = radius
        self.stores = ["Walmart", "Best Buy", "Target", "Amazon"]

    def search_product_prices(self, product):
        """Simulate price lookup (Replace this with a real API later)"""
        dummy_prices = {
            "Walmart": random.uniform(10, 500),
            "Best Buy": random.uniform(10, 500),
            "Target": random.uniform(10, 500),
            "Amazon": random.uniform(10, 500)
        }

        best_store = min(dummy_prices, key=dummy_prices.get)
        best_price = round(dummy_prices[best_store], 2)
        best_link = f"https://{best_store.lower()}.com/search?q={product.replace(' ', '+')}"

        return {"product": product, "store": best_store, "price": best_price, "link": best_link}

    def find_best_shopping_plan(self, shopping_list):
        """Finds the best stores to minimize total cost for the given shopping list."""
        shopping_plan = []
        total_cost = 0

        for product in shopping_list:
            best_deal = self.search_product_prices(product)
            shopping_plan.append(best_deal)
            total_cost += best_deal["price"]

        return {"shopping_plan": shopping_plan, "total_cost": round(total_cost, 2)}

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

