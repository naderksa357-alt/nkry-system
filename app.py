from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

# تعريف التطبيق أولاً
app = FastAPI()


# الصفحة الرئيسية
@app.get("/")
def home():
    return {"message": "NKRY system is running"}


# صفحة الطلب (لإنستقرام / واتساب)
@app.get("/order", response_class=HTMLResponse)
def order_form():
    return """
    <h2>طلب منتج NKRY</h2>
    <form action="https://wa.me/966502888357" method="get">
        الاسم:<br>
        <input type="text" name="name"><br><br>
        الجوال:<br>
        <input type="text" name="phone"><br><br>
        المدينة:<br>
        <input type="text" name="city"><br><br>
        المنتج:<br>
        <input type="text" name="product"><br><br>
        <button type="submit">إرسال عبر واتساب</button>
    </form>
    """


# تشغيل Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
