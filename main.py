
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import requests

# Initialize the Flask application
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the search results route
@app.route('/search', methods=["POST"])
def search():
    # Get the user's location from the request
    location = request.form['location']

    # Perform a search for coffee shops near the user's location
    params = {"location": location, "radius": "5000", "type": "cafe"}
    response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params)
    results = response.json()['results']

    # Store the results in a variable
    coffee_shops = []
    for result in results:
        coffee_shops.append({
            "name": result['name'],
            "address": result['vicinity'],
            "distance": result['distance'],
            "link": result['url']
        })

    # Render the results page
    return render_template('results.html', coffee_shops=coffee_shops)

# Define the coffee shop details route
@app.route('/coffee-shop/<coffee_shop_id>')
def coffee_shop_details(coffee_shop_id):
    # Fetch the details of the specified coffee shop
    response = requests.get(f"https://maps.googleapis.com/maps/api/place/details/json?place_id={coffee_shop_id}&fields=name,formatted_address,formatted_phone_number,website")
    coffee_shop_details = response.json()['result']

    # Render the coffee shop details page
    return render_template('coffee_shop_details.html', coffee_shop_details=coffee_shop_details)

# Define the fallback route
@app.route('/<any_other_route>')
def fallback():
    return render_template('404.html')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)


This code is a complete Flask application that allows users to search for coffee shops near a given location. It uses the Google Maps API to perform the search and fetch the details of a specific coffee shop. The application also includes a fallback route to handle incorrect URLs.