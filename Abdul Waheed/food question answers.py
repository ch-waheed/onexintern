import requests

def get_product_names(query):
    # Make a request to the linked API with the query parameter
    response = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&json=1')

    # Check if the request was successful
    if response.status_code == 200:
        # Access the data from the response
        data = response.json()

        # Process the data
        if 'products' in data:
            products = data['products']
            for product in products:
                if 'product_name' in product:
                    print(product['product_name'])
                else:
                    print('Product name not available')
        else:
            print('No products found')
    else:
        print('Failed to fetch product data.')

# Get user input
user_query = input("Enter your food / Drink, noddles rice etc: ")

# Call the function to retrieve and process the product names
get_product_names(user_query)
