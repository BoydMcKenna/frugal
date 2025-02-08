# 🛒 Smart Shopping Assistant

A simple web app that finds the best local deals for your shopping list by comparing prices across different stores.

## 🚀 Features
- Find the cheapest prices for products.
- Get a shopping plan that minimizes total cost.
- Links to buy from Walmart, Best Buy, Target, and Amazon.
- Easy to use and completely **free**.

## 📢 How to Use
1. **Enter product names** in the text box.
2. **Click "Find Deals"** to get the best shopping plan.
3. **See the results**, including the best store and a link to buy.

## 🔥 Live Demo
➡ **[Click Here to Use the App](https://yourusername.github.io/shopping-assistant/)**

## 🛠️ Technologies Used
- **HTML** (Frontend)
- **CSS** (Styling)
- **JavaScript** (Client-side logic)
- **Flask** (Backend API)
- **GitHub Pages** (Hosting)

## 🎯 Future Enhancements
- ✅ Add more stores like Costco, Newegg, eBay.
- ✅ Include coupons and promo codes.
- ✅ Allow price range filtering.

---

### **2️⃣ index.html (Frontend UI)**
Save this as `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Shopping Assistant</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>🛍️ Smart Shopping Assistant</h1>
        <p>Enter the products you want to buy, and we’ll find the best deals for you!</p>
        <textarea id="shoppingList" placeholder="Enter each product on a new line..."></textarea>
        <button onclick="searchDeals()">Find Deals</button>
        <div id="results"></div>
    </div>

    <script>
        async function searchDeals() {
            const shoppingList = document.getElementById("shoppingList").value.split("\n").filter(item => item.trim() !== "");
            
            if (shoppingList.length === 0) {
                document.getElementById("results").innerHTML = "<p style='color: red;'>Please enter at least one product.</p>";
                return;
            }

            document.getElementById("results").innerHTML = "<p>🔍 Searching for the best deals...</p>";

            try {
                const response = await fetch("https://your-api-url.com/search", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ shopping_list: shoppingList })
                });

                const data = await response.json();
                let output = "<h2>🛒 Best Shopping Plan:</h2><ul>";
                data.shopping_plan.forEach(item => {
                    output += `<li>Buy <strong>${item.product}</strong> at <strong>${item.store}</strong> for <strong>$${item.price}</strong> <a href="${item.link}" target="_blank">[Buy Now]</a></li>`;
                });
                output += `</ul><h3>Total Cost: <strong>$${data.total_cost}</strong></h3>`;
                document.getElementById("results").innerHTML = output;
            } catch (error) {
                document.getElementById("results").innerHTML = "<p style='color: red;'>⚠️ Error retrieving data. Please try again.</p>";
            }
        }
    </script>
</body>
</html>
