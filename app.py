from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NKRY system is running"}


@app.get("/order", response_class=HTMLResponse)
def order_form():
    return """
    <html>
        <body>
            <h2>NKRY Order Form</h2>
            <form action="/submit-order" method="post">
                Name:<br>
                <input type="text" name="name"><br>
                Phone:<br>
                <input type="text" name="phone"><br>
                City:<br>
                <input type="text" name="city"><br>
                Product:<br>
                <input type="text" name="product"><br><br>
                <input type="submit" value="Send Order">
            </form>
        </body>
    </html>
    """


@app.post("/submit-order")
def submit_order(
    name: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...),
    product: str = Form(...)
):
    print("New Order:", name, phone, city, product)
    return {"status": "Order received"}
