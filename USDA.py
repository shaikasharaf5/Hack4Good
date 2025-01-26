from flask import Flask, render_template, request
import requests
import os
import re

# Flask app setup
app = Flask(__name__)

# USDA API Key
USDA_API_KEY = "vkMS6MLFv7HK6g43Ex0vU9yRurcM66JGDDrcoeWe"  # Replace with your actual USDA API key
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def fetch_usda_data(query, api_key):
    """Fetch food data from the USDA API based on a query."""
    params = {
        "query": query,
        "api_key": api_key,
        "pageSize": 10  # Number of results per request
    }
    response = requests.get(USDA_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

@app.route('/')
def index():
    return render_template('details.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        # Retrieve user inputs
        age = request.form['age']
        gender = request.form['gender']
        weight = request.form['weight']
        height = request.form['height']
        veg_or_nonveg = request.form['veg_or_nonveg']
        disease = request.form['disease']
        region = request.form['region']
        allergies = request.form['allergies']
        foodtype = request.form['foodtype']

        # USDA API queries based on user preferences
        try:
            # Query restaurants or related foods (example: breakfast foods)
            breakfast_query = "breakfast"
            dinner_query = "dinner"
            breakfast_data = fetch_usda_data(breakfast_query, USDA_API_KEY)
            dinner_data = fetch_usda_data(dinner_query, USDA_API_KEY)

            # Process API results to extract food names
            breakfast_names = [item["description"] for item in breakfast_data.get("foods", [])]
            dinner_names = [item["description"] for item in dinner_data.get("foods", [])]

            # Example static workout recommendations
            workout_names = ["Jogging", "Yoga", "Strength Training", "Cycling", "Swimming", "Pilates"]

            # Restaurants can still be provided statically or by a different API
            restaurant_names = ["Local Diner", "Healthy Eats Cafe", "Asian Fusion", "Mediterranean Bistro", "Vegan Delight", "Protein Paradise"]

            return render_template(
                'result.html',
                restaurant_names=restaurant_names,
                breakfast_names=breakfast_names,
                dinner_names=dinner_names,
                workout_names=workout_names
            )
        except Exception as e:
            return f"An error occurred while fetching recommendations: {str(e)}"

    return render_template('details.html')

if __name__ == '__main__':
    app.run(debug=True)
