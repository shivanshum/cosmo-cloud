# cosmo-cloud
### CosmoCloud backend internship assignment - Shivanshu Mishra
### This simple FastAPI application provides an E-commerce API for managing products and orders.

## Install the dependencies:
### Step 1: Open Visual Studio Code.
#### Create a new folder for your project and open it in VS Code.
#### Open the terminal in VS Code by going to View > Terminal.
### Step 2: Initialize a New Python Virtual Environment
~ python3 -m venv venv
#### Activate the virtual environment
~ venv\Scripts\activate
### Step 3: Install Required Packages
#### pip install fastapi uvicorn
### To run the application
##### uvicorn main:app --reload
#### the code includes all five APIs as specified in the assignment:
```
1 API to list all available products: GET /products
2 API to create a new order: POST /orders
3 API to fetch all orders with pagination: GET /orders
4 API to fetch a single order by order ID: GET /orders/{order_id}
5 API to update a product's available quantity: PUT /products/{product_id}
```
#### You can run this code using python main.py and access the APIs as per the specified endpoints.
#### Use the provided endpoints to interact with the API.
```
API Endpoints
List all available products
Endpoint: GET /products
Description: Retrieve a list of all available products in the system.
Response: Returns a JSON object containing the list of products.
```
```
Create a new order
Endpoint: POST /orders
Description: Create a new order with the specified items and user information.
Request Body: Requires a JSON object containing the order details.
Response: Returns the created order details in JSON format.
```
```
Fetch all orders
Endpoint: GET /orders
Description: Retrieve a list of all orders in the system with pagination support.
Query Parameters: limit (optional) - The maximum number of orders to retrieve per page, offset (optional) - The offset for pagination.
Response: Returns a JSON object containing the list of orders.
```
```
Fetch a single order
Endpoint: GET /orders/{order_id}
Description: Retrieve a single order by its order ID.
Path Parameter: order_id - The ID of the order to retrieve.
Response: Returns the order details in JSON format if found, or an error message if the order is not found.
```
```
Update a product's available quantity
Endpoint: PUT /products/{product_id}
Description: Update the available quantity for a product.
Path Parameter: product_id - The ID of the product to update.
Query Parameter: available_quantity - The new available quantity for the product.
Response: Returns the updated product details in JSON format if found, or an error message if the product is not found.
```
