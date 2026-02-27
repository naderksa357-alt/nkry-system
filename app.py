from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()


@app.get("/")
def home():
    return {"message": "NKRY system is running"}


@app.get("/order", response_class=HTMLResponse)
def order_page():
    return """
    <html>
    <body style="font-family: Arial; direction: rtl;">
        <h2>طلب منتج</h2>
        <form action="/send">
            الاسم:<br>
            <input name="name"><br><br>

            الجوال:<br>
            <input name="phone"><br><br>

            المدينة:<br>
            <input name="city"><br><br>

            المنتج:<br>
            <input name="product"><br><br>

            <button type="submit">إرسال الطلب</button>
        </form>
    </body>
    </html>
    """
    

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
