from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>NKRY Order System</h2>
    <a href='/order'>Create Order</a>
    """

@app.get("/order", response_class=HTMLResponse)
def order_form():
    return """
    <h2>New Order</h2>
    <form action="/submit" method="post">
        Name:<br>
        <input type="text" name="name"><br>
        Phone:<br>
        <input type="text" name="phone"><br>
        City:<br>
        <input type="text" name="city"><br>
        Product:<br>
        <input type="text" name="product"><br><br>
        <button type="submit">Send Order</button>
    </form>
    """

from fastapi import Form

@app.post("/submit")
def submit_order(
    name: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...),
    product: str = Form(...)
):
    print("New Order:", name, phone, city, product)
    return {"status": "Order received"}
    
