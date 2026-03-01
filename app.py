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
@app.get("/orders")
def get_orders():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, city, product FROM orders ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return {
        "orders": [
            {
                "id": r[0],
                "name": r[1],
                "phone": r[2],
                "city": r[3],
                "product": r[4]
            }
            for r in rows
        ]
    }
from fastapi.responses import HTMLResponse

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, city, product FROM orders ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    html = """
    <html>
    <head>
        <title>NKRY Dashboard</title>
        <style>
            body {font-family: Arial; padding:20px; background:#f4f4f4;}
            table {width:100%; border-collapse: collapse; background:white;}
            th, td {padding:10px; border-bottom:1px solid #ddd;}
            th {background:black; color:white;}
            .wa {background:#25D366; color:white; padding:5px 10px; text-decoration:none; border-radius:5px;}
        </style>
    </head>
    <body>
        <h2>NKRY Orders</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Phone</th>
                <th>City</th>
                <th>Product</th>
                <th>WhatsApp</th>
            </tr>
    """

    for r in rows:
        phone = r[2].replace("0", "966", 1)
        html += f"""
        <tr>
            <td>{r[0]}</td>
            <td>{r[1]}</td>
            <td>{r[2]}</td>
            <td>{r[3]}</td>
            <td>{r[4]}</td>
            <td><a class='wa' href='https://wa.me/{phone}' target='_blank'>Contact</a></td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """
    return html
@app.get("/delete/{order_id}")
def delete_order(order_id: int):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("DELETE FROM orders WHERE id = %s", (order_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "deleted", "id": order_id}
from fastapi import Request, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()

USERNAME = "nkry"
PASSWORD = "1234"

def check_auth(credentials: HTTPBasicCredentials = security):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials.username
