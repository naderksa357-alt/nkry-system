from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>NKRY Order System</h1>
    <a href="/order">Create Order</a>
    """

# صفحة الفورم
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

# استقبال الطلب
@app.post("/submit")
def submit_order(
    name: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...),
    product: str = Form(...)
):
    print("New Order:", name, phone, city, product)

    return {
        "status": "Order received",
        "name": name,
        "phone": phone,
        "city": city,
        "product": product
    }
    
