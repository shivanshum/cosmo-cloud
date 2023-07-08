from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import datetime

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    available_quantity: int


class Address(BaseModel):
    city: str
    country: str
    zip_code: str


class OrderItem(BaseModel):
    productId: int
    boughtQuantity: int


class Order(BaseModel):
    timestamp: str
    items: List[OrderItem]
    totalAmount: float
    userAddress: Address


products = [
    Product(name="TV", price=499.99, available_quantity=10),
    Product(name="Laptop", price=999.99, available_quantity=5),
    Product(name="Phone", price=299.99, available_quantity=15),
    Product(name="Headphones", price=99.99, available_quantity=20),
    Product(name="Tablet", price=399.99, available_quantity=8),
    Product(name="Camera", price=799.99, available_quantity=3),
    Product(name="Smartwatch", price=199.99, available_quantity=12),
    Product(name="Speakers", price=149.99, available_quantity=7),
    Product(name="Gaming Console", price=499.99, available_quantity=4),
    Product(name="Printer", price=199.99, available_quantity=6),
]

orders = []


@app.get("/products")
def get_products():
    return products


@app.post("/orders")
def create_order(order: Order):
    order.timestamp = str(datetime.datetime.now())
    orders.append(order)
    return order


@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    return orders[offset:offset + limit]


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    if 0 <= order_id < len(orders):
        return orders[order_id]
    else:
        return {"error": "Order not found"}


@app.put("/products/{product_id}")
def update_product(product_id: int, available_quantity: int):
    if 0 <= product_id < len(products):
        products[product_id].available_quantity = available_quantity
        return products[product_id]
    else:
        return {"error": "Product not found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
