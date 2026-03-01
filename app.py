from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import psycopg2

app = FastAPI()

# قراءة رابط قاعدة البيانات من Railway
DATABASE_URL = os.getenv("DATABASE_URL")

# الاتصال بقاعدة البيانات
def get_connection():
    return psycopg2.connect(DATABASE_URL)

# إنشاء الجدول إذا لم يكن موجود
def create_table():
    try:
        conn = get_connection()
        cur = conn.cursor()
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
        cur.close()
        conn.close()
    except Exception as e:
        print("DB Error:", e)

# إنشاء الجدول عند تشغيل التطبيق
create_table()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>NKRY Order System</h2>
    <a href="/order">Create Order</a>
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

@app.post("/submit")
def submit_order(
    name: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...),
    product: str = Form(...)
):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO orders (name, phone, city, product) VALUES (%s, %s, %s, %s)",
            (name, phone, city, product)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return {"error": str(e)}

    return {
        "status": "Order saved",
        "name": name,
        "phone": phone,
        "city": city,
        "product": product
    }
    
