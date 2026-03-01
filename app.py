from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os

app = FastAPI()


# الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>NKRY Order System</h1>
    <a href="/order">Create Order</a>
    """


# صفحة نموذج الطلب
@app.get("/order", response_class=HTMLResponse)
def order_form():
    return """
    <h2>New Order</h2>
    <form action="/submit-order" method="post">
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
@app.post("/submit-order")
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


# تشغيل السيرفر (مهم لـ Railway)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
