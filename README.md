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
"  the code includes all five APIs as specified in the assignment:

> 1 API to list all available products: GET /products
> 2 API to create a new order: POST /orders
3 API to fetch all orders with pagination: GET /orders
4 API to fetch a single order by order ID: GET /orders/{order_id}
5 API to update a product's available quantity: PUT /products/{product_id}

You can run this code using python main.py and access the APIs as per the specified endpoints.
