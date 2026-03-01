from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import psycopg2

app = FastAPI()

# الاتصال بقاعدة البيانات من Railway
DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# إنشاء جدول إذا لم يكن موجود
cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone TEXT,
    city TEXT,
    product TEXT
)
""")
conn.commit()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>NKRY Order System</h1>
    <a href="/order">Create Order</a>
    """


@app.get("/order", response_class=HTMLResponse)
def order_form():
    return """
    <h2>New Order</h2>
    <form action="/submit" method="post">
        Name:<br>
        <input name="name"><br>
        Phone:<br>
        <input name="phone"><br>
        City:<br>
        <input name="city"><br>
        Product:<br>
        <input name="product"><br><br>
        <button type="submit">Send Order</button>
    </form>
    """


@app.post("/submit")
def submit_order(
    name: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...),
    product: str = Form(...)
):
    cur.execute(
        "INSERT INTO orders (name, phone, city, product) VALUES (%s, %s, %s, %s)",
        (name, phone, city, product)
    )
    conn.commit()

    return {
        "status": "Order saved",
        "name": name
    }
