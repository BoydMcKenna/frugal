from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

@app.route("/", methods=["GET"])
def home():
    return "✅ Smart Shopping Assistant API is running!", 200

@app.route("/search", methods=["POST"])
def search():
    """Handles user shopping list and queries OpenAI for price comparisons."""
    data = request.json
    shopping_list = data.get("shopping_list", [])

    if not shopping_list:
        return jsonify({"error": "No products provided"}), 400

    shopping_plan = []
    
    for product in shopping_list:
        try:
            # Query OpenAI for best price insights
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a shopping assistant that finds the best prices."},
                    {"role": "user", "content": f"Find the best prices for {product} from Walmart, Amazon, and Best Buy."}
                ],
                temperature=0.7,
                max_tokens=100
            )
            
            price_info = response["choices"][0]["message"]["content"]
            shopping_plan.append({"product": product, "price_info": price_info})

        except Exception as e:
            shopping_plan.append({"product": product, "error": str(e)})

    return jsonify({"shopping_plan": shopping_plan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


