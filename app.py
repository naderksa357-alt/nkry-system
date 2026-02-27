from fastapi.responses import HTMLResponse

@app.get("/order", response_class=HTMLResponse)
def order_page():
    return """
    <html>
    <head>
        <title>طلب من NKRY</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 40px; }
            input, button { padding: 10px; margin: 5px; width: 250px; }
        </style>
    </head>
    <body>
        <h2>طلب منتج من NKRY</h2>
        <form action="/orders" method="post">
            <input name="name" placeholder="الاسم" required><br>
            <input name="phone" placeholder="رقم الجوال" required><br>
            <input name="city" placeholder="المدينة" required><br>
            <input name="product" placeholder="اسم المنتج" required><br>
            <button type="submit">إرسال الطلب</button>
        </form>
    </body>
    </html>
    """
