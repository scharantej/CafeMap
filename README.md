**Flask Application Design**

**HTML Files**

1. **index.html**:
   - **Purpose**: Home page of the website.
   - **Content**:
     - Title: Coffee Shop Locator
     - Paragraph: Welcome to the Coffee Shop Locator website! Find the best local coffee shops near you.
     - Input field for location: Ask the user to enter their location (city or zip code).
     - Submit button.

2. **results.html**:
   - **Purpose**: Display the search results.
   - **Content**:
     - Title: Coffee Shop Locator Results
     - Table with the following columns:
       - Name: Name of the coffee shop.
       - Address: Address of the coffee shop.
       - Distance: Distance from the user's location.
       - Link: A link to the coffee shop's website or Google Maps page.

**Routes**

1. **Home Page Route**:
   - **Route**: /
   - **Method**: GET
   - **Function**: Renders the index.html file.

2. **Search Results Route**:
   - **Route**: /search
   - **Method**: POST
   - **Function**:
     - Retrieves the user's location from the request.
     - Performs a search for coffee shops near the user's location using an API (e.g., Google Places API).
     - Stores the results in a variable.
     - Renders the results.html file with the search results.

3. **Coffee Shop Details Route**:
   - **Route**: /coffee-shop/<coffee_shop_id>
   - **Method**: GET
   - **Function**:
     - Retrieves the ID of the coffee shop from the request.
     - Fetches the details of the specified coffee shop (e.g., name, address, phone number, website) from a database or an API.
     - Renders a details page for the coffee shop with the fetched information.

4. **Fallback Route**:
   - **Route**: /<any_other_route>
   - **Method**: GET
   - **Function**: Renders a 404 (Not Found) error page.